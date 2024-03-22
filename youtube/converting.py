from moviepy.editor import VideoFileClip
import os
import re


DIR = str

def convert_to_mp3(input_file: DIR) -> Exception|DIR:
    try:
        video_clip = VideoFileClip(input_file, verbose=False)
        audio_clip = video_clip.audio
        output_file = input_file.replace(".mp4", ".mp3")
        audio_clip.write_audiofile(output_file)
        video_clip.close()
        os.remove(input_file)

        return output_file
    
    except Exception as e:
        #Temporary
        print(f"Error:{e}")
