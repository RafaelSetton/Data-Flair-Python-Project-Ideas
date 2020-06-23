from tkinter import Tk, Button, Label, DISABLED, NORMAL
from time import sleep
from winsound import Beep
from threading import Thread


class CountDown:
    def __init__(self):

        self.stop_thread = False
        self.hup = None
        self.hdo = None
        self.mup = None
        self.mdo = None
        self.sup = None
        self.sdo = None
        self.hours = None
        self.minutes = None
        self.seconds = None
        self.st_btn = None

        self.janela = Tk(screenName="CountDown")
        self.janela.title("CountDown")
        self.janela['bg'] = '#122288'
        self.janela.geometry("235x120+1000+100")

        Label(self.janela, text='', width=10, height=2, background='#122288').grid(row=0, column=0)

        self.hour()
        self.minute()
        self.second()
        self.start_stop_button()
        self.__disable()

        self.janela.mainloop()

    def __time_adjust(self, first_row, column):
        up = Button(self.janela, text="△", height=1, command=lambda: self.__up(main), bg='#221277')
        up.grid(row=first_row, column=column)

        main = Label(self.janela, text='00', font=50, height=2, background='#122266', foreground='#ffffff')
        main.grid(row=first_row+1, column=column)

        down = Button(self.janela, text="▽", height=1, command=lambda: self.__down(main), bg='#221277')
        down.grid(row=first_row+2, column=column)

        return up, main, down

    def __disable(self):
        if self.seconds['text'] == '00':
            self.sdo['state'] = DISABLED
        elif self.seconds['text'] == '59':
            self.sup['state'] = DISABLED
        else:
            self.sup['state'] = NORMAL
            self.sdo['state'] = NORMAL

        if self.minutes['text'] == '00':
            self.mdo['state'] = DISABLED
        elif self.minutes['text'] == '59':
            self.mup['state'] = DISABLED
        else:
            self.mup['state'] = NORMAL
            self.mdo['state'] = NORMAL

        if self.hours['text'] == '00':
            self.hdo['state'] = DISABLED
        elif self.hours['text'] == '99':
            self.hup['state'] = DISABLED
        else:
            self.hup['state'] = NORMAL
            self.hdo['state'] = NORMAL

        if self.hours['text'] == self.minutes['text'] == self.seconds['text'] == '00':
            self.st_btn['state'] = DISABLED
        else:
            self.st_btn['state'] = NORMAL

    def __up(self, obj, disable=True):
        obj['text'] = str(int(obj['text']) + 1).zfill(2)
        if disable:
            self.__disable()

    def __down(self, obj, disable=True):
        obj['text'] = str(int(obj['text']) - 1).zfill(2)
        if disable:
            self.__disable()

    def __start(self):
        self.hup['state'] = DISABLED
        self.hdo['state'] = DISABLED
        self.mup['state'] = DISABLED
        self.mdo['state'] = DISABLED
        self.sup['state'] = DISABLED
        self.sdo['state'] = DISABLED
        self.st_btn['text'] = "Stop"
        self.st_btn['command'] = self.__stop

        def loop():
            while True:
                if self.stop_thread:
                    break
                sleep(1)
                if self.seconds['text'] != '00':
                    self.__down(self.seconds, False)
                elif self.minutes['text'] != '00':
                    self.__down(self.minutes, False)
                    self.seconds['text'] = '59'
                elif self.hours['text'] != '00':
                    self.__down(self.hours, False)
                    self.minutes['text'] = '59'
                    self.seconds['text'] = '59'
                else:
                    for _ in range(5):
                        Beep(frequency=800, duration=500)
                        Beep(frequency=500, duration=500)
                    break

            self.hours['text'] = '00'
            self.minutes['text'] = '00'
            self.seconds['text'] = '00'

            self.hup['state'] = NORMAL
            self.mup['state'] = NORMAL
            self.sup['state'] = NORMAL
            self.st_btn['state'] = DISABLED

            self.st_btn['text'] = "Start"
            self.st_btn['command'] = self.__start
            self.stop_thread = False

        Thread(target=loop).start()

    def __stop(self):
        self.stop_thread = True

    def hour(self):
        self.hup, self.hours, self.hdo = self.__time_adjust(0, 1)

    def minute(self):
        self.mup, self.minutes, self.mdo = self.__time_adjust(0, 2)

    def second(self):
        self.sup, self.seconds, self.sdo = self.__time_adjust(0, 3)

    def start_stop_button(self):
        self.st_btn = Button(self.janela, text="Start", height=1, width=4,
                             command=self.__start,
                             bg='#4444cc', state=DISABLED)
        self.st_btn.grid(row=1, column=4)


CountDown()
