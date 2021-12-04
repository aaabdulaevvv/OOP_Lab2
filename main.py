import PySimpleGUI as sg
import searcher
import xml.etree.ElementTree as xml

sg.theme('GreenTan')
column1 = [
    [sg.Checkbox('Name', size=(20, 1), key="CB_N"), sg.InputText(size=(22, 1), key="IT_N")],
    [sg.Checkbox('Faculty', size=(20, 1), key="CB_Faculty"),
     sg.InputCombo(('Cybernetics', 'Lyceum'), size=(20, 1), key="IC_Faculty")],
    [sg.Checkbox('Department', size=(20, 1), key="CB_Department"),
     sg.InputCombo(('Math', 'Informatics', 'Culture'), size=(20, 1), key="IC_Department")],
    [sg.Checkbox('Material', size=(20, 1), key="CB_Material"), sg.InputText(size=(22, 1), key="IC_Material")],
    [sg.Checkbox('Material type', size=(20, 1), key="CB_MaterialT"),
     sg.InputCombo(('Report', 'Project', 'Essay', 'Dissertation', 'Article', 'Tutorial'), size=(20, 1), key="IC_MaterialT")],
    [sg.Checkbox('Number of Pages', size=(20, 1), key="CB_Extent"), sg.InputText(size=(8, 1), key="IC_Extent1"), sg.Text('to'), sg.InputText(size=(8, 1), key="IC_Extent2")],
    [sg.Checkbox('Date (dd.mm.yyyy)', size=(20, 1), key="CB_Date"), sg.InputText(size=(22, 1), key="IC_Date")],
    [sg.Radio('DOM', "Radio1", size=(20, 1), key='R_DOM'), sg.Radio('SAX', "Radio1", default=True, key='R_SAX')],
    [sg.Button('Search', size=(20, 1), key='B_Search'), sg.Button('Convert to HTML', size=(21, 1), key='B_HTML')]
]

layout = [[sg.Column(column1), sg.Multiline(size=(50, 15), key='ML_SearchRes')]]
window = sg.Window('Second Lab', layout, default_element_size=(50, 1), grab_anywhere=False)

while True:
    event, values = window.read()
    filter = {}
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "B_Search":
        if values['CB_N']:
            filter['Name'] = values['IT_N']
        if values['CB_Faculty']:
            filter['Faculty'] = values['IC_Faculty']
        if values['CB_Department']:
            filter['Department'] = values['IC_Department']
        if values['CB_Material']:
            filter['Material'] = values['IC_Material']
        if values ['CB_MaterialT']:
            filter['MaterialT'] = values['IC_MaterialT']
        if values['CB_Extent']:
            filter['Extent'] = values['IC_Extent1'], values['IC_Extent2']
        if values['CB_Date']:
            filter['Date'] = values['IC_Date']
        if values['R_DOM'] or values['R_SAX']:
            teachers = searcher.search('mydata.xml', (searcher.DOM_Searcher() if values['R_DOM'] else searcher.SAX_Searcher()), filter)
            window['ML_SearchRes'].update('')
            for teacher in teachers:
                window['ML_SearchRes'].write('Name: ' + teacher.Name + '\n')
                window['ML_SearchRes'].write('Faculty: ' + teacher.Faculty + '\n')
                window['ML_SearchRes'].write('Department: ' + teacher.Department + '\n')
                window['ML_SearchRes'].write('Material: ' + teacher.Material + '\n')
                window['ML_SearchRes'].write('Material Type: ' + teacher.MaterialT + '\n')
                window['ML_SearchRes'].write('Number of Pages: ' + teacher.Extent + '\n')
                window['ML_SearchRes'].write('Date: ' + teacher.Date + '\n\n')

    elif event == 'B_HTML':
        searcher.transform()


window.close()
