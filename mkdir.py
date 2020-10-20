
#创建文件夹
def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return 0

# from mkdir import mkdir
# mkpath = "picture"
# mkdir(mkpath)
