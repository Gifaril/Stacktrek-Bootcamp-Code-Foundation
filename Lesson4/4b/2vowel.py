import os 
os.system('cls||clear')

# Code Starts Here

sentece = input()
count = 0
if ("a" in sentece) or ("A" in sentece):
    count += 1
if ("e" in sentece) or ("E" in sentece):
    count += 1
if ("i" in sentece) or ("I" in sentece):
    count += 1
if ("o" in sentece) or ("O" in sentece):
    count += 1
if ("u" in sentece) or ("U" in sentece):
    count += 1
print(count)