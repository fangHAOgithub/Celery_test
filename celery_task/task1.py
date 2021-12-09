# -*- coding: utf-8 -*-
from .celery import app

# 1、添加任务
@app.task
def add(x, y):
    print(x, y)
    return x + y


