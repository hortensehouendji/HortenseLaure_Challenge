import re

def checkCard(card):
    grouping = re.compile(r'^(?:.{4}\-){3}.{4}$').match
    consecutive = re.compile(r'(.)\1{3}').search
    valid = re.compile(r'^[456]\d{15}$').match

    if grouping(card):
        card = card.replace('-', '')
    if valid(card) and not consecutive(card):
        card_state = "Valid"
    else:
        card_state = "Invalid"
        
    return card_state
  
n = int(input())

while (n!=0):
    c = input().strip()
    #print(c)
    card_state = checkCard(c)
    print(card_state)
    n-=1
