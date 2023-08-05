#Wikicivi Crawler Client SDK
import os,time
import datetime

#LOG,INFO,WARN,ERROR,

from .demo import *

def intro():
    print("这是TechYoung课程的机器学习辅助工具包")
    return True

def demo(name="iris"):
    if name == "iris": run_demo_iris()
    elif name == "boston":run_demo_boston()
    elif name == "galton":run_demo_galton()
    else:
        print("仅仅支持iris/boston_house_price/galton")




