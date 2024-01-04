#!/usr/bin/python3
if __name__ == "__main__":
  import sys
  lenargv = len(sys.argv) - 1
  if lenargv == 1:
    print("{} argument:".format(lenargv))
  else:
    if lenargv  == 0:
      print("{} arguments:".format(lenargv))
    else:
      print("{} arguments:".format(lenargv))


    if lenargv >= 1:
        lenargv = 0
        for i in sys.argv:
            if lenargv != 0:
                print("{}: {}".format(lenargv, i))
            lenargv += 1
