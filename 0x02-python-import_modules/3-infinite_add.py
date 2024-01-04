#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0

    for i, args in enumerate(sys.argv):
        if i == 0:
            continue
        result += int(args)
    print(f"{result:d}")
