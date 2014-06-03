__author__ = 'lidl'
import os

os.system("ssh tomcat@192.168.1.102 'rm -r /home/tomcat/code/zonlolo2'")
os.system('scp -r ~/code/zonlolo2 tomcat@192.168.1.102:~/code/')
os.system("ssh tomcat@192.168.1.103 'rm -r /home/tomcat/code/zonlolo2'")
os.system('scp -r ~/code/zonlolo2 tomcat@192.168.1.103:~/code/')
