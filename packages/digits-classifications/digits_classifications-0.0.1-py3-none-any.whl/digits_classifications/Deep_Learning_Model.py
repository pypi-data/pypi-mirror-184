from abc import ABC, abstractmethod

class Deep_Learning(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def prepare_model(self):
        pass

    @abstractmethod
    def train_model(self):
        pass

    @abstractmethod
    def processing_images(self):
        pass

    @abstractmethod
    def predict_model(self):
        pass

