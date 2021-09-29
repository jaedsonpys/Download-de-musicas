from pytube import YouTube
import pytube
import pytube.exceptions as pt

class PyTube:
    def download_video(self, url):
        try:
            video = YouTube(url).streams.filter(file_extension='mp4').first()
            if video is None:
                return False

            video.download()
        except (pt.AgeRestrictedError, pt.VideoRegionBlocked, pt.PytubeError):
            return False
        return True


    def download_audio(self, url):
        try:
            video = YouTube(url).streams.filter(file_extension='mp4',only_audio=True).first()
            if video is None:
                return False

            video.download(filename=video.title+'.mp3')
        except (pt.AgeRestrictedError, pt.VideoRegionBlocked, pt.PytubeError):
            return False
        else:
            return True


    def get_info(self, url):
        try:
            video = YouTube(url).streams.filter(file_extension='mp4').first()
            if video is None:
                return False

            video_info = {
                'title': video.title,
                'size': video.filesize,
            }
        except (pt.AgeRestrictedError, pt.VideoRegionBlocked, pt.PytubeError):
            return False
        else:
            return video_info