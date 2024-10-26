import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

class ScoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("★ 위스키 평점 ★")

        # Set window size
        self.root.geometry("720x800")
        
        self.questions = [
            "Q1. 부담스럽거나 다른 향을 해치는 알콜 부즈가 있다. ",
            "Q2. 인위적인 향(-) / 자연스러운 향(+) ",
            "Q3. 복합적인 여러 향들의 존재감이 조화롭고 정도가 적당하다.",
            "Q4. 입 안에서 맛이 향과 어울리게 잘 느껴진다.",
            "Q5. 단순하고 적은 향(-) / 복합적인 여러 향(+) ",
            "Q6. 잔향이 부담스럽게 올라온다(-) / 기분좋게 잔향이 남는다(+) ",
            "Q7. Nose와 비교해 차이 혹은 Finish 만의 포인트가 있다.",
            "Q8. Nose -> Palete -> Finish 까지의 어울림과 연계가 조화롭다. ",
            "Q9. 풍미의 무게와 존재감이 액체의 느낌과 어울린다."
        ]
        
        self.scores = [0] * 9
        self.score_labels = []

        # Name entry at the top
        self.name_label = tk.Label(root, text="위스키 이름 :")
        self.name_label.place(x=200, y=10)
        
        self.name_entry = tk.Entry(root)
        self.name_entry.place(x=300, y=10)
        
#=======================================================================================================================

        # Draw line
        RowNWord = [[40, "Nose"], [230, "Palete"], [360, "Finish"], [490, "Balance"], [645, "Util"]]

        for i in range(len(RowNWord)):
            self.line_frame = tk.Frame(root)
            self.line_frame.place(x=0, y=RowNWord[i][0])

            self.line = tk.Canvas(self.line_frame, height=7, width=500, bg="black")
            self.line.pack(fill=tk.X)

            self.label_a = tk.Label(self.line_frame, text=RowNWord[i][1], bg="white")
            self.label_a.place(relx=0.4, rely=0.35, anchor='center')
        
#=======================================================================================================================

        questions_row = {0:50, 1:110, 2:170, 3:240, 4:300, 5:370, 6:430, 7:500, 8:560}
        rating_range = {0:[-5, 1], 1:[0, 6], 2:[0, 6], 3:[0, 6], 4:[0, 6], 5:[-5, 6], 6:[0, 6], 7:[-5, 6], 8:[0, 6]}
        
        for i, question in enumerate(self.questions):
            label = tk.Label(root, text=question)
            label.place(x=10, y=questions_row[i])

            score_label = tk.Label(root, text="0", width=3)
            self.score_labels.append(score_label)
            score_label.place(x=445, y=questions_row[i])

            for j in range(rating_range[i][0], rating_range[i][1]):
                button = tk.Button(root, text=str(j), width=4, height=1, command=lambda i=i, j=j: self.set_score(i, j))
                button.place(x=210+j*40, y=questions_row[i]+25)

