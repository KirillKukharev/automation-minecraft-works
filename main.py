import tkinter
import tkinter.messagebox
import customtkinter
import sys
# import keyboard

# import cv2
# import numpy as np
import pytesseract
from PIL import ImageGrab

# customtkinter.ScalingTracker.set_user_scaling(0.5)
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def detection_digits():
    # Test
    counter = 0
    while True:
        # This instance will generate an image from
        # the point of (1308, 263) and (1405, 277) in format of (x, y)
        cap_1 = ImageGrab.grab(bbox=(2617, 525, 2695, 555), all_screens=True)

        cap_2 = ImageGrab.grab(bbox=(2733, 525, 2807, 555), all_screens=True)

        text_1 = pytesseract.image_to_string(cap_1, lang='eng',
                                             config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        text_2 = pytesseract.image_to_string(cap_2, lang='eng',
                                             config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

        text = text_1 + " " + text_2

        if len(text) > 0:
            print(text)

        # if keyboard.is_pressed('z'):
        #     print('You Pressed A Key!')
        #     break
        if counter > 10:
            break


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("Приложение для Lavacraft")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Меню",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Бродилка",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                # command=self.button_event)
                                                command=lambda: switch_to_walking(list_of_widgets))
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Пират",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                # command=self.button_event)
                                                # command = lambda:self.radio_button_2.grid_remove())
                                                command=lambda: switch_to_pirat(list_of_widgets))
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        # self.button_3 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Кнопка 3",
        #                                         fg_color=("gray75", "gray30"),  # <- custom tuple-color
        #                                         command=self.button_event)
        # self.button_3.grid(row=4, column=0, pady=10, padx=20)

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left)
        self.switch_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode)
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="CTkLabel: Lorem ipsum dolor sit,\n" +
                                                        "amet consetetur sadipscing elitr,\n" +
                                                        "sed diam nonumy eirmod tempor",
                                                   height=100,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        # self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        # self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Кол-во координат:")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           text="1 координата (высота) \n"+
                                                                "     (по умолчанию)",
                                                           value=0,
                                                           command=lambda: change_number_coordingates(self, 0))
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           text="2 координаты (X  и  Y)",
                                                           value=1,
                                                           command=lambda: change_number_coordingates(self, 1))
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         from_=0,
        #                                         to=1,
        #                                         number_of_steps=3,
        #                                         command=self.progressbar.set)
        # self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")
        #
        # self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         command=self.progressbar.set)
        # self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        # self.slider_button_1 = customtkinter.CTkButton(master=self.frame_right,
        #                                                height=25,
        #                                                text="CTkButton",
        #                                                command=self.button_event)
        # self.slider_button_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
        #                                                height=25,
        #                                                text="CTkButton_hide_pic",
        #                                                command=self.button_event)
        #                                                # command = lambda:self.radio_button_2.grid_remove())
        #                                                # command=lambda:switch_to_pirat())
        # self.slider_button_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.checkbox_button_1 = customtkinter.CTkButton(master=self.frame_right,
        #                                                  height=25,
        #                                                  text="CTkButton1",
        #                                                  border_width=3,   # <- custom border_width
        #                                                  fg_color=None,   # <- no fg_color
        #                                                  command=self.button_event)

        # self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        # self.checkbox_button_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.label_info_2 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="Введите координаты X и Y (по центру) из игры",
                                                   height=25,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   # justify=tkinter.LEFT)
                                                   )
        # self.label_info_2.grid(row=4, column=0, sticky="nwe", padx=5, pady=10)

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=30,
                                            placeholder_text="Координата X")
        # self.entry.grid(row=4, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=30,
                                            placeholder_text="Координата Y")
        # self.entry_2.grid(row=4, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.label_info_3 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="Введите левый верхний и правый нижний \n" +
                                                        "углы областей для X и Y",
                                                   height=25,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   # justify=tkinter.LEFT)
                                                   )
        self.label_info_3.grid(row=4, columnspan=2, sticky="nwe", padx=10, pady=10)

        self.left_upper_1 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=30,
                                            placeholder_text="Левый верх (1)")
        self.left_upper_1.grid(row=5, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        self.right_lower_1 = customtkinter.CTkEntry(master=self.frame_right,
                                              width=30,
                                              placeholder_text="Правый низ (1)")
        self.right_lower_1.grid(row=5, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.left_upper_2 = customtkinter.CTkEntry(master=self.frame_right,
                                                   width=20,
                                                   placeholder_text="Левый верх (2)")
        self.left_upper_2.grid(row=6, column=0, pady=20, padx=20, sticky="we")

        self.right_lower_2 = customtkinter.CTkEntry(master=self.frame_right,
                                                    width=20,
                                                    placeholder_text="Правый низ (2)")
        self.right_lower_2.grid(row=6, column=1, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Начать",
                                                command=self.button_event)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_6 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Запустить",
                                                command=self.button_event)

        # set default values
        self.radio_button_1.select()
        self.switch_2.select()
        self.left_upper_2.configure(state=tkinter.DISABLED)
        self.right_lower_2.configure(state=tkinter.DISABLED)
        # self.slider_1.set(0.2)
        # self.slider_2.set(0.7)
        # self.progressbar.set(0.5)
        # self.slider_button_1.configure(state=tkinter.DISABLED, text="Disabled Button")
        # self.radio_button_3.configure(state=tkinter.DISABLED)
        # self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        # self.check_box_2.select()

        list_of_widgets = [self.radio_button_1, self.radio_button_2,
                           self.label_info_2, self.entry, self.entry_2, self.label_info_3,
                           self.left_upper_1, self.right_lower_1, self.left_upper_2, self.right_lower_2,
                           self.button_5, self.label_radio_group, self.button_6]

    def button_event(self):
        print("Кнопка нажата")

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

def change_number_coordingates(self, number):
        if number == 0:
            self.left_upper_2.configure(state=tkinter.DISABLED)
            self.right_lower_2.configure(state=tkinter.DISABLED)
        elif number == 1:
            self.left_upper_2.configure(state=tkinter.NORMAL)
            self.right_lower_2.configure(state=tkinter.NORMAL)

def switch_to_pirat(widget):
    for i in widget:
        i.grid_remove()
    widget[2].grid(row=4, columnspan=2, sticky="nwe", padx=10, pady=10)
    widget[3].grid(row=6, column=0, columnspan=1, pady=20, padx=20, sticky="we")
    widget[4].grid(row=6, column=1, columnspan=1, pady=20, padx=20, sticky="we")

    widget[-1].grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

def switch_to_walking(widget):
    for i in range(len(widget)):
        if i == 0:
            widget[i].grid(row=1, column=2, pady=10, padx=20, sticky="n")
        elif i == 1:
            widget[i].grid(row=2, column=2, pady=10, padx=20, sticky="n")
        elif i == 2:
            widget[i].grid_remove()
            # widget[i].grid(row=4, column=0, sticky="nwe", padx=5, pady=10)
            # pass
        elif i == 3:
            widget[i].grid_remove()
        elif i == 4:
            widget[i].grid_remove()
        elif i == 5:
            widget[i].grid(row=4, columnspan=2, sticky="nwe", padx=10, pady=10)
        elif i == 6:
            widget[i].grid(row=5, column=0, columnspan=1, pady=20, padx=20, sticky="we")
        elif i == 7:
            widget[i].grid(row=5, column=1, columnspan=1, pady=20, padx=20, sticky="we")
        elif i == 8:
            widget[i].grid(row=6, column=0, pady=20, padx=20, sticky="we")
        elif i == 9:
            widget[i].grid(row=6, column=1, pady=20, padx=20, sticky="we")
        elif i == 10:
            widget[i].grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")
        elif i == 11:
            widget[i].grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")
    widget[-1].grid_remove()

if __name__ == "__main__":
    app = App()
    app.start()