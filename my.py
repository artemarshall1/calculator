from customtkinter import CTk, CTkEntry, CTkButton
from math import *

class Calculator(CTk):
    def __init__(self):
        super().__init__()

        self.title("Modern Scientific Calculator")
        self.geometry("340x650") # Трохи збільшив висоту для нових кнопок
        self.resizable(False, False)
        self.configure(fg_color="#1e1e1e")

        # Світлий екран (поле вводу)
        self.entry = CTkEntry(
            self, width=310, height=70, 
            font=("Orbitron", 26), 
            justify="right",
            fg_color="#e0e0e0",
            text_color="#1a1a1a",
            border_color="#ffffff",
            corner_radius=15
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=15, pady=25)

        # Оновлений список кнопок (додано sin, cos, pi, дужки)
        # Формат: (текст, рядок, колонка, колір)
        buttons = [
            ("sin", 1, 0, "#FF8A65"), ("cos", 1, 1, "#FF8A65"), ("(", 1, 2, "#90A4AE"), (")", 1, 3, "#90A4AE"),
            ("C", 2, 0, "#FF5252"), ("√", 2, 1, "#FF4081"), ("^", 2, 2, "#E040FB"), ("/", 2, 3, "#7C4DFF"),
            ("7", 3, 0, "#536DFE"), ("8", 3, 1, "#448AFF"), ("9", 3, 2, "#40C4FF"), ("*", 3, 3, "#18FFFF"),
            ("4", 4, 0, "#64FFDA"), ("5", 4, 1, "#69F0AE"), ("6", 4, 2, "#B2FF59"), ("-", 4, 3, "#EEFF41"),
            ("1", 5, 0, "#FFFF00"), ("2", 5, 1, "#FFD740"), ("3", 5, 2, "#FFAB40"), ("+", 5, 3, "#FF6E40"),
            ("0", 6, 0, "#BCAAA4"), (".", 6, 1, "#90A4AE"), ("π", 6, 2, "#81C784"), ("=", 6, 3, "#00C853")
        ]

        for (text, row, col, color) in buttons:
            # Визначаємо колір тексту для читабельності
            text_color = "#000000" if text not in ["C", "/", "√", "^", "=", "sin", "cos", "(", ")"] else "#ffffff"

            button = CTkButton(
                self, 
                text=text,
                width=70,
                height=60,
                corner_radius=12,
                font=("Arial", 20, "bold"),
                fg_color=color,
                text_color=text_color,
                hover_color=self.adjust_brightness(color, 0.2),
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, padx=5, pady=5)

    def adjust_brightness(self, hex_color, factor):
        hex_color = hex_color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        new_rgb = [min(255, int(c + (255 - c) * factor)) for c in rgb]
        return "#%02x%02x%02x" % tuple(new_rgb)

    def on_button_click(self, char):
        if char == "C":
            self.entry.delete(0, "end")
        elif char == "=":
            self.calculate()
        elif char == "π":
            self.entry.insert("end", "pi")
        elif char == "sin":
            self.entry.insert("end", "sin(")
        elif char == "cos":
            self.entry.insert("end", "cos(")
        elif char == "√":
            self.entry.insert("end", "sqrt(")
        else:
            self.entry.insert("end", char)

    def calculate(self):
        try:
            # Отримуємо вираз та замінюємо символи на зрозумілі для Python
            expression = self.entry.get()
            expression = expression.replace("^", "**")
            
            # eval() в Python автоматично використовує функції з модуля math, 
            # оскільки ми зробили 'from math import *'
            result = eval(expression)
                
            if isinstance(result, float):
                result = round(result, 8)
                if result.is_integer(): result = int(result)
                
            self.entry.delete(0, "end")
            self.entry.insert(0, str(result))
        except Exception:
            self.entry.delete(0, "end")
            self.entry.insert(0, "Error")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()