#=======================================================================================================================

        self.calc_button = tk.Button(root, text="계산", command=self.calculate_total_score)
        self.calc_button.place(x=200, y=670)

        self.result_label = tk.Label(root, text="")
        self.result_label.place(x=310, y=670)
        
        self.star_label = tk.Label(root, text="", fg="gold", font=("Arial", 16))
        self.star_label.place(x=290, y=690)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_entries)
        self.reset_button.place(x=200, y=700)
        
        self.save_button = tk.Button(root, text="Save", command=self.save_to_file)
        self.save_button.place(x=340, y=760)
        
        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit)
        self.exit_button.place(x=430, y=760)
        
        self.info_visible = False
        self.info_dict = {"Agave":"아가베", "Anise":"아니스(팔각)", "Apple":"사과", "Apricot":"살구",
                          "Artificial":"인조적인", "Banana":"바나나", "Berries":"베리류", "Bitter":"쓴",
                          "Briny":"바다의 짠맛", "Butter":"버터", "Caramel":"캬라멜", "Chemical":"화학약품",
                          "Cinamon":"계피", "Citrus":"감귤류", "Clove":"클로브(정향)", "Coconut":"코코넛",
                          "Coffee":"커피", "Coriander":"고수", "Cream":"크림", "Cucumber":"오이",
                          "Dried Fruit":"말린 과일", "Earthy":"흙내", "Fennel":"펜넬(회향)", "Fig":"무화과",
                          "Floral":"꽃향기", "Fruity":"과일향", "Full":"꽉 차는", "Grain":"곡류의 씨앗",
                          "Grape":"포도", "Grapefruit":"자몽", "Harsh":"거친", "Herbal":"허브류",
                          "Honey":"꿀", "Hot":"화끈한", "Juniper":"주니퍼베리", "Leather":"가죽",
                          "Licorice":"서양 감초", "Light":"가벼움", "Lime":"라임", "Maple":"메이플(시럽)",
                          "Medicinal":"약품", "Mineral":"미네랄", "Mint":"민트", "Molasses":"몰라시스(당밀)",
                          "Musty":"퀴퀴한(묵은내)", "Neutral":"무미건조", "Nutty":"견과류", "Oak":"오크향",
                          "Oily":"기름진", "Orange":"오렌지", "Peaty":"피트향", "Pepper":"후추",
                          "Pineapple":"파인애플", "Piney":"소나무", "Plum":"자두", "Potato":"감자",
                          "Prune":"말린 서양자두", "Raisin":"건포도", "Rich":"풍부한", "Roast":"훈제",
                          "Salty":"짭잘함","Savory":"적당한 간", "Sherry":"쉐리향", "Smooth":"부드러움",
                          "Sweet":"달콤함", "Tannic":"타닌(쓴)", "Toasty":"구운 곡물", "Toffee":"토피넛",
                          "Tropical":"열대(과일)", "Umami":"감칠맛", "Vanila":"바닐라", "Woody":"나무"}
        self.selected_info = set()
        self.info_frame = tk.Frame(root, width=400, height=600, bg="lightgray")
        
        self.display_keys = True
        self.convert_button = tk.Button(self.info_frame, text="영/한", command=self.toggle_display)
        self.convert_button.pack(pady=5)

        self.toggle_info_button = tk.Button(root, text="Tasting Note", command=self.toggle_info)
        self.toggle_info_button.place(x=420, y=670)

#=======================================================================================================================

    def toggle_info(self):
        if self.info_visible:
            self.info_frame.place_forget()
        else:
            self.info_frame.place(x=510, y=40)
            self.update_info_panel()
        self.info_visible = not self.info_visible

    def toggle_display(self):
        self.display_keys = not self.display_keys
        self.update_info_panel()

    def update_info_panel(self):
        for widget in self.info_frame.winfo_children():
            if widget != self.convert_button:
                widget.destroy()
        
        items = self.info_dict.keys() if self.display_keys else self.info_dict.values()

        for item in items:
            button_text = str(item)
            button = tk.Button(self.info_frame, text=button_text, command=lambda item=item: self.toggle_selection(item))
            button.pack(anchor="w", fill=tk.X)
            if item in self.selected_info:
                button.config(bg="lightblue")  # Highlight selected buttons
        """
        for item in items:
            button_text = str(item)
            button = tk.Button(self.info_frame, text=button_text, command=lambda item=item: self.toggle_selection(item))
            button.pack(anchor="w", fill=tk.X)
            if item in self.selected_info:
                button.config(bg="lightblue")  # Highlight selected buttons
        """

    def toggle_selection(self, item):
        if item in self.selected_info:
            self.selected_info.remove(item)
        else:
            self.selected_info.add(item)
        self.update_info_panel()

    def set_score(self, question_index, score):
        self.scores[question_index] = score
        self.score_labels[question_index].config(text=str(score))

    def calculate_total_score(self):
        total_score = round(sum(self.scores) / 8, 2)
        self.result_label.config(text=f"총점 : {total_score}")
        self.total_score = total_score
        star_rating = total_score
        self.update_star_label(star_rating)

    def update_star_label(self, rating):
        num_stars = int(rating)
        stars = '★' * num_stars + '☆' * (5 - num_stars)
        self.star_label.config(text=stars)

    def reset_entries(self):
        self.name_entry.delete(0, tk.END)
        self.scores = [0] * 9
        for label in self.score_labels:
            label.config(text="0")
        self.result_label.config(text="")
        self.star_label.config(text="")
        self.selected_info.clear()

    def save_to_file(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Invalid Input", "Please enter your name.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        with open(file_path, 'w') as file:
            file.write(f"Name : {name}\n\n")
            for i, score in enumerate(self.scores):
                file.write(f"{self.questions[i]} {score}\n")

            self.selected_info=sorted(self.selected_info)
            selected_items = ', '.join(str(item) for item in self.selected_info)
            file.write(f"\nTasting Note : {selected_items}\n")
            
            file.write(f"\nTotal Score : {self.total_score}\n")
            
            

        messagebox.showinfo("Success", "Scores saved successfully!")

#=======================================================================================================================

# Create the application window
root = tk.Tk()
app = ScoreApp(root)
root.mainloop()
