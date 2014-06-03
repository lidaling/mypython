#!/bin/python
__author__ = 'lidl'
import os
import datetime

def append_content(file_path,content):
    file= open(file_path, 'a')
    file.write('\n')
    file.write(content)
    file.close()
def append_ff_at(file_path,fileadd_path,str):
    file=open(file_path,"r")
    file_add=open(fileadd_path,'r')
    content=file.read()
    content_add=file_add.read()
    file.close()
    file_add.close()
    pos=content.find(str)
    if(pos!=-1):
        content=content[:pos]+content_add+content[pos:]
        file=open(file_path,'w')
        file.write(content)
        file.close()
        print('append '+fileadd_path +'to '+file_path +'-OK')
    else:
        file=open(file_path,'a')
        file.write(content)
        file.close()
def envset(hadoop_home):
    file=open('/home/hadoop/.bashrc','a')
    file.write('export HADOOP_HOME='+hadoop_home)
    file.write('\n')
    file.write('export PATH=${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:$PATH')
    file.close()
def copyjars(hadoop_home):
    os.system('cp ../*.jar '+hadoop_home+'/share/hadoop/mapreduce/')

def mkdirs(root):
    os.system('mkdir -p '+root+'/dfs/data')
    os.system('mkdir -p '+root+'/dfs/name')

H_ROOT='/opt/cloud'
H_HOME="/opt/cloud/hadoop"
INSTALLED_FLAG=H_HOME+"/installed.log"
if(os.path.exists(INSTALLED_FLAG)):
    print("already installed... this script will not work")
else:
    try:
        os.system('tar zxvf ../hadoop-2.2.0.tar.gz -C '+H_ROOT+'/')
        os.system('ln -s '+H_ROOT+'/hadoop-2.2.0 '+H_HOME)
        os.system('rm '+H_HOME+'/lib/native/*')
        os.system('tar zxvf ../hadoop-native.tar.gz -C '+H_HOME+'/lib/native/')

        envset(H_HOME)

        HCONF_HOME=H_HOME+"/etc/hadoop"
        os.system('cp '+HCONF_HOME+'/mapred-site.xml.template '+HCONF_HOME+'/mapred-site.xml')

        H_ENVFILE=HCONF_HOME+"/hadoop-env.sh"
        YARN_ENVFILE=HCONF_HOME+"/yarn-env.sh"

        SLAVES=HCONF_HOME+'/slaves'

        CORE_SITE=HCONF_HOME+'/core-site.xml'
        HDFS_SITE=HCONF_HOME+'/hdfs-site.xml'
        MAPRED_SITE=HCONF_HOME+'/mapred-site.xml'
        YARN_SITE=HCONF_HOME+'/yarn-site.xml'

        J_HOME_STRING="export JAVA_HOME="+os.environ.get("JAVA_HOME")
        append_content(H_ENVFILE,J_HOME_STRING)
        append_content(YARN_ENVFILE,J_HOME_STRING)

        APPEND_POS='</configuration>'
        append_ff_at(SLAVES,'./slaves','')
        append_ff_at(CORE_SITE,'./core-site',APPEND_POS)
        append_ff_at(HDFS_SITE,'./hdfs-site',APPEND_POS)
        append_ff_at(MAPRED_SITE,'./mapred-site',APPEND_POS)
        append_ff_at(YARN_SITE,'./yarn-site',APPEND_POS)

        # copy jars to hadoop lib dir
        copyjars(H_HOME)
        mkdirs(H_ROOT)

    finally:
        file=open(INSTALLED_FLAG,"w")
        now = datetime.datetime.now()
        nowStr=now.strftime('%Y-%m-%d %H:%M:%S')
        file.write("exected on "+nowStr );
        file.close()
