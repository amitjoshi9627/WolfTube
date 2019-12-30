from utils import *
from URL_process import *
from download import *

try:
    arg = parse_argument()
    download(arg)
except:
    print("Due to some technical Error the program is exiting.. Please Try again..")
    sys.exit(0)
