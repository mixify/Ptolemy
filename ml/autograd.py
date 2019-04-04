import torch

x = torch.ones(2, 2, requires_grad=True)
print(x)
print(x+2)

y = x+2;
z = y*y*3
print(z)
out = z.mean()
print(out)
out.backward()

print(x.grad)

