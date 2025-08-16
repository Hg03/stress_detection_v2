from stress_detection.utils import get_config

class FEOrchestrator:
    def __init__(self, config):
        self.config = config
    
    def load(self):
        pass
    
    def process(self):
        pass

    def store(self):
        pass

    def execute(self):
        self.load()
        self.process()
        self.store()

if __name__ == "__main__":
    FEOrchestrator(get_config("feature_config")).execute()
    print("Feature Pipeline Completed Successfully")