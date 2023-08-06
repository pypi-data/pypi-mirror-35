import itertools
from .comm import MockSocket
from .constants import Tag, MsgType
import ssl
import logging
import socket
import errno
import select

LOG = logging.getLogger(__name__)

TAG2NAME = { str(v): k for k,v in Tag.__dict__.iteritems() if "_" != k[0] }
MSGTYPE2NAME = { v: k for k,v in MsgType.__dict__.iteritems() if "_" != k[0] }

class InvalidPart(Exception): pass

class InvalidMessage(Exception):
    def __init__(self, parts, cause):
        self.parts = parts
        self.cause = cause
        super(InvalidMessage, self).__init__("Invalid message %r. Cause: %s" % (parts, cause))

class InvalidChecksum(InvalidMessage):
    def __init__(self, checksum, parts):
        self.checksum = checksum
        super(InvalidChecksum, self).__init__(parts = parts, cause="Invalid checksum. Expected %s" % checksum)

class MultipleTags(Exception):
    def __init__(self, fix_message, tag_number):
        self.fix_message = fix_message
        self.tag_number = tag_number
        
        super(MultipleTags, self).__init__('Tag %s repeated in %r' % (tag_number, fix_message))
        
class TagNotFound(Exception):
    def __init__(self, fix_message, tag_number):
        self.fix_message = fix_message
        self.tag_number = tag_number
        
        super(TagNotFound, self).__init__('Tag %s not found in %r' % (tag_number, fix_message))
        
class InvalidGroup(Exception):
    def __init__(self, group, first_tag, other_tags):
        self.group = group
        self.first_tag = first_tag
        self.other_tags = other_tags
        
        super(InvalidGroup, self).__init__('Invalid group %r with first tag %s and other tags %r' % (group, first_tag, other_tags))
        
class NotEnoughGroups(Exception):
    def __init__(self, fix_message, count_tag, first_tag, other_tags):
        self.fix_message = fix_message
        self.count_tag = count_tag
        self.first_tag = first_tag
        self.other_tags = other_tags
        
        super(NotEnoughGroups, self).__init__('Not enough groups for count tag %s first tag %s other_tags %r in %r' (count_tag, first_tag, other_tags, fix_message ))

NO_DEFAULT = object()
        
