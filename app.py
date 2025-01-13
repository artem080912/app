import json
import  random
import  tkinter as tk
import recommand as r
import ftypes as f
from  tkinter import messagebox
var = tk.StringVar(value="бойовик")

def main():
    root = tk.Tk()
    root.title("Рекомендаційний фільм!")

    with open("data.json","r",encoding="utf-8") as file:
        data = json.load(file)


    for genre in f.genres:
        tk.Radiobutton(root,text=genre,variable=var,value=genre).pack(anchor="w")

    tk.Button(root,text="Порекомендуй мені фільм",command =r.recommend_voice(var)).pack(pady=10)

    root.mainloop()

main()