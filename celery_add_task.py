# -*- coding: utf-8 -*-


from celery_task.task1 import add
from celery_task.task2 import sub

# 普通执行
# res1 = add(5, 6)
# print(res1)


# 提交任务
# res1 = add.delay(5, 6)
# print(res1)

# res2 = sub(5, 6)
# print(res2)


# 提交延迟任务
from datetime import datetime, timedelta
# 需要utc时间
eta = datetime.utcnow() + timedelta(seconds=10)
ret = add.apply_async(args=(240, 50), eta=eta)
print(ret)

