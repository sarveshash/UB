"""
from subprocess import getoutput as r
import logging 
a = r("ls Sophia/plugins")
a = a.split('\n')
helpNames = []
help = {}
for x in a:
  if x.endswith('.py'):
    try:
      exec(f"from Sophia.plugins.{x.split('.py')[0]} import MOD_NAME, MOD_HELP")
      helpNames += MOD_NAME
      help[MOD_NAME] = MOD_HELP
    except: pass
p(help)
"""
