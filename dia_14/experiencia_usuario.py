import time
import sys
import os
# sys.platform detecta el sistema operativo de donde estamos trabajando
print(sys.platform)

time.sleep(3)
print('Han pasado 3 segundos')
time.sleep(1)
# Codificación tradicional
"""
if sys.platform == 'win32':
    clear = 'cls'
else:
    clear = 'clear'
"""
# exit()

clear = 'cls' if sys.platform == 'win32' else 'clear'
os.system(clear)

