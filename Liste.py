def first_part():
    # BEGINNING
    q = [1, 2, 3, 4]
    print(q)
    print(len(q))
    print(3*q)
    print(3*q[:2]+[10, 'asd'])
    a, b = 0, 1
    print(a, b)
    while b < 10:
        print(b)
        a, b = b, a+b
    # IF
    x = 10
    if x<12:
        print("Do something")
    elif x>10:
        print("Do another thing")
    else:
        print("Do something else")
    # FOR
    a = ['no', 'capra', 'sedia', 'tavolo', 'poltrona']
    for x in a:
        print(x) # printa il contenuto di a, x diventa un iteratore (pensa a C++)
    print("\n\t###\n")
    for x in a[:]:          #fa una copia tramite affettamento dell'intera lista
        if len(x) >= 6:
            print(a)
            a.insert(0, x)
            print("###")
    print(a)
    print("\n\t###\n")
    # RANGE
    y = range(10)
    print(y)
    print(len(y))
    print("\n")
    for i in y:
        print(i)
    y = range(10, 20)
    print(y)
    y = range(0, 10, 3)
    print(y)
    y = range(-10, -100, -4)
    print(y)

def second_part():
    # clausola ELSE nei cicli
    for n in range(2,10):
        for x in range(2, n):
            if n % x == 0:
                print(n, ' è uguale a ', x, '*', n/x)
                break #evita esecuzione istruzione ELSE
        else:
            # il ciclo scorre sequenza senza trovare il fattore
            print(n, ' è un numero primo')

def fibonacci(n=10):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

print(fibonacci(32))

def initialized_parameter(y = 3):
    x = 10
    print(x*y)
initialized_parameter()
initialized_parameter(6)

def different_call_parameter(x, y = 4):
    print(x+y)
different_call_parameter(1)
different_call_parameter(3,5)

def keyword_parameter(stanza, sedia="IkeaS", tavolo='ikeaT', cucina='IkeaC'):
    print("In",stanza,"ci sono: ",sedia,tavolo,cucina)
keyword_parameter("Sala da pranzo")
keyword_parameter(cucina="frullatore",sedia="panca",tavolo="Bancale",stanza="Cesso")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I’m sorry, we’re all out of", kind)
    for arg in arguments: print(arg)
    print("-"*40)
    keys = keywords.keys()
    #keys.sort()
    for kw in keys: print(kw, "-", keywords[kw])

cheeseshop("Limburger", "It’s very runny, sir.","It’s really very, VERY runny, sir.",client="John Cleese",shopkeeper="Michael Palin",sketch="Cheese Shop Sketch")

#lambda

