import elist.elist as elel
import tlist.tlist as tltl
import edict.edict as eded
import estring.estring as eses
import re
from xdict.jprint import pobj
from xdict.jprint import pdir
from nvhead.consts import *

#################
def is_sarr(one):
    if(isinstance(one,list)):
        if(one.__len__()==0):
            return(True)
        else:
            if(isinstance(one[0],str)):
                return(True)
            else:
                return(False)
    else:
        return(False)

def is_darr(one):
    if(isinstance(one,list)):
        if(one.__len__()==0):
            return(True)
        else:
            if(isinstance(one[0],dict)):
                return(True)
            else:
                return(False)
    else:
        return(False)

#################
def fmt_one(s):
    s = eses.replace(s,re.compile("[\x20]+"),'\x20')
    s = s.replace(':\x20',':')
    s = s.replace(',\x20',',')
    s = s.replace(':',':\x20')
    s = s.replace(',',',\x20')
    return(s)

def one_s2t(s,**kwargs):
    '''
        single http head string to tuple
    '''
    s = fmt_one(s)
    regex = re.compile('(.*?):\x20(.*)')
    m = regex.search(s)
    if(m):
        name = m.group(1)
        body = m.group(2)
    else:
        name = ''
        body = s
    return((name,body))

def one_t2s(t,**kwargs):
    name = t[0]
    body = t[1]
    body = fmt_one(body)
    if(name == ""):
        s = body
    else:
        s = name +":\x20"+body
    return(s)

#################
# s = '''Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'''
# s = '''text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8'''
# RFC 7231,Page 38,If no "q" parameter is present,the default weight is 1.

def type_subtype_q_fmt(s):
    s = s.replace(";\x20",";")
    s = s.replace("\x20;",";")
    s = s.replace("\x20;\x20",";")
    return(s)

def type_subtype_q_s2sarr(s,**kwargs):
    s = type_subtype_q_fmt(s)
    name,body = one_s2t(s)
    sarr = body.split(",\x20")
    return(sarr)

def type_subtype_q_ele_s2d(ele,sp='/',**kwargs):
    arr = ele.split(sp)
    type = arr[0]
    tmp = arr[1]
    if(";q=" in tmp):
        arr2 = tmp.split(";q=")
        subtype = arr2[0]
        q = arr2[1]
    else:
        subtype = tmp
        q = None
    d = {
        'type':type,
        'subtype':subtype,
        'q':q
    }
    return(d)

def type_subtype_q_ele_d2s(d,sp='/',**kwargs):
    if(d["q"] == None):
        s = d['type'] + sp + d['subtype']
    else:
        s = d['type'] + sp + d['subtype'] + ';q=' + str(d['q'])
    return(s)

def type_subtype_q_sarr2darr(sarr,sp='/',**kwargs):
    darr = elel.array_map(sarr,type_subtype_q_ele_s2d,sp)
    return(darr)

def type_subtype_q_darr2sarr(darr,sp='/',**kwargs):
    sarr = elel.array_map(darr,type_subtype_q_ele_d2s,sp)
    return(sarr)

def type_subtype_q_cond_slct(sarr,key,match_value):
    darr = type_subtype_q_sarr2darr(sarr)
    darr = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele[key]==match_value))
    sarr = type_subtype_q_darr2sarr(darr)
    return(sarr)

def type_subtype_q_cond_slct_not(sarr,key,match_value):
    darr = type_subtype_q_sarr2darr(sarr)
    darr = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele[key]!=match_value))
    sarr = type_subtype_q_darr2sarr(darr)
    return(sarr)

def type_subtype_q_floatize(dele):
        if(dele['q'] == None):
            dele['q'] = 1.0
        else:
            dele['q'] = float(dele['q'])
        return(dele)

def type_subtype_q_sort_by_q(darr):
    darr1 = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele['q']==None))
    darr2 = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele['q']!=None))
    ndarr1 = elel.sortDictList(darr1,cond_keys=['q','type','subtype'],reverse=True)
    idarr2 = elel.array_map(darr2,type_subtype_q_floatize)
    ndarr2 = elel.sortDictList(darr2,cond_keys=['q','type','subtype'],reverse=True)
    ndarr = elel.concat(ndarr1,ndarr2)
    return(ndarr)

