class BaseApp(object):
    def __init__(self, upper_klass=None, lower_app=None, send = None):
        self.upper_app = upper_klass(lower_app=self) if upper_klass else None
        self.lower_app = lower_app
        
    def _on_msg_in(self, message):
        message = self.on_msg_in(message)
        if message and self.upper_app:
            message = self.upper_app._on_msg_in(message)
            
        return message
    
    def on_msg_in(self, message):
        "Override to define what to do on the message. Return message to be passed to the upper app. If none stop processing"
        return message
    
    def _on_msg_not_rcvd(self, message):
        message = self.on_msg_not_rcvd(message)
        if message and self.upper_app:
            message = self.upper_app._on_msg_not_rcvd(message)
            
        return message
    
    def on_msg_not_rcvd(self, message):
        "Override to define what to do on the message. Return message to be passed to the upper app. If none stop processing"
        return message

    
    def send(self, message):
        message = self.on_send_request(message)
        if message:
            return self.lower_app.send(message)
    
    def on_send_request(self, message):
        "Override to define what to send. Return message to be sent. If none stop processing"
        return message
    
def stack(*args):
    "Build stack of apps. Each parameter is for a layer in the stack. Bottom first"
    
    if not args:
        raise Exception("Cannot make empty stack")
    
    if 1 == len(args):
        raise Exception("Cannot make stack of a single layer. Just run the app constructor!")
    
    # Generate upper constructor
    klass, kwargs = args[-1]
    upper_klass = (lambda klass, kwargs: lambda lower_app: klass(lower_app=lower_app, **kwargs))(klass, kwargs)
    
    def build_constructor(klass, kwargs, upper_klass):
        return lambda lower_app: klass(lower_app=lower_app, upper_klass=upper_klass, **kwargs)

    # Chain middle    
    for klass, kwargs in reversed(args[1:-1]): 
        upper_klass = build_constructor(klass, kwargs, upper_klass)
    
    # Generate base and return
    klass, kwargs = args[0]
    return klass(upper_klass=upper_klass, **kwargs)

def on(type_):
    def decorator(f):
        f.on_type = type_
        return f
    
    return decorator

class ByMessageTypeApp(BaseApp):
    
    def __init__(self, *args, **kwargs):
        
        self.handlers = {}
        
        for n in dir(self):
            a = getattr(self, n)
            t = getattr(a, "on_type", None)
            if t:
                self.handlers[t] = a
        
        super(ByMessageTypeApp, self).__init__(*args, **kwargs)
    
    def on_msg_in(self, message):
        t = message.get_field(35)
        return self.handlers.get(
            t, self.on_unhandled
        )(message)
    
    def on_unhandled(self, message):
        return message
