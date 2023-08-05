import torch


class Linear(torch.nn.Module):
    def __init__(self, input_num, output_num):
        super(Linear, self).__init__()
        self.linear = torch.nn.Linear(input_num, output_num)
        self.input_num = input_num
        self.output_num = output_num

    def forward(self, input):
        input = input.view(-1, self.input_num)
        return self.linear(input)
