import time

flag = True
print("***欢迎来到好男人检测器***")
while flag:
    name = input("请输入姓名：")
    for i in range(3):
        print("***检测中***")
        time.sleep(1)
    if name == "阿宝" or name == "abao" or name == "a bao" or name == "阿 宝":
        print("结果为： 渣男！")
    else:
        print("结果为： 好男人！")
    
    choice = input("按任意继续，按q退出: ")
    if choice != "q":
        pass
    else:
        flag = False