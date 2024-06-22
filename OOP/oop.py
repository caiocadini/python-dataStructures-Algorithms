class Item():
    #Pertence à classe em si não apenas ao objeto
    pay_rate = 0.8

    #Variável estática para salvar todas as instâncias desta classe
    allInstances = []
    contadorInstancias = 0
    #Initializer (with typing)
    def __init__(self, name: str,  price: float, quantity=0):
        #Validação
        assert price >= 0, 'price should be a float value equal to or higher than 0'
        assert quantity >=0, 'quantity should be a int value equal to or higher than 0'
        self.name = name
        self.quantity = quantity
        self.price = price

        #Ação para adicionar à variável estática
        Item.allInstances.append(self)
        Item.contadorInstancias = Item.contadorInstancias + 1
    

    # Methods
    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discout(self):
        self.price = self.price * self.pay_rate

    # Método igual toString em Java
    def __repr__(self):
        return f"name: {self.name}, price: {self.price}, quantity: {self.quantity}"
    

Item1 = Item('Caio', 5, 2.0)

Item1.apply_discout()
