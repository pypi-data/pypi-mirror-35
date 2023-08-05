import torch
from taolu.vision.base_nets.base_net import BaseNet
from taolu.vision.utils.trainers.triplet_trainer import TripletTrainer
import random


class FaceRecognitionJob:
    def __init__(self, cfg, num_classes=None, cuda=False):
        self.num_classes = num_classes
        self.cfg = cfg
        self.cuda = cuda
        self.model = self.build_model()
        self.optimizer = torch.optim.Adam(self.model.parameters(),lr=1e-3)
        self.trainer = TripletTrainer(cuda, self.model, 0.01, self.optimizer)

    def build_model(self):
        model = BaseNet(self.cfg)
        return model.cuda() if self.cuda else model

    def train(self, x, y):
        for i in range(540):
            triplet = self.model.transformer.transform(x, y)
            self.trainer.train(triplet)
        torch.save(self.model.state_dict(), open("bbt_faces.pt", "wb"))
