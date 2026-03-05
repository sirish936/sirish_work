from threading import Thread
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("Hello")

class World(Thread):
    def run(self):
        for i in range(5):
            sleep(1)
            print("World")

t1 = Hello()
t2 = World()

t1.start()
t2.start()

t1.join()
t2.join()

print("Main thread continues to run while Hello and World threads are executing.")
