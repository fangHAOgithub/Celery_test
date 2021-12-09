# -*- coding: utf-8 -*-

# 导包必须像下面这样，不能【from celery import app】 少丶
from .celery import app

# 1、添加任务
@app.task
def sub(x, y):
    print(x, y)
    return x - y
