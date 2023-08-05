from taolu.vision.utils.transformers.transformer import Transformer
import torch


class EmptyTransformer(Transformer):
    def __init__(self, cfg):
        super(EmptyTransformer, self).__init__(cfg)

    def transform(self, images, labels):
        return images, labels
