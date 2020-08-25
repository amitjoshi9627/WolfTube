from __future__ import unicode_literals
import utils
import youtube_dl
import sys


def download(arg):

    if arg:
        choice, url = arg
        video_found,if_error = utils.check_url(url)
        if not video_found:
            return False,if_error
        if choice == 1:
            download_video(url)
        elif choice == 2:
            download_audio(url)
        elif choice == 3:
            download_video(url, False)
        elif choice == 4:
            download_audio(url, False)
        return True, None


def download_audio(url='https://youtu.be/8VK3YUhZKx8', no_playlist=True, start=1, end=None):
    utils.check_dir("A")
    ydl_opts = {
        'outtmpl': 'Audio/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'writesubtitles': False,
        'noplaylist': no_playlist,
        'restrictfilenames': True,
        'ignoreerrors': True,
        'playliststart': start,
        'plalistend': end,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'logger': utils.MyLogger(),
        'progress_hooks': [my_hook_audio],
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as Error:
        print("Download Error")

def download_video(url="https://youtu.be/8VK3YUhZKx8", no_playlist=True, start=1, end=None):
    utils.check_dir("V")
    ydl_opts = {'outtmpl': 'Video/%(title)s.%(ext)s',
                'restrictfilenames': True,
                'ignoreerrors': True,
                'playliststart': start,
                'plalistend': end,
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio',
                'logger': utils.MyLogger(),
                'writesubtitles': True,
                'noplaylist': no_playlist,
                'progress_hooks': [my_hook_video]

                }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except Exception as Error:
        print("Download Error")


def my_hook_video(d):
    filename = d['filename']
    flag = 0
    if '.mp4' in filename:
        flag = 1
    if d['status'] == 'finished' and flag:
        print('Done downloading')
        print("File Size: ", str(round(d['total_bytes']/1024, 2)), 'Kib')
        try:
            filename = utils.format_filename(d['filename'])
        except:
            filename = d['filename']
        utils.show_notification(filename)

    else:

        if flag == 0:
            print("Converting...", '\r', end='')
        else:
            utils.progress(d['_percent_str'])


def my_hook_audio(d):

    if d['status'] == 'finished':
        print('Done downloading')
        print("File Size:", {round(d['total_bytes']/1024, 2)}, "Kib")
        try:
            filename = utils.format_filename(d['filename'])
        except:
            filename = d['filename']
        utils.show_notification(filename, 'Audio')

    else:
        utils.progress(d['_percent_str'])
