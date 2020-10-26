
def drawline (path):  #画出人脸和人眼的线
    import cv2
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #opencv库的文件，检测人脸
    eye_cascade = cv2.CascadeClassifier( 'haarcascade_eye.xml')#OpenCV库的文件，检测人眼
    faces = face_cascade.detectMultiScale(path, 1.3, 2)
    img = path
    for (x, y, w, h) in faces:
        # 画出人脸框，蓝色，画笔宽度微
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
        face_area = img[y:y + h, x:x + w]

        ## 人眼检测
        # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
        eyes = eye_cascade.detectMultiScale(face_area, 1.3, 10)
        for (ex, ey, ew, eh) in eyes:
            # 画出人眼框，绿色，画笔宽度为1
            cv2.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 1)

def world (path):   #写字
    import cv2
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(path, "Face Register", (20, 40), font, 1, (0, 0, 255), 1, cv2.LINE_AA)
    # cv2.putText(frame, "N: New face folder", (20, 350), font, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(path, "S: Save face", (20, 400), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.putText(path, "Q: Quit", (20, 450), font, 0.8, (0, 0, 255), 1, cv2.LINE_AA)



def fps (path): #显示视频帧率 ，，已经弃用
    import cv2
    # ——————————————————————————————
    # ————————添加自己的视频播放路径———————————
    video_path = path


    # 创建一个视频读写类
    video_capture = cv2.VideoCapture(video_path)

    # 读取视频的fps,  大小
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    size = (video_capture.get(cv2.CAP_PROP_FRAME_WIDTH), video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print("fps: {}\nsize: {}".format(fps, size))


