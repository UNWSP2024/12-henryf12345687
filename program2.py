#Henry Forst
#Week 12
#11/21/25
import tkinter
import tkinter.messagebox

class AutomotiveGUI:
    def __init__(self):
      
        self.main_window = tkinter.Tk()
        self.main_window.title("Joe's Automotive")
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
          
        self.cb_vars = [tkinter.IntVar() for _ in range(7)]
        self.services = [  
            ("Oil Change" , 30.00),
            ("Lube Job" , 20.00),
            ("Radiator Flush" , 40.00),
            ("Transmission Fluid" , 100.00),
            ("Inspection" , 35.00),
            ("Muffler replacement" , 200.00),
            ("Tire Rotation" , 20.00)
        ]


        for i, (service, price) in enumerate(self.services):
            cb = tkinter.Checkbutton(
                  self.top_frame,
                  text=f"{service} - ${price:.2f}",
                  variable=self.cb_vars[i]
            )
            cb.pack()



        
 
    
        self.calc_button = tkinter.Button(self.bottom_frame,
                                           text='Calculate Total',
                                           command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                            text='Quit',
                                            command=self.main_window.destroy)
        self.calc_button.pack(side='left', padx=5)
        self.quit_button.pack(side='left', padx=5)
        self.top_frame.pack(pady=10)
        self.bottom_frame.pack(pady=10)
        tkinter.mainloop()
    def show_choice(self):
        total = 0
        message = "You Selected: \n"
        for i, (service, price) in enumerate(self.services):
            if self.cb_vars[i].get()== 1:
                total += price
                message += service + "\n"
        if total > 0:
            message += f"\nTotal Charges: ${total:.2f}"
        else:
            message = "None"

        
        tkinter.messagebox.showinfo('Total Services ', message)
 
   # Create an instance of the MyGUI class.
if __name__ == '__main__':
    AutomotiveGUI()