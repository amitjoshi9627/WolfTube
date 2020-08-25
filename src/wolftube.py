import download
import sys
import URL_process

def Download_file(arg):
    return download.download(arg)

try:
    arg = URL_process.parse_argument()
    Download_file(arg)
except:
    print("\nDue to some technical Error the program is exiting.. Please Try again..")
    sys.exit(0)
