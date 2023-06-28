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

import json
from PIL import Image

def _get_block_name(pixel: tuple) -> str:
    """
    Returns the name of the block that matches the given pixel color the closest.

    Args:
        pixel: A tuple representing the RGB values of a pixel.

    Returns:
        The filename of the block that matches the pixel color the closest.
    """
    matching_image_name = "none"
    smallest_value = float("inf")
    for block in BLOCKS:
        r = abs(pixel[0] - block["r"])
        g = abs(pixel[1] - block["g"])
        b = abs(pixel[2] - block["b"])

        if r + g + b < smallest_value:
            smallest_value = r + g + b
            matching_image_name = block["filename"]
    return matching_image_name

def _calculate_average_pixel_color(image: Image, x: int, y: int, block_size: int) -> list[int]:
    """
    Calculates the average RGB values of a block in the given image.

    Args:
        image: The image to calculate the average color from.
        x: The starting x-coordinate of the block.
        y: The starting y-coordinate of the block.
        block_size: The size of the block.

    Returns:
        A list representing the average RGB values of the block.
    """
    pixel_sum = [0, 0, 0]  # Initialize sum of pixel values for RGB channels

    # Iterate over the block area
    for block_y in range(y, y + block_size):
        for block_x in range(x, x + block_size):
            pixel = image.getpixel((block_x, block_y))
            pixel_sum[0] += pixel[0]  # Add red value
            pixel_sum[1] += pixel[1]  # Add green value
            pixel_sum[2] += pixel[2]  # Add blue value

    pixel_count = block_size * block_size
    average_pixel = [
        pixel_sum[0] // pixel_count,
        pixel_sum[1] // pixel_count,
        pixel_sum[2] // pixel_count
    ]

    return average_pixel

def convert(original_image_path: str, composite_image_path: str) -> None:   
    global BLOCKS
    """
    Converts the original image into a composite image made up of blocks.

    Args:
        original_image_path: The file path of the original image.
        composite_image_path: The file path to save the composite image.
    """

    with open("data.json", "r") as data:
        BLOCKS = json.loads(str(data.read()))

    original_image = Image.open(original_image_path)
    block_size = 16
    width, height = original_image.size
    block_count_x = width // block_size
    block_count_y = height // block_size

    area_avarage_pixel = []

    # Iterate over the blocks in the image
    for y in range(block_count_y):
        for x in range(block_count_x):
            average_color = _calculate_average_pixel_color(original_image, x * block_size, y * block_size, block_size)
            area_avarage_pixel.append(average_color)

    composite_image = Image.new("RGB", (width, height))

    # Iterate over the blocks in the main image
    for y in range(block_count_y):
        for x in range(block_count_x):
            # Crop the grass image to the block size
            block_name = _get_block_name(area_avarage_pixel[x + y * block_count_x])
            block_image = Image.open(f"block/{block_name}")
            # Paste the grass block onto the composite image
            composite_image.paste(block_image, (x * block_size, y * block_size))

    composite_image.save(composite_image_path)
