import threading


def camera():
    global name
    import os
    import shutil
    import cv2
    import dlib
    import img as img
    import numpy

    # name = input("name")
    cap = cv2.VideoCapture(0)  # 参数0表示调用笔记本内置摄像头

    #face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    #eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    face_cascade = cv2.CascadeClassifier('/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('/haarcascade_eye.xml')

    while True:

        ret, frame = cap.read()  # 见下
        ret2, frame2=cap.read()  #一份给划线，一份给后台处理
        if cv2.waitKey(100) & 0xFF == ord('s'):
            import shutil
            # shutil.rmtree(name)
            from mkdir import mkdir
            mkdir(name)
            from save_picture import save_picture
            save_picture(frame2, name)
            # 存储29张图片,重写调用函数

        from drawline import world    #在页面上显示文字
        world(frame)


        from drawline import drawline  #在页面框取人脸和眼睛
        drawline(frame)

        cv2.imshow("Video", frame)

        if cv2.waitKey(10) == ord("q"):
            break
            # 随时准备按q退出



    """
    函数名：cap.read()
    功  能：返回两个值
           先返回一个布尔值，如果视频读取正确，则为 True，如果错误，则为 False，也可用来判断是否到视频末尾
           再返回一个值，为每一帧的图像，该值是一个三维矩阵
           通用接收方法为：
           ret,frame = cap.read();
           这样 ret 存储布尔值，frame 存储图像
           若使用一个变量来接收两个值，如
           frame = cap.read()
           则 frame 为一个元组，原来使用 frame 处需更改为 frame[1]
    返回值：R1：布尔值
           R2：图像的三维矩阵qq
    """

    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 删除窗口
if __name__ == '__main__':
    camera()
# t2 = threading.Thread(target=camera())
