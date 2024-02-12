#!/usr/bin/python3

""" 
import the super class
"""
from models.rectangle import Rectangle

"""
define the new class
"""
class Square(Rectangle):
  def __init__(self, size, x=0, y=0, id=None):
    """
    call the super class from the Rectangle with id, x, y, size = width size= height
    """
    super().__init__(size, size, id, x, y)

  def __str__(self):
    return "[Square] ({:d}) {:d}/:d{} - {:d}".format(self.id, self.x, self.y, self.width)


  @property
  def size(self)
  """
  define a getter for the size attribute
  """
    return self.width
  @size.setter
  def size(self, value):
    """
    define a setter for the size
    """
    if type(value) is not int:
      raise  TypeError("width must be an integer")
    if value <= 0:
      raise ValueError("width must be > 0")
    self.width = value
    self.height = value

  def  update(self, *args, **kwargs):
    """
    update method that assigns attributes 
    """
    if len(args) == 0:
      dict =  kwargs.keys()
      if 'size' in dict:
        self.size = kwargs['size']
      if 'x' in dict:
        self.x = kwargs['x']
      if 'y' in dict:
        self.y = kwargs['y']
      if 'id' in dict:
        self.id = kwargs['id']
      else:
        length = len(args)
        if length > 0:
          self.id = args[0]
        if length > 1:
          self.size = args[1]
        if length > 2:
          self.x = args[2]
        if length > 3:
          self.y = args[3]


    def to_dictionary(self):
      """
      returns a dictionary rep of a Square
      """
      squareDict = super().to_dictionary()
      del squareDict['height']
      del sqaureDict['width]
      squareDict.update({'size': self.size})
      return squareDict
