#Henry Forst
#Week 12
#11/21/25
import tkinter 
import tkinter.messagebox 
class CallChargeGUI: 
    def __init__(self): 
        # Create the main window. 
        self.main_window = tkinter.Tk() 
        self.main_window.title("Call Charge Calculator") 
        self.top_frame = tkinter.Frame(self.main_window) 
        self.mid_frame = tkinter.Frame(self.main_window) 
        self.bottom_frame = tkinter.Frame(self.main_window) 
        self.rate_var = tkinter.IntVar() 
        self.rate_var.set(1) 
        # Create the Radiobutton widgets in the top_frame. 
        self.rb_day = tkinter.Radiobutton(self.top_frame, text='Daytime (6:00 A.M. through 5:59 P.M.) $0.02/min', variable=self.rate_var, value=1) 
        self.rb_evening = tkinter.Radiobutton(self.top_frame, text='Evening (6:00 P.M. through 11:59 P.M.) $0.12/min' , variable=self.rate_var, value=2) 
        self.rb_offpeak = tkinter.Radiobutton(self.top_frame, text='Off-Peak (midnight through 5:59 A.M.) $0.05/min', variable=self.rate_var, value=3) # Pack the Radiobuttons. 
        self.rb_day.pack() 
        self.rb_evening.pack() 
        self.rb_offpeak.pack() 
        self.minutes_label = tkinter.Label(self.mid_frame, text="Enter how many minutes:") 
        
        self.minutes_entry = tkinter.Entry(self.mid_frame, width=10) 
        self.minutes_label.pack(side="left") 
        self.minutes_entry.pack(side='left') 
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate Charge', command=self.calculate_charge) 
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy) 
        self.calc_button.pack(side='left', padx=5) 
        self.quit_button.pack(side='left', padx=5) 
        self.top_frame.pack(pady=10) 
        self.mid_frame.pack(pady=10) 
        self.bottom_frame.pack(pady=10) 
        tkinter.mainloop() 
    def calculate_charge(self): 
        try: 
            minutes = float(self.minutes_entry.get()) 
            choice = self.rate_var.get() 
            if choice == 1: 
                rate = 0.02    
            elif choice == 2: 
                rate = 0.12  
            else: 
                rate = 0.05 
            charge = minutes * rate 
            tkinter.messagebox.showinfo('Call charge', f"Total Charge: ${charge:.2f}") 
        except ValueError: tkinter.messagebox.showerror("Error","Enter a valid number of minutes") 
if __name__ == '__main__': 
    CallChargeGUI()