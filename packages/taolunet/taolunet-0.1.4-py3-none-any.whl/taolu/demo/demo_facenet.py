from taolu.demo.demo_base import DemoBase
from taolu.vision.base_nets.base_net import BaseNet
import json
from taolu.vision.utils.trainers.triplet_trainer import TripletTrainer
import torch
from taolu.vision.jobs.face_recognition import FaceRecognitionJob
import pickle

if __name__ == '__main__':
    # demo = DemoBase("../vision/base_nets/resnet18.json", "classification")
    # demo.go()
    cfg = json.load(open("../vision/base_nets/facenet.json"))
    data = pickle.load(open("demo_images/bbt_faces.pydata", "rb"))
    cuda = torch.cuda.is_available()
    job = FaceRecognitionJob(cfg, 6, False)
    job.train(data['train_X'], data['train_y'])

