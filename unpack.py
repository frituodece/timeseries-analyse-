#! /usr/bin/env python
#coding=utf-8
#open

import os
import struct
import datetime
import pandas as pd

def divide(name,period):
    pathDir =  os.listdir('D:\work\work')
    namelist=['ag','al','au','bu','cu','fu','hc','ni','pb','rb','ru','sn','wr','zn']
    timeseries=[]
    filenames=[] 
    if period=='month':
        for allDir in pathDir:
            child = os.path.join('%s%s' % ('D:\work\work', allDir))
            filename=child.decode('gbk')
            filename='D:\work\work\\'+filename[12:]
            f = open(filename, 'rb')
            s=f.read()
            f.close()
            p=24
            while True:
                if len(s) < p+16:
                    break
                a=struct.unpack('=q2i', s[p:p+16])
                p+=16
                if len(s) < p+a[2]:
                    break
                pkg=s[p:p+a[2]]
                b=struct.unpack('=I3ci31s9sic',pkg[42:42+56])
                if b[5]>name and b[5]<namelist[namelist.index(name)+1]:
                    if b[8] == '\x00':
                            pass
                    elif b[8]=='\x02':
                            c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                            if c[4]<100000 and c[6]<100000:
                                dta.append(c[4]/2+c[6]/2)
                                if b[7]==0:
                                    d='0'
                                elif b[7]==500:
                                    d='500'
                                tim=filename[21:31]+' '+b[6][:8]+':'+d
                                time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                time.append(time1) 
                            else:
                                pass
                    elif b[8]=='\x01':
                            pass
                    elif b[8]=='\x03':
                            c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                            if c[4]<100000 and c[6]<100000:
                                dta.append(c[4]/2+c[6]/2)
                                if b[7]==0:
                                    d='0'
                                elif b[7]==500:
                                    d='500'
                                tim=filename[21:31]+' '+b[6][:8]+':'+d
                                time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                time.append(time1) 
                            else:
                                pass
                    elif b[8]=='\x04':
                        pass
                else:
                    pass
                p+=a[2]
        x=0
        while True:
            if x==len(time)-1:
                break
            if time[x+1]==time[x]+datetime.timedelta(microseconds=500000):
                x+=1
            elif  time[x]==time[x+1] :
                time.pop(x+1)
                dta[x]=dta[x]/2+dta.pop(x+1)/2        
            else:
                time.insert(x+1,time[x]+datetime.timedelta(microseconds=500000))
                dta.insert(x+1,dta[x])
                x+=1        
        d=pd.DataFrame({'timeseries':dta},index=time)
        timeseries.append(d)
        return timeseries
    if period=='week':          
        pathDir =  os.listdir('D:\work\work')
        for allDir in pathDir:
            child = os.path.join('%s%s' % ('D:\work\work', allDir))
            filename=child.decode('gbk')
            filename='D:\work\work\\'+filename[12:]
            filenames.append(filename)
        o=0
        while True:
            time=[]
            dta=[]
            if len(filenames)<o+15:
                break
            for i in range(15):
                f = open(filenames[o+i], 'rb')
                s=f.read()
                f.close()
                p=24
                while True:
                    if len(s) < p+16:
                        break
                    a=struct.unpack('=q2i', s[p:p+16])
                    p+=16
                    if len(s) < p+a[2]:
                        break
                    pkg=s[p:p+a[2]]
                    b=struct.unpack('=I3ci31s9sic',pkg[42:42+56])
                    if b[5]>name and b[5]<namelist[namelist.index(name)+1]:
                        if b[8] == '\x00':
                                pass
                        elif b[8]=='\x02':
                                c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                                if c[4]<100000 and c[6]<100000:
                                    dta.append(c[4]/2+c[6]/2)
                                    if b[7]==0:
                                        d='0'
                                    elif b[7]==500:
                                        d='500'
                                    tim=filenames[o+i][21:31]+' '+b[6][:8]+':'+d
                                    time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                    time.append(time1) 
                                else:
                                    pass
                        elif b[8]=='\x01':
                                pass
                        elif b[8]=='\x03':
                                c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                                if c[4]<100000 and c[6]<100000:
                                    dta.append(c[4]/2+c[6]/2)
                                    if b[7]==0:
                                        d='0'
                                    elif b[7]==500:
                                        d='500'
                                    tim=filenames[o+i][21:31]+' '+b[6][:8]+':'+d
                                    time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                    time.append(time1) 
                                else:
                                    pass
                        elif b[8]=='\x04':
                            pass
                    else:
                        pass
                    p+=a[2]
            x=0
            while True:
                if x==len(time)-1:
                    break
                if time[x+1]==time[x]+datetime.timedelta(microseconds=500000):
                    x+=1
                elif  time[x]==time[x+1] :
                    time.pop(x+1)
                    dta[x]=dta[x]/2+dta.pop(x+1)/2        
                else:
                    time.insert(x+1,time[x]+datetime.timedelta(microseconds=500000))
                    dta.insert(x+1,dta[x])
                    x+=1            
            d=pd.DataFrame({'timeseries':dta},index=time)
            timeseries.append(d)
            o+=15
        return timeseries
    if period=='day':
            for allDir in pathDir:
                child = os.path.join('%s%s' % ('D:\work\work', allDir))
                filename=child.decode('gbk')
                filename='D:\work\work\\'+filename[12:]
                filenames.append(filename)
            o=0
            while True:
                time=[]
                dta=[]
                if len(filenames)<o+3:
                    break
                for i in range(3):
                    f = open(filenames[o+i], 'rb')
                    s=f.read()
                    f.close()
                    p=24
                    while True:
                        if len(s) < p+16:
                            break
                        a=struct.unpack('=q2i', s[p:p+16])
                        p+=16
                        if len(s) < p+a[2]:
                            break
                        pkg=s[p:p+a[2]]
                        b=struct.unpack('=I3ci31s9sic',pkg[42:42+56])
                        if b[5]>name and b[5]<namelist[namelist.index(name)+1]:
                            if b[8] == '\x00':
                                    pass
                            elif b[8]=='\x02':
                                    c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                                    if c[4]<100000 and c[6]<100000:
                                        dta.append(c[4]/2+c[6]/2)
                                        if b[7]==0:
                                            d='0'
                                        elif b[7]==500:
                                            d='500'
                                        tim=filenames[o+i][21:31]+' '+b[6][:8]+':'+d
                                        time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                        time.append(time1) 
                                    else:
                                        pass
                            elif b[8]=='\x01':
                                    pass
                            elif b[8]=='\x03':
                                    c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                                    if c[4]<100000 and c[6]<100000:
                                        dta.append(c[4]/2+c[6]/2)
                                        if b[7]==0:
                                            d='0'
                                        elif b[7]==500:
                                            d='500'
                                        tim=filenames[o+i][21:31]+' '+b[6][:8]+':'+d
                                        time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                        time.append(time1) 
                                    else:
                                        pass
                            elif b[8]=='\x04':
                                pass
                        else:
                            pass
                        p+=a[2]
                x=0
                if x<len(time)-2:
                    if time[x+1]==time[x]+datetime.timedelta(microseconds=500000):
                        x+=1
                    elif  time[x]==time[x+1] :
                        time.pop(x+1)
                        dta[x]=dta[x]/2+dta.pop(x+1)/2        
                    else:
                        time.insert(x+1,time[x]+datetime.timedelta(microseconds=500000))
                        dta.insert(x+1,dta[x])
                        x+=1                
                d=pd.DataFrame({'timeseries':dta},index=time)
                timeseries.append(d)
                o+=3
            return timeseries
    if period=='mor':
            for allDir in pathDir:
                child = os.path.join('%s%s' % ('D:\work\work', allDir))
                filename=child.decode('gbk')
                filename='D:\work\work\\'+filename[12:]
                filenames.append(filename)
            o=0
            while True:
                time=[]
                dta=[]
                if len(filenames)<o+3:
                    break
                for i in range(3):
                    if i==0:
                        f = open(filenames[o+i], 'rb')
                        s=f.read()
                        f.close()
                        p=24
                        while True:
                            if len(s) < p+16:
                                break
                            a=struct.unpack('=q2i', s[p:p+16])
                            p+=16
                            if len(s) < p+a[2]:
                                break
                            pkg=s[p:p+a[2]]
                            b=struct.unpack('=I3ci31s9sic',pkg[42:42+56])
                            if b[5]>name and b[5]<namelist[namelist.index(name)+1]:
                                if b[8] == '\x00':
                                        pass
                                elif b[8]=='\x02':
                                        c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                                        if c[4]<100000 and c[6]<100000:
                                            dta.append(c[4]/2+c[6]/2)
                                            if b[7]==0:
                                                d='0'
                                            elif b[7]==500:
                                                d='500'
                                            tim=filenames[o+i][21:31]+' '+b[6][:8]+':'+d
                                            time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                            time.append(time1) 
                                        else:
                                            pass
                                elif b[8]=='\x01':
                                        pass
                                elif b[8]=='\x03':
                                        c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                                        if c[4]<100000 and c[6]<100000:
                                            dta.append(c[4]/2+c[6]/2)
                                            if b[7]==0:
                                                d='0'
                                            elif b[7]==500:
                                                d='500'
                                            tim=filenames[o+i][21:31]+' '+b[6][:8]+':'+d
                                            time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                            time.append(time1) 
                                        else:
                                            pass
                                elif b[8]=='\x04':
                                    pass
                            else:
                                pass
                            p+=a[2]
                            x=0                              
                    else:
                        pass    
                if x<len(time)-2:
                    if time[x+1]==time[x]+datetime.timedelta(microseconds=500000):
                        x+=1
                    elif  time[x]==time[x+1] :
                        time.pop(x+1)
                        dta[x]=dta[x]/2+dta.pop(x+1)/2        
                    else:
                        time.insert(x+1,time[x]+datetime.timedelta(microseconds=500000))
                        dta.insert(x+1,dta[x])
                        x+=1    
                d=pd.DataFrame({'timeseries':dta},index=time)
                timeseries.append(d)
                o+=3
            return timeseries
    if period=='aft':
            for allDir in pathDir:
                child = os.path.join('%s%s' % ('D:\work\work', allDir))
                filename=child.decode('gbk')
                filename='D:\work\work\\'+filename[12:]
                filenames.append(filename)
            o=0
            while True:
                time=[]
                dta=[]
                if len(filenames)<o+3:
                    break
                for i in range(3):
                    if i==1:
                        f = open(filenames[o+i], 'rb')
                        s=f.read()
                        f.close()
                        p=24
                        while True:
                            if len(s) < p+16:
                                break
                            a=struct.unpack('=q2i', s[p:p+16])
                            p+=16
                            if len(s) < p+a[2]:
                                break
                            pkg=s[p:p+a[2]]
                            b=struct.unpack('=I3ci31s9sic',pkg[42:42+56])
                            if b[5]>name and b[5]<namelist[namelist.index(name)+1]:
                                if b[8] == '\x00':
                                        pass
                                elif b[8]=='\x02':
                                        c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                                        if c[4]<100000 and c[6]<100000:
                                            dta.append(c[4]/2+c[6]/2)
                                            if b[7]==0:
                                                d='0'
                                            elif b[7]==500:
                                                d='500'
                                            tim=filenames[o+i][21:31]+' '+b[6][:8]+':'+d
                                            time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                            time.append(time1) 
                                        else:
                                            pass
                                elif b[8]=='\x01':
                                        pass
                                elif b[8]=='\x03':
                                        c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                                        if c[4]<100000 and c[6]<100000:
                                            dta.append(c[4]/2+c[6]/2)
                                            if b[7]==0:
                                                d='0'
                                            elif b[7]==500:
                                                d='500'
                                            tim=filenames[o+i][21:31]+' '+b[6][:8]+':'+d
                                            time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                            time.append(time1) 
                                        else:
                                            pass
                                elif b[8]=='\x04':
                                    pass
                            else:
                                pass
                            p+=a[2]
                    else:
                        pass
                x=0
                if x<len(time)-2:
                    if time[x+1]==time[x]+datetime.timedelta(microseconds=500000):
                        x+=1
                    elif  time[x]==time[x+1] :
                        time.pop(x+1)
                        dta[x]=dta[x]/2+dta.pop(x+1)/2        
                    else:
                        time.insert(x+1,time[x]+datetime.timedelta(microseconds=500000))
                        dta.insert(x+1,dta[x])
                        x+=1 
                
                    if x==len(time)-1:
                        break
                    if time[x+1]==time[x]+datetime.timedelta(microseconds=500000):
                        x+=1
                    elif  time[x]==time[x+1] :
                        time.pop(x+1)
                        dta[x]=dta[x]/2+dta.pop(x+1)/2        
                    else:
                        time.insert(x+1,time[x]+datetime.timedelta(microseconds=500000))
                        dta.insert(x+1,dta[x])
                        x+=1                
                d=pd.DataFrame({'timeseries':dta},index=time)
                timeseries.append(d)
                o+=3
            return timeseries
    if period=='eve':
        for allDir in pathDir:
            child = os.path.join('%s%s' % ('D:\work\work', allDir))
            filename=child.decode('gbk')
            filename='D:\work\work\\'+filename[12:]
            filenames.append(filename)
        o=0
        while True:
            time=[]
            dta=[]
            if len(filenames)<o+3:
                break
            for i in range(3):
                if i==2:
                    f = open(filenames[o+i], 'rb')
                    s=f.read()
                    f.close()
                    p=24
                    while True:
                        if len(s) < p+16:
                            break
                        a=struct.unpack('=q2i', s[p:p+16])
                        p+=16
                        if len(s) < p+a[2]:
                            break
                        pkg=s[p:p+a[2]]
                        b=struct.unpack('=I3ci31s9sic',pkg[42:42+56])
                        if b[5]>name and b[5]<namelist[namelist.index(name)+1]:
                            if b[8] == '\x00':
                                    pass
                            elif b[8]=='\x02':
                                    c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                                    if c[4]<100000 and c[6]<100000:
                                        dta.append(c[4]/2+c[6]/2)
                                        if b[7]==0:
                                            d='0'
                                        elif b[7]==500:
                                            d='500'
                                        tim=filenames[o+i][21:31]+' '+b[6][:8]+':'+d
                                        time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                        time.append(time1) 
                                    else:
                                        pass
                            elif b[8]=='\x01':
                                    pass
                            elif b[8]=='\x03':
                                    c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                                    if c[4]<100000 and c[6]<100000:
                                        dta.append(c[4]/2+c[6]/2)
                                        if b[7]==0:
                                            d='0'
                                        elif b[7]==500:
                                            d='500'
                                        tim=filenames[o+i][21:31]+' '+b[6][:8]+':'+d
                                        time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                        time.append(time1) 
                                    else:
                                        pass
                            elif b[8]=='\x04':
                                pass
                        else:
                            pass
                        p+=a[2]
                else:
                    pass
            x=0
            if x<len(time)-2:
                if time[x+1]==time[x]+datetime.timedelta(microseconds=500000):
                    x+=1
                elif  time[x]==time[x+1] :
                    time.pop(x+1)
                    dta[x]=dta[x]/2+dta.pop(x+1)/2        
                else:
                    time.insert(x+1,time[x]+datetime.timedelta(microseconds=500000))
                    dta.insert(x+1,dta[x])
                    x+=1             
            d=pd.DataFrame({'timeseries':dta},index=time)
            timeseries.append(d)
            o+=3
        return timeseries
    if period=='45':
        time=[]
        dta=[]
        for allDir in pathDir:
            child = os.path.join('%s%s' % ('D:\work\work', allDir))
            filename=child.decode('gbk')
            filename='D:\work\work\\'+filename[12:]
            f = open(filename, 'rb')
            s=f.read()
            f.close()
            p=24
            while True:
                if len(s) < p+16:
                    break
                a=struct.unpack('=q2i', s[p:p+16])
                p+=16
                if len(s) < p+a[2]:
                    break
                pkg=s[p:p+a[2]]
                b=struct.unpack('=I3ci31s9sic',pkg[42:42+56])
                if b[5]>name and b[5]<namelist[namelist.index(name)+1]:
                    if b[8] == '\x00':
                            pass
                    elif b[8]=='\x02':
                            c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                            if c[4]<100000 and c[6]<100000:
                                dta.append(c[4]/2+c[6]/2)
                                if b[7]==0:
                                    d='0'
                                elif b[7]==500:
                                    d='500'
                                tim=filename[21:31]+' '+b[6][:8]+':'+d
                                time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                time.append(time1) 
                            else:
                                pass
                    elif b[8]=='\x01':
                            pass
                    elif b[8]=='\x03':
                            c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                            if c[4]<100000 and c[6]<100000:
                                dta.append(c[4]/2+c[6]/2)
                                if b[7]==0:
                                    d='0'
                                elif b[7]==500:
                                    d='500'
                                tim=filename[21:31]+' '+b[6][:8]+':'+d
                                time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                time.append(time1) 
                            else:
                                pass
                    elif b[8]=='\x04':
                        pass
                else:
                    pass
                p+=a[2]
            x=0
            if x<len(time)-2:
                if time[x+1]==time[x]+datetime.timedelta(microseconds=500000):
                    x+=1
                elif  time[x]==time[x+1] :
                    time.pop(x+1)
                    dta[x]=dta[x]/2+dta.pop(x+1)/2        
                else:
                    time.insert(x+1,time[x]+datetime.timedelta(microseconds=500000))
                    dta.insert(x+1,dta[x])
                    x+=1 
            u=0
            timeori=time[u]
            for x in time:
                if x>timeori+datetime.timedelta(0,2700):
                    timeori=x
                    d=pd.DataFrame({'timeseries':dta[u:time.index(x)]},index=time[u:time.index(x)])
                    timeseries.append(d)
                    u=time.index(x)
                elif x==time[len(time)-1]:
                    d=pd.DataFrame({'timeseries':dta[u:time.index(x)]},index=time[u:time.index(x)])
                    timeseries.append(d)
                    break
        return timeseries
    if period=='30':
        time=[]
        dta=[]
        for allDir in pathDir:
            child = os.path.join('%s%s' % ('D:\work\work', allDir))
            filename=child.decode('gbk')
            filename='D:\work\work\\'+filename[12:]
            f = open(filename, 'rb')
            s=f.read()
            f.close()
            p=24
            while True:
                if len(s) < p+16:
                    break
                a=struct.unpack('=q2i', s[p:p+16])
                p+=16
                if len(s) < p+a[2]:
                    break
                pkg=s[p:p+a[2]]
                b=struct.unpack('=I3ci31s9sic',pkg[42:42+56])
                if b[5]>name and b[5]<namelist[namelist.index(name)+1]:
                    if b[8] == '\x00':
                            pass
                    elif b[8]=='\x02':
                            c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                            if c[4]<100000 and c[6]<100000:
                                dta.append(c[4]/2+c[6]/2)
                                if b[7]==0:
                                    d='0'
                                elif b[7]==500:
                                    d='500'
                                tim=filename[21:31]+' '+b[6][:8]+':'+d
                                time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                time.append(time1) 
                            else:
                                pass
                    elif b[8]=='\x01':
                            pass
                    elif b[8]=='\x03':
                            c=struct.unpack('=di3didi', pkg[42+56:42+56+52])
                            if c[4]<100000 and c[6]<100000:
                                dta.append(c[4]/2+c[6]/2)
                                if b[7]==0:
                                    d='0'
                                elif b[7]==500:
                                    d='500'
                                tim=filename[21:31]+' '+b[6][:8]+':'+d
                                time1 = datetime.datetime.strptime(tim,'%Y-%m-%d %H:%M:%S:%f')
                                time.append(time1) 
                            else:
                                pass
                    elif b[8]=='\x04':
                        pass
                else:
                    pass
                p+=a[2]
            x=0
            if x<len(time)-2:
                if time[x+1]==time[x]+datetime.timedelta(microseconds=500000):
                    x+=1
                elif  time[x]==time[x+1] :
                    time.pop(x+1)
                    dta[x]=dta[x]/2+dta.pop(x+1)/2        
                else:
                    time.insert(x+1,time[x]+datetime.timedelta(microseconds=500000))
                    dta.insert(x+1,dta[x])
                    x+=1                
            u=0
            timeori=time[u]
            for x in time:
                if x>timeori+datetime.timedelta(0,1800):
                    timeori=x
                    d=pd.DataFrame({'timeseries':dta[u:time.index(x)]},index=time[u:time.index(x)])
                    timeseries.append(d)
                    u=time.index(x)
                elif x==time[len(time)-1]:
                    d=pd.DataFrame({'timeseries':dta[u:time.index(x)]},index=time[u:time.index(x)])
                    timeseries.append(d)
                    break
        return timeseries
    else:
        pass