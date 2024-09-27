"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['inplace', 'collate_dict']

# %% ../nbs/00_core.ipynb 33
def inplace(f):
  def _f(b):
    f(b)
    return b
  return _f

# %% ../nbs/00_core.ipynb 52
def collate_dict(ds):
  get = itemgetter(*ds.features)
  def _f(b): return get(default_collate(b))
  return _f
