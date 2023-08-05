import elist.elist as elel
import tlist.tlist as tltl
import edict.edict as eded
import estring.estring as eses
import re
from xdict.jprint import pobj
from xdict.jprint import pdir
from nvhead.consts import *



def underscorize_head_name(name):
    name = name.lower().replace("-","_")
    return(name)

def standlize_head_name(name,headers_ref=HEADERS_REF):
    name = underscorize_head_name(name)
    return(headers_ref[name])

#4 个层面
#s                 head_str    
#sarr              head_sarr   
#tl                head_tlist
#d                 head_dict


def head_s2sarr(s,**kwargs):
    if('mode' in kwargs):
        mode = kwargs['mode']
    else:
        mode = 'loose'
    if(mode == 'loose'):
        s = s.replace('\r','')
        sp = '\n'
    else:
        sp = '\r\n'
    sarr = s.split(sp)
    return(sarr)

def head_sarr2s(sarr,**kwargs):
    s = elel.join(sarr,"\r\n")
    return(s)

def head_s2tl(s,**kwargs):
    '''
        head_str = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36\nAccept-Encoding: gzip,deflate,sdch\nAccept-Language: en;q=1.0, zh-CN;q=0.8'
        tl = head_s2tl(head_str)
    '''
    sarr = head_s2sarr(s,**kwargs)
    tl = head_sarr2tl(sarr,**kwargs)
    return(tl)

def head_tl2s(tl,**kwargs):
    sarr = head_tl2sarr(tl,**kwargs)
    s = head_sarr2s(sarr,**kwargs)
    return(s)

def head_s2d(s,**kwargs):
    tl = head_s2tl(s,**kwargs)
    d = eded.dict2tlist(h)
    return(d)

def head_sarr2tl(sarr,**kwargs):
    tl = []
    regex = re.compile('(.*?):(.*)')
    for i in range(0,sarr.__len__()):
        m = regex.search(sarr[i])
        k = m.group(1)
        v = m.group(2).lstrip("\x20")
        tl.append((k,v))
    return(tl)

def head_tl2sarr(tl,**kwargs):
    sarr = elel.array_map(tl,lambda ele:(ele[0]+': '+ele[1]))
    return(sarr)

def head_sarr2d(sarr,**kwargs):
    tl = head_sarr2tl(sarr,**kwargs)
    d = tltl.tlist2dict(tl)
    return(d)

def head_d2sarr(d,**kwargs):
    tl = eded.dict2tlist(d)
    sarr = head_tl2sarr(tl,**kwargs)
    return(sarr)

def head_tl2d(tl,**kwargs):
    return(tltl.tlist2dict(tl))

def head_d2tl(d,**kwargs):
    return(eded.dict2tlist(d))

#us underscore
def head_update(self,tl):
    d = head_tl2d(tl)
    super(Head,self).__setattr__('_dict',d)
    objt = tltl.Tlist(tl)
    super(Head,self).__setattr__('_tlist',objt)
    kl,vl = objt.kvlists()
    methods = elel.array_map(kl,underscorize_head_name)
    refd_o2u = eded.kvlist2d(kl,methods)
    super(Head,self).__setattr__('_orig2us_ref',refd_o2u)
    refd_u2o = eded.dict_mirror(refd_o2u)
    super(Head,self).__setattr__('_us2orig_ref',refd_u2o)
    lngth = methods.__len__()
    super(Head,self).__setattr__('count',lngth)
    for i in range(0,lngth):
        method = methods[i]
        values = tltl.get_value(self._tlist.tl,kl[i])
        if(values.__len__()==1):
            #setattr(self,method,values[0])
            # self.__dict__[method] = values[0]
            super(Head,self).__setattr__(method,values[0])
        else:
            #setattr(self,method,values)
            # self.__dict__[method] = values
            super(Head,self).__setattr__(method,values)


def update_after_remove(self,tl,name):
    lngth = tltl._indexes_all(tl,key=name).__len__()
    if(lngth == 0):
        usname = self._orig2us_ref[name]
        super(Head,self).__delattr__(usname)
    else:
        pass



