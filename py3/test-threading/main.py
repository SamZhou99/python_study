import threading
import time
import atexit


@atexit.register
def exit():
    for th in ths:
        th.stop()
    print("主程序退出")


class MyThreading(threading.Thread):
    def __init__(self, threadID, name, delay) -> None:
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
        self._stop_event = threading.Event()

    def run(self):
        print("开始线程：" + self.name)
        print_time(self, self.name, self.delay, 9)
        print("退出线程：" + self.name)

    def stop(self):
        self._stop_event.set()
        print("停止")


def print_time(thread, threadName, delay, counter):
    while counter:
        if counter <= 6:
            thread.stop()

        if thread._stop_event.is_set():
            break
        time.sleep(delay)
        print(threadName, counter)
        counter -= 1


th_len = 3
ths = []
for i in range(th_len):
    th = MyThreading(i, "th{}".format(i), (i + 1) / 2)
    ths.append(th)

for th in ths:
    th.start()
    print("start")

for th in ths:
    th.join()
    print("join")


print("退出主线程")
