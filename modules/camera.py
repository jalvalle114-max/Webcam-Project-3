import cv2

class Camera:

    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.video = None

    def start(self):
        self.video = cv2.VideoCapture(self.camera_index)
        if not self.video.isOpened():
            raise ValueError("Unable to open webcam.")

    def get_frame(self):
        if self.video is None:
            raise ValueError("Camera has not been started.")
        ret, frame = self.video.read()
        if not ret:
            raise ValueError("Failed to read frame from camera.")
        return frame

    def release(self):
        if self.video:
            self.video.release()
            self.video = None
s
