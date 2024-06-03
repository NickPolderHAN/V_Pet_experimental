import pyautogui
import random
import tkinter as tk

x = None
cycle = 0
check = 1
idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1, 3, 1)
impath = 'Animations\\'


class VirtualPet:
    def __init__(self):
        self.window = tk.Tk()
        # window configuration
        self.window.config(highlightbackground='black')

        self.sprite_label = tk.Label(self.window, bd=0, bg='black')

        self.window.overrideredirect(True)
        self.window.wm_attributes('-transparentcolor', 'black')
        self.window.attributes('-topmost', True)

        self.sprite_label.pack()

        # Backup base screen size.
        self.screen_width = 1920
        self.screen_height = 1080

        # Sets screensize depending on system screen.
        self.adjust_on_screen_size()

        # Adjust the y position to be higher
        y_position = self.screen_height - 150

        self.idle = None
        self.idle_to_sleep = None
        self.sleep = None
        self.sleep_to_idle = None
        self.walk_positive = None
        self.walk_negative = None

        self.get_animation_gifs()

        self.window.after(1, self.update, cycle, check, event_number,
                          self.screen_width - 400, y_position)
        self.window.mainloop()

    # Used in order to adjust walking limits and spawning position on screen size.
    def adjust_on_screen_size(self):
        # Get screen size
        self.screen_width, self.screen_height = pyautogui.size()

        return None

    # transfer random no. to event
    def event(self, cycle, check, event_number, x, y):
        # Idle Event.
        if event_number in idle_num:
            check = 0
            self.window.after(400, self.update, cycle, check, event_number, x, y)  # no. 1,2,3,4 = idle

        # From Idle to Sleep.
        elif event_number == 5:
            check = 1
            self.window.after(100, self.update, cycle, check, event_number, x, y)  # no. 5 = idle to sleep

        # Walking to Left.
        elif event_number in walk_left:
            check = 4
            self.window.after(100, self.update, cycle, check, event_number, x, y)  # no. 6,7 = walk towards left

        # Walking to Right
        elif event_number in walk_right:
            check = 5
            self.window.after(100, self.update, cycle, check, event_number, x, y)  # no 8,9 = walk towards right

        # Sleep
        elif event_number in sleep_num:
            check = 2
            self.window.after(1000, self.update, cycle, check, event_number, x, y)  # no. 10,11,12,13,15 = sleep

        # From Sleep to Idle
        elif event_number == 14:
            check = 3
            self.window.after(100, self.update, cycle, check, event_number, x, y)  # no. 14 = sleep to idle

    # making gif work
    def gif_work(self, cycle, frames, event_number, first_num, last_num):
        if cycle < len(frames) - 1:
            cycle += 1
        else:
            cycle = 0
            event_number = random.randrange(first_num, last_num + 1, 1)
        return cycle, event_number

    def update(self, cycle, check, event_number, x, y):
        # idle
        if check == 0:
            frame = self.idle[cycle]
            cycle, event_number = self.gif_work(cycle, self.idle, event_number, 1, 9)
        # idle to sleep
        elif check == 1:
            frame = self.idle_to_sleep[cycle]
            cycle, event_number = self.gif_work(cycle, self.idle_to_sleep, event_number, 10, 10)
        # sleep
        elif check == 2:
            frame = self.sleep[cycle]
            cycle, event_number = self.gif_work(cycle, self.sleep, event_number, 10, 15)
        # sleep to idle
        elif check == 3:
            frame = self.sleep_to_idle[cycle]
            cycle, event_number = self.gif_work(cycle, self.sleep_to_idle, event_number, 1, 1)
        # walk toward left
        elif check == 4:
            frame = self.walk_positive[cycle]
            cycle, event_number = self.gif_work(cycle, self.walk_positive, event_number, 1, 9)
            x -= 3
        # walk towards right
        elif check == 5:
            frame = self.walk_negative[cycle]
            cycle, event_number = self.gif_work(cycle, self.walk_negative, event_number, 1, 9)
            x += 3
        self.window.geometry(f'100x100+{x}+{y}')
        self.sprite_label.configure(image=frame)
        self.window.after(1, self.event, cycle, check, event_number, x, y)

    def get_animation_gifs(self):
        # call buddy's action gif
        self.idle = [tk.PhotoImage(file=impath + 'idle.gif', format='gif -index %i' % (i)) for i in range(5)]  # idle gif
        self.idle_to_sleep = [tk.PhotoImage(file=impath + 'idle_to_sleep.gif', format='gif -index %i' % (i)) for i in
                         range(8)]  # idle to sleep gif
        self.sleep = [tk.PhotoImage(file=impath + 'sleeping.gif', format='gif -index %i' % (i)) for i in range(3)]  # sleep gif
        self.sleep_to_idle = [tk.PhotoImage(file=impath + 'sleep_to_idle.gif', format='gif -index %i' % (i)) for i in
                         range(8)]  # sleep to idle gif
        self.walk_positive = [tk.PhotoImage(file=impath + 'walk_left.gif', format='gif -index %i' % (i)) for i in
                         range(8)]  # walk to left gif
        self.walk_negative = [tk.PhotoImage(file=impath + 'walk_right.gif', format='gif -index %i' % (i)) for i in
                         range(8)]  # walk to right gif


if __name__ == '__main__':
    vpet = VirtualPet()