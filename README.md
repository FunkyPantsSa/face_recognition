- 基于python+OpenCV的人脸识别考勤系统
- 基于python3.7，
  - 需要安装的python库：os , cv2 , dlib , numpy，
  - dlib安装比较麻烦，多查看教程

- 正在开发，目前还不可用
- 开发进度：
    - 实现了动态实现人脸的位置的辨别以及人眼位置的辨别，同时拍30张照片用于机器学习生成人脸数据。
    - 在脚本开始之前输入名字
    - 新增保存文件函数和重写创建文件夹函数，按照输入名字来命名文件夹。
    
    
 - 已知bug  
   - 截图的时候会吧drawline函数的线截图进去，
   - 录入完成后只能手动关闭窗口
   - 只能录入一次，随后需要再次运行函数，逻辑问题
    