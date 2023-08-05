from taolu.vision.utils.transformers.transformer import Transformer
import torch
import random
import numpy as np
import torchvision.transforms as transforms


def normalize(triplets):
    transformer = transforms.Normalize(mean=[0.5, 0.5, 0.5],
                                       std=[0.5, 0.5, 0.5])
    triplets[0][0] = transformer(triplets[0][0])
    triplets[1][0] = transformer(triplets[1][0])
    triplets[2][0] = transformer(triplets[2][0])
    return triplets


def pick_triplet(train_image_batch, train_label_batch, num_triplets):
    inds = {}
    for i, o in enumerate(train_label_batch):
        o = o[0]
        if o not in inds:
            inds[o] = []
        inds[o].append(i)
    anchor_samples = []
    positive_samples = []
    negative_samples = []

    anchor_labels = []
    positive_labels = []
    negative_labels = []

    while len(anchor_samples) < num_triplets:
        index_anchor_person = random.randint(0, len(inds) - 1)
        if len(inds[index_anchor_person]) < 2:
            continue
        index_anchor_face = random.randint(0, len(inds[index_anchor_person]) - 1)
        index_positive_face = -1
        while index_anchor_face == index_positive_face or index_positive_face == -1:
            index_positive_face = random.randint(0, len(inds[index_anchor_person]) - 1)
        index_negative_person = -1
        while index_negative_person == -1 or index_negative_person == index_anchor_person:
            index_negative_person = random.randint(0, len(inds) - 1)
        index_negative_face = random.randint(0, len(inds[index_negative_person]) - 1)
        anchor_samples.append(train_image_batch[inds[index_anchor_person][index_anchor_face]])
        positive_samples.append(train_image_batch[inds[index_anchor_person][index_positive_face]])
        negative_samples.append(train_image_batch[inds[index_negative_person]][index_negative_face])

        anchor_labels.append(train_label_batch[inds[index_anchor_person][index_anchor_face]])
        positive_labels.append(train_label_batch[inds[index_anchor_person][index_positive_face]])
        negative_labels.append(train_label_batch[inds[index_negative_person]][index_negative_face])
    triplets = ((torch.Tensor(np.array(anchor_samples)), torch.Tensor(np.array(anchor_labels)).long()),
                (torch.Tensor(np.array(positive_samples)), torch.Tensor(np.array(positive_labels)).long()),
                (torch.Tensor(np.array(negative_samples)), torch.Tensor(np.array(negative_labels)).long()))
    # triplets = ((torch.Tensor(train_image_batch),torch.Tensor(train_label_batch).long()),
    #              (torch.Tensor(train_image_batch), torch.Tensor(train_label_batch).long()),
    #               (torch.Tensor(train_image_batch), torch.Tensor(train_label_batch).long()))
    return triplets


class FaceNetTransformer(Transformer):
    def __init__(self, cfg):
        super(FaceNetTransformer, self).__init__(cfg)
        self.num_triplets = cfg['num_triplets']

    def transform(self, images, labels):
        return pick_triplet(images, labels, self.num_triplets)
