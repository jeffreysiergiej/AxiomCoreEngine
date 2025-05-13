import time

class AxiomOSKernel:
    def __init__(self):
        self.task_queue = []

    def schedule_task(self, task):
        self.task_queue.append(task)

    def run_all(self):
        while self.task_queue:
            task = self.task_queue.pop(0)
            print(f"Running: {task.__name__}")
            task()
            time.sleep(0.1)
