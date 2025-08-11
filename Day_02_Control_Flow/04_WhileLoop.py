count = 5
while count > 0:
    print(f"Count {count}")
    count = count - 1

print()

#break keyword
countBreak = 5
while countBreak > 0:
    if(countBreak == 3):
        break
    print(f"Count {countBreak}")
    countBreak = countBreak - 1
    

#continue keyword
countContinue = 5
while countContinue > 0:
    if countContinue == 4:
        continue
    print(f"Count {countContinue}")
    countContinue = countContinue - 1
    
print()


#while with break keyword
while True:
    name = input("Enter your name or 'q' to quite:")
    if name.lower() == 'q':
        break
    print(f"Hello,{name}")