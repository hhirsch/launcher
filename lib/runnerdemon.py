from runner import Runner
import time
import json
import os, subprocess

class RunnerDemon:
    def __init__(self, queue):
        self.queue = queue
        self.alive = True
    def kill(self):
        self.alive = False
    def run(self):
        while(self.alive):
            job = self.queue.get()
            if (job):
                print(job)
                if (job == 'kill'):
                    self.kill()
                else:
                    runner = json.loads(job)
                    subprocess.run(runner['call'], cwd=runner['path'], capture_output=False)
