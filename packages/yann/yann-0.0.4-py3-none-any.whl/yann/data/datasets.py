from itertools import zip_longest
from torch.utils.data import Dataset


class TransformDataset(Dataset):
  def __init__(self, dataset, transforms):
    super().__init__()
    self.dataset = dataset
    self.transforms = transforms if isinstance(transforms, tuple) else (
      transforms,)

  def __len__(self):
    return len(self.dataset)

  def __getitem__(self, idx):
    return tuple(
      t(x) if t else x
      for (x, t) in zip_longest(self.dataset[idx], self.transforms)
    )

  def __repr__(self):
    return (
      f'{self.__class__.__name__}('
      f'\nDataset: {repr(self.dataset)}'
      f'\nTransforms: {repr(self.transforms)}'
      f'\n)')