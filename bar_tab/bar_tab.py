class Tab:

    menu = {
        'wine': 5,
        'beer': 3,
        'soft_drink': 2,
        'chicken': 10,
        'beef': 15,
        'veggie': 12,
        'desert': 6
    }

    #função que é chamada pra criar o objeto
    def __init__(self):
        #valor inicial da conta
        self.total = 0
        #lista que irá guardar o itens que forem sendo pedidos
        self.items = []

    #método da instância
    def add(self, item):
        #appends o item que for pedido lá na lista [] vazia que foi criada pro objeto
        self.items.append(item)
        #atualiza o total da conta, adicionando o valor do item, de acordo com o que tem na dict do menu
        #aqui o item é a key!
        self.total += self.menu[item]

    #método da instância
    def print_bill(self, tax, service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        #aqui é o total real
        #self.total é atualizado pelo metodo add
        total = self.total + tax + service

        #loops through the list self.items
        for item in self.items:
            print(f'{item:15} R${self.menu[item]}')

        print(f'{"Tax":15} R${tax:.2f}')
        print(f'{"Service":15} R${service:.2f}')
        print(f'{"Total":15} R${total:.2f}')

#Como chamar no terminal
#from bar_tab import Tab
#table01 = Tab()
#table01.add('item_name')
#table01.print_bill(tax, service)