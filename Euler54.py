def parse():
    f = open('Euler54Data.txt','r')
    data = list()
    for line in f:
        line = line.strip("\n")
        line = line.split(" ")
        data.append(line)
    return data
def player_hands(data):
    return [Card(card[0],card[1]) for card in data]

"""
def compare(p1,p2):
    royal_flush
    straight_flush
    fourofakind
    fullhouse

def high_card(p1):

def royal_flush(p1):
"""
class Card():
    def __init__(self,number,color):
        if number in values:
            self.value = values[number]
        else:
            self.value = int(number) 
        self.color = color
    def __str__(self):
        return str(self.value) +" "+ self.color 


values = {'T':10,'J':11, 'Q':12, 'K':13, 'A':14}  
data = parse()
s = 0
for i in range(1):
    
    p1 = play
    er_hands(data[i])
    print p1'
    """
    if compare(p1,p2):
        s++
    """