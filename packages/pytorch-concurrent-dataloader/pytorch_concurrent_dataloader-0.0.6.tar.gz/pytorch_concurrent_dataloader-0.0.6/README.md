# PytorchConcurrentDataloader

[![publish](https://github.com/BenediktAlkin/PytorchConcurrentDataloader/actions/workflows/publish.yaml/badge.svg)](https://github.com/BenediktAlkin/PytorchConcurrentDataloader/actions/workflows/publish.yaml)


Minimal version of the [ConcurrentDataloader repository](https://github.com/iarai/concurrent-dataloader) published to pip.

#### Setup

`pip install pytorch-concurrent-dataloader`


#### Usage
- replace `torch.utils.data.DataLoader` with `pytorch_concurrent_dataloader.DataLoader`
- pass new parameters for concurrent dataloading
```
from pytorch_concurrent_dataloader import DataLoader
dataloader = DataLoader(
    # pass old parameters as usual
    dataset=..., 
    batch_size=...,
    num_workers=...,
    # pass new parameters
    num_fetch_workers=...,
)
```