#!/usr/bin/python
# coding=utf-8

import re,sys,os,stat

#file=sys.argv[1]
file="test.groovy"
dir="C:\\Users\\jingzhwa\\Desktop\\voucher"
dir="D:\\Workspace\\ODCS\\ChinaLocalization_Automation\\src\\test\\java\\com\\netsuite\\chinalocalization\\cashflow"

reg=r'void \"[c/C]ase(.*)\"'

def alter(file, reg):
    with open(file, "r") as f1, open("after.groovy", "w", ) as f2:
        for line in f1:
            searchObj = re.search(reg, line, re.M | re.I)
            if searchObj:
                oriString = searchObj.group()
                afterString = oriString.replace('.','_').replace('\"','').lower()
                f2.write(re.sub(oriString,afterString,line))
            else:
                f2.write(line)
    os.remove(file)
    os.rename("after.groovy",file)


def list_all_files(rootdir):
    import os
    _files = []
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0,len(list)):
           path = os.path.join(rootdir,list[i])
           if os.path.isdir(path):
              _files.extend(list_all_files(path))
           if os.path.isfile(path):
              _files.append(path)
    return _files

dirs = list_all_files(dir)

for file in dirs:
    if ".groovy" in file:
        print file
        alter(file,reg)






# def alter(file,old_str,new_str):
#      with open(file, "r") as f1,open("after.groovy", "w",) as f2:
#         for line in f1:
#              f2.write(re.sub(old_str,new_str,line))
#      # os.remove(file)
#      # os.rename("%s.bak" % file, file)
#








# alter(file, "admin", "password")
#
# void "Case_1.6.1.3"() {

#
#
# #Read from original json
# fobj = open(file, 'r')
# firstLine = fobj.readline()
# fobj.close()
#
# all = []
# fobj = open(file, 'w')
# needToEliminate=['SuiteTeardown','SuiteSetup','BeforeClass','AfterClass']
# result=firstLine
#
# #Delete suitesetup/teardown.. cases
# for setup in needToEliminate:
#   n=1
#   while n<100:
#     reg=r',?{("result":)((?:(?!result).)*?)'+setup+'([^}])*},?'# Reg to match reduntdant result
#     result = re.sub(reg,'', result)
#     n=n+1
#
# #Calculate how many pass and how many fail
# p = re.findall('"result":"passed"',result)
# passed=str(len(p))
# print("Passed:"+passed)
#
# f = re.findall('"result":"failed"',result)
# failed=str(len(f))
# print("Failed:"+failed)
#
#
# #Rewrite the report according actual pass and failed
# reg = r'"total_passed":.*?,'
# result = re.sub(reg,'"total_passed":'+passed+',', result)
#
# reg = r'"total_failed":.?,'
# result = re.sub(reg,'"total_failed":'+failed+',', result)
#
#
# all.append(result)
# fobj.write(''.join(all))
# fobj.close()
