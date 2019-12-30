import argparse


def print_error(error_msg):
    if "unrecognized arguments" in error_msg:
        print("Invalid Arguments. Please see help [-h] or [--help]")
    else:
        pass


def parse_argument():
    parser = argparse.ArgumentParser(
        prog="wolftube.py", description="Youtube Downloader")

    parser.add_argument("-P", '--playlist', dest='<playlist_url>',
                        help="Download Playlist", action='store_true', default=False)

    parser.add_argument('-V', '--video', dest='<video_url>',
                        help="Download Video", required=True)
    parser.add_argument('-A', '--audio', dest='<audio_url>',
                        help="Download Audio", required=True)

    try:
        parser.error = print_error
        args = parser.parse_args()
        if not args.playlist_url:
            if args.video_url:
                return (1, args.video_url)
            elif args.audio_url:
                return (2, args.audio_url)
        else:
            if args.video_url:
                return (3, args.video_url)
            elif args.audio_url:
                return (4, args.audio_url)
    except:
        print("After Arguments Please add URL")