class TypeSubtypeQ():
    def __init__(self,one,**kwargs):
        if(isinstance(one,str)):
            self.sarr = type_subtype_q_s2sarr(one)
            self.darr = type_subtype_q_sarr2darr(self.sarr)
        elif(is_sarr(one)):
            self.sarr = one
            self.darr = type_subtype_q_sarr2darr(self.sarr)
        else:
            self.sarr = type_subtype_q_darr2sarr(one)
            self.darr = one
    def __repr__(self):
        pobj(self.sarr)
        return("")
    def str(self):
        s = elel.join(self.sarr,",\x20")
        print(s)
        return(s)
    def qsort(self):
        self.darr = type_subtype_q_sort_by_q(self.darr)
        self.sarr = type_subtype_q_darr2sarr(self.darr)
        pobj(self.sarr)
    def modify(self,func,*func_args,**func_kwargs):
        self.sarr = func(self.sarr,*func_args,**func_kwargs)
        self.darr = type_subtype_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_not_type(self,typename):
        self.sarr =type_subtype_q_cond_slct(self.sarr,'type',typename)
        self.darr = type_subtype_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_type(self,typename):
        self.sarr =type_subtype_q_cond_slct_not(self.sarr,'type',typename)
        self.darr = type_subtype_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_not_subtype(self,subtypename):
        self.sarr =type_subtype_q_cond_slct(self.sarr,'subtype',subtypename)
        self.darr = type_subtype_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_subtype(self,subtypename):
        self.sarr =type_subtype_q_cond_slct_not(self.sarr,'subtype',subtypename)
        self.darr = type_subtype_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_q(self,cond_func):
        indexes = elel.cond_select_indexes_all(self.darr,cond_func = lambda ele:(ele['q']==None))
        idarr = elel.array_map(self.darr,type_subtype_q_floatize)
        orig_indexes = elel.cond_select_indexes_all(idarr,cond_func=cond_func)
        idarr = elel.cond_select_values_all(idarr,cond_func=cond_func)
        for index in indexes:
            curr_index = orig_indexes.index(index)
            idarr[curr_index]['q'] = None
        self.darr = idarr
        self.sarr = type_subtype_q_darr2sarr(self.darr)
        pobj(self.sarr)
    def append(self,*args):
        if(args.__len__()==1):
            if(isinstance(args[0],dict)):
                self.darr.append(args[0])
                self.sarr = type_subtype_q_darr2sarr(args[0])
            elif( "/" in args[0]):
                self.sarr.append(args[0])
                self.darr = type_subtype_q_sarr2darr(self.sarr)
            else:
                print("invalid")
                # self.sarr = type_subtype_q_s2sarr(args[0])
                # self.darr = type_subtype_q_sarr2darr(self.sarr)
        elif(args.__len__()==2):
            self.darr.append({"type":args[0],"subtype":args[1],"q":None})
            self.sarr = type_subtype_q_darr2sarr(self.darr)
        elif(args.__len__()==3):
            self.darr.append({"type":args[0],"subtype":args[1],"q":str(args[2])})
            self.sarr = type_subtype_q_darr2sarr(self.darr)
        pobj(self.sarr)

##########################

# s = '''Accept-Charset: gb2312;q=0.3, utf-8, iso-8859-1;q=0.5, *;q=0.1'''

def type_q_fmt(s):
    s = s.replace(";\x20",";")
    s = s.replace("\x20;",";")
    s = s.replace("\x20;\x20",";")
    return(s)

def type_q_s2sarr(s,**kwargs):
    s = type_q_fmt(s)
    name,body = one_s2t(s)
    sarr = body.split(",\x20")
    return(sarr)

def type_q_ele_s2d(ele,**kwargs):
    if(";q=" in ele):
        arr2 = ele.split(";q=")
        type = arr2[0]
        q = arr2[1]
    else:
        type = ele
        q = None
    d = {
        'type':type,
        'q':q
    }
    return(d)

def type_q_ele_d2s(d,**kwargs):
    if(d["q"] == None):
        s = d['type'] 
    else:
        s = d['type'] + ';q=' + str(d['q'])
    return(s)

def type_q_sarr2darr(sarr,**kwargs):
    darr = elel.array_map(sarr,type_q_ele_s2d)
    return(darr)

def type_q_darr2sarr(darr,**kwargs):
    sarr = elel.array_map(darr,type_q_ele_d2s)
    return(sarr)

def type_q_cond_slct(sarr,key,match_value):
    darr = type_q_sarr2darr(sarr)
    darr = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele[key]==match_value))
    sarr = type_q_darr2sarr(darr)
    return(sarr)

def type_q_cond_slct_not(sarr,key,match_value):
    darr = type_q_sarr2darr(sarr)
    darr = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele[key]!=match_value))
    sarr = type_q_darr2sarr(darr)
    return(sarr)

def type_q_floatize(dele):
        if(dele['q'] == None):
            dele['q'] = 1.0
        else:
            dele['q'] = float(dele['q'])
        return(dele)

def type_q_sort_by_q(darr):
    darr1 = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele['q']==None))
    darr2 = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele['q']!=None))
    ndarr1 = elel.sortDictList(darr1,cond_keys=['q','type'],reverse=True)
    idarr2 = elel.array_map(darr2,type_q_floatize)
    ndarr2 = elel.sortDictList(darr2,cond_keys=['q','type'],reverse=True)
    ndarr = elel.concat(ndarr1,ndarr2)
    return(ndarr)


