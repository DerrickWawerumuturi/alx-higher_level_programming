#!/usr/bin/python3
if __name__ == "__main__":
<<<<<<< HEAD
  import sys
  lenargv = len(sys.argv) - 1
  if lenargv == 1:
    print("{} argument:".format(lenargv))
  else:
    if lenargv  == 0:
      print("{} arguments:".format(lenargv))
=======
    import sys
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
>>>>>>> 18dea83cb974baee465a697b9294d1abd5c8442a
    else:
        print("{} arguments:".format(i))

<<<<<<< HEAD

    if lenargv >= 1:
        lenargv = 0
        for i in sys.argv:
            if lenargv != 0:
                print("{}: {}".format(lenargv, i))
            lenargv += 1
=======
    if i >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(i, arg))
            i += 1
>>>>>>> 18dea83cb974baee465a697b9294d1abd5c8442a
