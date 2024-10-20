from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Инициализация веб-камеры
cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = cap.read()  # Чтение кадра
        if not success:
            break
        else:
            # Кодирование в JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Возвращение кадра

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)