import tkinter as tk
import random
import tkinter.messagebox
window = tk.Tk()
window.title("Guess the Number")
window.geometry("640x400")
window.config(bg="#737373")  
window.resizable(width=False, height=False)  
game_play = False
class Gamesetup :
    def __init__(self,window) :
        self.label = tk.Label(window, text="Choose a number (1-1000):", font=("Arial", 20,"bold"), bg="#737373", fg="black")
        self.label.place(x=145, y=140)
        self.window = window
        self.secret_entry = tk.Entry(window, font=("Arial", 18), width=10)
        self.secret_entry.place(x=265, y=190)
        self.result_label = tk.Label(self.window, text="", font=("Arial", 12), bg="#737373", fg="black")
        self.secret_button = tk.Button(window, text="I don't want to know the secret number", font=("Arial", 12), command=self.gen_secret,width=30)
        self.secret_button.place(x=200, y=285)
        self.genrand_button = tk.Button(window, text="Generate a random number", font=("Arial", 12), command=self.gen_rand,width=30)
        self.genrand_button.place(x=200, y=240)
        self.start_button = tk.Button(window, text="Start", font=("Arial", 12), command=self.start,width=15)
        self.start_button.place(x=260, y=330)
    def gen_secret(self):
        self.secret_entry.delete(0, tk.END)
        self.secret_number = random.randint(1,1000)
        self.secret_entry.place_forget()
        self.genrand_button.place_forget()
        self.secret_button.place_forget()
        self.start_button.place_forget()
        self.label.place_forget()
        
        self.gameplay = Gameplay(self.window, self.secret_number)
    def gen_rand(self) :
        self.secret_entry.delete(0, tk.END)
        self.secret_number = random.randint(1,1000)
        self.secret_entry.insert(tk.END,self.secret_number)

    def start(self) :
         try : 
            self.secret_number = int(self.secret_entry.get())
            if self.secret_number < 1 or self.secret_number > 1000 :
                tkinter.messagebox.showinfo("Error","Your number is not valid! Please type again!")
                return
            self.secret_entry.place_forget()
            self.genrand_button.place_forget()
            self.secret_button.place_forget()
            self.start_button.place_forget()
            self.label.place_forget()

            self.gameplay = Gameplay(self.window, self.secret_number)
         except ValueError :
            tkinter.messagebox.showinfo("Error","Your number is not valid! Please type again!")


# Label
class Gameplay:
    def __init__(self, window, secret_number):
        self.secret_number = secret_number
        self.window = window
        self.low_thres = 1
        self.high_thres = 1000

        label = tk.Label(self.window, text="Guess a number (1-1000):", font=("Arial", 20,"bold"), bg="#737373", fg="black")
        label.place(x=140, y=140)

        self.guess_entry = tk.Entry(self.window, font=("Arial", 18), width=10)
        self.guess_entry.place(x=230, y=200)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 12), bg="#737373", fg="black")

        self.check_button = tk.Button(self.window, text="Check", font=("Times New Roman", 12), command=self.check_guess)
        self.check_button.place(x=270, y=245) 

    def check_guess(self):
        user_guess = int(self.guess_entry.get())
        if user_guess < self.low_thres or user_guess > self.high_thres:
            tkinter.messagebox.showinfo("Error","Your number is not valid! Please type again!")
            self.guess_entry.delete(0, tk.END)
        else:
            if user_guess == self.secret_number:
                self.guess_entry.delete(0, tk.END)
                tkinter.messagebox.showinfo("Congratulations","You made it!")
                self.check_button.place_forget()
                self.try_again_button = tk.Button(self.window, text="Try Again", font=("Arial", 12),command=self.start_new_game)
                self.try_again_button.place(x=240, y=240)

                self.exit_button = tk.Button(self.window, text="Exit", font=("Arial", 12), command=window.destroy)
                self.exit_button.place(x=240, y=280)
            elif user_guess < self.secret_number:
                self.low_thres = user_guess
                self.result_label.config(text=f"({self.low_thres} - {self.high_thres})")
                self.result_label.place(x=255, y=170)
                self.guess_entry.delete(0, tk.END)
            else:
                self.high_thres = user_guess
                self.result_label.config(text=f"({self.low_thres} - {self.high_thres})")
                self.result_label.place(x=255, y=170)
                self.guess_entry.delete(0, tk.END)
    def start_new_game(self):

        self.result_label.place_forget()
        self.try_again_button.place_forget()
        self.exit_button.place_forget()
        self.gamesetup = Gamesetup(window)

k = Gamesetup(window)
window.mainloop()
