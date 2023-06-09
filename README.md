# FlipperZeroAnimator
This script converts GIFs into 2-color frames for Flipper Zero. It resizes frames to 128x64 pixels, saves as PNG files, and generates the meta file for it. Ideal for Flipper Zero animations.


# Flipper Zero GIF to 2-Color Frames Converter

This script is designed for the Flipper Zero device, allowing you to convert GIF images into a series of 2-color frames compatible with its display.

## Usage

1. Install the required dependencies: `pip install pillow`

2. Run the script using the command-line interface:

`python main.py <input_file> <output_folder>`



- `<input_file>`: Path to the input GIF file.
- `<output_folder>`: Path to the output folder where the frames and meta will be saved.

3. Once the script finishes, the `<output_folder>` is ready to be compiled into a Flipper Zero firmware. You can use the Flipper Zero development tools to integrate these frames into your projects.

## Important Notes

- The script uses the Python Imaging Library (PIL) to handle image operations. Make sure to install it before running the script.
- The output folder contains the frames as PNG files and a meta file specifying animation details.
- Ensure that the resized frames fit the Flipper Zero's display dimensions (128x64 pixels).
- For more information on Flipper Zero development and firmware integration, refer to the official Flipper Zero documentation.

Feel free to customize and enhance this script to fit your specific requirements. Enjoy creating animations for your Flipper Zero device!

## Usage Example

I would use this image to make a animation, the software scales the image so i prefer to use a 2x1 scale for the images, so width is 2 times the height like in the Flipper Zero.

![rocklee](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/4525e801-1457-4b1a-b25e-00bf815f4e09)

