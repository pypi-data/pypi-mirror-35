import torch
from torch.autograd import Variable
# from taolu.vision.vision_units.losses.triplet_loss import TripletMarginLoss
from torch.nn import TripletMarginLoss


class PairwiseDistance(torch.autograd.Function):
    def __init__(self, p):
        super(PairwiseDistance, self).__init__()
        self.norm = p

    def forward(self, x1, x2):
        assert x1.size() == x2.size()
        eps = 1e-4 / x1.size(1)
        diff = torch.abs(x1 - x2)
        out = torch.pow(diff, self.norm).sum(dim=1)
        return torch.pow(out + eps, 1. / self.norm).unsqueeze(-1)


def select_hard_sample(anchor_feature, positive_feature, negative_feature, function, margin):
    l1 = function(anchor_feature, positive_feature)
    l2 = function(anchor_feature, negative_feature)
    selected_indexes = l2 - l1 < margin
    while selected_indexes[(selected_indexes == 1).squeeze()].squeeze().dim() == 0 or \
            len(selected_indexes[(selected_indexes == 1).squeeze()].squeeze()) == 0:
        margin = margin + 0.1
        selected_indexes = l2 - l1 < margin
    return selected_indexes == 1


class TripletTrainer:
    def __init__(self, cuda, model, margin, optimizer):
        self.cuda = cuda
        self.model = model
        self.triplet_loss = TripletMarginLoss(margin)
        self.ce_loss = torch.nn.CrossEntropyLoss()
        self.optimizer = optimizer
        self.margin = margin
        self.distance_function = PairwiseDistance(2)

    def train(self, triplet_batch):
        anchor, positive, negative = triplet_batch
        anchor_x, anchor_label = anchor
        positive_x, positive_label = positive
        negative_x, negative_label = negative
        self.model.train()
        if self.cuda:
            self.model.cuda()
            anchor_x = anchor_x.cuda()
            anchor_label = anchor_label.cuda()
            positive_x = positive_x.cuda()
            positive_label = positive_label.cuda()
            negative_x = negative_x.cuda()
            negative_label = negative_label.cuda()
        anchor_x = Variable(anchor_x)
        anchor_label = Variable(anchor_label)
        positive_x = Variable(positive_x)
        positive_label = Variable(positive_label)
        negative_x = Variable(negative_x)
        negative_label = Variable(negative_label)
        anchor_feature = self.model.seq[:-1](anchor_x)
        positive_feature = self.model.seq[:-1](positive_x)
        negative_feature = self.model.seq[:-1](negative_x)
        selected_indexes = select_hard_sample(anchor_feature, positive_feature, negative_feature,
                                              self.distance_function, self.margin)
        selected_anchor_feature = anchor_feature[selected_indexes.squeeze()]
        selected_positive_feature = positive_feature[selected_indexes.squeeze()]
        selected_negative_feature = negative_feature[selected_indexes.squeeze()]

        selected_anchor = anchor_x[selected_indexes.squeeze()]
        selected_positive = positive_x[selected_indexes.squeeze()]
        selected_negative = negative_x[selected_indexes.squeeze()]

        selected_anchor_label = anchor_label[selected_indexes.squeeze()].squeeze()
        selected_positive_label = positive_label[selected_indexes.squeeze()].squeeze()
        selected_negative_label = negative_label[selected_indexes.squeeze()].squeeze()

        anchor_pred = self.model(selected_anchor)
        positive_pred = self.model(selected_positive)
        negative_pred = self.model(selected_negative)
        anchor_label = anchor_label.squeeze()
        positive_label = positive_label.squeeze()
        negative_label = negative_label.squeeze()
        pred = torch.cat([anchor_pred, positive_pred, negative_pred])
        label = torch.cat([selected_anchor_label, selected_positive_label, selected_negative_label])

        cls_loss = self.ce_loss(pred, label)
        pred_class = torch.argmax(pred, 1)
        # print(label)
        # print(pred_class)
        triplet_loss = self.triplet_loss(selected_anchor_feature, selected_positive_feature, selected_negative_feature)
        loss = cls_loss*10 + triplet_loss
        print(cls_loss)
        print(triplet_loss)
        print(pred_class == label)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
