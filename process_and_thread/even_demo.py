# coding=utf-8

""" Event（事件）

Event内部包含了一个标志位，初始的时候为false。可以使用set()来将其设置为true；或者使用clear()将其从新设置为false；可以使用is_set()来检查标志位的状态；

另一个最重要的函数就是wait(timeout=None)，用来阻塞当前线程，直到event的内部标志位被设置为true或者timeout超时。如果内部标志位为true则wait()函数理解返回。


"""

import multiprocessing
import time


def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    print('wait_for_event: starting')
    e.wait()
    print('wait_for_event: e.is_set()->', e.is_set())


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    print('wait_for_event_timeout: starting')
    e.wait(t)
    print('wait_for_event_timeout: e.is_set()->', e.is_set())


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(
        name='block',
        target=wait_for_event,
        args=(e,),
    )
    w1.start()

    w2 = multiprocessing.Process(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e, 2),
    )
    w2.start()
    print('main: waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    print('main: event is set')
