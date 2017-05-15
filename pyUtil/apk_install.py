import os
import time
from time import sleep


print('\n')
print('=============================================')
print('install apk')

def getFileName(sourceDir):
    filenames=[]
    if not os.path.exists(sourceDir):
        return;

    for filename in os.listdir(sourceDir):
        if '.apk' in filename:
            filenames.append(filename)
    return filenames


apk_dir='/Users/wangjingzhou/OneDrive/H_Huami/A_APK/APK_Huami_Health/5_11_branch'


apkNames = getFileName(apk_dir)

for apkName in apkNames:
    apkPath = apk_dir + '/' + apkName
    print(apkPath)
    try:
        os.system('adb install ' + apkPath)
        os.system('adb shell am start com.huami.midong/.ui.MidongLoginActivity')
        sleep(10)
        print('uninstall apk')
        print('=============================================')
        os.system('adb uninstall com.huami.midong')
    except IOError,e:
        print e.message