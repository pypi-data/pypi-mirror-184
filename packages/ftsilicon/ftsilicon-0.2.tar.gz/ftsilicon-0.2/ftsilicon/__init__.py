import mediapipe as mp
import cv2

class Ft():
    def __init__(self):
        self.facemd = mp.solutions.face_mesh
        self.face = self.facemd.FaceMesh(refine_landmarks = True)
        self.facecon = mp.solutions.face_mesh_connections

    def show_lm(self, img):
        img = cv2.flip(img, 1)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.face.process(rgb)
        mesh = result.multi_face_landmarks
        h, w, _ = img.shape
        if mesh:
            landmarks = mesh[0].landmark
            for landmark in landmarks:
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                cv2.circle(img, (x, y), 5, (0, 0, 255), 10, cv2.FILLED)
        return img
    def track(self, img, show_lm=True):
        img = cv2.flip(img, 1)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.face.process(rgb)
        self.mesh = result.multi_face_landmarks
        self.h, self.w, _ = img.shape
        if self.mesh:
            landmarks = self.mesh[0].landmark
            for landmark in landmarks:
                x = int(landmark.x * self.w)
                y = int(landmark.y * self.h)
                if show_lm:
                    cv2.circle(img, (x, y), 2, (0, 0, 255), 2, cv2.FILLED)
        return img
    def get_lm(self):
        lm = []
        if self.mesh:
            landmarks = self.mesh[0].landmark
            for landmark in landmarks:
                x = int(landmark.x * self.w)
                y = int(landmark.y * self.h)
                lm.append([x, y])
        return lm