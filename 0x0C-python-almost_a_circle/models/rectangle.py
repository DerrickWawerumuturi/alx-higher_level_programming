#!/usr/bin/python3
"""Rectangle class implement Base class """


from models.base import Base


class Rectangle(Base):
    """ rectangle class implement Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
            Returning private attribute (__width)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setting private attribute (__width)
        """
        self.setter_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
            Returning private attribute (___height)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setting private attribute (__height)
        """
        self.setter_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
            Returning private attribute (__x)
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Setting private attribute (__x)
        """
        self.setter_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """
            Returning private attribute (__y)
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Setting private attribute (__y)
        """
        self.setter_validator("y", value)
        self.__y = value

    def area(self):
        """ 
            return the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ 
            prints in stdout "#"
        """
        rectangle = ""
        print("\n" * self.y, end="")
        for i in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")
    def __str__(self):
        """ 
            returns a string 
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))
    def update(self, *args, **kwargs):
        if len(args) == 0:
            dict = kwargs.keys()
            if "height" in dict:
                self.height = kwargs['height']
            if "width" in dict:
                self.width = kwargs['width']
            if "x" in dict:
                self.height = kwargs['x']
            if "y" in dict:
                self.y = kwargs['y']
            if "id" in dict:
                self.id = kwargs['id']
        else:
            if len(args) > 0:
               self.id = args[0] 
            if len(args) > 1:
               self.width = args[1] 
            if len(args) > 2:
               self.height = args[2] 
            if len(args) > 3:
               self.x = args[3]
            if len(args) >4:
                self.y = args[4]
    @staticmethod
    def setter_validator(attribute, value):
        """
            validates if width or height are int 
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x"  or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0 :
            raise ValueError("{} must be > 0 ".format(attribute))


    def to_dictionary(self):
        rectDict = {}
        rectDict.update({'x' : self.x})
        rectDict.update({'y' : self.y})
        rectDict.update({'id' : self.id})
        rectDict.update({'height' : self.height})
        rectDict.update({'width' : self.width})
        return rectDict
