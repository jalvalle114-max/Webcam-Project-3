import cv2
from modules.camera import Camera
from modules.face_manager import FaceManager

def main():
    camera = Camera()
    faces = FaceManager()

    camera.start()
    print("Press 'a' to add a new face, 'q' to quit.")

    while True:
        frame = camera.get_frame()
        recognized_faces = faces.recognize_face(frame)


        for name, (top, right, bottom, left) in recognized_faces:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        cv2.imshow("Facial Recognition", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('a'):
            name = input("Enter name for new face: ")
            faces.add_face(name, frame)
            print(f"Added face for {name}")
        elif key == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