#req_head : 不允许重复entry
#res_head : 允许重复entry,例如set_cookie
#for_req  : for request

HEAD_INTERNAL_METHODS = ['str','dict','sarr','tlist','append','prepend','insert','remove','remove_all','uniqualize','uniqualize_all']
HEAD_INTERNAL_VARS =['count','_dict','_orig2us_ref','_us2orig_ref','_tlist']

class Head():
    def __init__(self,h,**kwargs):
        if('for_req' in kwargs):
            for_req = kwargs['for_req']
        else:
            for_req = None
        if('for_res' in kwargs):
            for_res = kwargs['for_res']
        else:
            for_res = None
        if(for_req == None):
            if(for_res == None):
                for_req = True
            else:
                for_req = not(for_res)
        else:
            pass
        ####################################3
        if(isinstance(h,str)):
            tl = head_s2tl(h,**kwargs)
        elif(isinstance(h,list)):
            tl = h
        elif(isinstance(h,dict)):
            tl = head_d2tl(h)
        else:
            print("type {0} header is not supported".format(type(h)))
        super(Head,self).__setattr__('for_req',for_req)
        super(Head,self).__setattr__('for_res',not(for_req))
        if(for_req):
            #req_head : 不允许重复entry
            tl = tltl.uniqualize_all(tl,mode='key')
        else:
            pass
        head_update(self,tl)
    def str(self):
        s = head_tl2s(self._tlist.tl)
        print(s)
        return(s)
    def dict(self):
        pobj(self._dict)
        return(self._dict)
    def tlist(self):
        pobj(self._tlist.tl)
        return(self._tlist.tl)
    def sarr(self):
        sarr = head_tl2sarr(self._tlist.tl)
        pobj(sarr)
        return(sarr)
    def __repr__(self):
        if(self.for_req):
            pobj(self._dict)
        else:
            sarr = head_tl2sarr(self._tlist.tl)
            pobj(sarr)
        return("")
    def __setattr__(self,name,value):
        name = str(name)
        value = str(value)
        if(name in HEAD_INTERNAL_METHODS):
            print("dont modify internal methods {0}".format(name))
        if(name in HEAD_INTERNAL_VARS):
            print("interval vars {0} is readonly".format(name))
        else:
            iname = self._us2orig_ref[name]
            cond = self._tlist.includes(key=iname)
            if(cond):
                self._tlist[iname] = value
            else:
                self._tlist.append(name,value)
            tl = self._tlist.tl
            head_update(self,tl)
    def __delattr__(self,name):
        name = str(name)
        if(name in HEAD_INTERNAL_METHODS):
            print("dont modify internal methods {0}".format(name))
        else:
            iname = self._us2orig_ref[name]
            cond = self._tlist.includes(key=iname)
            if(cond):
                self._tlist.remove_all(key=iname)
            else:
                pass
            tl = self._tlist.tl
            update_after_remove(self,tl,iname)
            head_update(self,tl)
    def __getitem__(self,*args,**kwargs):
        if(isinstance(args[0],tuple)):
            #very special in __getitem__
            args = list(args[0])
            key = args[0]
            key = str(key)
            whiches = elel.array_map(args[1:],int)
            rslt = tltl.get_value(self._tlist.tl,key,whiches=whiches)
        else:
            #very special in __getitem__
            key = args[0]
            key = str(key)
            rslt = tltl.get_value(self._tlist.tl,key)
        if(rslt.__len__() == 1):
            return(rslt[0])
        elif(rslt.__len__() == 0):
            raise(KeyError)
        else:
            return(rslt)
    def __setitem__(self,*args,**kwargs):
        if(isinstance(args[0],tuple)):
            #very special in __setitem__
            value = args[-1]
            value = str(value)
            args = list(args[0])
            key = args[0]
            key = str(key)
            whiches = elel.array_map(args[1:],int)
            rslt = self._tlist.tl
            for which in whiches:
                rslt = tltl.set_which(rslt,key,value,which=which)
        else:
            #very special in __setitem__
            key = args[0]
            key = str(key)
            value = args[-1]
            value = str(value)
            rslt = tltl.set_which(self._tlist.tl,key,value,which='all')
        tl = self._tlist.tl
        if(tltl._includes(tl,key=key)):
            pass
        else:
            tl.append((key,value))
        head_update(self,tl)
        if(rslt.__len__() == 1):
            return(rslt[0])
        else:
            return(rslt)
    def __delitem__(self,*args,**kwargs):
        if(isinstance(args[0],tuple)):
            #very special in __delitem__
            args = list(args[0])
            key = args[0]
            key = str(key)
            whiches = elel.array_map(args[1:],int)
            lngth = self._tlist.tl.__len__()
            tltl._pop_seqs(self._tlist.tl,set(whiches),key=key)
        else:
            #very special in __delitem__
            key = args[0]
            key = str(key)
            tltl._pop_all(self._tlist.tl,key=key)
        tl = self._tlist.tl
        update_after_remove(self,tl,key)
        head_update(self,tl)
    def append(self,name,value,**kwargs):
        if('force' in kwargs):
            force = kwargs['force']
        else:
            force = False
        name = str(name)
        value = str(value)
        cond = self._tlist.includes(key=name)
        if(cond):
            if(self.for_req):
                if(not(force)):
                    print('{0} already exist in headers,and request head did not allow duplicate head name'.format(name))
                else:
                    self._tlist.append(name,value)
                    tl = self._tlist.tl
                    head_update(self,tl)
            else:
                self._tlist.append(name,value)
                tl = self._tlist.tl
                head_update(self,tl)
        else:
            self._tlist.append(name,value)
            tl = self._tlist.tl
            head_update(self,tl)
    def prepend(self,name,value,**kwargs):
        if('force' in kwargs):
            force = kwargs['force']
        else:
            force = False
        name = str(name)
        value = str(value)
        cond = self._tlist.includes(key=name)
        if(cond):
            if(self.for_req):
                if(not(force)):
                    print('{0} already exist in headers,and request head did not allow duplicate head name'.format(name))
                else:
                    self._tlist.prepend(name,value)
                    tl = self._tlist.tl
                    head_update(self,tl)
            else:
                self._tlist.prepend(name,value)
                tl = self._tlist.tl
                head_update(self,tl)
        else:
            self._tlist.prepend(name,value)
            tl = self._tlist.tl
            head_update(self,tl)
    def insert(self,loc,name,value,**kwargs):
        if('force' in kwargs):
            force = kwargs['force']
        else:
            force = False
        name = str(name)
        value = str(value)
        cond = self._tlist.includes(key=name)
        if(cond):
            if(self.for_req):
                if(not(force)):
                    print('{0} already exist in headers,and request head did not allow duplicate head name'.format(name))
                else:
                    self._tlist.insert(loc,name,value)
                    tl = self._tlist.tl
                    head_update(self,tl)
            else:
                self._tlist.insert(loc,name,value)
                tl = self._tlist.tl
                head_update(self,tl)
        else:
            self._tlist.insert(loc,name,value)
            tl = self._tlist.tl
            head_update(self,tl)
    def remove(self,name,*args,**kwargs):
        if(args.__len__()==0):
            which = 0
        else:
            which = int(args[0])
        name = str(name)
        self._tlist.remove_which(which,key=name)
        tl = self._tlist.tl
        update_after_remove(self,tl,name)
        head_update(self,tl)
    def remove_all(self,name,**kwargs):
        name = str(name)
        self._tlist.remove_all(key=name)
        tl = self._tlist.tl
        update_after_remove(self,tl,name)
        head_update(self,tl)
    def uniqualize(self,name,**kwargs):
        name = str(name)
        self._tlist.uniqualize(name)
        tl = self._tlist.tl
        head_update(self,tl)
    def uniqualize_all(self,**kwargs):
        self._tlist.uniqualize_all(mode="key")
        tl = self._tlist.tl
        head_update(self,tl)
