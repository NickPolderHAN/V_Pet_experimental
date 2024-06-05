# Built-in Packages
from PIL import Image
import tkinter as tk
from tkinter import filedialog


def parse_gif_action(image_path):
    try:
        if '.gif' in image_path:
            # Open the image file
            im = Image.open(image_path)
        else:
            # Open the image file
            im = Image.open(image_path + '.gif')

        # Determine the number of frames
        num_frames = im.n_frames

        # call buddy's action gif and extract the frames.
        if ".gif" in image_path:
            animation = [tk.PhotoImage(file=image_path,
                                       format='gif -index %i' % i)
                         for i in range(num_frames)]
        else:
            animation = [tk.PhotoImage(file=image_path + '.gif',
                                       format='gif -index %i' % i)
                         for i in range(num_frames)]
        return animation
    except RuntimeError:
        print("Tkinter Root window has not been created yet. Image / gif can therefore not be loaded")


if __name__ == '__main__':
    # Open file dialog to choose a GIF file
    file_path = filedialog.askopenfilename(
        title="Select a GIF file",
        filetypes=(("GIF files", "*.gif"), ("All files", "*.*"))
    )

    # Sent the gif to be parsed.
    parse_gif_action(file_path)
