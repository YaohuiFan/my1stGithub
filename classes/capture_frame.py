
import cv2
import numpy as np
from PIL import Image, ImageDraw
from pathlib import Path


class CaptureFrame():
    """ This class handles capturing a frame from a video. """

    def __init__(self, src_video: Path):

        self.video = src_video

        self.video_capture = cv2.VideoCapture(src_video.as_posix())

    def get_frame_data(self) -> tuple:
        is_okay, image = self.video_capture.read()
        if is_okay:
            return is_okay, image
        else:
            print(f'Failed to capture frame from {self.video.as_posix()}')
            return is_okay, 0

    def view_img(self):
        is_okay, image = self.get_frame_data()
        if is_okay:
            im = Image.fromarray(image)
            im.show()

    def save_img(self, des_file: Path):
        is_okay, image = self.get_frame_data()

        if is_okay:
            im = Image.fromarray(image)
            im.save(des_file.as_posix())

        print(f'{des_file.as_posix()} saved.')


if __name__ == '__main__':

    default_video = Path(r'/home/trueview/Videos/sample.mp4')
    src_video = default_video

    # The VideoCapture method can take a variety of arguments
    video_capture = cv2.VideoCapture(src_video.as_posix())

    # The video capture object can then be used to read frame by frame
    #   The img is literally an image , type(img) -> numpy.ndarray
    # is_sucessfuly_read is a boolean which returns true or false depending
    #   on whether the next frame is successfully grabbed.
    is_sucessfully_read, img = video_capture.read()

    if is_sucessfully_read:
        to_file = src_video.parent / 'frame-1.png'
        save_img(img, to_file)