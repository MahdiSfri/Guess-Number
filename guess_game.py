import random
import tkinter as tk
from tkinter import font

import arabic_reshaper
from bidi.algorithm import get_display


MAX_ATTEMPTS = 10
secret_number = random.randint(1, 100)
attempts = 0


def fa(text):
    """Prepare Persian text for Tkinter widgets on Linux."""
    return get_display(arabic_reshaper.reshape(str(text)), base_dir="R")


def check_guess(event=None):
    global attempts

    if number_entry.cget("state") == "disabled":
        return

    try:
        guess = int(number_entry.get())
    except ValueError:
        result_label.config(text=fa("لطفاً یک عدد صحیح وارد کنید."))
        return

    if not 1 <= guess <= 100:
        result_label.config(text=fa("عدد باید بین ۱ تا ۱۰۰ باشد."))
        return

    attempts += 1
    attempts_label.config(text=fa(f"تلاش: {attempts} از {MAX_ATTEMPTS}"))
    number_entry.delete(0, tk.END)

    if guess == secret_number:
        result_label.config(text=fa("آفرین! درست حدس زدی!"))
        finish_game()
    elif attempts == MAX_ATTEMPTS:
        result_label.config(text=fa(f"فرصت‌ها تمام شد! عدد درست {secret_number} بود."))
        finish_game()
    elif guess > secret_number:
        result_label.config(text=fa("عدد شما بزرگ‌تر از عدد من است."))
    else:
        result_label.config(text=fa("عدد شما کوچک‌تر از عدد من است."))


def finish_game():
    number_entry.config(state="disabled")
    guess_button.config(state="disabled")


def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    attempts_label.config(text=fa(f"تلاش: {attempts} از {MAX_ATTEMPTS}"))
    result_label.config(text=fa("عدد را حدس بزن!"))
    number_entry.config(state="normal")
    guess_button.config(state="normal")
    number_entry.delete(0, tk.END)
    number_entry.focus_set()


window = tk.Tk()
window.title("بازی حدس عدد")
window.geometry("380x285")
window.resizable(False, False)

# A Persian-capable font; fall back to a widely available Linux font.
available_fonts = set(font.families(window))
font_family = "Noto Sans Arabic" if "Noto Sans Arabic" in available_fonts else "DejaVu Sans"


tk.Label(
    window, text=fa("حدس عدد از ۱ تا ۱۰۰"), font=(font_family, 14, "bold")
).pack(pady=(18, 10))

tk.Label(
    window, text=fa("۱۰ فرصت برای پیدا کردن عدد داری."), font=(font_family, 10)
).pack()

number_entry = tk.Entry(window, font=(font_family, 12), justify="center", width=12)
number_entry.pack(pady=11)

guess_button = tk.Button(
    window, text=fa("ثبت حدس"), command=check_guess,
    font=(font_family, 10), width=14
)
guess_button.pack()

result_label = tk.Label(
    window, text=fa("عدد را حدس بزن!"), font=(font_family, 10)
)
result_label.pack(pady=9)

attempts_label = tk.Label(
    window, text=fa(f"تلاش: ۰ از {MAX_ATTEMPTS}"), font=(font_family, 10)
)
attempts_label.pack()

tk.Button(
    window, text=fa("شروع دوباره"), command=restart_game,
    font=(font_family, 10)
).pack(pady=9)

window.bind("<Return>", check_guess)
number_entry.focus_set()
window.mainloop()
