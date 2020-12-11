import cv2 as cv


class Camera(object):
    # カメラ認識
    def __init__(self):
        # self.video = cv.VideoCapture('movie_01.mp4')
        self.video = cv.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):

        face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
        body_cascade = cv.CascadeClassifier('haarcascade_fullbody.xml')

        # while True:
        # while (cap.isOpened()):
        success, image = self.video.read()

        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        fullbody = body_cascade.detectMultiScale(gray, 1.1, 2)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # detect face
        for (x, y, w, h) in faces:
            cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            eye_gray = gray[y:y + h, x:x + w]

        # body detect
        for (x, y, w, h) in fullbody:
            cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 1)

        ret, frame = cv.imencode('.jpg', image)

        return frame


