# coding=utf-8
"""
携程：只有一个线程，并发执行
"""
from gevent import monkey

# 自动切换携程，通过greenlet实现
monkey.patch_all()
import gevent
import requests


def run_task(url):
    print('Visit - ->%s' % url)
    try:
        response = requests.get(url)
        data = response.text
        print("%d bytes received from %s." % (len(data),url))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    urls = ["https://github.com/","https://www.python.org/","http://www.cnblogs.com/"]
    # 形成携程
    greenlets = [gevent.spawn(run_task,url) for url in urls]
    # 启动任务
    gevent.joinall(greenlets)
