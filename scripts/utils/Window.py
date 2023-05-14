from tkinter import StringVar, Radiobutton, Tk

from configs import configs
from scripts.utils.Dimension import Dimension


class Window:
    def __init__(self, title: str, dimension: Dimension, resizable: bool):
        self.window = Tk()
        self.window.title(title)
        self.window.resizable(height=resizable, width=resizable)
        self.window.geometry(dimension.get_geometry())
        self.window.mainloop()

    def dimensionGeometry(self):
        options = configs.RESOLUTIONS

        variable = StringVar(self.window)
        variable.set(options[0])

        def show_selected_option():
            print("Opção selecionada:", variable.get())

        Radiobutton(self.window, text=options[0], variable=variable, value=options[0],
                    command=show_selected_option).pack()
        Radiobutton(self.window, text=options[1], variable=variable, value=options[1],
                    command=show_selected_option).pack()
        Radiobutton(self.window, text=options[2], variable=variable, value=options[2],
                    command=show_selected_option).pack()
