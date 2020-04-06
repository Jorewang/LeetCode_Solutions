import torch
import torch.nn as nn
import torch.nn.functional as F

if __name__ == '__main__':
    a = torch.rand(3, 4)
    print(a)
    b = a.softmax()
    print(b)
    print(b.sum())
