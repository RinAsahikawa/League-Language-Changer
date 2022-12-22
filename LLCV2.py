from tkinter import *
import tkinter as tk
import subprocess

language_map = {
    "Japanese": "ja_JP",
    "Korean": "ko_KR",
    "English": "en_GB",
    "Chinese (Traditional)": "zh_TW",
    "Chinese (Simplified)": "zh_CN",
    "Czech": "cz_CZ",
    "German": "de_DE",
    "Greek": "el_GR",
    "Spanish": "es_ES",
    "French": "fr_FR",
    "Hungarian": "hu_HU",
    "Italian": "it_IT",
    "Polish": "pl_PL",
    "Portuguese": "pt_BR",
    "Romanian": "ro_RO",
    "Russian": "ru_RU",
    "Turkish": "tr_TR",
}

my_list = ['Chinese (Traditional)', 
        'Chinese (Simplified)', 
        'Czech', 
        'English', 
        'French', 
        'German', 
        'Greek', 
        'Hungarian', 
        'Italian', 
        'Japanese', 
        'Korean', 
        'Polish', 
        'Portuguese', 
        'Romanian', 
        'Russian', 
        'Spanish', 
        'Turkish']

def quit():
    window.quit()

def dal():
    active_language = l1.get('active')
    language = language_map.get(active_language)

    with open("C:\Riot Games\League of Legends\system.yaml", "r") as f:
        lines = f.readlines()

    lines[167] = f"    - {language}\n"
    lines[172] = f"    default_locale: {language}\n"

    with open("C:\Riot Games\League of Legends\system.yaml", "w") as f:
        f.writelines(lines)

    with open("C:\Riot Games\League of Legends\Config\LeagueClientSettings.yaml", "r") as f:
        lines = f.readlines()

        lines[12] = f"        locale: {language}\n"

    with open("C:\Riot Games\League of Legends\Config\LeagueClientSettings.yaml", "w") as f:
        f.writelines(lines)

    subprocess.run(
        r"C:\Riot Games\League of Legends\LeagueClient.exe", check=True
    )

window = tk.Tk()
window.title("Language Selection")
window.resizable(False,False)
window.geometry("300x200")
window.rowconfigure([0, 1], minsize=5, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)

l1=tk.Label(window,text='Language List "Scrollable"')
l1.grid(row=0,column=0,columnspan=1,pady=0)

vscroll=tk.Scrollbar(window, orient=VERTICAL)
vscroll.grid(row=1, column=2, sticky=N+S)

l1 = tk.Listbox(window,height=7, yscrollcommand=vscroll.set)
l1.grid(row=1,column=0,padx=20,pady=20) 

Scrollbar
vscroll.config(command=l1.yview)

for element in my_list: # adding elements to Listbox
    l1.insert(tk.END,element)

selectbutton=Button(window, text="Select", command=lambda:[dal(),quit()])
selectbutton.grid(row=1, column=1)

mainloop()