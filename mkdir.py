
#创建文件夹
import os


def mkdir(path):
    import os

    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
        return True
    else:
        return False

#调用方式
# from mkdir import mkdir
# mkpath = "picture"
# mkdir(mkpath)
