import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class ScoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("★ 위스키 평점 ★")

        # Set window size (3 times wider)
        self.root.geometry("500x750")  # 900px width and 600px height

        self.questions = [
            "Q1. 부담스럽거나 다른 향을 해치는 알콜 부즈가 있다. ",
            "Q2. 인위적인 향(-) / 자연스러운 향(+)",
            "Q3. 복합적인 여러 향들의 존재감이 조화롭고 정도가 적당하다.",
            "Q4. 입 안에서 맛이 향과 어울리게 잘 느껴진다.",
            "Q5. 단순하고 적은 향(-) / 복합적인 여러 향(+)",
            "Q6. 잔향이 부담스럽게 올라온다(-) / 기분좋게 잔향이 남는다(+)",
            "Q7. Nose와 비교해 차이 혹은 Finish 만의 포인트가 있다.",
            "Q8. Nose -> Palete -> Finish 까지의 어울림과 연계가 조화롭다. ",
            "Q9. 향과 맛의 무게와 존재감이 액체의 무게감과 어울린다."
        ]
        
        self.scores = [0] * 9  # Initialize scores for each question to 0
        self.score_labels = []  # List to hold score labels for each question

        # Name entry at the top
        self.name_label = tk.Label(root, text="위스키 이름 :")
        self.name_label.grid(row=0, column=0, pady=0, sticky="w")
    
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, pady=0, sticky="w")
        
#===================================================================================================================

        # Draw line
        RowNWord = [[1, "Nose"], [8, "Palete"], [13, "Finish"], [18, "Balance"], [25, "Util"]]

        for i in range(len(RowNWord)):
            self.line_frame = tk.Frame(root)
            self.line_frame.grid(row=RowNWord[i][0], column=0, columnspan=2, pady=5)

            self.line = tk.Canvas(self.line_frame, height=7, width=500, bg="black")  # Set height and width
            self.line.pack(fill=tk.X)

            self.label_a = tk.Label(self.line_frame, text=RowNWord[i][1], bg="white")
            self.label_a.place(relx=0.5, rely=0.5, anchor='center')  # Center the word in the line
        
#===================================================================================================================

        questions_row = {0:2, 1:4, 2:6, 3:9, 4:11, 5:14, 6:16, 7:19, 8:21}
        score_row =     {0:3, 1:5, 2:7, 3:10, 4:12, 5:15, 6:17, 7:20, 8:22}

        # 질문지와 점수 선택 버튼, 점수 출력칸 GUI
        for i, question in enumerate(self.questions):
            # 각 질문별 선택 점수 출력칸
            score_label = tk.Label(root, text="0", width=3)
            score_label.grid(row=questions_row[i], column=1, padx=10, pady=0, sticky="w")  # Align to left (west)
            self.score_labels.append(score_label)  # Store the label for later updates

            # 질문지 출력
            label = tk.Label(root, text=question)
            label.grid(row=questions_row[i], column=0, padx=10, pady=0, sticky="w")

            # 점수 선택 버튼
            for j in range(0, 6):
                button = tk.Button(root, text=str(j), width=4, height=1, command=lambda i=i, j=j: self.set_score(i, j))
                button.grid(row=score_row[i], column=j, sticky="ew")

#===================================================================================================================

        # Button to calculate total score
        self.calc_button = tk.Button(root, text="계산", command=self.calculate_total_score)
        self.calc_button.grid(row=len(self.questions) + 17, column=0, columnspan=2, pady=5)

        # Label to show result under Submit button
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=len(self.questions) + 18, column=0, columnspan=2, pady=5)

        # Label to show star rating
        self.star_label = tk.Label(root, text="", fg="gold", font=("Arial", 16))
        self.star_label.grid(row=len(self.questions) + 19, column=0, columnspan=2, pady=5)

        # Button to save data to a file
        self.save_button = tk.Button(root, text="Save", command=self.save_to_file)
        #self.save_button.grid(row=len(self.questions) + 25, column=0, sticky="W")
        self.save_button.place(x = 250, y = 700)
        
        # Place Reset and Exit buttons at the bottom
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_entries)
        #self.reset_button.grid(row=len(self.questions) + 25, column=1, sticky="w")
        self.reset_button.place(x = 50, y = 700)
        
        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit)
        #self.exit_button.grid(row=len(self.questions) + 25, column=2, sticky="w")
        self.exit_button.place(x = 430, y = 700)
        
#===================================================================================================================

    def set_score(self, question_index, score):
        """Set the score for a given question and update the corresponding label."""
        self.scores[question_index] = score
        self.score_labels[question_index].config(text=str(score))  # Update score label
        #print(f"Score for Question {question_index + 1}: {score}")  # For debugging

    def calculate_total_score(self):
        total_score = round(sum(self.scores)/8, 2)  # Sum all the scores
        self.result_label.config(text=f"Total Score: {total_score}")
        self.total_score = total_score  # Save total score to use in file saving

        # Calculate star rating (out of 5)
        star_rating = total_score
        self.update_star_label(star_rating)

    def update_star_label(self, rating):
        """Update the star label based on the rating."""
        num_stars = int(rating)  # Get the integer part of the rating
        stars = '★' * num_stars + '☆' * (5 - num_stars)  # Create star string
        self.star_label.config(text=stars)

    def reset_entries(self):
        # Clear all scores and reset total score
        self.name_entry.delete(0, tk.END)
        self.scores = [0] * 9
        for label in self.score_labels:
            label.config(text="0")  # Reset score labels
        self.result_label.config(text="")  # Reset result label
        self.star_label.config(text="")  # Reset star label

    def save_to_file(self):
        # Get the name and check if it is valid
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Invalid Input", "Please enter your name.")
            return

        # Ask the user where to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file_path:
            return  # If no file is selected, return

        # Write the data to the file
        with open(file_path, 'w') as file:
            file.write(f"Name: {name}\n")
            for i, score in enumerate(self.scores):
                file.write(f"{self.questions[i]} {score}\n")
            file.write(f"Total Score: {self.total_score}\n")

        messagebox.showinfo("Success", "Scores saved successfully!")

#===================================================================================================================

# Create the application window
root = tk.Tk()
app = ScoreApp(root)
root.mainloop()
