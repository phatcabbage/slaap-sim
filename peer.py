class Peer:
    def __init__(self):
        self.peers = {}
        self.file = None
        self.chunks = set()
        self.remainingChunks = set()

    def _setFile(self, file):
        self.file = file
        self.chunks = set(range(self.chunkCount))
