import tkinter as tk
import screen_brightness_control as sbc

root = tk.Tk()
root.title("light")
root.configure(bg="#2c3e50")
# размер
root.geometry("300x150") 

def go(val):
    sbc.set_brightness(val)

slider = tk.Scale(
    root, 
    from_=0, 
    to=100, 
    orient="horizontal", 
    command=go, 
    length=300,
    bg="#2c3e50",    # Фон ползунка
    fg="white",      # Цвет текста 
    troughcolor="#34495e", # Цвет желобка, по которому бегает ползунок
    highlightthickness=0 # Убирает рамку вокруг
)
slider.pack(pady=50)

root.mainloop()