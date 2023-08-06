from __future__ import print_function, absolute_import, division
from base64 import b64decode, b64encode
from subprocess import Popen
from tempfile import mkdtemp
from shutil import rmtree
from time import time
import psutil
import os

SESSION_TIMEOUT = 1 * 60
VALID_SOLVERS = ['gurobi']

class Worker:
    def __init__(self, model, solver, solver_options):
        self.tmp_dir = mkdtemp()
        self.stub = os.path.join(self.tmp_dir, 'model')
        open(self.stub + '.nl', 'wb').write(b64decode(model))
        env = os.environ.copy()
        if solver_options is not None and len(solver_options) > 0:
            env['{}_options'.format(solver)] = str(solver_options)
        self.output = os.path.join(self.tmp_dir, 'output')

        with open(self.output, 'w') as output:
            if solver in VALID_SOLVERS:
                self.process = Popen(
                    [solver, self.stub, '-AMPL'],
                    stderr=output, stdout=output, env=env
                )
            else:
                self.process = None
                print(
                    "Error: {} is not a valid solver!".format(solver),
                    file=output
                )
        self.last_request = time()

    def __del__(self):
        self.terminate()
        rmtree(self.tmp_dir)

    def getSolution(self):
        if self.isAlive():
            return None
        else:
            try:
                return b64encode(open(self.stub + '.sol', 'rb').read())
            except:
                return b64encode('')

    def isActive(self, timeout=SESSION_TIMEOUT):
        return self.isAlive() and time()-self.last_request <= timeout

    def keepActive(self):
        self.last_request = time()

    def isAlive(self):
        if self.process is None:
            return False
        try:
            proc = psutil.Process(self.process.pid)
            if proc.status() == psutil.STATUS_ZOMBIE:
                self.process.wait()
                return False
            return True
        except psutil.NoSuchProcess:
            return False

    def terminate(self):
        try:
            self.process.terminate()
            self.process.wait()
        except Exception:
            pass

    def read(self):
        self.keepActive()
        with open(self.output, 'r') as output:
            return output.read()

