# coding=utf-8
"""
进程间通信
"""
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def proc_write(q, urls):
    print('Process(%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())


# 读数据进程执行的代码
def proc_read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)

if __name__ == '__main__':
    # 父进程创建Queue并传给各个子进程
    q = Queue()
    proc_writer1 = Process(target=proc_write,args=(q,['url_1','url_2','url_3']))
    proc_writer2 = Process(target=proc_write,args=(q,['url_4','url_5','url_6']))
    proc_reader = Process(target=proc_read,args=(q,))

    # 启动子进程proc_writer,写入
    proc_writer1.start()
    proc_writer2.start()

    # 启动子进程proc_reader,读取
    proc_reader.start()

    # 等待proc_writer结束
    proc_writer1.join()
    proc_writer2.join()

    # 终止proc_reader
    proc_reader.terminate()

