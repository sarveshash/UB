import sys
import os
from subprocess import getoutput as r

def restart_program():
    try:
        python = sys.executable
        script = os.path.abspath(sys.argv[0])
        os.execl(python, python, script, *sys.argv[1:])
    except:
        r("cd && cp SophiaUB restarter && cd restartet && python3 -m Sophia")
