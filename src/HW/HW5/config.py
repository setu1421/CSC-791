# Default configuration
the = {
    'dump': False,
    'go': "all",
    'seed': 937162211,
    'p': 2,
    'file': 'repgrid1.csv',
    'help': False
}

# Help string
help = '''USAGE: python main.py  [OPTIONS] [-g ACTION]

OPTIONS:
  -d  --dump    on crash, dump stack   = false
  -f  --file    name of file           = data/repgrid1.csv
  -g  --go      start-up action        = all
  -h  --help    show help              = false
  -p  --p       distance coefficient   = 2
  -s  --seed    random number seed     = 937162211
    '''

egs = {}
# Default Seed
Seed = 937162211

n = 0