#!/usr/bin/python3

""" Define a class 
"""


class Base:
    """Create a private class attribute """
    __nb_objects = 0

    """define a class constructor 

    args:
        id: default is None
    """

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a JSON string rep of a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == [] :
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ 
        writes the JSON string rep of list_obj to a file
        """
        filename = cls.__name__+ ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
    @staticmethod
    def from_json_string(json_string):
        """
        return json rep json_string
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attrributes already set
        """
        Rectangle = __import__('rectangle').Rectangle
        rect = Rectangle(20, 30, 40, 50, 60)
        rect.update(**dictionary)
        return rect

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = str(cls.__name__)+ ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dict = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes in cvs
        """
        filename  = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    write.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of class instantiated from a CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []    
    @staticmethod
    def draw(cls, list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
