# -*- coding: utf-8 -*-


from celery import Celery

# broker任务队列
broker = 'redis://127.0.0.1:6379/1'
# 结构存储
backend = 'redis://127.0.0.1:6379/2'

app = Celery(__name__, broker=broker, backend=backend,
             include=['celery_task.task1', 'celery_task.task2'])

# 2 启动worker
# 启动命令是：celery -A celery_t worker -l info
# Windows会报错
'''
Traceback (most recent call last):
  File "d:\virtualenvs\luffy\lib\site-packages\billiard\pool.py", line 362, in workloop
    result = (True, prepare_result(fun(*args, **kwargs)))
  File "d:\virtualenvs\luffy\lib\site-packages\celery\app\trace.py", line 635, in fast_trace_task
    tasks, accept, hostname = _loc
ValueError: not enough values to unpack (expected 3, got 0)
worker: Hitting Ctrl+C again will terminate all running tasks!
'''
# 解决：
#
# pip install eventlet
# celery -A celery_t worker -l info -P eventlet

# 定时任务
# celery -A celery_task beat -l info


# ======================================
# 执行定时任务
# 时区
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False
# 任务的定时配置
from datetime import timedelta
from celery.schedules import crontab
app.conf.beat_schedule = {
    'add-task': {
        'task': 'celery_task.task1.add',
        'schedule': timedelta(seconds=3),  # 隔三秒执行一次
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        'args': (300, 150),
    }
}