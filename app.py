import json
import  random
import  tkinter as tk
import recommand as r
from  tkinter import messagebox

root = tk.Tk()
root.title("Рекомендаційний фільм!")

with open("data.json","r",encoding="utf-8") as file:
    data = json.load(file)

genres = ['бойовик', 'трилер', 'фантастика', 'пригоди', 'драма', 'кримінал', 'музика',
          'жахи', 'комедія', 'фентезі', 'військовий', 'документальний', 'детектив', 'сімейний',
          'мелодрама', 'мультфільм', 'біографія', 'аніме', 'концерт', 'вестерн', 'спорт', 'історія',
          'мюзикл']

var = tk.StringVar(value="бойовик")

for genre in genres:
    tk.Radiobutton(root,text=genre,variable=var,value=genre).pack(anchor="w")

tk.Button(root,text="Порекомендуй мені фільм",command =r.recommend_voice(var)).pack(pady=10)

root.mainloop()