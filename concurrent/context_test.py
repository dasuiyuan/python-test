# -*- coding: utf-8 -*-
# @Time: 2025/7/10 15:38
# @Author: Sui Yuan
# @Software: PyCharm
# @Desc:

import asyncio
import contextvars

my_var = contextvars.ContextVar('my_var', default=None)


def parent_task_1():
    my_var.set('aa')
    print(my_var.get())
