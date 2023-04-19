import tkinter as tk
import DHT11_MQTT_Subscribe

class MQTT_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("DHT11 MQTT Subscribe")
        self.root.configure(bg='#b2eff5')

        self.label = tk.Label(self.root, 
                              text="DHT11 MQTT Subscribe", 
                              font=('Courier', 20), 
                              bg='#b2eff5')
        self.label.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, 
                                text="Subscribe", 
                                font=('Terminal', 12), 
                                command = self.subscribe, 
                                bg='#06b9ca', 
                                activebackground='#058d9b', 
                                activeforeground='#fff')
        self.button.pack(padx=5, pady=5)

        self.checkBox_state = tk.IntVar()
        self.checkBox = tk.Checkbutton(self.root, 
                                       text="Show Latest!", 
                                       font=("MS Sans Serif", 12), 
                                       variable=self.checkBox_state, 
                                       bg='#b2eff5', 
                                       activebackground='#b2eff5', 
                                       activeforeground='#000')
        self.checkBox.pack(padx=5, pady=10)

        self.textBox = tk.Text(self.root, 
                               height=8, 
                               font=("MS Sans Serif", 10), 
                               bg='#d2fbff')
        self.textBox.tag_configure("center", justify='center')

        self.root.mainloop()

    def subscribe(self):
        showLatest = self.checkBox_state.get()

        message = DHT11_MQTT_Subscribe.mqtt_subscribe()
        # message = "Hello"
        if not showLatest:
            self.textBox.configure(state='normal')
            self.textBox.insert("1.0", message + '\n', "center")
            self.textBox.configure(state='disabled')
            self.textBox.pack(padx=5, pady=5)
        else:
            self.textBox.configure(state='normal')
            self.textBox.delete("1.0", "end")
            self.textBox.insert("1.0", message + '\n', "center")
            self.textBox.configure(state='disabled')
            self.textBox.pack(padx=5, pady=5)

if __name__ == "__main__":
    MQTT_GUI()

