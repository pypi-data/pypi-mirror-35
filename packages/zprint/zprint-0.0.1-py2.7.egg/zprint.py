import sys
import datetime
#lineNumber = sys._getframe().f_back.f_lineno
#sys._getframe().f_code.co_filename
def get_tree():
    filename=sys._getframe().f_code.co_filename
    
    name=[]
    a = sys._getframe()
    linenum=a.f_back.f_lineno
    #filename+='(line-'+str(linenum)+')'
    while a is not None and a.f_back is not None:
       name.append(a.f_code.co_name+'(%s line:'%(filename)+str(a.f_back.f_lineno)+')')
       a=a.f_back
    #print(100*'*')
    #print len(name)
    #print name
    funclist='%s main'%(filename)
    spacelist=4*' '
    for i in range(-1,-len(name)+1,-1):
        #print name[i]
        funclist+=' - '+name[i]

    return funclist,'%s %s %s'%(filename,(len(name)-2)*' -  ',name[2])
def addinfo(message,flag=1):
    funclist,spacelist=get_tree()
    flist=(funclist,spacelist)[flag]
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    info="[%s] %s :: %s"%(nowTime,spacelist,message)
    return info
def zprint(message,flag=1):
    funclist,spacelist=get_tree()
    flist=(funclist,spacelist)[flag]
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    info="[%s] %s :: %s"%(nowTime,flist,message)
    #info=addinfo(message,flag)
    sys.stdout.write(info+'\n')
    #print info
def epprint(message,flag=1):
    funclist,spacelist=get_tree()
    flist=(funclist,spacelist)[flag]
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    info="[%s] %s :: %s"%(nowTime,flist,message)
    #info=addinfo(message,flag)
    sys.stderr.write(info)

def fun2():
    zprint(" I am in fun2",1)
    zprint(" I am in fun2",0)

def fun1():
    zprint(" I am in fun1")
    fun2()



if __name__=="__main__":
   print 1 
   fun1() 
