import cv2 as cv

from flask import Flask, render_template, Response

from camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/controller/')
def controller():
    return render_template('controller.html')


def gen(camera):
    while True:
        frame = camera.get_frame()

        if frame is not None:
            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n\r\n" + frame.tobytes() + b"\r\n")
        else:
            print("frame is none")


@app.route("/video_feed")
def video_feed():
    return Response(gen(Camera()),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.debug = True
    app.run(host="127.0.0.1", port=5000, threaded=True)
