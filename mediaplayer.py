#!/usr/bin/python

from globals import *

class MediaPlayer:
    STOPPED = 0
    PAUSED = 1
    PLAYING = 2

    def __init__(self):
        self.file = None
        self.chunks = set()
        self.position = 0
        self.state = MediaPlayer.STOPPED

    def play(self): 
        self.state = MediaPlayer.PLAYING
        Timer.schedule(Timer.now + 1.0, MediaPlayer.PlayTimer(self,"PLAYING",self.position))

    def _event(self, e, arg):
        print("Event: " + e + "(" + str(arg)+ ") @ "+ str(Timer.now))
        if e == "PLAYING":
            if self.state == MediaPlayer.PLAYING:
                self._play(arg)
        elif e == "UNDERRUN":
            self.stop()
        elif e == "PAUSE":
            self.pause()
        elif e == "STOP":
            self.stop()
        elif e == "PLAY":
            self.play()

    def _receive(self, chunk):
        self.chunks.add(chunk)
            
    def _play(self, chunk):
        if chunk in self.chunks:
            self._event("PLAYED",self.position)
            self.position += 1
            Timer.schedule(Timer.now + 1.0, MediaPlayer.PlayTimer(self,"PLAYING",self.position))
        else:
            self._event("UNDERRUN", self.position)

    def pause(self):
        self.state = MediaPlayer.PAUSED

    def stop(self):
        self.position = 0
        self.state = MediaPlayer.STOPPED

    class PlayTimer:
        def __init__(self, player, eventtype, arg=None):
            self.type = eventtype
            self.arg = arg
            self.player = player

        def __call__(self):
            self.player._event(self.type, self.arg)
        
        
if __name__ == "__main__":
    mp = MediaPlayer()
    mp.chunks.update(range(10))
    Timer.schedule(0, MediaPlayer.PlayTimer(mp,"PLAY"))
    Timer.schedule(1.5, MediaPlayer.PlayTimer(mp,"PAUSE"))
    Timer.schedule(3, MediaPlayer.PlayTimer(mp,"PLAY"))
    Timer.schedule(6, MediaPlayer.PlayTimer(mp,"STOP"))
    Timer.schedule(8, MediaPlayer.PlayTimer(mp,"PLAY"))
    
    while not Timer.empty():
        Timer.tick()
