import torch
from taolu.vision.base_nets.base_net import BaseNet
import json

state_dict = torch.load(open("bbt_faces.pt","rb"))
net = BaseNet(json.load(open("../vision/base_nets/facenet.json")))
net.load_state_dict(state_dict)