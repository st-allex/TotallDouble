import tkinter as tk
from tkinter.ttk import Scrollbar as ttk_Scrollbar, Treeview as ttk_Treeview


class FileViewer(ttk_Treeview):

    heads = ['ind', 'parent_ind', 'file_name', 'type', 'size', 'date', 'attr']  # порядок полей как в загрузке будет

    def __init__(self, hndWnd):
        ttk_Treeview.__init__(self, hndWnd, show='headings')

        self['columns'] = self.heads
        self['displaycolumns'] = ['file_name', 'size', 'date']  # что и как отображаем после сопоставления в цикле

        for header in self.heads:
            self.heading(header, text=header, anchor='w')
            self.column(header) #, anchor='w')

\
    def pack(self):
        viewer_y_scroll = ttk_Scrollbar(self.master, command=self.yview)
        self.configure(yscrollcommand=viewer_y_scroll.set)
        viewer_y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        ttk_Treeview.pack(self, expand=tk.YES, fill=tk.BOTH)

    def set_data(self, data_set):
        par_dict = {0: ''}
        for cur_val in data_set:
            oid = self.insert(par_dict[cur_val[1]], 'end', text=cur_val[2], values=cur_val)  # 'end', text=p, open=False)
            # oid = filePanel.insert(par_dict[0], tk.END, value=cur_val) #'end', text=p, open=False)
            if cur_val[3] == 'folder':
                par_dict[cur_val[0]] = oid