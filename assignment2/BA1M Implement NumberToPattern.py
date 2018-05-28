def NumberToSymbol(index):      # definiere Funktion, die Zahlen in Buchstaben übersetzt
    if index == 0:
        return "A"
    elif index == 1:
        return "C"
    elif index == 2:
        return "G"
    elif index == 3:
        return "T"
    else:
        return ' '

def NumberToPattern(index, k):  # definiere rekursive Funtkion, die den Index teilt
    if k==1:                    # und NumberToSymbol zum Rest addiert
        return NumberToSymbol(index)
    
    return NumberToPattern(index // 4, k-1) + NumberToSymbol(index % 4)


index = 5353
k = 7
print(NumberToPattern(index, k))
