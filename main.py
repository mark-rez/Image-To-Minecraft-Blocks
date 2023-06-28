# author: GiorDior aka Giorgio
# date: 28.06.2023
# topic: Image Converter
# version: 1.0

import time
import argparse
from mcimgconverter import convert

def main():
    # adding arguments
    parser = argparse.ArgumentParser(description='TikTok TTS')
    parser.add_argument('-o', help='original file path')
    parser.add_argument('-f', help='composite file path')

    args = parser.parse_args()

    # executing script
    if not args.f:
        print("Provide a path for the composite image")
    if not args.o:
        print("Provide a path for the original image")

    try:
        start = time.time()
        convert(args.o, args.f)
        print(f"Image successfully generated: {args.o}")
        print(f"Time of procedure: {round(time.time() - start, 2)}s")
    except Exception as e:
        print("Error: " + str(e))

if __name__ == "__main__":
    main()