# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 01:46:02 2023

@author: Neno
"""
import os
import sys
from PIL import Image

def make_gif_2color(input_path, folder_name):
    # Open the GIF image
    image = Image.open(input_path)

    # Create a list to store each frame of the GIF
    frames = []

    try:
        while True:
            # Convert the current frame to grayscale
            grayscale_frame = image.convert("L")

            # Convert the grayscale frame to a 2-color image using thresholding
            threshold = 128  # Adjust the threshold value as needed
            binary_frame = grayscale_frame.point(lambda x: 0 if x < threshold else 255, "1")

            # Resize the frame to 128x64 pixels
            resized_frame = binary_frame.resize((128, 64))

            # Append the 2-color frame to the list
            frames.append(resized_frame)

            # Move to the next frame
            image.seek(image.tell() + 1)
    except EOFError:
        pass

    # Create a directory for the output frames
    frames_dir = folder_name
    os.makedirs(frames_dir, exist_ok=True)

    # Save each frame as a separate PNG file and collect frame order
    frame_order = []
    for i, frame in enumerate(frames):
        frame_filename = os.path.join(frames_dir, f"frame_{i}.png")
        frame.save(frame_filename, format="PNG")
        frame_order.append(str(i))

    # Create the manifest.txt file
    manifest_path = os.path.join(frames_dir, "meta.txt")
    with open(manifest_path, "w") as manifest_file:
        manifest_file.write("Filetype: Flipper Animation\n")
        manifest_file.write("Version: 1\n\n")
        manifest_file.write("Width: 128\n")
        manifest_file.write("Height: 64\n")
        manifest_file.write("Passive frames: {}\n".format(len(frames)))
        manifest_file.write("Active frames: 0\n")
        manifest_file.write("Frames order: {}\n".format(" ".join(frame_order)))
        manifest_file.write("Active cycles: 0\n")
        manifest_file.write("Frame rate: 6\n")
        manifest_file.write("Duration: " + str(28800) +"\n")
        manifest_file.write("Active cooldown: 0\n\n")
        manifest_file.write("Bubble slots: 0\n")

    print("Frames and manifest saved successfully!")


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py <folder_name> <input_file>")
    else:
        # Retrieve the folder name and input file from the arguments
        folder_name = sys.argv[1]
        input_file = sys.argv[2]

        make_gif_2color(input_file, folder_name)
