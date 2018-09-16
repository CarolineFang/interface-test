#!C:\Users\15295\Desktop\py\interface-test\seleniumAPI\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'up==0.2.1','console_scripts','up'
__requires__ = 'up==0.2.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('up==0.2.1', 'console_scripts', 'up')()
    )
