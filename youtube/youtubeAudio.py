from dataclasses import dataclass
import os
from pytube import YouTube, Playlist
from .converting import convert_to_mp3

@dataclass
class DownloadInfo:
    title:str
    file_name:str
    image_url:str
    youtuber:str

@dataclass
class PlaylistInfo:
    title:str
    length:int
    
    
class YoutubeAudio:
    def __init__(self, downloads_folder:str):
        self.download_folder = downloads_folder
        
    def download_song(self, song_url:str, folder:str) -> DownloadInfo:
        try:
            video = YouTube(song_url)
            file_name = f"{video.title}.mp4"
            file_path = os.path.join(folder, file_name)
            
            data = DownloadInfo(video.title, f"{video.title}.mp3", video.thumbnail_url, video.author)
            
            audio = video.streams.filter(file_extension='mp4').first()
            
            if audio:
                audio.download(output_path=folder, filename=file_name)
                convert_to_mp3(file_path)
                return data
                
        except Exception as e:
            print(e)
            return e
        
    def download_playlist(self, playlist_url:str) -> tuple[PlaylistInfo, list[DownloadInfo]]:
        try:
            playlist = Playlist(playlist_url)
            
            playlist_data = PlaylistInfo(playlist.title, playlist.length)
            song_data:list[DownloadInfo] = []
            
            for video_url in playlist.video_urls:
                data = self.download_song(video_url, os.path.join(self.download_folder, playlist.title))
                if data:
                    song_data.append(data)
            return playlist_data, song_data
        except Exception as e:
            print(e)
            return e
        