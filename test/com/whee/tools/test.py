__author__ = 'lidl'
import pexpect
import pxssh
import getpass
import os

#aa=pexpect.run('env')
#print(aa)
#aa=pexpect.run('pwd')
#print(aa)
#remote=pexpect.spawn('scp /Users/lidl/jekyll-theme1* tomcat@192.168.1.101:~/')
#remote.expect("tomcat@192.168.1.101's password:")
#remote.sendline('tom0828.')

str='/Users/lidl/tmp/in/aaaa';
a='/Users/lidl/tmp/in/';
b='/Users/lidl/tmp/worker/';
print(str.replace(a,b))