class Message(object):
    
    @classmethod
    def from_socket(cls, socket):
        for ps in cls._parts(socket):
            if ps is None: # timeout
                yield None
                continue
            parts = map(lambda p: p.split("=",1), ps)
            parts = [(int(n), v[:-1]) for n,v in parts]
            
            if len(parts) < 3:
                raise InvalidMessage(parts=parts, cause="Not enough parts. At least fields 8,9 and 10 must be present")
            
            if (8, b'FIXT.1.1') != parts[0]:
                raise InvalidMessage(parts=parts, cause="Invalid BeginString")
            
            if 9 != parts[1][0]:
                raise InvalidMessage(parts=parts, cause="No BodyLength")
            
            declared_body_length = int(parts[1][1])
            real_body_length = sum(len(p) for p in ps[2:-1])
            
            if declared_body_length != real_body_length:
                raise InvalidMessage(parts=parts, cause="Declared length: %s. Real length: %s" % (declared_body_length, real_body_length))
            
            if parts[-1][0] != 10:
                raise InvalidMessage(parts = parts, cause="Does not end with 10 group")
            
            checksum = cls._checksum(*ps[:-1])
            
            if checksum != int(parts[-1][1]):
                raise InvalidChecksum(parts=parts, checksum=checksum)
            
            m = cls(*parts[2:-1])
            yield m 
    
    @classmethod
    def from_string(cls, s):
        return cls.from_socket(MockSocket(s))
    
    def __init__(self, *args):
        
        for p in args:
            self.check_part(p)
        self.parts = list(args)
        
    def __add__(self, other):
        return Message( *itertools.chain(self, other) )
    
    def __eq__(self, other):
        return self.parts == other.parts
        
    def __iter__(self):
        return iter(self.parts)
    
    def __getitem__(self, key):
        item = self.parts.__getitem__(key)
        return self.__class__(*item) if isinstance(item, list) else item

    def __len__(self):
        return len(self.parts)
    
    def __repr__(self):
        return "Message(*%r)" % self.parts
    
    def pprint(self): # Podria usar __str__
        rv = ''    
        for tag, value in self.parts:
            tag_legend = TAG2NAME.get(str(tag), "Unknown") + " ("  + str(tag) + ")"
            if 35 == tag:
                value_legend = MSGTYPE2NAME.get(str(value), "Unknown") + " (" + str(value) + ")"
            else:
                value_legend = value.decode('iso8859-1')
            rv += u'{}: {}\n'.format(tag_legend, value_legend)         
        
        return rv

    def append(self, n, v):
        return self.parts.append((n,v))
    
    def to_buf(self):
        body = b"".join(b"{:d}={}\x01".format(n,v) for n,v in self.parts)
        header = b"8=FIXT.1.1\x019={:d}\x01".format(len(body))
        trailer = b"10=%03d\x01" % self._checksum(header + body)
        
        return header + body + trailer
    
    def get_field(self, n, default=NO_DEFAULT):
        parts = [ v for k,v in self if k == n ]
        
        if 0 == len(parts):
            if default is NO_DEFAULT:
                raise TagNotFound(self, n)
            else:
                return default
        
        if 1 < len(parts):
            raise MultipleTags(self, n)
        
        return parts[0] 
    
    @classmethod
    def group(cls, counting_tag, *args):
        rv = cls((counting_tag, str(len(args))))
        for g in args:
            rv += g
        
        return rv
    
    def get_groups(self, count_tag, first_tag, other_tags):
        
        count_tags = [(pos, int(part[1])) for pos , part in list(enumerate(self)) if part[0] == count_tag]
        
        if 0 == len(count_tags):
            raise TagNotFound(self, count_tag)
        
        if 1 < len(count_tags):
            raise MultipleTags(self, count_tag)
        
        pos, count = count_tags[0] 
        
        if count == 0:
            return []

        pos += 1 # Advance to avoid count field
        if pos >= len(self.parts):
            raise NotEnoughGroups(fix_message=self, count_tag=count_tag, first_tag=first_tag, other_tags=other_tags)
        
        if first_tag != self[pos][0]:
            raise InvalidGroup(group=self[pos:pos+1], first_tag=first_tag, other_tags=other_tags)
        
        starts = [pos]
        
        pos += 1
         
        while len(starts) < count :
            if pos >= len(self):
                raise NotEnoughGroups(fix_message=self, count_tag=count_tag, first_tag=first_tag, other_tags=other_tags)
            if self[pos][0] == first_tag:
                starts.append(pos)
            elif not self[pos][0] in other_tags:
                raise InvalidGroup(group=self[starts[-1]: pos + 1], first_tag=first_tag, other_tags = other_tags) 
            
            pos += 1
            
        last_end = pos
        
        while last_end < len(self) and self[last_end][0] in other_tags:
            last_end += 1
            
        ends = starts[1:] + [last_end]
        
        return [self[s:e] for s,e in zip(starts, ends)]
            
         
            
    @staticmethod
    def _parts(s):
        
        def fetch_next_chunk():
            while True:
                try:
                    return s.read()
                except ssl.SSLWantReadError as e:
                    # Somehow our blocking socket gets non-blocking some times!!!!
                    select.select([s], [], [], 0.1)
                except socket.error as e:
                    if errno.EWOULDBLOCK == e.errno:
                        # Somehow our blocking socket gets non-blocking some times!!!!
                        select.select([s], [], [], 0.1)  
                    else:
                        raise
                         
        """Iterate through messages, yields a list of strings (one for each part) as read from the socket"""
        buf = b""
        current =  []
        while True:
            while True:
                pos = buf.find('\x01')
                if -1 == pos: 
                    break
                part = buf[:pos+1]
                if not "=" in part:
                    raise InvalidPart(part)
                current.append( part )
                n = part.split("=",1)[0]
                if "10" == n: # checksum
                    yield current
                    current = []
                     
                buf = buf[pos+1:]
            
            try: 
                next_chunk = fetch_next_chunk()
                if "" == next_chunk:
                    return
                
            except ssl.SSLError as e:
                if e.message.endswith('timed out'):
                    LOG.info("Time out reading FIX messages")
                    yield None
                    next_chunk = ""
                else:
                    raise e
                
            buf += next_chunk
            
    @staticmethod
    def check_part(part):
        if not isinstance(part, tuple):
            raise InvalidPart(repr(part) + " is not a tuple")
        
        if 2 != len(part):
            raise InvalidPart(repr(part) + " has len different than 2")
        
        if int != type(part[0]):
            raise InvalidPart(repr(part) + " tag not an integer")
        
        if str != type(part[1]):
            raise InvalidPart(repr(part) + " value not a binary string")

    @staticmethod
    def _checksum(*args):
        return sum( sum(ord(c) for c in buf) for buf in args ) % 256
