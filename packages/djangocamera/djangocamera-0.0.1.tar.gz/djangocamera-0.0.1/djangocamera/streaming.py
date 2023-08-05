from django.http import StreamingHttpResponse
from djangocamera.camera import VideoCamera
    
def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed():
    return StreamingHttpResponse(gen(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')
