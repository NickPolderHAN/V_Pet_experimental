# Built-in
import tkinter as tk

# Custom
from Packages.Buddy_Pet_package import VirtualPetBuddy


class Home:
    def __init__(self):
        self.window = None
        self.home_label = None
        self.buddy_button = None

        self.setup_window()
        self.setup_widgets()
        self.window.mainloop()

    def setup_window(self):
        # Creates and configures the window.
        self.window = tk.Tk()
        self.window.title('Home Menu')
        self.window.geometry('500x500')

    def setup_widgets(self):
        self.home_label = tk.Label(self.window, text='Home Menu')
        self.home_label.pack()

        self.buddy_button = tk.Button(self.window, text='Buddy', command=self.show_buddy)
        self.buddy_button.pack()

    def show_buddy(self):
        self.window.destroy()
        vpet = VirtualPetBuddy()


if __name__ == '__main__':
    inst = Home()