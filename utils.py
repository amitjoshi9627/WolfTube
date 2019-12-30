import requests
import itertools
import os
import sys
import string
import subprocess
import zipfile

global spinner
spinner = itertools.cycle('-/|\\')
spin = itertools.cycle('-/|\\')


def windows_requirements_fix():

    if os.name is not 'nt':
        return

    try:
        print("Beginning file download with requests..")
        try:
            url = 'https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20191126-59d264b-win64-static.zip'
            r = requests.get(url, stream=True)
            file = 'ffmpeg-20191126-59d264b-win64-static.zip'
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

        print()
        print("Downloaded ffmpeg. Extracting...")
        try:
            with zipfile.ZipFile("ffmpeg-20191126-59d264b-win64-static.zip", "r") as zip_ref:
                zip_ref.extractall("ffmpeg")
        except:
            print("Error extracting zipfile. Please try again..")
            return

        print("Setting path variable..")
        try:
            cwd = os.getcwd()
            path = 'ffmpeg/ffmpeg-20191126-59d264b-win64-static/bin'
            path_variable = os.path.join(cwd, path)

            subprocess.call(f"setx PATH '%path%;{path_variable}'")
        except:
            print("Error setting path variable. Please try again..")
            return

    except:
        print("Error fixing Windows requirements. Please try again!")


def format_filename(filename):
    filename = filename.split('/')[-1].split('.')[0]
    punc = string.punctuation + "'"+'"'
    for p in punc:
        filename = filename.replace(p, '')
    return filename


def show_notification(file_Name, content='Video'):
    file_Name = file_Name.replace(' ', '_')
    message = f"Downloaded-{content}={file_Name}"
    if os.name == 'posix':
        title = "Wolftube"
        os.system(f"notify-send  {title} {message}")
    else:
        print(message)


def progress(percent):

    percent = percent.strip()
    perc = percent.replace('%', '')
    filled_len = int(round(float(perc) * 0.5))
    empty_len = 50 - filled_len
    prog = '[' + '='*filled_len + '-' * empty_len + ']'

    print("Downloading file", next(spinner),
          prog, percent, '\r', end='')


def check_dir(content):
    if content == "V":
        if not os.path.exists("Video"):
            os.mkdir("Video")
    else:
        if not os.path.exists("Audio"):
            os.mkdir("Audio")


def check_formats(url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(url, download=False)
    formats = meta.get('formats', [meta])
    for i in formats:
        if i['format_note'] != 'tiny':
            print(i['format_id'], i['ext'], i['format_note'])


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
