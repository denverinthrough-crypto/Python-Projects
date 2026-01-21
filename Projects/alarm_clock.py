import tkinter as tk
from tkinter import messagebox, filedialog
import time
import threading
import pygame

pygame.mixer.init()

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Alarm Clock")
        self.root.geometry("420x350")

        self.alarm_time_24 = None
        self.alarm_active = False
        self.alarm_sound = None

        # Live Clock

        self.clock_label = tk.Label(root, text="", font=("Arial", 24))
        self.clock_label.pack(pady=10)
        self.update_clock()

        # Time input

        frame = tk.Frame(root)
        frame.pack(pady=5)

        self.hour_entry = tk.Entry(frame, width=5)
        self.hour_entry.insert(0, "07")
        self.hour_entry.grid(row=0, column=0)

        self.min_entry = tk.Entry(frame, width=5)
        self.min_entry.insert(0, "00")
        self.min_entry.grid(row=0, column=1)

        self.sec_entry = tk.Entry(frame, width=5)
        self.sec_entry.insert(0, "00")
        self.sec_entry.grid(row=0, column=2)

        self.ampm_var = tk.StringVar(value="AM")
        tk.OptionMenu(frame, self.ampm_var, "AM", "PM").grid(row=0, column=3, padx=5)

        # Buttons

        tk.Button(root, text="Choose Alarm Sound", command=self.choose_sound).pack(pady=5)
        self.set_btn = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_btn.pack(pady=5)

        self.snooze_btn = tk.Button(root, text="Snooze (5 min)", command=self.snooze_alarm, state="disabled")
        self.snooze_btn.pack(pady=5)

        self.stop_btn = tk.Button(root, text="Stop Alarm", command=self.stop_alarm, state="disabled")
        self.stop_btn.pack(pady=5)

        self.status_label = tk.Label(root, text="Alarm not set")
        self.status_label.pack(pady=5)

    def update_clock(self):
        self.clock_label.config(text=time.strftime("%I:%M:%S %p"))
        self.root.after(1000, self.update_clock)

    def choose_sound(self):
        file = filedialog.askopenfile(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file:
            self.alarm_sound = file
            self.status_label.config(text="Alarm sound selected")

    def set_alarm(self):
        try:
            hour = int(self.hour_entry.get())
            minute = int(self.min_entry.get())
            second = int(self.sec_entry.get())
            ampm = self.ampm_var.get()

            if ampm ==  "PM" and hour != 12:
                hour += 12
            if ampm == "AM" and hour == 12:
                hour = 0

            self.alarm_time_24 = f"{hour:02d}:{minute:02d}:{second:02d}"
        except ValueError:
            messagebox.showerror("Error", "Invalid time")
            return
        
        self.alarm_active = True
        self.status_label.config(text=f"Alarm set for {self.alarm_time_24}")
        threading.Thread(target=self.check_alarm, daemon=True).start()

    def check_alarm(self):
        while self.alarm_active:
            if time.strftime("H%:%M:%S") == self.alarm_time_24:
                self.trigger_alarm()
                break
            time.sleep(1)

    def snooze_alarm(self):
        pygame.mixer.music.stop()
        snooze_time = time.time() + 300
        self.alarm_time_24 = time.strftime("%H:%M:%S", time.localtime(snooze_time))
        self.alarm_active = True
        self.snooze_btn.config(state="disabled")
        self.stop_btn.config(state="disabled")
        self.status_label.config(text=f"Snoozed until {self.alarm_time_24}")
        threading.Thread(target=self.check_alarm, daemon=True).start()

    def stop_alarm(self):
        pygame.mixer.music.stop()
        self.snooze_btn.config(state="disabled")
        self.stop_btn.config(state="disabled")
        self.status_label.config(text="Alarm stopped")

if __name__ == "__main__":
    root = tk.Tk()
    AlarmClock(root)
    root.mainloop()

    

