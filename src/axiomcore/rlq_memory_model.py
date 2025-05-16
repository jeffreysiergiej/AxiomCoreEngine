class RLQMemoryModel:
    def __init__(self):
        self.memory = {}

    def update(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key, None)

    def export_state(self):
        return dict(self.memory)  # Safe shallow copy
