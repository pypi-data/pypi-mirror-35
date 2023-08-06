import torch

import time
from yann.callbacks.base import Callback
from yann.viz import plot_line



class History(Callback):
  def __init__(self, **metrics):
    super(History, self).__init__()
    self.metric_funcs = metrics
    self.metrics = {m: [] for m in metrics}
    self.metrics['loss'] = []
    self.times = []
    self.steps = []


    self.val_metrics = {m: [] for m in metrics}
    self.val_metrics['loss'] = []
    self.val_steps = []
    self.val_times = []

  def on_batch_end(self, batch, inputs, targets, outputs, loss, trainer=None):
    self.times.append(time.time())
    self.steps.append(trainer.num_steps)
    self.metrics['loss'].append(loss.item())

    with torch.no_grad():
      for name, metric in self.metric_funcs.items():
        self.metrics[name].append(
          metric(targets, outputs)
        )

  def on_validation_end(self, loss=None, outputs=None, targets=None,
    trainer=None):
    self.val_times.append(time.time())
    self.val_steps.append(trainer.num_steps)
    self.val_metrics['loss'].append(loss.item())


class HistoryPlotter(Callback):
  def __init__(self, history: History, freq=500, window=50, metrics=None,
               clear=False):
    super().__init__()
    self.history = history
    self.freq = freq
    self.window = window

    self.metrics = metrics

    self.clear = clear

  def plot(self, metric=None, time=False, validation=False, **kwargs):
    if self.clear:
      try:
        from IPython.display import clear_output
        clear_output(wait=True)
      except:
        pass

    if validation:
      ms, steps, times = (
        self.history.val_metrics,
        self.history.val_steps,
        self.history.val_times
      )
    else:
      ms, steps, times = (
        self.history.metrics,
        self.history.steps,
        self.history.times
      )

    if metric:
      metrics = [metric]
    else:
      metrics = self.metrics or ms.keys()

    for m in metrics:
        plot_line(
          ms[m],
          x=times if time else steps,
          xlabel='time' if time else 'step',
          ylabel=f'validation {m}' if validation else m,
          window=1 if validation else self.window,
          **kwargs
      )

  def on_batch_end(self, *args, trainer=None, **kwargs):
    if trainer.num_steps % self.freq == 0:
      self.plot(
        title=f'Epoch: {trainer.num_epochs} Steps: {trainer.num_steps}'
      )

  def on_validation_end(self, *args, trainer=None, **kwargs):
    self.plot(
      validation=True,
      title=f'Epoch: {trainer.num_epochs} Steps: {trainer.num_steps}'
    )



class HistoryLogger(Callback):
  pass