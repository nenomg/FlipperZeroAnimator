# FlipperZeroAnimator
This script converts GIFs into 2-color frames for Flipper Zero. It resizes frames to 128x64 pixels, saves as PNG files, and generates the meta file for it. Ideal for Flipper Zero animations.


# Flipper Zero GIF to 2-Color Frames Converter

This script is designed for the Flipper Zero device, allowing you to convert GIF images into a series of 2-color frames compatible with its display.

## Usage

1. Install the required dependencies: `pip install pillow`

2. Run the script using the command-line interface:

`python flipperAnimator.py <input_file> <output_folder>`



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

Create a folder with the gif and the flipper zero animator script

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/0266ee0d-4de6-402a-b401-c9a5895629e3)

Open a command line in the folder and run the command

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/5ca1088c-2a5a-4a61-8d01-742acd1913e2)

Then the image and the meta file will be created in the folder

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/a3958455-8846-4aed-b36a-d588c9824f43)

This is the content of the meta.txt file:

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/2a00166f-ee37-4648-91be-49c3ff679c38)

Now it is ready to be compiled with the desired firmware, for this case i would use the roguemaster one: https://github.com/RogueMaster/flipperzero-firmware-wPlugins

###Build
First you need to clone the firmware from the repository using:
`git clone --recursive https://github.com/RogueMaster/flipperzero-firmware-wPlugins.git`

Then go to the external folder and paste the animation folder

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/2cfd0274-5044-4760-b37b-5235eb6e100b)

Finally update the manifest inside the external folder and add the reference to the animation

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/668049ec-9c24-4ed0-a3a4-5e1155f61d77)

Inside the roguemaster firmware folder run this command to build it

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/60935b40-fd69-474f-b152-de958af45f2d)

It will generate an output like this at the end

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/62f8497f-b4fa-4abe-9649-3ab157590200)

Go to the folder where the compiled firmware is and copy it inside the update folder in the flipper

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/b7598923-96fa-41f3-958d-53c0d677d83b)

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/d3a89eff-9e90-49fc-8f94-21c7c889d9a5)

Then take to the flipper zero and go to the update directory in the file explorer

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/cf2acb9a-b9b6-46c2-a6a3-4f8aa67f4c2a)

Run the update

![image](https://github.com/nenomg/FlipperZeroAnimator/assets/105873794/031094da-fe90-4f9f-9ad3-231cc3fbea1d)






