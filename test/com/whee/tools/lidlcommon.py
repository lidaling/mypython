import os
__author__ = 'lidl'
def killpid(port):
    list=os.popen("lsof -i:"+str(port)+"|grep LISTEN|awk '{print $2}'").read();
    if(list!=''):
        pid=int(list)
        print('pid is'+str(pid))
        os.system('kill '+str(pid))
