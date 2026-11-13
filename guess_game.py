import random
import tkinter as tk

secret_number = random.randint(1, 100)
attempts = 0
MAX_ATTEMPTS = 10


def check_guess(event=None):
    global attempts

    try:
        guess = int(number_entry.get())
    except ValueError:
        result_label.config(text="لطفاً یک عدد صحیح وارد کنید.")
        return

    if not 1 <= guess <= 100:
        result_label.config(text="عدد باید بین ۱ تا ۱۰۰ باشد.")
        return

    attempts += 1
    attempts_label.config(text=f"تلاش: {attempts} از {MAX_ATTEMPTS}")
    number_entry.delete(0, tk.END)

    if guess == secret_number:
        result_label.config(text="آفرین! درست حدس زدی 🎉")
        finish_game()
    elif attempts == MAX_ATTEMPTS:
        result_label.config(text=f"فرصت‌ها تمام شد! عدد درست {secret_number} بود.")
        finish_game()
    elif guess > secret_number:
        result_label.config(text="عدد شما بزرگ‌تر از عدد من است.")
    else:
        result_label.config(text="عدد شما کوچک‌تر از عدد من است.")


def finish_game():
    number_entry.config(state="disabled")
    guess_button.config(state="disabled")


def restart_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    attempts_label.config(text=f"تلاش: ۰ از {MAX_ATTEMPTS}")
    result_label.config(text="عدد را حدس بزن!")
    number_entry.config(state="normal")
    guess_button.config(state="normal")
    number_entry.delete(0, tk.END)
    number_entry.focus_set()


window = tk.Tk()
window.title("بازی حدس عدد")
window.geometry("350x280")
window.resizable(False, False)


tk.Label(window, text="حدس عدد از ۱ تا ۱۰۰", font=("Tahoma", 14, "bold")).pack(pady=(20, 10))
tk.Label(window, text="۱۰ فرصت برای پیدا کردن عدد داری.").pack()

number_entry = tk.Entry(window, font=("Tahoma", 13), justify="center", width=12)
number_entry.pack(pady=12)

guess_button = tk.Button(window, text="ثبت حدس", command=check_guess, width=14)
guess_button.pack()

result_label = tk.Label(window, text="عدد را حدس بزن!", font=("Tahoma", 10))
result_label.pack(pady=10)

attempts_label = tk.Label(window, text="تلاش: ۰ از ۱۰")
attempts_label.pack()

tk.Button(window, text="شروع دوباره", command=restart_game).pack(pady=10)

window.bind("<Return>", check_guess)
number_entry.focus_set()
window.mainloop()
