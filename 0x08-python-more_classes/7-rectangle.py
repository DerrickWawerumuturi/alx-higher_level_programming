#!/usr/bin/python3

"""
Real Definition of a rectangle
"""


class Rectangle:
	"""Class rectangle"""

	number_of_instances = 0
	print_symbol = None
	print_symbol = "#"
    
	def __init__(self, width = 0, height = 0):

		""" Method that initializes the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle


        """

		self._width = width
		self._height = height
		Rectangle.number_of_instances += 1

	@property
	def width(self):
		""" method that returns width value

        Returns:
            width of the rectangle


        """
		return self._width
	
	@width.setter
	def width(self, value):
		""" method that defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero


        """


		if isinstance(value, int) == False:
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		else:
			self._width = value

	@property
	def height(self):
		""" method that returns height value

        Returns:
            height of the rectangle


        """

		return self._height
	
	@height.setter
	def height(self, value):
		""" method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero


        """

		if isinstance(value, int) == False:
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		
		self._height = value

	def area(self):
		return self._width * self._height
	
	def perimeter(self):
		if self._width == 0 or self._height == 0:
			return 0
		return 2* (self._height + self._width)
	

	def __str__(self):
		rect = ""
		if self._height == 0 or self._width == 0:
			return rect
		for i in range(self._height):
			rect += ("#" * self._width + '\n')
		return rect[:-1]
	
	def __repr__(self):
		return "Rectangle({}, {})".format(self._width, self._height)
	
	def __del__(self):
		Rectangle.number_of_instances -= 1
		print("Bye rectangle...")
