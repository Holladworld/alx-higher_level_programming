#!/usr/bin/bash
if __name__ == "__main__":
    import hidden_4

    num = dir(hidden_4)
    for i in num:
        if i[:2] != "__":
            print(i)
