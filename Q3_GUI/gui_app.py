import tkinter as tk
import client

class MQTT_GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("DHT11 GUI")
        self.root.configure(bg='#b2eff5')

        self.label = tk.Label(self.root, 
                              text="DHT11 GUI", 
                              font=('Courier', 20), 
                              bg='#b2eff5')
        self.label.pack(padx=10, pady=10)

        self.button1 = tk.Button(self.root, 
                                text="Collect & Store", 
                                font=('Terminal', 12), 
                                command = self.collect_store, 
                                bg='#06b9ca', 
                                activebackground='#058d9b', 
                                activeforeground='#fff')
        self.button1.pack(padx=5, pady=5)

        self.checkBox_state = tk.IntVar()
        self.checkBox = tk.Checkbutton(self.root, 
                                       text="Show Entries", 
                                       font=("MS Sans Serif", 12), 
                                       variable=self.checkBox_state, 
                                       bg='#b2eff5', 
                                       activebackground='#b2eff5', 
                                       activeforeground='#000')
        self.checkBox.pack(padx=5, pady=10)

        self.button2 = tk.Button(self.root, 
                                text="Show Database", 
                                font=('Terminal', 12), 
                                command = self.show_DB, 
                                bg='#06b9ca', 
                                activebackground='#058d9b', 
                                activeforeground='#fff')
        self.button2.pack(padx=5, pady=5)

        self.textBox = tk.Text(self.root, 
                               height=8, 
                               font=("MS Sans Serif", 10), 
                               bg='#d2fbff')
        self.textBox.tag_configure("center", justify='center')

        self.root.mainloop()

    def collect_store(self):
        showEntries = self.checkBox_state.get()

        message = client.read_store()
        # message = "Hello"
        if showEntries:
            self.textBox.configure(state='normal')
            self.textBox.delete("1.0", "end")
            self.textBox.insert("1.0", message + '\n', "center")
            self.textBox.configure(state='disabled')
            self.textBox.pack(padx=5, pady=5)
        else:
            self.textBox.configure(state='normal')
            self.textBox.delete("1.0", "end")
            self.textBox.configure(state='disabled')


    def show_DB(self):
        data = client.getDB()

        self.textBox.configure(state='normal')
        self.textBox.delete("1.0", "end")
        if (type(data) == str):
            self.textBox.insert("1.0", data + '\n', "center")
        else:
            for entry in data:
                message = f"ID: {entry['id']} :: Humidity: {entry['humidity']} | Temperature: {entry['temperature']}"
                self.textBox.insert("end", message + '\n', "center")
        self.textBox.configure(state='disabled')
        self.textBox.pack(padx=5, pady=5)

if __name__ == "__main__":
    MQTT_GUI()

