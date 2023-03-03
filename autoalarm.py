import os
import time as t

activate = input('Enter password to start: ')

    
if activate == 'a':
    print('Activated')
    os.system('python3 alarm2.py')
else:
    print('Not activated')