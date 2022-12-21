from tkinter import *
import tkinter as tk

#scroller
window = tk.Tk()
window.title("Language Selection")
window.geometry("300x200")

window.rowconfigure([0, 1], minsize=5, weight=1)
window.columnconfigure([0, 1], minsize=50, weight=1)

l1=tk.Label(window,text='Language List')
l1.grid(row=0,column=0,columnspan=1,pady=0)

def close():
    window.quit()

def swap():
    if l1.get('active') == "Japanese":
        language = "ja_JP"
    elif l1.get('active') == "Korean":
        language = "ko_KR"
    elif l1.get('active') == "English":
        language = "en_GB"
    elif l1.get('active') == "Chinese (Traditional)":
        language = "zh_TW"
    elif l1.get('active') == "Chinese (Simplified)":
        language = "zh_CN"
        
    def Run():
        line_num1 = 167
        line_num2 = 172
        line_num3 = 12

        def replace_line(file_name, line_num, text):
            lines = open(file_name, 'r').readlines()
            lines[line_num] = text
            out = open(file_name, 'w')
            out.writelines(lines)
            out.close()
        replace_line("C:\Riot Games\League of Legends\system.yaml", line_num1, '    - {}\n'.format(language))
        replace_line("C:\Riot Games\League of Legends\system.yaml", line_num2, '    default_locale: {}\n'.format(language))
            
        def replace_line2(file_name, line_num, text):
            lines = open(file_name, 'r').readlines()
            lines[line_num] = text
            out = open(file_name, 'w')
            out.writelines(lines)
            out.close()
        replace_line2("C:\Riot Games\League of Legends\Config\LeagueClientSettings.yaml", line_num3, '        locale: {}\n'.format(language))
    
        import sys, string, os
        os.popen(r"C:\Riot Games\League of Legends\LeagueClient.exe")

    Run()

selectbutton=Button(window, text="Select", command=lambda:[swap(),close()])
selectbutton.grid(row=1, column=1)

my_list=["Japanese", "Korean", "English", "Chinese (Traditional)", "Chinese (Simplified)"]
l1 = tk.Listbox(window,height=5) #, yscrollcommand = sb.set)
l1.grid(row=1,column=0,padx=20,pady=20) 

for element in my_list: # adding elements to Listbox
    l1.insert(tk.END,element)

#sb.config( command = l1.yview )

mainloop()