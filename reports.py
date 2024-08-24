from modulos import *

class Reports():
    def printClient(self):
        webbrowser.open('client.pdf')

    def generateReport(self):
        self.c = canvas.Canvas('client.pdf')

        self.code_report = self.entry_code.get()
        self.name_report = self.entry_name.get()
        self.phone_report = self.entry_phone.get()
        self.city_report = self.entry_city.get()
        self.district_report = self.entry_district.get()
        self.address_report = self.entry_address.get()

        self.c.setFont('Helvetica-Bold', 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont('Helvetica-Bold', 17)
        self.c.drawString(50, 700, 'Código: ')
        self.c.drawString(50, 670, 'Nome: ')
        self.c.drawString(50, 640, 'Telefone: ')
        self.c.drawString(50, 610, 'Cidade: ')
        self.c.drawString(50, 580, 'Bairro: ')
        self.c.drawString(50, 550, 'Endereço: ')

        self.c.setFont('Helvetica', 17)
        self.c.drawString(100, 700, self.code_report)
        self.c.drawString(100, 670, self.name_report)
        self.c.drawString(100, 640, self.phone_report)
        self.c.drawString(100, 610, self.city_report)
        self.c.drawString(100, 580, self.district_report)
        self.c.drawString(100, 550, self.address_report)

        self.c.rect(20, 500, 550, 2, fill=True, stroke=False)

        self.c.showPage()
        self.c.save()
        self.printClient()
        