#!/usr/bin/python3
if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4
    for c in dir(hidden_4):
        if c[:2] != "__":
            print("{}".format(c))
