import customtkinter as ctk
from collections import defaultdict

def isPrime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isInteger(number: float | int) -> bool:
    return number % 1 == 0

#-------------------------------------------------#
#                   Interface                     #
#-------------------------------------------------#

class Interface:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry("400x400")
        self.master.resizable(False, False)
        self.master.wm_title("Prime Factoring")

        self.titel = ctk.CTkLabel(self.master, text="Number Prime Factoring", font=("Helvetica bold", 26))
        self.titel.place(relx=0.5, rely= 0.1, anchor="center")
        self.inputbox = ctk.CTkEntry(self.master, width=300, height=50, font=("Helvetica", 18))
        self.inputbox.place(relx=0.5, rely= 0.4, anchor="center")
        self.button = ctk.CTkButton(self.master, text="Calculate Prime Factors", font=("Helvetica bold", 20), command=self.factor)
        self.button.place(relx=0.5, rely= 0.6, anchor="center")
        self.ausgabe_1 = ctk.CTkLabel(self.master, text=" ", font=("Helvetica bold", 20))
        self.ausgabe_1.place(relx=0.5, rely= 0.7, anchor="center")
        self.ausgabe_2 = ctk.CTkLabel(self.master, text=" ", font=("Helvetica bold", 20))
        self.ausgabe_2.place(relx=0.5, rely= 0.78, anchor="center")

        self.master.bind("<Return>", self.factor)


    #-------------------------------------------------#
    #                     Logik                       #
    #-------------------------------------------------#
    
    def factor(self, event=None):
        self.result_1 = " "
        self.result_2 = " "
        self.master.update_idletasks()

        primefactors: list[int] = []
        number = self.inputbox.get()

        try:
            number = int(number)
            if number > 0:
                self.ausgabe_1.configure(text="Calculating...")
                self.master.update_idletasks()

                if isPrime(number):
                    self.result_1 = f"{number} is a prime"
                else:
                    numberCalc = number
                    for factorToTry in range(2, number + 1):
                        while isInteger(numberCalc / factorToTry):
                            primefactors.append(factorToTry)
                            numberCalc = int(numberCalc / factorToTry)
                        if numberCalc == 1:
                            break
                    self.result_1 = " × ".join(map(str, primefactors))

                    # Schreibweise als Produkt von Potezen
                    temp = defaultdict(int)
                    for element in primefactors:
                        temp[element] += 1
                    result = []
                    for prime, power in dict(temp).items():
                        result.append(f"{prime}^{power}")
                    self.result_2 = " × ".join(result)

            else:
                raise ValueError
        except:
            self.result_1 = "Please input a valid positive integer"


        self.ausgabe_1.configure(text=self.result_1)
        self.ausgabe_2.configure(text=self.result_2)


#-------------------------------------------------#
#                 Hauptprogramm                   #
#-------------------------------------------------#

if __name__ == "__main__":
    window = ctk.CTk()
    gui = Interface(master=window)
    window.mainloop()
