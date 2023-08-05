import torch

print(torch.cuda.is_available())

import jax

print(jax.default_backend())