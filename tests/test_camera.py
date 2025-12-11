import pytest
from modules.camera import Camera

def test_camera_start_release():
    cam = Camera()
    cam.start()
    frame = cam.get_frame()
    assert frame is not None
    cam.release()
