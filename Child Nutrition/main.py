from msilib.schema import File
from operator import imod
#Application for Nutrition Value

from tkinter import *
from tkinter import messagebox
import mainfunc

class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("Child Nutrition Application")
        self.switch(Menu)
        self.geometry('650x650')
        self.config(bg = "green")

    #Destroyes the current frame and replace it with what the user have choosed
    def switch(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

#Main Menu
class Menu(Frame):
    def __init__(self, user):
        Frame.__init__(self, user)
        self.config(bg = 'green')

        label = Label(self, text = "Child Nutrition Application Project!\n Please Choose an option."\
                      , bg = "green", fg = "white")
        label.pack()
        button1 = Button(self, text = "Calculator", width = 20, command = lambda: user.switch(Calculator))
        button1.pack(padx = 10, pady = 10)
        button2 = Button(self, text = "Add Product", width = 20, command = lambda: user.switch(Write_File))
        button2.pack()
        button3 = Button(self, text = "Exit", width = 20, command = self.close)
        button3.pack(padx = 10, pady = 10)
    
    #For Closing the Application
    def close(self):
        self.destroy
        exit()

#Nutrition value of the user defined food
class Calculator(Frame):
    def __init__(self, user):
        Frame.__init__(self, user)
        self.config(bg = "green")

        def On_Click(): #Checks the data and then writes the result
            product = entryProduct.get()
            gram = entryGram.get()
            output.delete(0.0, END)

            Error = False
            try:
                gram = int(entryGram.get())
            except:
                Error = True
            try:
                x = int(product)
                Error = True
            except:
                pass
            if Error == True:
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                mainfunc.Open_File()
                output.insert(END, mainfunc.Final_result(product, gram))

        #Frame widgets
        label = Label(self, text ="Enter a product that you ate.", bg = "green", fg = "white")
        label.pack()

        # user input, product
        label2 = Label(self, text = "Name: ", bg = "green", fg = "white")
        label2.pack()
        entryProduct = Entry(self, width = 20, bg = "white")
        entryProduct.pack()

        # user input, amount
        label3 = Label(self, text = "Amount: ", bg = "green", fg = "white")
        label3.pack()
        entryGram = Entry(self, width = 20, bg = "white")
        entryGram.pack()

        # submit
        submit = Button(self, text = "Submit", width = 8, command = On_Click)
        submit.pack(padx = 10, pady = 10)

        # output
        label4 = Label(self, text = "These are the nutrinion values:", bg = "green", fg = "white")
        label4.pack()
        output = Text(self, width = 20, height = 6, wrap = WORD, bg = "white")
        output.pack()

        #going back to menu
        self.button = Button(self, text = "Back", width = 8, command = lambda: user.switch(Menu))
        self.button.pack(padx = 10, pady = 10)

            


class Write_File:
    #User can add new new Products to their Nutrition file
    def __init__(self, user):
        Frame.__init__(self, user)
        self.config(bg = "Green")
        
        #Checks the User Input is correct or not
        def Vali_Date():
            def write(name, kcal, protein, carb, fat): #Writes to the file
                file = open("Product.txt", "a")
                Product_Value = "%s,%s:%s:%s:%s" % (name, kcal, protein, carb, fat)
                file.write("\n", + Product_Value)
                file.close()

                #Emptying the input
                nameEntry.delete(0, END)
                kcalEntry.delete(0, END)
                proteinEntry.delete(0, END)
                carbEntry.delete(0, END)
                fatEntry.delete(0, END)
            error = False

            #Checking if Kcal, protein, carb and fat arer in integer and ProductName is a string
            try:
                name = int(nameEntry.get())
                error = True
            except:
                 name = nameEntry.get()
            try:
                kcal = int(kcalEntry.get())
                protein = int(proteinEntry.get())
                carb = int(carbEntry.get())
                fat = int(fatEntry.get())
            except:
                error = True
            if error == True:
                messagebox.showerror("Error", "Please enter correct data!")
            else:
                #writing the input in the file
                write(name, kcal, protein, carb, fat)

        #Frame widgets
        label = Label(self, text ="Enter the product name and its nutritional "\
                "values per 100 gram", bg = "green", fg = "white")
        label.pack()
        label1 = Label(self, text = "Name:", bg = "green", fg = "white")
        label1.pack()
        nameEntry = Entry(self, width = 20, bg = "white")
        nameEntry.pack()

        label2 = Label(self, text = "Calories:", bg = "green", fg = "white")
        label2.pack()
        kcalEntry = Entry(self, width = 20, bg = "white")
        kcalEntry.pack()

        label3 = Label(self, text = "Protein:", bg = "green", fg = "white")
        label3.pack()
        proteinEntry = Entry(self, width = 20, bg = "white")
        proteinEntry.pack()

        label4 = Label(self, text = "Carbs:", bg = "green", fg = "white")
        label4.pack()
        carbEntry = Entry(self, width = 20, bg = "white")
        carbEntry.pack()

        label5 = Label(self, text = "Fat:", bg = "green", fg = "white")
        label5.pack()
        fatEntry = Entry(self, width = 20, bg = "white")
        fatEntry.pack()

        submit = Button(self, text = "Submit", width = 8, command = Vali_Date)
        submit.pack(padx = 10, pady = 10)

        button3 = Button(self, text = "Back", width = 20, command = lambda: user.switch(Menu))
        button3.pack(padx = 10, pady = 10)

if __name__ == "__main__":
    app = Application()
    app.mainloop()