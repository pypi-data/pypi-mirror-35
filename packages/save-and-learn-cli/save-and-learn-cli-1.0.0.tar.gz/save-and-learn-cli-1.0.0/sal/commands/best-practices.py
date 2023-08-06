"""The best practices command."""

from json import dumps
from .base import Base

class BestPractices(Base):
  """Handle Best practices command."""

  def run(self):
    print("Best practice command")
    print('With this options : ', dumps(self.options, indent=2, sort_keys=True))