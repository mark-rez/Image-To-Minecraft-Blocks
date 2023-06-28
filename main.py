# author: GiorDior aka Giorgio
# date: 28.06.2023
# topic: Image Converter
# version: 1.0

"""
The Python Imaging Library (PIL) is

    Copyright © 1997-2011 by Secret Labs AB
    Copyright © 1995-2011 by Fredrik Lundh

Pillow is the friendly PIL fork. It is

    Copyright © 2010-2023 by Jeffrey A. Clark (Alex) and contributors.

Like PIL, Pillow is licensed under the open source HPND License:

By obtaining, using, and/or copying this software and/or its associated
documentation, you agree that you have read, understood, and will comply
with the following terms and conditions:

Permission to use, copy, modify and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appears in all copies, and that
both that copyright notice and this permission notice appear in supporting
documentation, and that the name of Secret Labs AB or the author not be
used in advertising or publicity pertaining to distribution of the software
without specific, written prior permission.

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL,
INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
"""

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
