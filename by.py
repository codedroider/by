#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        print(f"script by {arg}")
    else:
        print("argument is null!")

if __name__ == "__main__":
    main()
