import PySimpleGUI as sg
import pickle
import os

#os.chdir('/scratch/e/esargent/mxyptlkr/nlp/NLP/new_process')

with open('total_data.pkl','rb') as f:
    total_data = pickle.load(f)

for lkey in total_data.keys():
    for i in range(0,len(total_data[lkey])):
        if (total_data[lkey][i][2] < 0):
            para_no = 'Paragraph no: '+ str(i)
            layout = [[sg.Text(para_no)], [sg.Text(total_data[lkey][i][0],size=(50,30),font=('Arial',14))],[sg.Yes('Synthesis'),sg.No('Not Synthesis')]]
            window = sg.Window('NLP project desperately needs your help! Thanks for your time!').Layout(layout)
            event = window.Read()
            window.Close()
            if event[0] is None or event[0] == 'Exit':
                break
            else:
                total_data[lkey][i][2] = 1
            print(event)
            if (event[0]=='Synthesis'):
                total_data[lkey][i][1] = True
    else:
    
        continue
        
    break

with open('total_data.pkl','wb') as f:
    total_data = pickle.dump(total_data,f)
