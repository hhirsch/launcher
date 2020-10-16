from demon import Demon
from runner import Runner
import time
import json
import os, subprocess

class RunnerDemon(Demon):
    def startSubprocess(self, runner):
        if (runner['runInShell'] == 'yes'):
            subprocess.run(runner['call'], cwd=runner['path'],
                           capture_output=True, shell=True, check=True)
        else:
            subprocess.run(runner['call'], cwd=runner['path'], capture_output=False)
    def work(self):
        job = self.queue.get()
        if (job):
            if (job == 'kill'):
                self.kill()
            else:
                runner = json.loads(job)
                self.startSubprocess(runner)
                if runner['startup']:
                    for index, startupRunner in enumerate(runner['startup']):
                        self.startSubprocess(startupRunner)
