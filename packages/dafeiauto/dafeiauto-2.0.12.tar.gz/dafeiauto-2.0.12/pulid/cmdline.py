#!/usr/bin/env python
# coding=utf-8
import subprocess, shutil, os, tarfile, importlib, sys
from zipfile import *
import zipfile

try:
    importlib.import_module("requests")
except ImportError:
    os.system("pip install requests")

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

if sys.argv[2]=="":
    sys.argv[2] = "dafeiauto"
prjtname = sys.argv[2]

def zip(file_name):
    with ZipFile(file_name, 'r') as zip:
        zip.printdir()
        print('Extracting all the files now...')
        zip.extractall()
        zip.close()

def un_zip(file_name):
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names,file_name + "_files/")
    zip_file.close()

def fileremove(filepath):
    if os.path.isdir(filepath):
        shutil.rmtree(filepath)
    else:
        os.remove(filepath)

def un_tar(file_name):
    tar = tarfile.open(file_name)
    names = tar.getnames()
    filename = os.path.splitext(file_name)[0] + "_files"
    if os.path.isdir(filename):
        pass
    else:
        os.mkdir(filename)
    # 因为解压后是很多文件，预先建立目录
    for name in names:
        tar.extract(name, filename)
    tar.close()
    shutil.copytree(filename + "/dafeiauto-2.0.11", prjtname)
    fileremove("autodemo")

def filemove(src, dict):
    shutil.move(src, dict)

def execute():
    import requests
    r = requests.get('https://files.pythonhosted.org/packages/16/31/1f4d07b139d9b8f71f143c1b62c52e30be4a6f7b24370aee0c1eb6b2f0f2/dafeiauto-2.0.11.tar.gz')
    if os.path.exists(prjtname):
        print("The project of " + prjtname + " has already existed....")
    else:
        os.makedirs("autodemo")
        with open("autodemo/autodemo.tar", "wb") as code:
            code.write(r.content)
        un_tar("autodemo/autodemo.tar")
        print("Successfully bulid project of "+ prjtname +"....")

if __name__ == "__main__":
   # execute() # 打包dafeiauto init xxx命令 如无必要最好不修改哦
   if sys.argv[1] == "init":
       execute()