# -*- coding:utf-8 -*-
__anthor__ = 'Jarvix'

import os
import platform
import logging

# print(platform.platform()) # Windows-7-6.1.7601-SP1
# x.startswith(obj) 函数匹配x字符串开头是否以obj开头，是返回true
# print(os.path) # Windows-7-6.1.7601-SP1
# print(os.getenv('HOMEDRIVE')) # C:
# print(os.getenv('HOMEPATH')) # \Users\xiaoweiping
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')
