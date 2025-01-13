import json
import  random
import  tkinter as tk
from  tkinter import messagebox

def recommend_voice(var):
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    selected_choice = var.get()
    if selected_choice in data:
        movie_recommendation = random.choice(data[selected_choice])
        print(movie_recommendation)
        title_recommend = movie_recommendation["Title"]
        messagebox.showinfo("Рекомендація!",f"АІ порекомендував вам - {title_recommend}")
    else:
        messagebox.showwarning("Помилка","На жаль,ми не хочемо рекомендувати фільм")