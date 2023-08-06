import ssl
import socket
import hashlib
import functools
import logging

logger = logging.getLogger(__name__)

class InvalidFingerprint(Exception): pass

def client_socket_builder(*args, **kwargs):
    return functools.partial(ssl_connect, *args, **kwargs)

def ssl_connect(host, port, fingerprints, timeout=None):
    try:
        fingerprints = [f.replace(":","").lower() for f in fingerprints]
        rv = ssl.wrap_socket(socket.socket(socket.AF_INET,socket.SOCK_STREAM))
        rv.settimeout(timeout)
        rv.connect((host, port))
        rv.do_handshake(True)
        
        fingerprint = hashlib.sha256(rv.getpeercert(True)).hexdigest()
        
        if not fingerprint in fingerprints:
            rv.close()
            raise InvalidFingerprint(fingerprint)
        
        return rv
    
    except IOError:
        logger.exception("Error conection to %s:%s" % (host, port))
        return None

def close(s):
    try:
        s.shutdown(socket.SHUT_RDWR)
        s.close()
    except:
        # ignore errors.
        pass


class MockSocket(object):
    def __init__(self, *args):
        self.parts_to_read = args
        self.written_parts = []
        
    def read(self):
        if not self.parts_to_read:
            return ""
        
        rv = self.parts_to_read[0]
        self.parts_to_read = self.parts_to_read[1:]
        
        if rv is None:
            raise ssl.SSLError("Simulating a socket that timed out")
        
        return rv
    
    def sendall(self, buf):
        self.written_parts.append(buf)
        
    def shutdown(self, ignored):
        pass
    
    def close(self):
        pass
    
    def settimeout(self, ignored):
        pass
    
