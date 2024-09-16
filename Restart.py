import sys
import os
from subprocess import getoutput as r

def restart_program():
    try:
        r("cd && cp SophiaUB restarter && cd restartet && python3 -m Sophia")
    except:
        python = sys.executable
        script = os.path.abspath(sys.argv[0])
        os.execl(python, python, script, *sys.argv[1:])
