import torch

torch.cuda.current_device()
torch.cuda.device(0)
print(torch.cuda.get_device_name(0))
print(torch.cuda.is_available())
