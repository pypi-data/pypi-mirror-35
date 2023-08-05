#python3
#make:kele email:kele@masong.me
import warnings
warnings.filterwarnings("ignore")#忽略警告

class fleader():
    #===============请求类=========================================
    @staticmethod#请求器
    def get(url,data='',cookie='',ip='',timeout=60,headers='',encode='',redect=True,timetry=3,files='',session='',prce='',ex='',tail='',rw='',cache=False):
        import requests
        parm=fleader.struct_parm({'url':url,'data':data,'headers':headers,'cookie':cookie})#构造器
        if session=='':
            s=requests
        else:
            s=session#requests.Session()#同步cookies
        if ip!='':
            ip={"http": ip,"https": ip}
        if cache:#文件缓存
            hash=fleader.md5(parm['url']+str(data))#参数哈希待调优
            state,res_text=fleader.rwcache(hash,suffix='.html')
            if state:
                return fleader.ex(res_text,ex)
        response,try_time=None,1
        while 1:
            try:
                if data=='':
                    response=s.get(parm['url'],headers=parm['headers'],proxies=ip,timeout=timeout,verify=False,allow_redirects=redect)
                    response.par={'url':parm['url'],'action':'get','headers':parm['headers'],'proxies':ip,'timeout':timeout,'verify':False,'allow_redirects':redect}
                else:
                    response=s.post(parm['url'],headers=parm['headers'],proxies=ip,data=parm['data'],timeout=timeout,files=files,verify=False,allow_redirects=redect)   
                    response.par={'url':parm['url'],'action':'post','headers':parm['headers'],'proxies':ip,'data':parm['data'],'timeout':timeout,'verify':False,'allow_redirects':redect}
                if response.status_code!=None:
                    break
            except Exception as e:
                try_time+=1
                if try_time>timetry:
                    if ex!='':
                        return 404,e
                    else:
                        return e
        if response.status_code==200:
            if encode=='':
                encode=fleader._get_encode(response,'html')
            response.encoding=encode
            res_text=response.text
            res_text=fleader.filter(res_text,prce)
            if rw!='':
                fleader.rw(rw, res_text,aw='w')
            if cache:
                if len(res_text)>0:
                    fleader.rwcache(hash,res_text,suffix='.html')
            return fleader.filter(fleader.ex(res_text,ex,response),tail)
        else:
            if response.status_code==302:
                return response.status_code,response.headers
            if ex!='':
                return response.status_code,''
            return response.status_code,response

    @staticmethod#文本拦截器
    def filter(res_text,filter=''):
        if type(filter)==list:
            if filter[0]=='rpc':
                res_text=fleader.rpc(res_text,list(filter[1]))
                return res_text
            if filter[0]=='func':
                res_text=filter[1](res_text)
                return res_text                
        if filter=='emoji':
            res_text=fleader.filter_emoji(res_text)
            return res_text
        if filter=='xa0':
            res_text=fleader.rpc(res_text,['\xbb','\xa9','\xa0'])
            # '\ue606','\ue619','\ue607','\ue60c','\ue604','\ue61b','\ue61a','\ue60f'
            return res_text
        return res_text
               
    @staticmethod#文本处理器
    def ex(res_text,ex='',rp=None):
        if type(ex)==list:
            if ex[0]=='mid':
                rt=fleader.mid(res_text,ex[1],ex[2])
                return res_text,rt
            if ex[0]=='re':
                import re
                rt=re.findall(ex[1], res_text)  
                return res_text,rt
            if ex[0]=='func':
                res_text=ex[1](res_text)
                return res_text
        if ex=='bs4':
            import bs4
            soup=bs4.BeautifulSoup(res_text,"html.parser")
            return res_text,soup
        if ex=='xpath':
            from lxml import etree
            selector=etree.HTML(res_text)
            return res_text,selector
        if ex=='jq':
            from lxml import etree
            from pyquery import PyQuery as pq
            try:
                doc = pq(etree.fromstring(res_text))
            except:
                doc = pq(res_text)
            return res_text,doc
        if ex=='json':
            import json
            js=json.loads(res_text)
            return res_text,js
        if ex=='btf':
            import bs4
            soup=bs4.BeautifulSoup(res_text,"html.parser")
            return soup.prettify() 
        if ex=='rp':
            return rp,res_text   
        if ex=='par':
            return rp.par,res_text        
        return res_text

    @staticmethod#编码处理器
    def _get_encode(response,type='html'):
        import requests
        if type=='html':
            rxt=response.text
            encodings = requests.utils.get_encodings_from_content(rxt)
            if encodings:
                return encodings[0]
            else:
                return response.apparent_encoding
        if type=='text':
            try:
                with open(response, 'r', encoding='utf-8') as f:
                    f.read()
                    encoding='utf-8'                     
            except:
                encoding='gbk'
            return encoding
    @staticmethod        
    def f2h(txt):#fiddler转header
        arr=txt.split("\n")
        headers={}
        for i in arr:
            if ": " in i:
                ic=i.split(": ")
                headers[ic[0].replace("\t","").replace(" ","")]=ic[1]            
        return headers

    @staticmethod#参数构造器
    def struct_parm(parm):
        if 'headers' in parm:
            cookie=''
            if 'cookie' in parm:
                cookie=parm['cookie']
            parm['headers']=fleader.struct_headers(parm['headers'],cookie)
        if 'url' in parm:
            parm['url']=fleader.struct_url(parm['url'])
        if 'data' in parm:
            parm['data']=fleader.struct_data(parm['data'])
        return parm

    @staticmethod    
    def struct_headers(header,cookie):
        header_s = {"User-Agent":fleader.rua()}#生成最新ua
        if type(header)==str and header!='':
            header=fleader.f2h(header)
        if type(header)==list:
            hd1,hd2=header
            hd=fleader.f2h(hd1)
            hd.update(hd2)
            header=hd
        if header!='':
            header_s.update(header)#更新ua   
        if cookie!='':
            header_s['cookie']=cookie
        header=header_s  
        return header

    @staticmethod    
    def struct_url(url):
        if url[:4]!='http':
            url=r'http://'+url
        if type(url)==list:
            urlc,parc=url
            if r'?' in urlc:
                urld=urlc.split('?')
                urldd,pardd=urld
                parddd=pardd.split('&')
                dd={}
                for d in parddd:
                    if '=' in d:
                        d1,d2=d.split('=')
                        dd[d1]=d2
                dd.update(parc)
                urlc,parc=urldd,dd
            par=''
            for key in parc:
                par=par+key+"="+str(parc[key])+"&";
            url=urlc+"?"+par[:-1]
        return url

    @staticmethod    
    def struct_data(data):
        if type(data)==str and data!='':
            import urllib.parse
            mdata=map(lambda i:i.split('='),urllib.parse.unquote(data).split('&'))
            data={}
            for i in mdata:
                if i[0] not in data:
                    data[i[0]]=i[1]
                else:
                    if type(data[i[0]])==str:
                        data[i[0]]=[data[i[0]]]
                    if type(data[i[0]])==list:
                        data[i[0]].append(i[1])
        return data

    @staticmethod#图片下载器
    def u2f(url,path,headers=""):   
        if headers=="":
            header_s = {"User-Agent":fleader.rua()}
        content=requests.get(url,headers=headers,stream=True,verify=False,timeout=60).content
        fleader.rw(path,content,aw='wb')
        
    @staticmethod#最新浏览器随机useragent
    def rua(lang="zh-CN"):
        import random
        #header_s = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'}
        user_agent_list = [
            'Mozilla/5.0 (Windows NT {WindowsNT};{WOW64}{language} rv:{Firefox}) Gecko/{builddata} Firefox/{Firefox}'.format(
            **{'WindowsNT': fleader._wc(["6.1","6.2","6.3","10.0"],[3,2,2,3]),'WOW64':fleader._wc([""," WOW64;"," Win64;"," x64;"],[3,4,2,1]),'language':fleader._wc([""," {};".format(lang)],[6,4]),'builddata':random.choice(["201{}0{}{}".format(random.randint(0, 6),random.randint(1, 9), random.randint(10, 28))]), 'Firefox': random.choice(["50.0.1","50.0.2","50.0","50.01","50.010","50.011","50.02","50.03","50.04","50.05","50.06","50.07","50.08","50.09","50.1.0","51.0.1","51.0","51.01","51.010","51.011","51.012","51.013","51.014","51.02","51.03","51.04","51.05","51.06","51.07","51.08","51.09","52.0.1","52.0.2","52.0","52.01","52.02","52.03","52.04","52.05","52.06","52.07","52.08","52.09","52.1.0","52.1.1","52.1.2","52.2.0","52.2.1","52.3.0","52.4.0","52.4.1","53.0.2","53.0.3","53.0","53.01","53.010","53.02","53.03","53.04","53.05","53.06","53.07","53.08","53.09","54.0.1","54.0","54.01","54.010","54.011","54.012","54.013","54.02","54.03","54.04","54.05","54.06","54.07","54.08","54.09","55.0.1","55.0.2","55.0.3","55.0","55.01","55.010","55.011","55.012","55.013","55.02","55.03","55.04","55.05","55.06","55.07","55.08","55.09","56.0.1","56.0","56.01","56.010","56.011","56.012","56.02","56.03","56.04","56.05","56.06","56.07","56.08","56.09","57.03","57.04","57.05","57.06"]), }),
            'Mozilla/5.0 (Windows NT {WindowsNT};{WOW64}{language}) AppleWebKit/{Safari} (KHTML, like Gecko) Chrome/{Chrome} Safari/{Safari}'.format(
            **{'WindowsNT': fleader._wc(["6.1","6.2","6.3","10"],[3,2,2,3]),'WOW64':fleader._wc([""," WOW64;"," Win64;"," x64;"],[3,4,2,1]),'language':fleader._wc([""," {};".format(lang)],[6,4]), 'Chrome': '{0}.{1}.{2}.{3}'.format(random.randint(50, 61), random.randint(0, 9), random.randint(1000, 9999), random.randint(10, 99)), 'Safari': '{0}.{1}'.format(random.randint(100, 999), random.randint(0, 99)), }),
            'Mozilla/5.0 ({compatible}Windows NT {WindowsNT};{WOW64} MSIE {ie}.0; Trident/{Trident}.0;){Gecko}'.format(
            **{'compatible':random.choice(["","compatible; "]),'WindowsNT': fleader._wc(["6.1","6.2","6.3","10"],[3,2,2,3]),'WOW64':fleader._wc([""," WOW64;"," Win64;"," x64;"],[3,4,2,1]),'ie': random.randint(10, 11),'Trident': random.randint(5, 7),'Gecko':random.choice([""," like Gecko;"]) }),
            'Mozilla/5.0 (Windows NT {WindowsNT}; MSIE 9.0;) Opera {opera1}.{opera2}'.format(
            **{'WindowsNT': fleader._wc(["6.1","6.2","6.3","10"],[3,2,2,3]),'opera1': random.randint(10, 12),'opera2': random.randint(10, 99) }),
           ]
        rs=fleader._wc(user_agent_list, [2, 4, 3, 1])#201706 chrome63 firefox14 ie9 opera2
        return rs


    #===============文件类=========================================
    @staticmethod
    def mk(path,cut=True):
        import os,sys
        if cut:
            path=path.replace('.','/')
        rpath=os.path.dirname(os.path.realpath(__file__)).replace('\\','/')+'/'+path
        if not os.path.exists(path):
            os.makedirs(path)
        return rpath

    @staticmethod         
    def rw(path, line=None, aw='a',sp=""):
        import os
        path0=os.path.split(path)[0]
        if path0!='':
            fleader.mk(path0,False)
        if line == None:
            aw='r'
        if line == '':
            aw='w'
        if aw=='r':
            arr = []
            with open(path, 'r', encoding=fleader._get_encode(path,'text')) as f:
                if aw=="r":
                    return f.read().strip()
                for l in f:
                    if sp=="":
                        arr.append(l.replace("\n", ""))
                    else:
                        arr.append(l.replace("\n", "").split(sp))
            return arr
        if aw=='w' or aw=='a':
            if type(line)==set or type(line)==list:
                cont=''
                for l in line:
                    cont+=l + "\n"
                with open(path, aw, encoding='utf-8') as f:
                    f.write(cont)
            else:
                with open(path, aw, encoding='utf-8') as f:
                    if aw == 'w' and line == '':
                        f.write('')
                    else:
                        f.write(line  + "\n")
        if aw=='wb':
            with open(path, 'wb') as f:
                f.write(line)     


    @staticmethod
    def rwini(path,rnode,snode,txt=""):
        import configparser      
        cf = configparser.ConfigParser()
        try:
            cf.read(path)
        except:
            cf.readfp(open(path, 'r', encoding='utf-8'))
        if txt=="":
            txt=cf.get(rnode,snode)
            return str(txt)
        else:
            cf.set(rnode,snode,txt)
            f=open(path, "w")
            cf.write(f)
            f.close()   

    #===============文本处理类=========================================
    @staticmethod
    def mid(s1,s2,s3):
        if type(s2)==list:
            for i in s2:
                if i in s1:
                    s=s1[s1.find(i)+len(i):len(s1)]
                    return s[0:s.find(s3)]
        if type(s3)==list:
            for i in s3:
                if i in s1:
                    s=s1[s1.find(s2)+len(s2):len(s1)]
                    return s[0:s.find(i)]
        s=s1[s1.find(s2)+len(s2):len(s1)]
        return s[0:s.find(s3)]

    @staticmethod
    def var(arr,var,value=''):
        if var in arr:
            return arr[var]
        else:
            return value

    @staticmethod
    def get1(arr):
        if len(arr)>0:
            return arr[0]
        return ''

    @staticmethod
    def int(st):
        if st!='':
            if '.' in st:
                return float(st)
            else:
                return int(st)
        return 0

    @staticmethod
    def getc(arr):
        for i in arr:
            if i != None:
                if len(i)>0:
                    return i
        return ''

    @staticmethod
    def rpc(str,arr=[' ']):
        for i in arr:
            str=str.replace(i,'')
        return str

    @staticmethod
    def https(str):
        if len(str)>0:
            if str[:2]=='//':
                str='http:'+str
            return str
        return ''

    @staticmethod
    def filter_emoji(desstr,restr=''):
        import re
        try:
            co = re.compile(u'[\U00010000-\U0010ffff]')
        except re.error:
            co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        return co.sub(restr, desstr)
    #===============数据处理类=====================================
    @staticmethod#数组切片
    def cut(arr,cp=20):
        arc,tmp_arr,tmp_a=[],[],[]
        for x,i in enumerate(arr):
            tmp_arr.append(i)
            if (x+1)%cp==0:
                arc.append(tmp_arr)
                tmp_arr=[]
            tmp_a=tmp_arr
        arc.append(tmp_a)
        return arc

    @staticmethod
    def feed(q,urls):#q是值传递
        [q.put(url) for url in urls]
    #===============并发类=========================================
    @staticmethod#线程池
    def pool(callback, lists,threadNum=10):
        import threadpool         
        pool = threadpool.ThreadPool(threadNum) 
        requests = threadpool.makeRequests(callback, lists) 
        [pool.putRequest(req) for req in requests] 
        pool.wait()


    @staticmethod
    def bPool(arg):
        from multiprocessing.dummy import Pool as ThreadPool # 线程池
        tpool = ThreadPool(arg['tnum'])
        arr=list(map(lambda i:{'cnum':arg['cnum'],'tnum':i,'arg':arg['arg']},range(arg['tnum'])))
        tpool.map(arg['callback'], arr)
        tpool.close()  
        tpool.join() 

    @staticmethod#进程池
    def sPool(callback,tnum=20,cnum='',arg=[]):
        from multiprocessing import Pool as ProcessPool # 进程池
        from multiprocessing import cpu_count #cpu数量
        if cnum=='':
            spool = ProcessPool(cpu_count())
        else:
            spool = ProcessPool(cnum)
        arr=list(map(lambda i:{'cnum':i,'tnum':tnum,'callback':callback,'arg':arg},range(cnum)))
        spool.map(fleader.bPool, arr)
        spool.close()  
        spool.join()

    def Manager():
        from multiprocessing import Manager
        manager = Manager()
        q = manager.Queue()
        lock = manager.Lock()
        return q,lock

    @staticmethod #gevent协程
    def gPool(callback,urls=[],pnum=800):
        from gevent import monkey; monkey.patch_all(socket=True,select=True)
        from gevent.pool import Pool
        gpool = Pool(pnum)
        gpool.map(callback, urls)

    @staticmethod#gevent常量
    def getGevent():
        from gevent import monkey; monkey.patch_all(socket=True,select=True)
        from gevent.queue import Queue#get,put
        from gevent.local import local
        try:
            from gevent.lock import BoundedSemaphore
        except:
            from gevent.coros import BoundedSemaphore 
        sem = BoundedSemaphore(2)#acquire,release
        return local,Queue,sem#返回常量,队列,锁
    #===============校验类=========================================
    @staticmethod
    def md5(*arg):
        import hashlib   
        hl = hashlib.md5()
        line=''.join(list(map(lambda x:str(x),arg)))
        hl.update(line.encode(encoding='utf-8'))    
        return hl.hexdigest()

    #===============随机类=========================================   

    @staticmethod
    def _wc(list, weight):
        import random
        new_list = []
        for i, val in enumerate(list):
            for i in range(weight[i]):
                new_list.append(val) 
        return random.choice(new_list)

    @staticmethod
    def rs(cc):
        import random
        return ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', int(cc)))

    @staticmethod
    def hash():
        import time,random
        time12 = int(time.time()*1000)
        rand04 = random.randint(1000,9999)
        return fleader.md5(str(time12)+str(rand04))
    #===============工具类=========================================
    @staticmethod    
    def sleep(t):
        import time
        time.sleep(t)

    @staticmethod
    def print(arg):
        from pprint import pprint
        pprint(arg)

    #===============pythonic 修饰器=========================================
    @staticmethod
    def exp():
        def deco(func):
            def wrapper(*arg, **kw):
                import time
                t0 = time.time()
                res=func(*arg, **kw)
                t = time.time() - t0
                t = 0.1 if t==0.0 else t
                print('call %s %.4fs' % (func.__name__,t))
                return res
            return wrapper
        return deco

    @staticmethod    
    def rwcache(fhash,res_text='',suffix='',path='cache'):
        res_text=str(res_text)
        if res_text=='':
            import os
            for root, dirs, fs in os.walk(r'%s/%s'%(path,fleader.time(2))): #目录路径,所有子目录,非目录子文件   
                for f in fs: 
                    if f==fhash+suffix:#os.path.splitext()
                        res_text=fleader.rw(os.path.join(root,f))
                        return True,res_text
            return False,''
        else:
            fleader.rw(r'%s/%s/%s%s'%(path,fleader.time(2),fhash,suffix), res_text,aw='w')

    @staticmethod
    def cache(suffix='.txt',path='cache',ext=[]):#类似functools.lru_cache()#只能对字符串变量进程缓存
        def deco(func):
            def wrapper(*arg, **kw):
                arg_arr,kw_arr=fleader._getarg(func,arg,kw,ext)#ext过滤
                fhash=fleader.md5(func.__name__,arg_arr,kw_arr)
                state,res=fleader.rwcache(fhash,suffix=suffix,path=path)
                if not state:
                    res=func(*arg, **kw)
                    fleader.rwcache(fhash,res,suffix=suffix,path=path)
                return res
            return wrapper
        return deco

    @staticmethod
    def _getarg(func,arg,kw,ext=[]):
        if len(ext)>0:
            import copy
            arg_arr,kw_arr=list(copy.deepcopy(arg)),copy.deepcopy(kw)
            arg_len,kw_len,arg_kw_len=len(arg),len(kw),len(arg)+len(kw)
            func_vname_arr=func.__code__.co_varnames[:arg_kw_len]
            fvarr=[]
            for x,name in enumerate(func_vname_arr):
                for e in ext:
                    if name==e:
                        if x<arg_len:
                            fvarr.append(x)
            for i in fvarr:
                del arg_arr[i]
            for i in ext:
                if i in kw_arr:
                    del kw_arr[i]
            # print(tuple(arg_arr),kw_arr)
            return tuple(arg_arr),kw_arr
        else:
            return arg,kw
    #===============时间类=========================================   
    @staticmethod
    def time(i=0):
        import time
        if i==0:return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        if i==1:return time.strftime("%Y-%m-%d %H%M%S", time.localtime()) 
        if i==2:return time.strftime("%Y-%m-%d", time.localtime()) 
        if i==3:return time.strftime("%Y%m%d", time.localtime()) 
        if i==4:return time.strftime("%Y%m", time.localtime()) 
    #===============类型转换类========================================= 
    @staticmethod
    def bool(arg):
        arg=arg.lower()
        if arg=='true':
            return True
        return False
if __name__ == '__main__':
    # print(fleader.time(2))
    pass