from youtube import YoutubeAudio, DownloadInfo, PlaylistInfo
import sys
import json


DOWNLOADED_SONGS_CACHE = "downloaded.json"
DOWNLOADS_FOLDER = "playlists"

class IncorrectArgs(Exception):
    pass

class App:
    def __init__(self) -> None:
        self.downloader = YoutubeAudio(DOWNLOADS_FOLDER)
        self.downloaded = self.get_downloaded()
    
    def get_downloaded(self) -> list[str]:
        with open(DOWNLOADED_SONGS_CACHE, "r") as f:
            data = json.load(f)
        return data
        
    def download_playlists(self, links:list[str]) -> None:
        for link in links:
            self.download_playlist(link)
        
    def download_playlist(self, link:str) -> None:
        if link not in self.downloaded:
            #Downloading
            self.downloader.download_playlist(link)
            
            #Updating download list
            self.downloaded.append(link)
            with open(DOWNLOADED_SONGS_CACHE, "w") as f:
                json.dump(self.downloaded, f)
    
    
def main() -> None:
    #getting passed in args
    args:list[str] = sys.argv
    
    if len(args) == 1:
        raise IncorrectArgs("You must specify environment args when running this script")
    
    app = App()
    app.download_playlists(args[1::])
    

if __name__ == "__main__":
    main()
    