class TypeQ():
    def __init__(self,one,**kwargs):
        if(isinstance(one,str)):
            self.sarr = type_q_s2sarr(one)
            self.darr = type_q_sarr2darr(self.sarr)
        elif(is_sarr(one)):
            self.sarr = one
            self.darr = type_q_sarr2darr(self.sarr)
        else:
            self.sarr = type_q_darr2sarr(one)
            self.darr = one
    def __repr__(self):
        pobj(self.sarr)
        return("")
    def str(self):
        s = elel.join(self.sarr,",\x20")
        print(s)
        return(s)
    def qsort(self):
        self.darr = type_q_sort_by_q(self.darr)
        self.sarr = type_q_darr2sarr(self.darr)
        pobj(self.sarr)
    def modify(self,func,*func_args,**func_kwargs):
        self.sarr = func(self.sarr,*func_args,**func_kwargs)
        self.darr = type_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_not_type(self,typename):
        self.sarr =type_q_cond_slct(self.sarr,'type',typename)
        self.darr = type_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_type(self,typename):
        self.sarr =type_q_cond_slct_not(self.sarr,'type',typename)
        self.darr = type_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_q(self,cond_func):
        indexes = elel.cond_select_indexes_all(self.darr,cond_func = lambda ele:(ele['q']==None))
        idarr = elel.array_map(self.darr,type_q_floatize)
        orig_indexes = elel.cond_select_indexes_all(idarr,cond_func=cond_func)
        idarr = elel.cond_select_values_all(idarr,cond_func=cond_func)
        for index in indexes:
            curr_index = orig_indexes.index(index)
            idarr[curr_index]['q'] = None
        self.darr = idarr
        self.sarr = type_q_darr2sarr(self.darr)
        pobj(self.sarr)
    def append(self,*args):
        if(args.__len__()==1):
            if(isinstance(args[0],dict)):
                self.darr.append(args[0])
                self.sarr = type_q_darr2sarr(args[0])
            else:
                self.darr.append({"type":args[0],"q":None})
                self.sarr = type_q_darr2sarr(self.darr)
        else:
            self.darr.append({"type":args[0],"q":str(args[1])})
            self.sarr = type_q_darr2sarr(self.darr)
        pobj(self.sarr)


##########@@@@@#############
#s = '''en;q=0.8, de;q=0.7, *;q=0.5, fr-CH, fr;q=0.9, sr-Lat'''


def language_locale_q_fmt(s):
    s = s.replace(";\x20",";")
    s = s.replace("\x20;",";")
    s = s.replace("\x20;\x20",";")
    return(s)

def language_locale_q_s2sarr(s,**kwargs):
    s = language_locale_q_fmt(s)
    name,body = one_s2t(s)
    sarr = body.split(",\x20")
    return(sarr)

def language_locale_q_ele_s2d(ele,sp='-',**kwargs):
    if(sp in ele):
        arr = ele.split(sp)
        language = arr[0]
        tmp = arr[1]
        if(";q=" in tmp):
            arr2 = tmp.split(";q=")
            locale = arr2[0]
            q = arr2[1]
        else:
            locale = tmp
            q = None
    else:
        if(";q=" in ele):
            arr2 = ele.split(";q=")
            language = arr2[0]
            locale = None
            q = arr2[1]
        else:
            language = ele
            locale = None
            q = None
    d = {
        'language':language,
        'locale':locale,
        'q':q
    }
    return(d)

def language_locale_q_ele_d2s(d,sp='-',**kwargs):
    if((d["q"] == None) & (d["locale"] == None)):
        s = d['language']
    elif((d["q"] == None) & (d["locale"] != None)):
        s = d['language'] + sp + d['locale']
    elif((d["q"] != None) & (d["locale"] == None)):
        s = d['language'] + ';q=' + str(d['q'])
    else:
        s = d['language'] + sp + d['locale'] + ';q=' + str(d['q'])
    return(s)

def language_locale_q_sarr2darr(sarr,sp='-',**kwargs):
    darr = elel.array_map(sarr,language_locale_q_ele_s2d,sp)
    return(darr)

def language_locale_q_darr2sarr(darr,sp='-',**kwargs):
    sarr = elel.array_map(darr,language_locale_q_ele_d2s,sp)
    return(sarr)

def language_locale_q_cond_slct(sarr,key,match_value):
    darr = language_locale_q_sarr2darr(sarr)
    darr = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele[key]==match_value))
    sarr = language_locale_q_darr2sarr(darr)
    return(sarr)

