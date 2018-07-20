
from classes.capture_frame import CaptureFrame
from pathlib import Path

class MainWindow():

    def __init__(self, src_video: Path):

        self.cf = CaptureFrame(src_video)

if __name__ == '__main__':

    default_video = Path(r'/home/fanwillow/Videos/myVideos/Samsung/20140604_184135.mp4')

    main = MainWindow(default_video)

    to_file = default_video.parent / 'frame-1.png'
    main.cf.save_img(to_file)