import glob
import os

for filename in glob.glob('P:\d\F_FAMILY\Photo\MobileBackup\dxy\iPhone\2023'):
    print(filename)
    # os.remove(filename)

# def del_files(path):
#     for root,dirs,files in os.walk(path):
#         for name in files:
#             if name.endswith('INFO'):
#                 # os.remove(os.path.join(root,name))
#                 print("file:" + name)
#     print("Delete file:")
    
# if __name__== "__main__":
#     path = r'P:\d\F_FAMILY\Photo\MobileBackup\dxy\iPhone\2023\07'   
#     del_files(path)
    