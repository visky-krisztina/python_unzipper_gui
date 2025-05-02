import FreeSimpleGUI as sg
import zipfile

def unzip_archive(arch_file, folder_path):
    with zipfile.ZipFile(arch_file, 'r') as archive:
            archive.extractall(folder_path)

label1 = sg.Text("Select the archived file to unzip: ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key='arch_file')

label2 = sg.Text("Select destination where to unzipp: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key='folder')

unzip_button = sg.Button("UnZipp")
output_label = sg.Text("", key='output_message')

window = sg.Window("File Un-Zipper",
                   layout=[
                       [label1, input1, choose_button1],
                       [label2, input2, choose_button2],
                       [unzip_button, output_label],
                   ])
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "UnZipp":
        arch_file = values['arch_file']
        folder_path = values['folder']

        if not arch_file or not folder_path:
            sg.popup("Please select both a zip file and a destination folder!", font=('Helvetica', 14))
        elif not zipfile.is_zipfile(arch_file):
            sg.popup("The selected file is not a valid zip archive!", font=('Helvetica', 14))
        else:
            try:
                unzip_archive(arch_file, folder_path)
                window['output_message'].update("File unzipped successfully!")
            except Exception as e:
                sg.popup(f"An error occurred: {e}", font=('Helvetica', 14))

window.close()
