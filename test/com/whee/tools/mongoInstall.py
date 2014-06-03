#!/bin/python
import os
import time

__author__ = 'lidl'
def shell(cmd):
    os.system(cmd)

print 'will install mongo tar file'
print 'create 3 shards in this machine.'
time.sleep(3)
machine_number=int(raw_input('input the number of the shards machine:'))
print(machine_number)


shell("tar zxvf mongodb-linux-x86_64*.tgz -C /var/lib/")

shell('ln -s /var/lib/mongo*/bin/mongo /usr/bin/mongo')
shell('ln -s /var/lib/mongo*/bin/mongod /usr/bin/mongod')
shell('ln -s /var/lib/mongo*/bin/mongodump /usr/bin/mongodump')
shell('ln -s /var/lib/mongo*/bin/mongos /usr/bin/mongos')
shell('ln -s /var/lib/mongo*/bin/mongorestore /usr/bin/mongorestore')

#rm -rf config && rm -rf shard1_* && rm -rf shard2_* && rm -rf shard3_*



