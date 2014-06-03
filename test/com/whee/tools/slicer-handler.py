#!/usr/bin/python
import os
import time
import zipfile

class Foldermonitor:
    def __init__(self):
        print('start...')
        self.homedir='/home/denghui/test/test666/'
        self.uploaddir=self.homedir+"in/"
        self.workerdir=self.homedir+'worker/'
        self.resultdir=self.homedir+"out"
        self.slicerpath = self.homedir+"slicer"
        self.templateconfigpath =self.homedir+"config/templateConfig.conf"

    def start(self):
        while True:
            print('in start block...')
            self.parsefolder()
            time.sleep(1)

    def parsefolder(self):
        print(self.uploaddir)
        for root, dirs, files in os.walk(self.uploaddir, True):
            for name in files:
                self.handlezipfile(root,name)

    def handlezipfile(self,base,name):
        if(name.startswith('.')==False and name.count('.zip')>0):
            src=base+'/'+name;
            basename=os.path.splitext(name)
            dest=base.replace(self.uploaddir,self.workerdir);
            os.system('mkdir -p '+dest);
            os.system('mv '+src+' '+dest);
            os.system('cd '+dest)
            print(basename[0])

            f=zipfile.ZipFile(dest+'/'+name);
            f.extractall(dest+'/'+basename[0]);
            f.close();
            os.system('rm '+dest+'/'+name);

            self.dealWithTiffFiles(dest+'/'+basename[0])

            os.system('cd '+self.workerdir);
            print('pwd where:')
            os.system('pwd')

            targetzip=basename[0]+'.zip';
            os.system('zip -r --exclude=*.tif* '+targetzip+' ./worker/'+basename[0]+'/*')

            os.system('mv '+targetzip+' '+self.resultdir)
	    os.system('rm -rf '+dest+'/'+basename[0])


    def dealWithTiffFiles(self,folder):
        print('in dealWithTiffFies '+folder)
        for root, dirs, files in os.walk(folder, True):
             for name in files:
                 if(name.startswith('.')==False and name.count('.tif')>0):
                    basename=os.path.splitext(name)[0];
                    os.system('convert '+os.path.join(root,name)+' '+os.path.join(root,basename+'.jpg'));
                    os.system('rm '+os.path.join(root,name));
                    os.system(self.slicerpath+' '+root+' '+self.templateconfigpath);
                    os.system('rm '+os.path.join(root,basename+'.jpg'))

                    #os.system('zip -r '+basename+' ./*');
                    #dest=root.replace(self.uploaddir,self.resultdir);
                    #os.system('mkdir -p '+dest);
                    #os.system('cp ./'+basename+' '+dest);
                    #os.system('rm -rf '+folder);

monitor=Foldermonitor();
monitor.start();
