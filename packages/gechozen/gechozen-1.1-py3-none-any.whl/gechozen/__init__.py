import os
import re
import glob
import shutil
import zipfile
import subprocess
import colorama
from colorama import Back, Fore
from xml.dom import minidom
from .axmlprinter import AXMLPrinter


class Apk:

    def __init__(self):
        self.key = "resource/apkeasy.pk8"
        self.cert = "resource/apkeasy.pem"

    def recompile(self,foldername,output):
        x = subprocess.Popen(['apktool','b',foldername,'-o',output],shell=False,stdout=subprocess.PIPE,preexec_fn=os.setsid)
        return x.stdout

    def decompile(self,filename,output):
        return subprocess.Popen(
            ['apktool','d','-f','-r','--only-main-classes',filename,'-o',output],
            shell=False,
            stdout=subprocess.PIPE,
            preexec_fn=os.setsid
        ).stdout

    def signature(self,filename,output):
        return subprocess.Popen(
            ['apksigner','sign','--key',self.key,'--cert',self.cert,'--out',output,filename],
            shell=False,
            stdout=subprocess.PIPE,
            preexec_fn=os.setsid
        ).stdout

    def printer_result(self,x):
        for i in x:
            log = i.decode('utf-8').replace('\n','')

            if "Using" in log:
                print(
                    re.sub(
                        'Using\s.*?on','Decompile',log).replace('I:',f'{Fore.RESET}[{Fore.GREEN}*{Fore.RESET}]'
                    )
                )

            elif log == '': continue

            else: print(f"{log.replace('I:',f'{Fore.RESET}[{Fore.GREEN}*{Fore.RESET}]')}")

    def xml_decode(self,filename,output):
        fx = AXMLPrinter(open(filename,'rb').read())
        return minidom.parseString(fx.getBuff()).toxml()


    def move_lib(self,original,target):
        return shutil.move(original,target)


    def extract(self,filename,output):
        x = zipfile.ZipFile(filename,'r')
        return x.extractall(output)

    def valid_file(self,f):
        if os.path.exists(f):
            return True

        return False