def language_locale_q_cond_slct_not(sarr,key,match_value):
    darr = language_locale_q_sarr2darr(sarr)
    darr = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele[key]!=match_value))
    sarr = language_locale_q_darr2sarr(darr)
    return(sarr)

def language_locale_q_floatize(dele):
        if(dele['q'] == None):
            dele['q'] = 1.0
        else:
            dele['q'] = float(dele['q'])
        return(dele)

def language_locale_q_sort_by_q(darr):
    darr1 = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele['q']==None))
    darr2 = elel.cond_select_values_all(darr,cond_func = lambda ele:(ele['q']!=None))
    ndarr1 = elel.sortDictList(darr1,cond_keys=['q','language','locale'],reverse=True)
    idarr2 = elel.array_map(darr2,language_locale_q_floatize)
    ndarr2 = elel.sortDictList(darr2,cond_keys=['q','language','locale'],reverse=True)
    ndarr = elel.concat(ndarr1,ndarr2)
    return(ndarr)


class LanguageLocaleQ():
    def __init__(self,one,**kwargs):
        if(isinstance(one,str)):
            self.sarr = language_locale_q_s2sarr(one)
            self.darr = language_locale_q_sarr2darr(self.sarr)
        elif(is_sarr(one)):
            self.sarr = one
            self.darr = language_locale_q_sarr2darr(self.sarr)
        else:
            self.sarr = language_locale_q_darr2sarr(one)
            self.darr = one
    def __repr__(self):
        pobj(self.sarr)
        return("")
    def str(self):
        s = elel.join(self.sarr,",\x20")
        print(s)
        return(s)
    def qsort(self):
        self.darr = language_locale_q_sort_by_q(self.darr)
        self.sarr = language_locale_q_darr2sarr(self.darr)
        pobj(self.sarr)
    def modify(self,func,*func_args,**func_kwargs):
        self.sarr = func(self.sarr,*func_args,**func_kwargs)
        self.darr = language_locale_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_not_language(self,languagename):
        self.sarr =language_locale_q_cond_slct(self.sarr,'language',languagename)
        self.darr = language_locale_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_language(self,languagename):
        self.sarr =language_locale_q_cond_slct_not(self.sarr,'language',languagename)
        self.darr = language_locale_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_not_locale(self,localename):
        self.sarr =language_locale_q_cond_slct(self.sarr,'locale',localename)
        self.darr = language_locale_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_locale(self,localename):
        self.sarr =language_locale_q_cond_slct_not(self.sarr,'locale',localename)
        self.darr = language_locale_q_sarr2darr(self.sarr)
        pobj(self.sarr)
    def rm_q(self,cond_func):
        indexes = elel.cond_select_indexes_all(self.darr,cond_func = lambda ele:(ele['q']==None))
        idarr = elel.array_map(self.darr,language_locale_q_floatize)
        orig_indexes = elel.cond_select_indexes_all(idarr,cond_func=cond_func)
        idarr = elel.cond_select_values_all(idarr,cond_func=cond_func)
        for index in indexes:
            curr_index = orig_indexes.index(index)
            idarr[curr_index]['q'] = None
        self.darr = idarr
        self.sarr = language_locale_q_darr2sarr(self.darr)
        pobj(self.sarr)
    def append(self,*args):
        if(args.__len__()==1):
            if(isinstance(args[0],dict)):
                self.darr.append(args[0])
                self.sarr = language_locale_q_darr2sarr(args[0])
            elif( '-' in args[0]):
                self.sarr.append(args[0])
                self.darr = language_locale_q_sarr2darr(self.sarr)
            else:
                print("invalid")
        elif(args.__len__()==2):
            if(isinstance(args[1],str)):
                self.darr.append({"language":args[0],"locale":args[1],"q":None})
            else:
                self.darr.append({"language":args[0],"locale":None,"q":str(args[1])})
            self.sarr = language_locale_q_darr2sarr(self.darr)
        elif(args.__len__()==3):
            self.darr.append({"language":args[0],"locale":args[1],"q":str(args[2])})
            self.sarr = language_locale_q_darr2sarr(self.darr)
        pobj(self.sarr)



######

def comma_fmt(s):
    s = s.replace(";\x20",";")
    s = s.replace("\x20;",";")
    s = s.replace("\x20;\x20",";")
    return(s)

def comma_s2sarr(s,**kwargs):
    s = type_q_fmt(s)
    name,body = one_s2t(s)
    sarr = body.split(",\x20")
    return(sarr)


class Comma():
    def __init__(self,one,**kwargs):
        if(isinstance(one,list)):
            self.sarr = one
            self.str = elel.join(self.sarr,",\x20")
        else:
            self.str = comma_fmt(one)
            self.sarr = comma_s2sarr(self.str)
    def __repr__(self):
        pobj(self.sarr)
        return("")


#####


