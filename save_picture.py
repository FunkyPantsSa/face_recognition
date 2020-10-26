def save_picture( path,usr):
    #保存30张照片
    import cv2
    num = 0
    for i in range(1, 31):
        num = i
        cv2.imwrite('picture/'+usr+"/camera" + str(num) + '.jpg', path)
