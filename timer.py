#!/bin/usr/python

from heapq import heappush, heappop

class Timer:
    def __init__(self):
        self.heap = []
        self.timerid = 1
        self.now = 0.0

    def schedule(self, time, f):
        assert time >= self.now
        entry = [ time, self._allocateTimerId(), f]
        heappush(self.heap, entry)

    def _allocateTimerId(self):
        tempid = self.timerid
        self.timerid += 1
        return tempid

    def tick(self):
        entries = []
        time, timerid, f = heappop(self.heap)
        self.now = time
        
        entries.append(f)
        while self.heap:
            time, timerid, f = heappop(self.heap)
            if(time > self.now):
                heappush(self.heap, [time, timerid, f])
                break
            else:
                entries.append(f)
                
        for o in entries: o()

    def empty(self):
        return not self.heap

class Printer:
    def __init__(self, msg):
        self.message = msg
        
    def perform(self):
        print(self.message)

    def __call__(self):
        self.perform()

if __name__ == "__main__":
    t = Timer()
    t.schedule(1, Printer("Hello"))
    t.schedule(2, Printer("World"))
    t.schedule(3, Printer("I am the printer"))
    t.schedule(2.5, Printer("Going back to the future"))
               
    while not t.empty():
        t.tick()
        
