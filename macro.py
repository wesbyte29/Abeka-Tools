import subprocess
import sys
import time
import tkinter
import pynput

def set_window_size(root, width=300, height=200):
    root.geometry(f"{width}x{height}")



class App:
    def on_continue(self):
            selected_option = self.var.get()
            print(f"Selected option: {selected_option}")
            match selected_option:
                case "Option 1":
                    # run macro
                    subprocess.run(["python", "do_thing.py"], check=True)
                case "Option 2":
                    print("Option 2 selected")
                case "Option 3":
                    print("Option 3 selected")
                case _:
                    print("Invalid option selected")
    def __init__(self, root):

        

        self.root = root
        self.root.title("Radio Button Example")

        self.var = tkinter.StringVar()
        self.var.set("Option 1")

        self.radio1 = tkinter.Radiobutton(root, text="Option 1", variable=self.var, value="Option 1")
        self.radio1.pack(anchor=tkinter.W)

        self.radio2 = tkinter.Radiobutton(text="Option 2", variable=self.var, value="Option 2")
        self.radio2.pack(anchor=tkinter.W)

        self.radio3 = tkinter.Radiobutton(root, text="Option 3", variable=self.var, value="Option 3")
        self.radio3.pack(anchor=tkinter.W)

        # continue
        self.continue_button = tkinter.Button(root, text="Continue", command=self.on_continue)
        self.continue_button.pack(anchor=tkinter.W)

        

if __name__ == "__main__":
    root = tkinter.Tk()
    set_window_size(root)
    app = App(root)
    root.mainloop()