import os
from ubuntu_requirement_fix import ubuntu_req_fix
from windows_requirement_fix import windows_req_fix

if __name__ == "__main__":
    if os.name == 'posix':
        ubuntu_req_fix()
    elif os.name == 'nt':
        windows_req_fix()
