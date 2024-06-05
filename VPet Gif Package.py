# Built-in Packages
from PIL import Image
import tkinter as tk


def parse_gif_file_to_action(image_path):
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
    parse_gif_file_to_action("Animations\Idle.gif")
