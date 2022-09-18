import torch

# torch.Size([100, 64, 1])
# torch.Size([100, 1, 250])
# torch.Size([100, 64, 250])


xx = torch.Tensor(
    [[[1.],
      [2.],
      [3.]],

     [[4.],
      [5.],
      [6.]]])

xx = xx.permute(1,0,2)

print(xx.size()) #([3, 2, 1])
pose =  torch.Tensor(
    [[[11.,12,13,14],
      [21,22,23,24],
      [31,32,33,34.]]])
pose = pose.permute(1,0,2)

print(pose.size()) #([3, 2, 1])

sum = xx + pose
print(xx)
print(pose)
print(sum)