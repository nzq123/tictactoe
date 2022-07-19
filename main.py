# najprosciej jak sie da, pozniej mozna ulepszyc
#
# 1. tablica 3x3   ✅
# 2. X albo O <- wybor
# 3. X zawsze zaczyna, jak wybierzesz o to komp zaczyna
# 3. kondycja wygranej <- jak jest 3 w rzedzie to win
# 4. kondycja remisu
# 5. jak komputer ma myslec, zeby dążyc do 3 w żadku(na start komputer daje total rng, pozniej sie zmieni)
# 6. komp by dawal info ze sa pola od 1 do 9, gracz by je wybieral
# 7. regula samej gry / na zmiane / zaczynajacy zaczyna / kto czym gra / win/draw condition/ wyswietlenie kto wygral


# x = [["1", "2", "3"], ["4", "5", "6"], [["7", "8", "9"]]]

# for i in tab:
#     print(i)

tab = []
for j in range(3):
    tab.append([j * 3 + 1, j * 3 + 2, j * 3 + 3])

player1 = "X"
player2 = "O"

field = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def p1_is_win():
    if field[0][0] == "X" and field[0][1] == "X" and field[0][2] == "X":
        print("Gracz 1 wygrał wow")
    elif field[0][0] == "X" and field[1][0] == "X" and field[2][0] == "X":
        print("Gracz 1 wygrał wow")
    elif field[0][0] == "X" and field[1][1] == "X" and field[2][2] == "X":
        print("Gracz 1 wygrał wow")
    elif field[1][0] == "X" and field[1][1] == "X" and field[1][2] == "X":
        print("Gracz 1 wygrał wow")
    elif field[2][0] == "X" and field[2][1] == "X" and field[2][2] == "X":
        print("Gracz 1 wygrał wow")
    elif field[2][0] == "X" and field[1][1] == "X" and field[0][2] == "X":
        print("Gracz 1 wygrał wow")
    elif field[0][1] == "X" and field[1][1] == "X" and field[2][1] == "X":
        print("Gracz 1 wygrał wow")
    elif field[0][2] == "X" and field[1][2] == "X" and field[2][2] == "X":
        print("Gracz 1 wygrał wow")
    return True

def p2_is_win():
    if field[0][0] == "O" and field[0][1] == "O" and field[0][2] == "O":
        print("Gracz 2 wygrał wow")
    elif field[0][0] == "O" and field[1][0] == "O" and field[2][0] == "O":
        print("Gracz 2 wygrał wow")
    elif field[0][0] == "O" and field[1][1] == "O" and field[2][2] == "O":
        print("Gracz 2 wygrał wow")
    elif field[1][0] == "O" and field[1][1] == "O" and field[1][2] == "O":
        print("Gracz 2 wygrał wow")
    elif field[2][0] == "O" and field[2][1] == "O" and field[2][2] == "O":
        print("Gracz 2 wygrał wow")
    elif field[2][0] == "O" and field[1][1] == "O" and field[0][2] == "O":
        print("Gracz 2 wygrał wow")
    elif field[0][1] == "O" and field[1][1] == "O" and field[2][1] == "O":
        print("Gracz 2 wygrał wow")
    elif field[0][2] == "O" and field[1][2] == "O" and field[2][2] == "O":
        print("Gracz 2 wygrał wow")
    return True

while True:
    a = int(input("Gracz 1 podaję pierwsze pole: " ))
    b = int(input("Gracz 1 podaję drugie pole: " ))
    field[a][b] = "X"
    for i in field:
        print(i)

    a = int(input("Gracz 2 podaję pierwsze pole: "))
    b = int(input("Gracz 2 podaję drugie pole: "))
    while field[a][b] == "X":
        print("Nie możesz zagrać na polu przeciwnika")
        a = int(input("Gracz 2 podaję pierwsze pole: "))
        b = int(input("Gracz 2 podaję drugie pole: "))
    else:
        field[a][b] = "O"
    for i in field:
        print(i)

    a = int(input("Gracz 1 podaję pierwsze pole: "))
    b = int(input("Gracz 1 podaję drugie pole: "))
    while field[a][b] == "X" or field[a][b] == "O":
        print("Nie możesz zagrać na zajętym polu")
        a = int(input("Gracz 1 podaję pierwsze pole: "))
        b = int(input("Gracz 1 podaję drugie pole: "))
    else:
        field[a][b] = "X"
    for i in field:
        print(i)

    a = int(input("Gracz 2 podaję pierwsze pole: "))
    b = int(input("Gracz 2 podaję drugie pole: "))
    while field[a][b] == "X" or field[a][b] == "O":
        print("Nie możesz zagrać na polu przeciwnika")
        a = int(input("Gracz 2 podaję pierwsze pole: "))
        b = int(input("Gracz 2 podaję drugie pole: "))
    else:
        field[a][b] = "O"
    for i in field:
        print(i)

    a = int(input("Gracz 1 podaję pierwsze pole: "))
    b = int(input("Gracz 1 podaję drugie pole: "))
    while field[a][b] == "X" or field[a][b] == "O":
        print("Nie możesz zagrać na polu przeciwnika")
        a = int(input("Gracz 1 podaję pierwsze pole: "))
        b = int(input("Gracz 1 podaję drugie pole: "))
    else:
        field[a][b] = "X"
    p1_is_win()
    for i in field:
        print(i)

    a = int(input("Gracz 2 podaję pierwsze pole: "))
    b = int(input("Gracz 2 podaję drugie pole: "))
    while field[a][b] == "X" or field[a][b] == "O":
        print("Nie możesz zagrać na polu przeciwnika")
        a = int(input("Gracz 2 podaję pierwsze pole: "))
        b = int(input("Gracz 2 podaję drugie pole: "))
    else:
        field[a][b] = "O"
    p2_is_win()
    for i in field:
        print(i)

    a = int(input("Gracz 1 podaję pierwsze pole: "))
    b = int(input("Gracz 1 podaję drugie pole: "))
    while field[a][b] == "X" or field[a][b] == "O":
        print("Nie możesz zagrać na polu przeciwnika")
        a = int(input("Gracz 1 podaję pierwsze pole: "))
        b = int(input("Gracz 1 podaję drugie pole: "))
    else:
        field[a][b] = "X"
    p1_is_win()
    for i in field:
        print(i)

    a = int(input("Gracz 2 podaję pierwsze pole: "))
    b = int(input("Gracz 2 podaję drugie pole: "))
    while field[a][b] == "X" or field[a][b] == "O":
        print("Nie możesz zagrać na polu przeciwnika")
        a = int(input("Gracz 2 podaję pierwsze pole: "))
        b = int(input("Gracz 2 podaję drugie pole: "))
    else:
        field[a][b] = "O"
    p2_is_win()
    for i in field:
        print(i)

    a = int(input("Gracz 1 podaję pierwsze pole: "))
    b = int(input("Gracz 1 podaję drugie pole: "))
    while field[a][b] == "X" or field[a][b] == "O":
        print("Nie możesz zagrać na polu przeciwnika")
        a = int(input("Gracz 1 podaję pierwsze pole: "))
        b = int(input("Gracz 1 podaję drugie pole: "))
    else:
        field[a][b] = "X"
    if p1_is_win() == False:
        print("REMIS")
    else:
        p1_is_win()

    for i in field:
        print(i)
    break

