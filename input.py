
while True:
    try:
        inputresult = int(input('Írj be egy számot '))
        break
    except ValueError:
            print("Nem számot írtál!")

