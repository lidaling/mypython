__author__ = 'lidl'
import os
import time
def killpid(port):
    list=os.popen("lsof -i:"+str(port)+"|grep LISTEN|awk '{print $2}'").read();
    if(list!=''):
        pid=int(list)
        print('pid is'+str(pid))
        os.system('kill '+str(pid))

ports=[30000,20000,27017,27018,27019]
for port in ports:
    print('will kill pid with port :'+str(port))
    time.sleep(1)
    killpid(port)
