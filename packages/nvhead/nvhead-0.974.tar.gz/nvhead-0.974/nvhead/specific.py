from nvhead.consts import *
from nvhead.common import *


class Accept(TypeSubtypeQ):
    def __init__(self,one,**kwargs):
        super(Accept,self).__init__(one,**kwargs)
        self.header_type = "req"
        self.forbidden_header_name = False
        self.cros_safelisted_request_header = True


class AcceptCharset(TypeQ):
    def __init__(self,one,**kwargs):
        super(AcceptCharset,self).__init__(one,**kwargs)
        self.header_type = "req"
        self.forbidden_header_name = False


#####
class AcceptEncoding(TypeQ):
    def __init__(self,one,**kwargs):
        super(AcceptEncoding,self).__init__(one,**kwargs)
        self.header_type = "req"
        self.forbidden_header_name = False
    def directives(self):
        #kl = ["gzip","compress","deflate","br","identity","*"]
        #vl = ["LZ77","LZW","zlib_deflate","brotli","no compression","no preference"]
        #d = eded.kvlist2d(kl,vl)
        d = {
            'gzip': 'LZ77',
            'compress': 'LZW',
            'deflate': 'zlib_deflate',
            'br': 'brotli',
            'identity': 'no compression',
            '*': 'no preference'
        }
        pobj(d)

class AcceptLanguage(LanguageLocaleQ):
    def __init__(self,one,**kwargs):
        super(AcceptLanguage,self).__init__(one,**kwargs)
        self.header_type = "req"
        self.forbidden_header_name = False
        self.cros_safelisted_request_header = True



######

class AcceptRange():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "res"
        self.forbidden_header_name = False
    def directives(self):
        pobj(["none","bytes"])

class AccessControlAllowCredentials():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "res"
        self.forbidden_header_name = False

class AccessControlAllowOrigin():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "res"
        self.forbidden_header_name = False

class AccessControlMaxAge():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "res"
        self.forbidden_header_name = False


class AccessControlAllowHeaders(Comma):
    def __init__(self,one,**kwargs):
        super(AccessControlAllowHeaders,self).__init__(one,**kwargs)
        self.header_type = "res"
        self.forbidden_header_name = False


class AccessControlAllowMethods(Comma):
    def __init__(self,one,**kwargs):
        super(AccessControlAllowMethods,self).__init__(one,**kwargs)
        self.header_type = "res"
        self.forbidden_header_name = False
    def directives(self):
        pobj(["GET","HEAD","POST","PUT","DELETE","CONNECT","OPTIONS","TRACE","PATCH"])

class AccessControlExposeHeaders(Comma):
    def __init__(self,one,**kwargs):
        super(AccessControlExposeHeaders,self).__init__(one,**kwargs)
        self.header_type = "res"
        self.forbidden_header_name = False
    def directives(self):
        print("by default the below six are exposed")
        pobj(["Cache-Control","Content-Language","Content-Type","Expires","Last-Modified","Pragma"])


class AccessControlRequestHeaders(Comma):
    def __init__(self,one,**kwargs):
        super(AccessControlRequestHeaders,self).__init__(one,**kwargs)
        self.header_type = "req"
        self.forbidden_header_name = True


class AccessControlRequestMethod():
    def __init__(self,one,**kwargs):
        self.str = one
        self.header_type = "req"
        self.forbidden_header_name = True
    def directives(self):
        print("one of the below http method")
        pobj(["GET","HEAD","POST","PUT","DELETE","CONNECT","OPTIONS","TRACE","PATCH"])


######################


