def PatternCount(text, pattern):
    result = 0
    for i in range(0, len(text)-len(pattern)+1):
        if (text[i:i+len(pattern)] == pattern):
            result += 1
    return result
def FrequentWords(text, k=4):   # liste mit häuftigsten Substrings in gegebenem Text
    import ba1m # vorherige Programme importieren
    import ba1l
    
    allPatternsWithCount = [0]*(4**k)   # erstellt einen Array mit allen pattern
    result = []     # erstellt eine Liste für alle Ergebnisse
    for i in range(0, len(text)-k): # pattern liegt im Bereich des texts
        pattern = text[i:i+k]        
        allPatternsWithCount[ba1l.PatternToNumber(pattern)] += 1 #erhöht den Zähler des Patterns um 1
         
    maximum = max(allPatternsWithCount) # sucht das Maximum
    print(maximum)                      # gibt maximum aus 
    for number, count in enumerate (allPatternsWithCount): # Gesamtschleife über alle Pattern
        if count == maximum: # zum zähler hinzugügen wenn Zähler dem maximum entspricht
            result.append((number, count))
            print(ba1m.NumberToPattern(number, k),end=' ')    
    return result
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()    

text = data[0]
print(FrequentWords(text, int(data[1])))
