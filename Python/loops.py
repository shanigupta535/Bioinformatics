# for loop - Jab hume pata ho ki kitni baar repeat karna hai, generally for loop use karte hain.

for i in range (5):
    print(i)

for i in range (1000):
    print(i)

# range(start, stop, step)

for i in range (20, 100, 20):
    print(i)


# EX List with loops
genes = ["BRCA1", "TP53", "EGFR"]

for gene in genes:
    print(gene)

# EX
dna = "ATGC"

for base in dna:
    print(base)


for i in range(1, 10):
    if i == 5:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue # 3 ko chood ka sab chelaga 
    print(i)

# 2 While loops - while loop tab tak chalta hai jab tak condition True hai.

i = 0
while i<=5:
    print(i)
    i+=1 # i = i + 1

  
