# Built-in
import tkinter as tk

# Custom
from Packages import Buddy_Package


class Home:
    def __init__(self):
        self.window = tk.Tk()
        self.home_label = None
        self.buddy_button = None

        self.setup_window()
        self.setup_widgets()

        self.window.mainloop()

    # Sets up the home window.
    def setup_window(self):
        # Creates and configures the window.
        self.window.title('Home Menu')
        self.window.geometry('500x500')

    # Sets up the widgets for the home screen.
    def setup_widgets(self):
        self.home_label = tk.Label(self.window, text='Home Menu')
        self.home_label.pack()

        self.buddy_button = tk.Button(self.window, text='Buddy', command=self.show_buddy)
        self.buddy_button.pack()

    # Triggers if the buddy button is pressed and the home screen needs to disappear.
    def show_buddy(self):
        self.window.destroy()
        vpet = Buddy_Package.VirtualPet()


if __name__ == '__main__':
    inst = Home()
