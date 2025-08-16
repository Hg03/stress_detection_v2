from stress_detection.utils import get_config

class TRAINOrchestrator:
    def __init__(self, config):
        self.config = config
    
    def load(self):
        pass
    
    def train(self):
        pass
    
    def store(self):
        pass

    def execute(self):
        self.load()
        self.train()
        self.store()

if __name__ == "__main__":
    TRAINOrchestrator(get_config("training_config")).execute()
    print("Training Pipeline Completed Successfully")