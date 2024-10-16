import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk  # Make sure to install Pillow: pip install Pillow

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.geometry("400x400")
        
        self.user_score = 0
        self.computer_score = 0

        # Title Label
        title_label = tk.Label(self.master, text="Rock Paper Scissors", font=("Arial", 16))
        title_label.pack(pady=10)

        # Score Display
        self.score_label = tk.Label(self.master, text=f"Score - You: {self.user_score} | Computer: {self.computer_score}", font=("Arial", 12))
        self.score_label.pack(pady=10)

        # Load Images
        self.rock_image = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
        self.paper_image = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
        self.scissors_image = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))

        # Buttons for user choices with images
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=20)

        rock_button = tk.Button(button_frame, image=self.rock_image, command=lambda: self.play("rock"))
        rock_button.grid(row=0, column=0, padx=5)

        paper_button = tk.Button(button_frame, image=self.paper_image, command=lambda: self.play("paper"))
        paper_button.grid(row=0, column=1, padx=5)

        scissors_button = tk.Button(button_frame, image=self.scissors_image, command=lambda: self.play("scissors"))
        scissors_button.grid(row=0, column=2, padx=5)

    def play(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        result = self.determine_winner(user_choice, computer_choice)
        
        if result == "You win!":
            self.user_score += 1
            messagebox.showinfo("Result", f"You chose {user_choice}.\nComputer chose {computer_choice}.\n\n{result}")
        elif result == "You lose!":
            self.computer_score += 1
            messagebox.showinfo("Result", f"You chose {user_choice}.\nComputer chose {computer_choice}.\n\n{result}")
        else:
            messagebox.showinfo("Result", f"You chose {user_choice}.\nComputer chose {computer_choice}.\n\n{result}")

        self.update_score()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "You lose!"

    def update_score(self):
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()