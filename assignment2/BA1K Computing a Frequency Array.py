def PatternToNumber(pattern):   # definiere Funktion, die DNA-String in Zhalen übersetzt
    if pattern=="":
        return 0
    #symbol is last character of pattern     
    symbol = pattern[-1]        # das Symbol ist das letzte Zeichen des Pattern 
    prefix = pattern[0:-1]      # weist Rest des Patterns aus mittels rekursiver Funktion
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def SymbolToNumber(symbol):     #Symbolen (Buchstaben) Zahlen zuweisen
	if symbol == "A":
		return 0
	if symbol == "C":
		return 1
	if symbol == "G":
		return 2
	if symbol == "T":
		return 3

text = "ACGCGGCTCTGAAA"
k = 2

patternFrequencies = [0] * 4**k     # Beginn Array mit der Länge 4^k

for i in range(len(text)-k+1):      # Schleife um Pattern im Text zu finden und in Array zu übertragen
	pattern = text[i:i+k]
	j = PatternToNumber(pattern)
	patternFrequencies[j] = patternFrequencies[j] + 1


p = ""
for i in patternFrequencies:
	p += str(i) + " "

print(p)
