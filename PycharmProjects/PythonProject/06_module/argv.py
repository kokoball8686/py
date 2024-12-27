#!/usr/bin/python3

import sys




def main():
    if len(sys.argv[1:]) != 1:
        print('Usage: %s <IP>' % sys.argv[0])
        sys.exit(1)
    IP = sys.argv[1]

    print(" ok ")


if __name__ == "__main__":
    main()