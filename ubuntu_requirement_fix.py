import os
import platform

def ubuntu_req_fix(): 
    os_version = platform.version()
    if '18.' in os_version:
        os.system('sudo apt install ffmpeg')
    else:
        os.system('sudo add-apt-repository ppa:jonathonf/ffmpeg-4')
        os.system('sudo apt update')
        os.system('sudo apt remove ffmpeg && sudo apt install -y ffmpeg')