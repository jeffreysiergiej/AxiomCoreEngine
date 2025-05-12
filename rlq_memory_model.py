import numpy as np

class RLQMemoryModel:
    def __init__(self, decay_rate=0.98):
        self.memory = {}
        self.decay_rate = decay_rate

    def update(self, key, value):
        if key not in self.memory:
            self.memory[key] = value
        else:
            self.memory[key] = self.decay_rate * self.memory[key] + (1 - self.decay_rate) * value

    def recall(self, key):
        return self.memory.get(key, 0)

    def reset(self):
        self.memory = {}
