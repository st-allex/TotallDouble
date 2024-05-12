import tkinter as tk
import GUI_FilePanel

fst = [
        (1, 0, 'folder0', 'folder', '', '', '----'),
        (2, 1, 'folder0_folder1', 'folder', '', '', '----'),
        (3, 1, 'folder0_folder2', 'folder', '', '', '----'),
        (4, 1, 'folder0_file1', 'file', '1000', '21.12.2012', '-a--'),
        (5, 1, 'folder0_file2', 'file', '100', '21.12.2012', '-a--'),
        (6, 2, 'folder1_file1', 'file', '1020', '21.12.2012', '-a--')
    ]


root = tk.Tk()

test = GUI_FilePanel.FileViewer(root)
test.set_data(fst)
test.pack()

root.mainloop()