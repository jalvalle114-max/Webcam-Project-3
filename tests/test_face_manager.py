import numpy as np
import pytest
from modules.face_manager import FaceManager

def test_add_face():
    fm = FaceManager("test_faces.pkl")
    dummy_face = np.zeros((100, 100, 3), dtype=np.uint8)
    try:
        fm.add_face("Test", dummy_face)
    except ValueError:
        pass

def test_save_load():
    fm = FaceManager("test_faces.pkl")
    fm.known_faces = {"Alice": np.zeros(128)}
    fm.save_faces()
    fm2 = FaceManager("test_faces.pkl")
    assert "Alice" in fm2.known_faces
