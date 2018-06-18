def hammingDistance(p, q):  # erstellt Funktion, die die Entfernung zwischen 
                            # DNA String p und längerem oder gleich laengem DNA
                            # String q
    ham = 0                 # setzt Zähler auf Null
    for x, y in zip(p, q):
        if x != y:          # wenn x y entspricht,
            ham += 1        # Zähler um 1 hochsetzen
    return ham


def distanceBetweenPatternAndString(pattern, dna):  # defniert Funktion, die 
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
        distance += hamming # sonst Entfernung um hamming erhöhen
    return distance


dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]
pattern = "AAA"
print(distanceBetweenPatternAndString(pattern, dna))
