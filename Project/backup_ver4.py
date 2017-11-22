import os
import time

# 在按年月日区分备份文件时，可提供输入备份信息，拼接在备份文件名后
source = ['"D:\\test"']

target_dir = 'D:\\jarvix\\python\\backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Successful create dir to',target_dir)

# 年月日目录
today  =    target_dir + os.sep + \
            time.strftime('%Y%m%d')

# 判断目录是否存在
if not os.path.exists(today):
    os.mkdir(today)
    print('Successful create dir to',today)

# 接收参数
inputDirName = input('enter modify content : ')
if len(inputDirName) == 0:
    target = today + os.sep + time.strftime('%H%M%S') + '.zip'
else:
    #  如果输入的空格，则将空格转换成下划线_
    target = today + os.sep + time.strftime('%H%M%S') + '_' + inputDirName.replace(' ', '_') + '.zip'
# target = today + os.sep + time.strftime('%H%M%S') + '.zip'

zip_command = 'zip -rv {0} {1}'.format(target, ' '.join(source))

print("Zip command is:")
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
print(os.sep)
