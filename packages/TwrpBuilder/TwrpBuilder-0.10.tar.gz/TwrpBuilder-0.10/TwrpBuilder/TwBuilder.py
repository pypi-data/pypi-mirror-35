#!/usr/bin/env python

from __future__ import print_function

import datetime
import json
import math
import os
from argparse import ArgumentParser
from os import path
from shutil import copyfile
import codecs
import firebase_admin
import requests
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from tqdm import tqdm

try:
    # For python3
    import urllib.request
except ImportError:
    # For python2
    import imp
    import urllib2

    urllib = imp.new_module('urllib')
    urllib.request = urllib2

slash = '/'
myPath = os.path.dirname(os.path.realpath(__file__)) + slash
Cred = credentials.Certificate(myPath + "Cert.py")
firebaseApp = firebase_admin.initialize_app(Cred, {'databaseURL': 'https://twrpbuilder.firebaseio.com',
                                                   'storageBucket': 'twrpbuilder.appspot.com'})
firebaseStorage = storage.bucket()
home = os.path.expanduser("~")
date = datetime.date.today().strftime('%d%m%y')

outDir = 'work'
AndroidImageKitchen = False
global boardType
lfsDir = 'lfs'
pushRepo = False

def update():
    key = '?client_id=8e59ef85a15407f3aaf0&client_secret=e931a914c3c3d4500e59766ffa6578e1d4318329'
    apiUrl = 'https://api.github.com/repos/TwrpBuilder/twrpbuilder_tree_generator/releases/latest' + key
    global jarFile
    out = urllib.request.urlopen(apiUrl)
    reader = codecs.getreader("utf-8")
    j = json.load(reader(out))
    dloadUrl = j['assets'][0]['browser_download_url']
    name = j['assets'][0]['name']
    size = j['assets'][0]['size']
    jarFile = name
    if not os.path.exists(name):
        downloadData(dloadUrl, name, size, workDir=False)


def build():
    ref = db.reference('RunningBuild')
    snapshot = ref.get()
    global backupFile
    global brand
    global board
    global model
    for key, val in snapshot.items():
        model = val['model']
        brand = val['brand']
        board = val['board']
        codeName = val['codeName']
        date = val['date']
        userMail = val['email']
        developerEmail = val['developerEmail']
        if developerEmail == email.strip():
            path = 'queue/' + brand + slash + board + slash + model
            blobData = firebaseStorage.get_blob(path + "/TwrpBuilderRecoveryBackup.tar.gz")
            blobData.make_public()
            url = firebaseStorage.get_blob(path + "/TwrpBuilderRecoveryBackup.tar.gz").public_url
            # print( f'Model= {model} \nCodename= {codeName} \nBoard={board} \nBrand={brand} \nRequested by= {userMail}\nRequested on= {date}')
            print('Model={0}\nCodename={1}\nBoard={2}\nBrand={3}\nRequested By={4}\nRequested on={5}\n'.format(model,
                                                                                                               codeName,
                                                                                                               board,
                                                                                                               brand,
                                                                                                               userMail,
                                                                                                               date))
            backupFile = outDir + slash + model.replace(" ", "_").replace("(", "_").replace(")", "") + '.tar.gz'
            switchBuild(getData(url, name=model.replace(" ", "_").replace("(", "_").replace(")", "") + '.tar.gz',
                                size=blobData.size))


def switchBuild(case):
    if (case == 0):
        exit(-1)
    elif (case == 1):
        buildTree()
    else:
        buildTree(old=True)


def buildTree(old=False):
    argument = ''
    if boardType:
        argument = ' -t ' + boardType
    elif AndroidImageKitchen == True:
        argument += ' -aik '
    if argument:
        result = os.system("script -eqa 'tmp.log' -c 'java -jar " + jarFile + " -f " + backupFile + argument + "'")
    else:
        result = os.system("script -eqa 'tmp.log' -c 'java -jar " + jarFile + " -f " + backupFile + "'")
    if result != 0:
        exit(-1)
    with open('tmp.log') as file:
        file = [x.strip() for x in file]
        lastLine = file[-2].split()
        codename = lastLine[3]
        path = lastLine[5]
        os.remove('tmp.log')
        try:
            raw_input('Press enter after inspecitng tree\n')
        except NameError:
            pass
            input("Press enter after inspecitng tree\n")
        if pushRepo:
            os.system("./Push.sh " + codename + " " + user + " " + token)
        errorCode = os.system("Build.sh " + codename)
        if errorCode != 0:
            exit(1)
        else:
            name = 'TWRP_' + codename + '-' + date + '.img'
            outputPath = 'out/target/product/' + codename + slash + name
            url = "https://gitlab.com/HosteBin" + slash + repo + slash + "raw/master" + slash + brand + slash + codename + slash + name
            path = lfsDir + slash + brand + slash + codename
            if not os.path.exists(path):
                os.makedirs(path)
            copyfile(outputPath, path + slash + name)
            os.system("cd lfs ; git add . ; git commit -am \"add " + name + "\" ; git push origin master")
            upstream = db.reference('upstreamUri')
            upstream.push().set({
                'model': model,
                'url': url,
            })
            print(url)
        if argument:
            exit(0)
    return 0


def getData(url, name='output.bin', size=0):
    if not os.path.exists(outDir):
        os.mkdir(outDir)
    if not os.path.exists(outDir + slash + name):
        if size != 0 and downloadData(url, name, size) != size:
            print("ERROR, something went wrong")
            return 0
        else:
            return 1
    else:
        print('Skipping download of ' + name)
        return 2


def downloadData(url, name, size, workDir=True):
    r = requests.get(url, stream=True)
    block_size = 1000
    wrote = 0
    if workDir == True:
        out = outDir + "/" + name
    else:
        out = name
    with open(out, 'wb') as f:
        for data in tqdm(r.iter_content(block_size), total=math.ceil(size // block_size), unit='Kb'):
            wrote = wrote + len(data)
            f.write(data)
    return wrote


def getUserData():
    global email
    global repo
    global user
    global token
    confDir = home + "/.TwrpBuilder.cfg"
    if path.exists(confDir):
        with open(confDir) as file:
            content = file.readlines()
            content = [x.strip() for x in content]
            for i in content:
                if (i.__contains__('email')):
                    email = i.split('=')[1]
                if (i.__contains__('repo')):
                    repo = i.split('=')[1]
                if (i.__contains__('user')):
                    user = i.split('=')[1]
                if (i.__contains__('token')):
                    token = i.split('=')[1]
    else:
        print("Please configure email and repo")
        exit(-1)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-t', '--type', help='mtk, samsung, mrvl')
    parser.add_argument('-aik', '--Android_Image_Kitchen', help='Use Android Image Kitchen', action='store_true')
    parser.add_argument('-p', '--pushRepo', help='Push repo to gitlab', action='store_true')
    args = parser.parse_args()
    if args.__getattribute__('type') != None:
        boardType = parser.parse_args().__getattribute__('type')
    else:
        boardType = None

    if args.__getattribute__('Android_Image_Kitchen') != False:
        AndroidImageKitchen = True

    if args.__getattribute__('pushRepo') != False:
        pushRepo = True

    getUserData()
    update()
    build()
