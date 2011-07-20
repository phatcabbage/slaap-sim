#!/usr/bin/python

class File:
    def __init__(self, name, chunkSize, chunkCount):
        assert chunkSize > 0
        assert chunkCount > 0
        self.name = name
        self.chunkSize = chunksize
        self.chunkCount = chunkCount

    def size(self):
        return self.chunkSize * self.chunkCount
    
