import threading
import time


def Example2():
    print(456)
    time.sleep(0.5)
    print(654)

def simplefunc():
    print(123)
    time.sleep(1)
    print(321)

if __name__ == "__main__":
    thread1 = threading.Thread(target=simplefunc)
    thread1.start()

    thread2 = threading.Thread(target=Example2)
    thread2.start()