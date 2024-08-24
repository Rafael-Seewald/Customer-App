from modulos import *

class Functions():
    def connectDB(self):
        self.db = sqlite3.connect('clients.db')
        self.cursor = self.db.cursor()

    def disconnectDB(self):
        self.db.close()

    def createTables(self):
        self.connectDB()
        # Creating tables
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40),
                endereco CHAR(40),
                bairro CHAR(20)
            );
        ''')
        self.db.commit
        self.disconnectDB()

    def cleanClient(self):
        self.entry_code.delete(0, END)
        self.entry_name.delete(0, END)
        self.entry_phone.delete(0, END)
        self.entry_city.delete(0, END)
        self.entry_address.delete(0, END)
        self.entry_district.delete(0, END)

    def variables(self):
        self.code = self.entry_code.get()
        self.name = self.entry_name.get()
        self.phone = self.entry_phone.get()
        self.city = self.entry_city.get()
        self.address = self.entry_address.get()
        self.district = self.entry_district.get()

    def add(self):
        self.variables()
        if self.entry_name.get() == '':
            msg = 'Para cadastrar um novo cliente é necessário que seja digitado pelo menos um nome'
            messagebox.showwarning('Cadastro de clientes - Aviso!', msg)
        else:
            self.connectDB()
            self.cursor.execute(''' INSERT INTO clientes (nome_cliente, telefone, cidade, endereco, bairro)
                VALUES (?, ?, ?, ?, ?)''', (self.name, self.phone, self.city, self.address, self.district))
            self.db.commit()
            self.disconnectDB()
            self.selectList()
            self.cleanClient()

    def selectList(self):
        self.listaClient.delete(*self.listaClient.get_children())
        self.connectDB()
        lista = self.cursor.execute(''' SELECT cod, nome_cliente, telefone, cidade, endereco, bairro FROM clientes
            ORDER BY nome_cliente ASC; ''')
        for i in lista:
            self.listaClient.insert('', END, values=i)
        self.disconnectDB()

    def click(self, event):
        self.cleanClient()
        self.listaClient.selection()

        for n in self.listaClient.selection():
            col1, col2, col3, col4, col5, col6 = self.listaClient.item(n, 'values')
            self.entry_code.insert(END, col1)
            self.entry_name.insert(END, col2)
            self.entry_phone.insert(END, col3)
            self.entry_city.insert(END, col4)
            self.entry_address.insert(END, col5)
            self.entry_district.insert(END, col6)

    def deleteClient(self):
        self.variables()
        self.connectDB()
        self.cursor.execute(
            ''' DELETE FROM clientes WHERE cod = ? ''', (self.code,))
        self.db.commit()
        self.disconnectDB()
        self.cleanClient()
        self.selectList()

    def editClient(self):
        self.variables()
        self.connectDB()
        self.cursor.execute(''' UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?, endereco = ?, bairro = ?
            WHERE cod = ? ''', (self.name, self.phone, self.city, self.address, self.district, self.code))
        self.db.commit()
        self.disconnectDB()
        self.selectList()
        self.cleanClient()

    def searchClient(self):
        self.connectDB()
        self.listaClient.delete(*self.listaClient.get_children())

        self.entry_name.insert(END, '%')
        nome = self.entry_name.get()
        self.cursor.execute(''' SELECT cod, nome_cliente, telefone, cidade, endereco, bairro FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC''' % nome)
        search_name_cli = self.cursor.fetchall()
        for i in search_name_cli:
            self.listaClient.insert('', END, values=i)
        self.cleanClient()
        self.disconnectDB()

    def cepFunc(self):
        try:
            self.entry_city.delete(0, END)
            self.entry_district.delete(0, END)
            self.entry_address.delete(0, END)

            cep = self.entry_CEP.get()
            url = f'https://viacep.com.br/ws/{cep}/json/'
            requisition = requests.get(url)
            requi_json = requisition.json()

            self.entry_city.insert(END, requi_json['uf'] + ' - ' + requi_json['localidade'])
            self.entry_district.insert(END, requi_json['bairro'])
            self.entry_address.insert(END, requi_json['logradouro'])
            self.entry_CEP.delete(0, END)
        except:
            messagebox.showerror('Erro', 'CEP inválido, tente digitar apenas 8 números')
