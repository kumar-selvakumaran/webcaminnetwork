from flask import Flask, render_template, Response
from camera import VideoCamera
import cv2
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type:image/jpeg\r\n'
            b'Content-Length: ' + f"{len(frame)}".encode() + b'\r\n'
            b'\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
