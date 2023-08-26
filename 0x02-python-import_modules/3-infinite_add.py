#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys
    infinite = 0
    
    for num in range(len(sys.argv) -1):
        infinite += int(sys.argv[num + 1])
    print("{}".format(infinite))
