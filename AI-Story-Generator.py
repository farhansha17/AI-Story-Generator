import random
import tkinter as tk
from tkinter import ttk

# Sample story elements
genres = {
    "Fantasy": [
        "In a realm ruled by dragons",
        "A young elf discovers a magical stone",
        "The sword of destiny is reborn"
    ],
    "Sci-Fi": [
        "In a future where robots govern humans",
        "An astronaut wakes up alone on Mars",
        "Earth's last hope is a time-traveling hacker"
    ],
    "Mystery": [
        "A detective receives an anonymous letter",
        "A locked room with no escape",
        "The killer left behind a single red glove"
    ]
}

middles = [
    "they meet a mysterious stranger",
    "they uncover a hidden truth",
    "they are forced to make a difficult choice",
    "an ancient prophecy comes true",
    "something they lost returns unexpectedly"
]

endings = [
    "and peace is finally restored.",
    "but not everyone survives the journey.",
    "and a new era begins.",
    "but the real story is just beginning...",
    "and history will never forget their name."
]

# GUI App
class StoryGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Story Generator")
        self.root.geometry("600x400")

        self.genre_label = tk.Label(root, text="Select Genre:", font=("Helvetica", 12))
        self.genre_label.pack(pady=10)

        self.genre_var = tk.StringVar()
        self.genre_dropdown = ttk.Combobox(root, textvariable=self.genre_var, values=list(genres.keys()))
        self.genre_dropdown.pack()
        self.genre_dropdown.current(0)

        self.generate_button = tk.Button(root, text="Generate Story", command=self.generate_story)
        self.generate_button.pack(pady=20)

        self.output_text = tk.Text(root, height=10, width=70, wrap=tk.WORD)
        self.output_text.pack(padx=10)

    def generate_story(self):
        genre = self.genre_var.get()
        start = random.choice(genres[genre])
        middle = random.choice(middles)
        end = random.choice(endings)
        story = f"{start}, {middle}, {end}"
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, story)

if __name__ == "__main__":
    root = tk.Tk()
    app = StoryGeneratorApp(root)
    root.mainloop()
