# WolfTube
WolfTube is a simple to use Video/Audio Downloader.
#### _UPDATE_: Added a Web app and URL check

<img src="img/screenshot1.png?raw=true" width="1000">
<img src="img/screenshot2.png?raw=true" width="1000">
<img src="img/screenshot3.png?raw=true" width="1000">

> Run `pip install -r requirements.txt`. If any problem occurs then run `pip install -r requirements.txt --user`

> For fixing ffmpeg requirements fix Please run `python3 requirement_fix.py`.

### Usage: wolftube.py [-h] [-P] -V <VIDEO_URL> -A <AUDIO_URL>

#### Optional arguments:

  > -h, --help            show this help message and exit. \
  > -P, --playlist        Download Playlist.
  
#### Mandatory arguments:

  > -V <VIDEO_URL>, --video <VIDEO_URL> 
                        Download Video. \
  > -A <AUDIO_URL>, --audio <AUDIO_URL> 
                        Download Audio.
##### After Arguments Please add URL


### Example: 
> First go to the _src/_ folder 
1. For Downloading Single Video  - `python3 wolftube.py -V https://youtu.be/lTTajzrSkCw?list=PLXCjrN_k057Fyr47rOTca9qfP1mfauhdu`

2. For Downloading Video Playlist - `python3 wolftube.py -P -V https://youtu.be/lTTajzrSkCw?list=PLXCjrN_k057Fyr47rOTca9qfP1mfauhdu`

3. For Downloading Single Audio - `python3 wolftube.py -A https://youtu.be/lTTajzrSkCw?list=PLXCjrN_k057Fyr47rOTca9qfP1mfauhdu`

4. For Downloading Audio Playlist - `python3 wolftube.py -P -A https://youtu.be/lTTajzrSkCw?list=PLXCjrN_k057Fyr47rOTca9qfP1mfauhdu`


##### If you are getting error on python versions in Windows. Please try changing `python3` to `python` in each command you run.

## Added Streamlit Web app
> Made a Web App using [__Streamlit__](https://www.streamlit.io/).
#### To run Web App:
1. Go to _src/_ folder.
2. Run command `streamlit run app.py`
3. On the Browser, Enter the Url and select a download option.
4. Click _Download_ button to start Downloading.
5. Video/ Audio will be downloaded in the Video/Audio Folder.

## Thank You!
__Please Give a :star2: if you :+1: it.__
