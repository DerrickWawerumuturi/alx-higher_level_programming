#!/usr/bin/python3
if __name__ == "__main__":
  import sys
  lenargv = (len(sys.argv)) - 1
  if lenargv == 1:
    print("{} argument:".format(lenargv))
  else:
    if lenargv  == 0:
      print("{} arguments:".format(lenargv))
    else:
      print("{} arguments:".format(lenargv))

for i in range(1, lenargv + 1):
  print("{}: {}".format(i, sys.argv[i]))
