import tkinter as tk


class Home:
    def __init__(self):
        self.window = None

    def setup_window(self):
        self.window = tk.Tk()

        self.window.mainloop()

    def set_window_size(self):
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Set window size as a fraction of screen size
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)

        # Set window position to center
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set window size and position
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")


if __name__ == '__main__':
    main_screen = Home()
