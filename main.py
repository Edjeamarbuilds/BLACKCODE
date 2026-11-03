import tkinter as tk
from tkinter import messagebox

# QUIZ APPLICATION

QUESTIONS = [
    {
        "question": "1. What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing User"
        ],
        "answer": 0
    },
    {
        "question": "2. Which device is used to type text?",
        "options": ["Monitor", "Keyboard", "Speaker", "Printer"],
        "answer": 1
    },
    {
        "question": "3. Which is an output device?",
        "options": ["Mouse", "Microphone", "Monitor", "Keyboard"],
        "answer": 2
    },
    {
        "question": "4. Which is an operating system?",
        "options": [
            "Microsoft Word",
            "Windows",
            "Google Chrome",
            "PowerPoint"
        ],
        "answer": 1
    },
    {
        "question": "5. What is the main function of a mouse?",
        "options": [
            "Print documents",
            "Display images",
            "Point, click, and select items",
            "Play sound"
        ],
        "answer": 2
    }
]


class QuizApplication:

    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("650x500")
        self.root.configure(bg="#eef2ff")
        self.root.resizable(False, False)

        self.index = 0
        self.score = 0
        self.answer = tk.IntVar(value=-1)

        # TITLE
        tk.Label(
            root,
            text="QUIZ APPLICATION",
            font=("Arial", 22, "bold"),
            bg="#4338ca",
            fg="white",
            pady=20
        ).pack(fill="x")

        self.body = tk.Frame(root, bg="#eef2ff")
        self.body.pack(fill="both", expand=True, padx=30, pady=20)

        # QUESTION NUMBER
        self.progress = tk.Label(
            self.body,
            text="",
            font=("Arial", 11),
            bg="#eef2ff"
        )
        self.progress.pack(anchor="w", pady=10)

        # QUESTION TEXT
        self.question = tk.Label(
            self.body,
            text="",
            font=("Arial", 14, "bold"),
            bg="#eef2ff",
            wraplength=570,
            justify="left"
        )
        self.question.pack(anchor="w", pady=10)

        # ANSWER OPTIONS
        self.options_frame = tk.Frame(
            self.body,
            bg="#eef2ff"
        )
        self.options_frame.pack(fill="x")

        self.options = []

        for i in range(4):
            button = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.answer,
                value=i,
                font=("Arial", 12),
                bg="#eef2ff",
                anchor="w",
                wraplength=550
            )
            button.pack(fill="x", pady=5)
            self.options.append(button)

        # NEXT BUTTON
        self.next_btn = tk.Button(
            self.body,
            text="Next Question",
            command=self.next_question,
            font=("Arial", 12, "bold"),
            bg="#4338ca",
            fg="white",
            padx=20,
            pady=10
        )
        self.next_btn.pack(pady=20)

        self.show_question()

    def show_question(self):
        item = QUESTIONS[self.index]

        self.progress.config(
            text=f"Question {self.index + 1} of {len(QUESTIONS)}"
        )

        self.question.config(text=item["question"])
        self.answer.set(-1)

        for i, text in enumerate(item["options"]):
            self.options[i].config(text=text, value=i)

        if self.index == len(QUESTIONS) - 1:
            self.next_btn.config(text="Submit Quiz")
        else:
            self.next_btn.config(text="Next Question")

    def next_question(self):
        selected = self.answer.get()

        if selected == -1:
            messagebox.showwarning(
                "No Answer",
                "Please select an answer first!"
            )
            return

        if selected == QUESTIONS[self.index]["answer"]:
            self.score += 1

        self.index += 1

        if self.index < len(QUESTIONS):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        total = len(QUESTIONS)
        percentage = (self.score / total) * 100

        if percentage >= 80:
            remarks = "Excellent! Great job!"
        elif percentage >= 60:
            remarks = "Good effort! Keep practicing."
        else:
            remarks = "Keep studying and try again."

        tk.Label(
            self.root,
            text="QUIZ APPLICATION",
            font=("Arial", 22, "bold"),
            bg="#4338ca",
            fg="white",
            pady=20
        ).pack(fill="x")

        frame = tk.Frame(self.root, bg="#eef2ff")
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="QUIZ COMPLETED!",
            font=("Arial", 20, "bold"),
            bg="#eef2ff"
        ).pack(pady=15)

        tk.Label(
            frame,
            text=f"Your Score: {self.score}/{total}",
            font=("Arial", 18, "bold"),
            fg="#4338ca",
            bg="#eef2ff"
        ).pack(pady=8)

        tk.Label(
            frame,
            text=f"Percentage: {percentage:.0f}%",
            font=("Arial", 14),
            bg="#eef2ff"
        ).pack(pady=5)

        tk.Label(
            frame,
            text=remarks,
            font=("Arial", 13),
            fg="green",
            bg="#eef2ff"
        ).pack(pady=10)

        tk.Button(
            frame,
            text="Retake Quiz",
            command=self.restart,
            font=("Arial", 12, "bold"),
            bg="#4338ca",
            fg="white",
            padx=15,
            pady=8
        ).pack(pady=8)

        tk.Button(
            frame,
            text="Exit",
            command=self.root.destroy
        ).pack()

    def restart(self):
        self.index = 0
        self.score = 0

        for widget in self.root.winfo_children():
            widget.destroy()

        self.__init__(self.root)


# RUN THE APPLICATION
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApplication(root)
    root.mainloop()
