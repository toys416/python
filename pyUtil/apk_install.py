import os
import time
import sys

def getFileName(sourceDir):
    filenames=[]
    if not os.path.exists(sourceDir):
        return;

    for filename in os.listdir(sourceDir):
        if '.apk' in filename:
            filenames.append(filename)
    return filenames


print('\n')
print('=============================================')
print('install apk')

print 'args count:', len(sys.argv), ' args'
print 'args list:', str(sys.argv)

adb_launch='adb shell am start com.huami.midong/.ui.MidongLoginActivity'
adb_uninstall='adb uninstall com.huami.midong'
adb_list='adb shell pm -l|grep com.huami.midong'
apk_dir=sys.argv[1]

sleep_time=10

if (len(sys.argv)>2):
    sleep_time = int(sys.argv[2])

exist=os.popen(adb_list).readline()
if('com.huami.midong' in exist):
    print('midong already installed, uninstall it first')
    os.system(adb_uninstall)
apkNames = getFileName(apk_dir)

for apkName in apkNames:
    apkPath = apk_dir + '/' + apkName
    print(apkPath)
    try:
        os.system('adb install ' + apkPath)
        os.system(adb_launch)
        time.sleep(sleep_time)
        print('uninstall apk')
        print('=============================================')
        os.popen(adb_uninstall)
    except IOError,e:
        print e.message