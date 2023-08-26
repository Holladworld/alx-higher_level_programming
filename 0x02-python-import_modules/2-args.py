#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    numm = len(sys.argv) - 1
    print("{} {}{}".format(
        numm,
        "argument" if numm == 1 else "arguments",
        "." if numm == 0 else ":"))
    for c, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(c + 1, arg))
