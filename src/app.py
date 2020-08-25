import streamlit as st
import time
import wolftube

st.title('WolfTube')

url = st.text_input('Enter the URL of the YouTube video')

download_type = st.radio("",("Audio","Video","Audio Playlist","Video Playlist"))

if st.button("Download"):
    if url:
        try:
            if download_type == "Audio":
                audio_downloaded,if_error = wolftube.Download_file((2,url)) 
                if audio_downloaded:
                    with st.spinner("Converting..."):
                        time.sleep(2)
                    st.success("File Downloaded to Audio/ ")
                else:
                    st.error(if_error)

            elif download_type == "Video":
                video_downloaded,if_error = wolftube.Download_file((1,url))
                if video_downloaded:
                    with st.spinner("Converting..."):
                        time.sleep(2)
                    st.success("File Downloaded to Video/ ")
                else:
                    st.error(if_error)

            elif download_type == "Video Playlist":
                audio_downloaded,if_error = wolftube.Download_file((3,url))
                if audio_downloaded:
                    with st.spinner("Converting..."):
                        time.sleep(2)
                    st.success("Files Downloaded to Audio/ ")
                else:
                    st.error(if_error)

            else:
                video_downloaded,if_error = wolftube.Download_file((4,url))
                if video_downloaded:
                    with st.spinner("Converting..."):
                        time.sleep(2)
                    st.success("Files Downloaded to Video/ ")
                else:
                    st.error(if_error)

        except Exception as e:
            print(e)
            st.error("Error occured! Please check the URL, Refresh the Page and Try Again!")