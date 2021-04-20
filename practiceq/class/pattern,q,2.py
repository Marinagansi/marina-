ascii_number=65
for i in range(4):
    for j in range (i+1):
        character = chr(ascii_number)
        print(character, end=" ")
        ascii_number +=1
    print()