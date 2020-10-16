class Demon:
    def __init__(self, config, queue):
        self.config = config
        self.queue = queue
        self.alive = True
    def kill(self):
        self.alive = False
    def run(self):
        while(self.alive):
            self.work()
