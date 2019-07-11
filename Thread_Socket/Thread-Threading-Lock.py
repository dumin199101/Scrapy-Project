# coding=utf-8
"""
线程同步
"""
import threading
import time
import random

mylock = threading.RLock()
num = 0


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print('%s locked,Number: %d' % (threading.current_thread().name, num))
            time.sleep(random.random())
            if num >= 100:
                mylock.release()
                time.sleep(random.random())
                print('%s released,Number:%d' % (threading.current_thread().name, num))
                break
            num += 1
            print('%s released,Number:%d' % (threading.current_thread().name, num))
            time.sleep(random.random())
            mylock.release()


if __name__ == '__main__':
    thread1 = myThread(name='Thread-1')
    thread2 = myThread(name='Thread-2')
    thread1.start()
    thread2.start()
