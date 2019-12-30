import itertools
import os
import sys
import string

global spinner
spinner = itertools.cycle('-/|\\')
spin = itertools.cycle('-/|\\')

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
