import subprocess
import re
import os
import zipfile
import requests


def download_ffmpeg(file):
    try:
        print("Beginning file download with requests..")
        url = 'https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20191126-59d264b-win64-static.zip'
        r = requests.get(url, stream=True)

        with open(file, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            if total_length is None:
                f.write(r.content)
            else:
                dl = 0
                for data in r.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    not_done = 50 - done
                    prog = '[' + '='*done + '-' * not_done + ']'
                    percent = str(round(50 * dl / total_length, 1)*2) + '%'
                    print("Downloading ffmpeg", next(spin),
                          prog, percent, '\r', end='')
    except:
        print()
        print("Error Downloading ffmpeg. Please try again..")
        return


def extract_ffmpeg(file):
    try:
        with zipfile.ZipFile(file, "r") as zip_ref:
            zip_ref.extractall("ffmpeg")
    except:
        print("Bad Zip file. Downloading ffmpeg again..")
        download_ffmpeg(file)

def path_exist(path):
    command = f'echo ;%PATH%; | find /C /I ";{path};"'
    output = subprocess.Popen(command, stdout=subprocess.PIPE,shell = True ).communicate()[0]
    check = int(re.findall(r'\d',str(output))[0])
    return check

def set_path():
    try:
        cwd = os.getcwd()
        path = r"ffmpeg\ffmpeg-20191126-59d264b-win64-static\bin"
        path_variable = os.path.join(cwd, path)
        if path_exist(path_variable):
            return
        print("Setting path variable..")
        subprocess.call(f'setx PATH %path%;{path_variable}')
    except:
        print("Error setting path variable. Please try again..")
        return


def windows_requirements_fix():
    try:
        file = 'ffmpeg-20191126-59d264b-win64-static.zip'
        if not os.path.isfile(file):
            download_ffmpeg(file)
            print()
            print("Downloaded ffmpeg. Extracting...")
        if not os.path.isdir('ffmpeg'):
            extract_ffmpeg(file)

        set_path()

    except Exception as error:
        print("Error fixing Windows requirements. Please try again!")


if __name__ == "__main__":
    if os.name is 'nt':
        windows_requirements_fix()