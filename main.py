# run: sudo python3.8 main.py

import tkinter
import tkinter.messagebox
import customtkinter
# import sys
import time
import keyboard

import pytesseract
from PIL import ImageGrab

# customtkinter.ScalingTracker.set_user_scaling(0.5)
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

def detection_digits(first_x, first_y, second_x, second_y, seconds_delay = 5, third_x = 0, third_y = 0, fourth_x = 0, fourth_y=0):
    # Test
    print("Start")
    time.sleep(seconds_delay)
    counter = 0
    if third_x == third_y == fourth_x == fourth_y ==0:
        while True:
            # This instance will generate an image from
            # the point of (1308, 263) and (1405, 277) in format of (x, y)
            cap_1 = ImageGrab.grab(bbox=(first_x, first_y, second_x, second_y), all_screens=True)
            # cap_1 = ImageGrab.grab(bbox=(2617, 525, 2695, 555), all_screens=True)

            # cap_2 = ImageGrab.grab(bbox=(2733, 525, 2807, 555), all_screens=True)

            text_1 = pytesseract.image_to_string(cap_1, lang='eng',
                                                 config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            # text_2 = pytesseract.image_to_string(cap_2, lang='eng',
            #                                      config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

            # text = text_1 + " " + text_2
            text = text_1

            if len(text) > 0:
                if 2100 < int(text) < 2160:
                    keyboard.press(2) # w - 13, a - 0, s - 1, d-2
                    print(text)
            else:
                print("Nothing")

            if keyboard.is_pressed("space"):
                break
    else:
        while True:
            # This instance will generate an image from
            # the point of (1308, 263) and (1405, 277) in format of (x, y)
            cap_1 = ImageGrab.grab(bbox=(first_x, first_y, second_x, second_y), all_screens=True)
            # cap_1 = ImageGrab.grab(bbox=(2617, 525, 2695, 555), all_screens=True)

            # cap_2 = ImageGrab.grab(bbox=(2733, 525, 2807, 555), all_screens=True)
            cap_2 = ImageGrab.grab(bbox=(third_x, third_y, fourth_x, fourth_y), all_screens=True)

            text_1 = pytesseract.image_to_string(cap_1, lang='eng',
                                                 config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            text_2 = pytesseract.image_to_string(cap_2, lang='eng',
                                                 config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')


            if len(text_1) > 0:
                if 2100 < int(text_1) < 2160:
                    # keyboard.press(2)  # w - 13, a - 0, s - 1, d-2
                    print(text_1+text_2)
            else:
                print("Nothing")

            # if len(text_2) > 0:
            #     if 3100 < int(text_2) < 3400:
            #         keyboard.press(2)  # w - 13, a - 0, s - 1, d-2
            #         print(text_2)
            # else:
            #     print("Nothing")

            if keyboard.is_pressed("space"):
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
                                                   text="Kosmak: Запуск - Начать,\n" +
                                                        "Остановить - пробел,\n" +
                                                        "Начинать с правого нижнего края",
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

        self.label_info_4 = customtkinter.CTkLabel(master=self.frame_right,
                                                   text="Задержка перед запуском \n" +
                                                        "(по умолчанию 5 сек.)",
                                                   height=20,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   # justify=tkinter.LEFT)
                                                   )
        self.label_info_4.grid(row=6, column=2, sticky="we", padx=20, pady=15)

        self.seconds_delay = customtkinter.CTkEntry(master=self.frame_right,
                                                    width=20,
                                                    placeholder_text="Число секунд")
        self.seconds_delay.grid(row=7, column=2, pady=10, padx=20, sticky="we")

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
                                            placeholder_text="Левый верх X (1)")
        self.left_upper_1.grid(row=5, column=0, columnspan=1, pady=20, padx=20, sticky="we")

        self.right_lower_1 = customtkinter.CTkEntry(master=self.frame_right,
                                              width=30,
                                              placeholder_text="Левый верх Y (1)")
        self.right_lower_1.grid(row=5, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.left_upper_2 = customtkinter.CTkEntry(master=self.frame_right,
                                                   width=20,
                                                   placeholder_text="Правый низ X (1)")
        self.left_upper_2.grid(row=6, column=0, pady=20, padx=20, sticky="we")

        self.right_lower_2 = customtkinter.CTkEntry(master=self.frame_right,
                                                    width=20,
                                                    placeholder_text="Правый низ Y (1)")
        self.right_lower_2.grid(row=6, column=1, pady=20, padx=20, sticky="we")

        self.left_upper_3 = customtkinter.CTkEntry(master=self.frame_right,
                                                    width=20,
                                                    placeholder_text="Левый верх X (2)")
        self.left_upper_3.grid(row=7, column=0, pady=10, padx=20, sticky="we")

        self.right_lower_3 = customtkinter.CTkEntry(master=self.frame_right,
                                                    width=20,
                                                    placeholder_text="Левый верх Y (2)")
        self.right_lower_3.grid(row=7, column=1, pady=10, padx=20, sticky="we")

        self.left_upper_4 = customtkinter.CTkEntry(master=self.frame_right,
                                                   width=20,
                                                   placeholder_text="Правый низ X (2)")
        self.left_upper_4.grid(row=8, column=0, pady=10, padx=20, sticky="we")

        self.right_lower_4 = customtkinter.CTkEntry(master=self.frame_right,
                                                    width=20,
                                                    placeholder_text="Правый низ Y (2)")
        self.right_lower_4.grid(row=8, column=1, pady=10, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Начать",
                                                command=self.button_event)
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        self.button_7 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Возникла проблема",
                                                fg_color='red',
                                                state=tkinter.DISABLED)
                                                # command=self.button_event)

        self.button_6 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Запустить",
                                                command=self.button_event)

        # set default values
        self.radio_button_1.select()
        self.switch_2.select()
        self.left_upper_3.configure(state=tkinter.DISABLED)
        self.right_lower_3.configure(state=tkinter.DISABLED)
        self.left_upper_4.configure(state=tkinter.DISABLED)
        self.right_lower_4.configure(state=tkinter.DISABLED)
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
                           self.button_5, self.label_radio_group, self.left_upper_3, self.right_lower_3,
                           self.left_upper_4, self.right_lower_4, self.seconds_delay,self.label_info_4,
                           self.button_6]


    def button_event(self):
        print("Кнопка нажата")
        # self.button_5.grid_remove()
        self.button_7.grid_remove()
        self.button_7.grid(row=4, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        if self.left_upper_3.state==tkinter.DISABLED and self.right_lower_3.state == tkinter.DISABLED and self.left_upper_4.state==tkinter.DISABLED and self.right_lower_4.state == tkinter.DISABLED:
            if self.left_upper_1.get() != "" and self.right_lower_1.get() != "" and self.left_upper_2.get() != "" and self.right_lower_2.get() != "":
                try:
                    left_up_1 = float(self.left_upper_1.get())
                    right_down_1 = float(self.right_lower_1.get())
                    left_up_2 = float(self.left_upper_2.get())
                    right_down_2 = float(self.right_lower_2.get())
                    left_up_3 = 0
                    right_down_3 = 0
                    left_up_4 = 0
                    right_down_4 = 0
                    if self.seconds_delay.get() != "":
                        seconds_timer = int(self.seconds_delay.get())
                    else:
                        seconds_timer = 4
                    # 2617, 525, 2695, 555
                    self.button_7.grid_remove()
                    print(detection_digits(left_up_1, right_down_1, left_up_2, right_down_2, seconds_timer, left_up_3, right_down_3, left_up_4, right_down_4))
                    # print("Ok")

                except ValueError:
                    print("Ошибка в 1 координате")
            else:
                print("gg")
            # print(self.left_upper_1.get())
        else:
            if self.left_upper_1.get() != "" and self.right_lower_1.get() != "" and self.left_upper_2.get() != "" and self.right_lower_2.get() != "" and self.left_upper_3.get() != "" and self.right_lower_3.get() != "" and self.left_upper_4.get() != "" and self.right_lower_4.get() != "":
                try:
                    left_up_1 = float(self.left_upper_1.get())
                    right_down_1 = float(self.right_lower_1.get())
                    left_up_2 = float(self.left_upper_2.get())
                    right_down_2 = float(self.right_lower_2.get())
                    left_up_3 = float(self.left_upper_3.get())
                    right_down_3 = float(self.right_lower_3.get())
                    left_up_4 = float(self.left_upper_4.get())
                    right_down_4 = float(self.right_lower_4.get())
                    if self.seconds_delay.get() != "":
                        seconds_timer = int(self.seconds_delay.get())
                    else:
                        seconds_timer = 4
                    # (2733, 525, 2807, 555)

                    self.button_7.grid_remove()
                    print(detection_digits(left_up_1, right_down_1, left_up_2, right_down_2, seconds_timer, left_up_3,
                                           right_down_3, left_up_4, right_down_4))
                except:
                    print("Ошибка в 2-х координатах")
        # print(self.right_lower_1.get())

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
            self.left_upper_3.configure(state=tkinter.DISABLED)
            self.right_lower_3.configure(state=tkinter.DISABLED)
            self.left_upper_4.configure(state=tkinter.DISABLED)
            self.right_lower_4.configure(state=tkinter.DISABLED)
        elif number == 1:
            self.left_upper_3.configure(state=tkinter.NORMAL)
            self.right_lower_3.configure(state=tkinter.NORMAL)
            self.left_upper_4.configure(state=tkinter.NORMAL)
            self.right_lower_4.configure(state=tkinter.NORMAL)

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
        elif i == 12:
            widget[i].grid(row=7, column=0, pady=10, padx=20, sticky="we")
        elif i == 13:
            widget[i].grid(row=7, column=1, pady=10, padx=20, sticky="we")
        elif i == 14:
            widget[i].grid(row=8, column=0, pady=10, padx=20, sticky="we")
        elif i == 15:
            widget[i].grid(row=8, column=1, pady=10, padx=20, sticky="we")
        elif i == 16:
            widget[i].grid(row=7, column=2, pady=10, padx=20, sticky="we")
        elif i == 17:
            widget[i].grid(row=6, column=2, sticky="we", padx=20, pady=15)
    widget[-1].grid_remove()

if __name__ == "__main__":
    app = App()
    app.start()