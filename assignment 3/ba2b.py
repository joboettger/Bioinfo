def hammingDistance(p, q):  # erstellt Funktion, die die Entfernung zwischen 
                            # DNA String p und längerem oder gleich langem DNA
                            # String q
    ham = 0                 # setzt Zähler auf Null
    for x, y in zip(p, q):
        if x != y:          # wenn Text y entspricht,
            ham += 1        # Zähler um 1 hochsetzen
    return ham


def distanceBetweenPatternAndString(pattern, dna): # defniert Funktion, die 
                            # die Entfernung zwischen Pattern und restlichem 
                            # DNA-String ausgibt
    k = len(pattern)        # weist Variable k die Länge des Patterns zu
    distance = 0            # setzt den Zähler für die Entfernung auf 0
    for x in dna:           # Schleife für jeden DNA-Strang x in DNA
        hamming = k + 1     # max. sind alle Basen veschieden, daher k+1 immer
                            # um höher als das mögliche
        for i in range(len(x) - k + 1):
            z = hammingDistance(pattern, x[i:i + k])
            if hamming > z: # für hamming > z
                hamming = z 
        distance += hamming     # sonst Entfernung um hamming erhöhen
    return distance


def numberToPattern(x, k):  # definiert rekursive Funtkion, die den Index teilt
    if k == 1:              # und NumberToSymbol zum Rest addiert
        return numberToSymbol(x)
    return numberToPattern(x // 4, k - 1) + numberToSymbol(x % 4)


def numberToSymbol(x):      # definiert Funktion, die Zahlen Symbole 
                            # (Buchstaben) zuweist
    if x == 0:
        return "A"
    if x == 1:
        return "C"
    if x == 2:
        return "G"
    if x == 3:
        return "T"


def medianString(dna, k):   # definiert Funktion, die genau das k-mer findet, 
                            # welches am häufigsten in allen DNA Strings 
                            # auftaucht
    distance = (k + 1) * len(dna)   # Enfernung max. so groß wie Länge der 
                                    # gesuchten Sequenz --> also unendlich
    median = ""
    for i in range(4 ** k):
        pattern = numberToPattern(i, k)
        z = distanceBetweenPatternAndString(pattern, dna)
        if distance > z:
            distance = z
            median = pattern
    return median


dna = ["AAATTGACGCAT", "GACGACCACGTT", "CGTCAGCGCCTG", "GCTGAGCACCGG", "AGTACGGGACAG"]
k = 3
print(medianString(dna, k))
