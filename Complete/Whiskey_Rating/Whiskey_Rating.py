import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class ScoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("★ 위스키 평점 ★")

        # Set window size (3 times wider)
        self.root.geometry("500x800")
        
        self.questions = [
            "Q1. 부담스럽거나 다른 향을 해치는 알콜 부즈가 있다. ",
            "Q2. 인위적인 향(-) / 자연스러운 향(+)",
            "Q3. 복합적인 여러 향들의 존재감이 조화롭고 정도가 적당하다.",
            "Q4. 입 안에서 맛이 향과 어울리게 잘 느껴진다.",
            "Q5. 단순하고 적은 향(-) / 복합적인 여러 향(+)",
            "Q6. 잔향이 부담스럽게 올라온다(-) / 기분좋게 잔향이 남는다(+)",
            "Q7. Nose와 비교해 차이 혹은 Finish 만의 포인트가 있다.",
            "Q8. Nose -> Palete -> Finish 까지의 어울림과 연계가 조화롭다. ",
            "Q9. 풍미의 무게와 존재감이 액체의 느낌과 어울린다."
        ]
        
        self.scores = [0] * 9  # Initialize scores for each question to 0
        self.score_labels = []  # List to hold score labels for each question

        # Name entry at the top
        self.name_label = tk.Label(root, text="위스키 이름 :")
        self.name_label.place(x=200, y=10)
        
        self.name_entry = tk.Entry(root)
        self.name_entry.place(x=300, y=10)
        
#===================================================================================================================
        
        # Draw line
        RowNWord = [[40, "Nose"], [230, "Palete"], [360, "Finish"], [490, "Balance"], [645, "Util"]]

        for i in range(len(RowNWord)):
            self.line_frame = tk.Frame(root)
            self.line_frame.place(x=0, y=RowNWord[i][0])

            self.line = tk.Canvas(self.line_frame, height=7, width=500, bg="black")  # Set height and width
            self.line.pack(fill=tk.X)

            self.label_a = tk.Label(self.line_frame, text=RowNWord[i][1], bg="white")
            self.label_a.place(relx=0.4, rely=0.35, anchor='center')  # Center the word in the line
        
#===================================================================================================================

        questions_row = {0:50, 1:110, 2:170, 3:240, 4:300, 5:370, 6:430, 7:500, 8:560}
        rating_range = {0:[-5, 1], 1:[0, 6], 2:[0, 6], 3:[0, 6], 4:[0, 6], 5:[-5, 6], 6:[0, 6], 7:[-5, 6], 8:[0, 6]}
        
        # 질문지와 점수 선택 버튼, 점수 출력칸 GUI
        for i, question in enumerate(self.questions):
            # 질문지 출력
            label = tk.Label(root, text=question)
            label.place(x=10, y=questions_row[i])

            # 각 질문별 선택 점수 출력칸
            score_label = tk.Label(root, text="0", width=3)
            self.score_labels.append(score_label)  # Store the label for later updates
            score_label.place(x=445, y=questions_row[i])

            
            # 점수 선택 버튼
            for j in range(rating_range[i][0], rating_range[i][1]):
                button = tk.Button(root, text=str(j), width=4, height=1, command=lambda i=i, j=j: self.set_score(i, j))
                button.place(x=210+j*40, y=questions_row[i]+25)

#===================================================================================================================

        # Button to calculate total score
        self.calc_button = tk.Button(root, text="계산", command=self.calculate_total_score)
        self.calc_button.place(x=220, y=670)

        # Label to show result under Submit button
        self.result_label = tk.Label(root, text="")
        self.result_label.place(x=330, y=670)
        
        # Label to show star rating
        self.star_label = tk.Label(root, text="", fg="gold", font=("Arial", 16))
        self.star_label.place(x=310, y=710)

        # Place Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_entries)
        self.reset_button.place(x = 220, y = 710)
        
        # Button to save data to a file
        self.save_button = tk.Button(root, text="Save", command=self.save_to_file)
        self.save_button.place(x=340, y=760)
        
        # Exit buttons at the bottom
        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit)
        self.exit_button.place(x = 430, y = 760)
        
#===================================================================================================================

    def set_score(self, question_index, score):
        """Set the score for a given question and update the corresponding label."""
        self.scores[question_index] = score
        self.score_labels[question_index].config(text=str(score))  # Update score label
        #print(f"Score for Question {question_index + 1}: {score}")  # For debugging

    def calculate_total_score(self):
        total_score = round(sum(self.scores)/8, 2)  # Sum all the scores
        self.result_label.config(text=f"총점 : {total_score}")
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
            file.write(f"Name: {name}\n\n")
            for i, score in enumerate(self.scores):
                file.write(f"{self.questions[i]} {score}\n")
            file.write(f"\nTotal Score: {self.total_score}\n")

        messagebox.showinfo("Success", "Scores saved successfully!")

#===================================================================================================================

# Create the application window
root = tk.Tk()
app = ScoreApp(root)
root.mainloop()
