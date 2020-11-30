import tkinter


class TrafficLights:
    __color = ['red', 'yellow', 'green']

    def running(self):
        window = tkinter.Tk()
        window.title("Светофор")
        tkinter.Label(text="График работы светофора: красный 7 секунд, желтый 2 секунды, зеленый 7 секунд").pack()
        self.canvas = tkinter.Canvas(window, width=350, height=350, bg="black")
        self.canvas.pack()
        self.oval_red = self.canvas.create_oval(120, 10, 220, 110, fill="white")
        self.oval_yellow = self.canvas.create_oval(120, 120, 220, 220, fill="white")
        self.oval_green = self.canvas.create_oval(120, 230, 220, 330, fill="white")
        self.change_color(self.__color[0])
        window.after(7000, self.change_color, self.__color[1])
        window.after(9000, self.change_color, self.__color[2])
        window.after(16000, self.change_color, self.__color[1])
        window.mainloop()

    def change_color(self, color):
        if color == 'red':
            self.canvas.itemconfig(self.oval_red, fill="red")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 'yellow':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="yellow")
            self.canvas.itemconfig(self.oval_green, fill="white")
        elif color == 'green':
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="green")


TrafficLights().running()
