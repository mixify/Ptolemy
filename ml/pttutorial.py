from __future__ import print_function
import torch
import numpy as np

x = torch.zeros(5,3,dtype=torch.long)
print(x)
x = torch.randn_like(x,dtype=torch.float)
print(x)
print(x.size())

y = x.view(15)
print(y)
y = x.view(15,-1) # -1 is divided?? or that kind of thing
print(y)
print(y.size())

x = torch.randn(1)
print(x)
print(x.item())

print('-------------')
a = torch.ones(5)
print(a)
b = a.numpy()
print(b)
a.add_(1)
print(a)
print(b)
a = np.array(range(8))
b = torch.from_numpy(a)
print(b)

# they all sharing memories


if torch.cuda.is_available():
    device = torch.device("cuda")
    y = torch.ones_like(x, device=device)
    x = x.to(device)
    z = x+y
    print(z)
    print(z.to("cpu", torch.double))
