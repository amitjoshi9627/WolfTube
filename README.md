# WolfTube
WolfTube is a simple to use Video/Audio Downloader

> For Windows Users Please run `python windows_requirements_fix.py` for ffmpeg requirements.

> Run `pip install -r requirements.txt`. If any problem occurs then run `pip install -r requirements.txt --user`

### Usage: wolftube.py [-h] [-P] -V <VIDEO_URL> -A <AUDIO_URL>

#### Optional arguments:

  > -h, --help            show this help message and exit.
  > -P, --playlist        Download Playlist.
  
#### Mandatory arguments:

  > -V <VIDEO_URL>, --video <VIDEO_URL>
                        Download Video.
  > -A <AUDIO_URL>, --audio <AUDIO_URL>
                        Download Audio.
##### After Arguments Please add URL


### Example: 
1. For Downloading Single Video  - `python wolftube.py -V https://youtu.be/lTTajzrSkCw?list=PLXCjrN_k057Fyr47rOTca9qfP1mfauhdu`

2. For Downloading Video Playlist - `python wolftube.py -P -V https://youtu.be/lTTajzrSkCw?list=PLXCjrN_k057Fyr47rOTca9qfP1mfauhdu`

3. For Downloading Single Audio - `python wolftube.py -A https://youtu.be/lTTajzrSkCw?list=PLXCjrN_k057Fyr47rOTca9qfP1mfauhdu`

4. For Downloading Audio Playlist - `python wolftube.py -P -A https://youtu.be/lTTajzrSkCw?list=PLXCjrN_k057Fyr47rOTca9qfP1mfauhdu`
