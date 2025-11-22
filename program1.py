#Henry Forst
#Week 12
#11/21/25
import tkinter 
class MpgCalculatorGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('MPG Calculator')
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.gallon_label = tkinter.Label(self.top_frame, 
                      text='Enter the number of gallons your car holds:')
        self.gallon_entry = tkinter.Entry(self.top_frame, 
                                           width=10)
        self.miles_label = tkinter.Label(self.mid_frame, 
                      text='How many miles can be driven on a full tank:')
        self.miles_entry = tkinter.Entry(self.mid_frame, 
                                           width=10)
             
        self.gallon_label.pack(side='left')
        self.gallon_entry.pack(side='left')
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        self.value = tkinter.StringVar()

    
        self.result_label = tkinter.Label(self.mid_frame, 
                             textvariable=self.value)
 
        
        
 
         
        self.calc_button = tkinter.Button(self.bottom_frame, 
                                             text='Calculate MPG', 
                                             command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, 
                                             text='Quit', 
                                            command=self.main_window.destroy)

        
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.result_label.pack(side='left')
        # Pack the frames.
        self.top_frame.pack(pady=5)
        self.mid_frame.pack(pady=5)
        self.bottom_frame.pack(pady=10)
        tkinter.mainloop()
    def convert(self):
        try:
            gallons = float(self.gallon_entry.get())
            miles = float(self.miles_entry.get())
            if gallons <= 0:
                self.value.set("Gallons must be greater than 0")
            else:
                mpg = miles /  gallons
                self.value.set(f"MPG: {mpg:.2f}")
        except ValueError:
            self.value.set("Enter valid numbers")
if __name__ == '__main__':
    mpg_calculator = MpgCalculatorGUI()