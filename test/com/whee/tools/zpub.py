#!/usr/bin/python
__author__ = 'lidl'
import os

app_base='~/code/zonlolo2/'
server_base='/var/lib/'

def kill(app_root,hard):
    list=os.popen("ps -ef|grep "+app_root+"|grep -v 'grep'|awk '{print $2}'").read();
    #list=os.popen("lsof|grep "+app_root+"|awk '{print $2}'").read();
    if(list!=''):
        pid=int(list)
        print('pid is'+str(pid))
        if hard:
            os.system('kill -9 '+str(pid))
        else:
            os.system('kill '+str(pid))
def rm_oldfile(dest_server,app):
    os.system('rm -rf '+dest_server+'/'+app+"*")
def clear_workdir(server):
    os.system('rm -rf '+server_base+'/'+server+'/work/*')

def copy(app_path,server_path):
    os.system('cp '+app_path+' '+server_path)
def start(server_path):
    os.system('sh '+server_path+'/bin/catalina.sh start')
def checklog(app):
    os.system('tail -f /var/log/zonlolo/'+app+'/'+app+'.log')


app=raw_input("input a app name:\r\n")
server=raw_input("input the destination server name:\r\n")

kill(server,True)
rm_oldfile(server_base+'/'+server,app)
clear_workdir(server)
copy(app_base+'/'+app+'/target/'+app+'*.war',server_base+'/'+server+'/webapps/'+app+'.war')
start(server_base+'/'+server);
checklog(app)
