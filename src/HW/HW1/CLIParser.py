import sys
import re

'''Defines command line arguments'''
help = "USAGE: py helper.py [OPTIONS] [-g ACTION]\n\n\
-d --dump   on crash, dump stack = false\n\
-g --go    start-up action = data\n\
-h --help   show help   = false\n\
-s --seed   random number seed  = 937162211"

def func(s):
    if re.search("^%s*(.-)%s*$", s):
        return True
    else:
        return False

def coerce(s):
    try:
        return int(s)
    except:
        try:
            return float(s)
        except:
            return func(s)
    
    
def settings(s):
  t = {}
  for k, v in re.findall('\n[\s]+[-][^\s]+[\s]+[-][-]([^\s]+)[^\n]+= ([^\s]+)', s):
    t[k] = coerce(v)
   
  return t

def cli(options):
    args = sys.argv
    for k, v in options.items():
        v = str(v)
        for i in range(1, len(args)):
            if args[i] == '-' + k[0:1] or args[i] == '--' + k:
              if v == "False":
                v = "true"
              elif v == "True":
                v = "false"
              else:
                v = args[i + 1]
        options[k] = coerce(v)
    return options

if __name__ == "__main__":
    print(settings(help))