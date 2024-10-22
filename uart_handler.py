


class Uart:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def encode_message(self, action):
        pass

    def send_to_cell(self):
        self.encode_message()


x = 0b101101 | 0b010010
y = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH']
x = ['AH', '5H', '5H', '8H', '6H', '9H', '10H', 'QH', 'KH', 'AC', '2C', '5C', '4C', '8C', 'JC', 'QC', 'KC', 'AD', '2D', '5D', '7D', '5D', '6D', '7D', '8D', '9D', '10D', 'QD', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '10S', '8S', 'JS', 'QS', 'KS']

dif = []
for card in y:
    if card not in x:
        #print(card)
        dif.append(card)

print(dif)
print(len(dif))

'''
['AH', '5H', '5H', '8H', '6H', '9H', '10H', 'QH', 'KH', 'AC', '2C', '5C', '4C', '8C', 'JC', 'QC', 'KC', 'AD', '2D', '5D', '7D', '8D', '6D', '10D', '9D', 'QD', '4S', '2S', '3S', '7S', '5S', '6S', '7S', '8S', 'JS', 'QS', 'KS']

['AH', '5H', '5H', '8H', '6H', '9H', '10H', 'QH', 'KH', 'AC', '2C', '5C', '4C', '8C', 'JC', 'QC', 'KC', 'AD', '2D', '5D', '7D', '5D', '6D', '7D', '8D', '9D', '10D', 'QD', 'AS', '2S', '3S', '4S', '5S', '6S', '7S', '10S', '8S', 'JS', 'QS', 'KS']
'''