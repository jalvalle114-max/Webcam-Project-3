import face_recognition
import pickle
import cv2
from .utils import save_pickle, load_pickle

class FaceManager:
    """Manages face encoding, recognition, and storage."""

    def __init__(self, known_faces_file="faces.pkl"):
        self.known_faces_file = known_faces_file
        self.known_faces = self.load_faces()

    def add_face(self, name: str, image):
        """Adds a new face with encoding."""
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb_image)
        if len(encodings) == 0:
            raise ValueError("No face detected in the image.")
        self.known_faces[name] = encodings[0]
        self.save_faces()

    def recognize_face(self, frame):
        """Recognizes faces in a given frame."""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        results = []

        for location, encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(list(self.known_faces.values()), encoding)
            name = "Unknown"
            if True in matches:
                matched_idx = matches.index(True)
                name = list(self.known_faces.keys())[matched_idx]
            results.append((name, location))
        return results

    def save_faces(self):
        """Saves known faces to file."""
        save_pickle(self.known_faces_file, self.known_faces)

    def load_faces(self):
        """Loads known faces from file."""
        data = load_pickle(self.known_faces_file)
        return data if data else {}

