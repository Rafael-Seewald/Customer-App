from modulos import *
from reports import Reports
from functionalities import Functions

class Application(Functions, Reports):
    def __init__(self):
        self.root = root
        self.colors()
        self.window()
        self.frames()
        self.widgetsFrame1()
        self.listFrame_2()
        self.createTables()
        self.selectList() 
        self.menus()
        root.mainloop()

    def colors(self):
        # COLORS
        self.primary = '#4d4b4b'
        self.secondary = '#272727'
        self.activebtn = '#7173c9'

    def window(self):
        self.root.title('Cadastro de pessoas')
        self.root.configure(background='#1a1919')
        self.root.minsize(width=900, height=600)

    def frames(self):
        self.frame_1 = Frame(self.root, bd=4, bg=self.secondary,
                             highlightbackground=self.primary, highlightthickness=3)
        self.frame_1.place(relx=0.03, rely=0.035, relwidth=0.94, relheight=0.40)

        self.frame_2 = Frame(self.root, bd=4, bg=self.secondary,
                             highlightbackground=self.primary, highlightthickness=3)
        self.frame_2.place(relx=0.03, rely=0.48, relwidth=0.94, relheight=0.48)

        self.sizegrip = ttk.Sizegrip(self.root)

    def widgetsFrame1(self):
        # Color outside the button
        self.canvas_bt1 = Canvas(self.frame_1, bd=0, bg='#383863',
                                 highlightbackground='gray', highlightthickness=2)
        self.canvas_bt1.place(relx=0.165, rely=0.066, relwidth=0.238, relheight=0.21)

        self.canvas_bt2 = Canvas(self.frame_1, bd=0, bg='#383863',
                                 highlightbackground='gray', highlightthickness=2)
        self.canvas_bt2.place(relx=0.605, rely=0.066, relwidth=0.379, relheight=0.21)

        self.canvas_bt3 = Canvas(self.frame_1, bd=0, bg='#383863',
                                 highlightbackground='gray', highlightthickness=2)
        self.canvas_bt3.place(relx=0.645, rely=0.34, relwidth=0.097, relheight=0.21)

        # BUTTONS
        self.bt_clean = Button(self.frame_1, bg=self.primary, bd=4, activebackground=self.activebtn,
                               activeforeground='white', font=('verdana', 9, 'bold'), text='Limpar',
                               command=self.cleanClient, cursor='hand2', fg='white')
        self.bt_clean.place(relx=0.18, rely=0.096, relwidth=0.1, relheight=0.15)

        self.bt_search = Button(self.frame_1, bg=self.primary, bd=4, activebackground=self.activebtn,
                                activeforeground='white', font=('verdana', 9, 'bold'), text='Buscar',
                                command=self.searchClient, cursor='hand2', fg='white')
        self.bt_search.place(relx=0.29, rely=0.096, relwidth=0.1, relheight=0.15)

        self.bt_add = Button(self.frame_1, bg=self.primary, bd=4, activebackground=self.activebtn,
                             activeforeground='white', font=('verdana', 9, 'bold'), text='Adicionar',
                             command=self.add, cursor='hand2', fg='white')
        self.bt_add.place(relx=0.62, rely=0.096, relwidth=0.12, relheight=0.15)

        self.bt_edit = Button(self.frame_1, bg=self.primary, bd=4, activebackground=self.activebtn,
                              activeforeground='white', font=('verdana', 9, 'bold'), text='Editar',
                              command=self.editClient, cursor='hand2', fg='white')
        self.bt_edit.place(relx=0.75, rely=0.096, relwidth=0.1, relheight=0.15)

        self.bt_remove = Button(self.frame_1, bg=self.primary, bd=4, activebackground=self.activebtn,
                                activeforeground='white', font=('verdana', 9, 'bold'), text='Remover',
                                command=self.deleteClient, cursor='hand2', fg='white')
        self.bt_remove.place(relx=0.86, rely=0.096, relwidth=0.11, relheight=0.15)

        self.bt_CEP = Button(self.frame_1, bg=self.primary, bd=4, activebackground=self.activebtn,
                             activeforeground='white', font=('verdana', 9, 'bold'), text='CEP',
                             command=self.cepFunc, cursor='hand2', fg='white')
        self.bt_CEP.place(relx=0.66, rely=0.37, relwidth=0.07, relheight=0.15)

        balloon_text = f'Digite no campo nome: % e o que lembra do nome do cliente'
        
        self.search_balloon = Balloon(self.frame_1)
        self.search_balloon.bind_widget(self.bt_search, balloonmsg=balloon_text)

        # CONFIG HOVER BUTTON
        def on_hover(event):
            event.widget.configure(bg='#6263b6')

        def on_default(event):
            event.widget.configure(bg=self.primary)

        self.bt_clean.bind('<Enter>', on_hover)
        self.bt_clean.bind('<Leave>', on_default)
        self.bt_search.bind('<Enter>', on_hover)
        self.bt_search.bind('<Leave>', on_default)
        self.bt_add.bind('<Enter>', on_hover)
        self.bt_add.bind('<Leave>', on_default)
        self.bt_edit.bind('<Enter>', on_hover)
        self.bt_edit.bind('<Leave>', on_default)
        self.bt_remove.bind('<Enter>', on_hover)
        self.bt_remove.bind('<Leave>', on_default)
        self.bt_CEP.bind('<Enter>', on_hover)
        self.bt_CEP.bind('<Leave>', on_default)

        # LABELS and ENTRIES
        # ID code
        self.lb_code = Label(self.frame_1, text='Código', bg=self.secondary,
                             fg='white', font=('verdana', 11))
        self.lb_code.place(relx=0.0275, rely=0.01, relwidth=0.1, relheight=0.08)

        self.entry_code = Entry(self.frame_1, font=('verdana', 13))
        self.entry_code.place(relx=0.036, rely=0.11, relwidth=0.1, relheight=0.11)

        # name
        self.lb_name = Label(self.frame_1, text='Nome', bg=self.secondary,
                             fg='white', font=('verdana', 11))
        self.lb_name.place(relx=0.024, rely=0.27, relwidth=0.1, relheight=0.08)

        self.entry_name = Entry(self.frame_1, font=('verdana', 13))
        self.entry_name.place(relx=0.036, rely=0.37, relwidth=0.57, relheight=0.11)

        # phone number
        self.lb_phone = Label(self.frame_1, text='Telefone', bg=self.secondary,
                              fg='white', font=('verdana', 11))
        self.lb_phone.place(relx=0.031, rely=0.51, relwidth=0.1, relheight=0.08)

        self.entry_phone = Entry(self.frame_1, font=('verdana', 13))
        self.entry_phone.place(relx=0.036, rely=0.61, relwidth=0.4, relheight=0.11)

        # city
        self.lb_city = Label(self.frame_1, text='Cidade', bg=self.secondary,
                             fg='white', font=('verdana', 11))
        self.lb_city.place(relx=0.487, rely=0.51, relwidth=0.1, relheight=0.08)

        self.entry_city = Entry(self.frame_1, font=('verdana', 13))
        self.entry_city.place(relx=0.5, rely=0.61, relwidth=0.4, relheight=0.11)

        # address
        self.lb_address = Label(self.frame_1, text='Endereço', bg=self.secondary,
                                fg='white', font=('verdana', 11))
        self.lb_address.place(relx=0.0329, rely=0.74, relwidth=0.1, relheight=0.08)

        self.entry_address = Entry(self.frame_1, font=('verdana', 13))
        self.entry_address.place(relx=0.036, rely=0.84, relwidth=0.4, relheight=0.11)

        # district
        self.lb_district = Label(self.frame_1, text='Bairro', bg=self.secondary,
                                 fg='white', font=('verdana', 11))
        self.lb_district.place(relx=0.487, rely=0.74, relwidth=0.1, relheight=0.08)

        self.entry_district = Entry(self.frame_1, font=('verdana', 13))
        self.entry_district.place(relx=0.5, rely=0.84, relwidth=0.4, relheight=0.11)

        # CEP
        self.entry_CEP = Entry(self.frame_1, font=('verdana', 13))
        self.entry_CEP.place(relx=0.755, rely=0.39, relwidth=0.2, relheight=0.11)

    def listFrame_2(self):
        self.listaClient = ttk.Treeview(self.frame_2, height=3, column=(
            'col1', 'col2', 'col3', 'col4', 'col5', 'col6'))

        self.listaClient.heading('#0')
        self.listaClient.heading('#1', text='Cód')
        self.listaClient.heading('#2', text='Nome')
        self.listaClient.heading('#3', text='Telefone')
        self.listaClient.heading('#4', text='Cidade')
        self.listaClient.heading('#5', text='Endereço')
        self.listaClient.heading('#6', text='Bairro')

        self.listaClient.column('#0', width=0)
        self.listaClient.column('#1', width=15)
        self.listaClient.column('#2', width=200)
        self.listaClient.column('#3', width=90)
        self.listaClient.column('#4', width=80)
        self.listaClient.column('#5', width=190)
        self.listaClient.column('#6', width=60)

        self.listaClient.place(relx=0.02, rely=0.09, relwidth=0.96, relheight=0.88)
        self.scroll_lista = Scrollbar(self.frame_2, orient='vertical')

        self.listaClient.configure(yscrollcommand=self.scroll_lista.set)
        self.scroll_lista.place(relx=0.965, rely=0.0910, relwidth=0.015, relheight=0.877)

        self.listaClient.bind('<ButtonRelease-1>', self.click)
        self.sizegrip.place(relx=0.98, rely=0.97)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        def quit(): self.root.destroy()

        menu_op = Menu(menubar, tearoff=False)
        menu_op.add_command(label="Sair", command=quit)
        menubar.add_cascade(menu=menu_op, label="Opções")

        menu_op2 = Menu(menubar, tearoff=False)
        menu_op2.add_command(label="Gerar PDF", command=self.generateReport)
        menubar.add_cascade(menu=menu_op2, label="Cliente")

if __name__ == '__main__':
    root = Tk()
    Application()
