'''工具函数'''
import sys,time
def exit():
    input("程序即将推出，按任意键继续！")
    for i in (4,3,2):
        print("程序正在退出···%s"%(i-1))
        time.sleep(1)
    sys.exit(1)
