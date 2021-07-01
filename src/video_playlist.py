"""A video playlist class."""

from .video_library import VideoLibrary

class Playlist:
    def __init__(self,playlist_name, video_id = ''): #default for new playlists
        self._video_library = VideoLibrary()
        #dictionary to store multiple playlists
        self.playlist = {}
        #dictionary with a list of videos in that specific playlist
        self.playlist[self.playlist][] = video_id
        
    """A class used to represent a Playlist."""
