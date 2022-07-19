tab = []
for j in range(3):
    tab.append([j * 3 + 1, j * 3 + 2, j * 3 + 3])

field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def is_win(num):
    if field[0][0] == num and field[0][1] == num and field[0][2] == num or\
        field[0][0] == num and field[1][0] == num and field[2][0] == num or\
        field[0][0] == num and field[1][1] == num and field[2][2] == num or\
        field[1][0] == num and field[1][1] == num and field[1][2] == num or\
        field[2][0] == num and field[2][1] == num and field[2][2] == num or\
        field[2][0] == num and field[1][1] == num and field[0][2] == num or\
        field[0][1] == num and field[1][1] == num and field[2][1] == num or\
        field[0][2] == num and field[1][2] == num and field[2][2] == num:
        return True


def answer(player):
    a = int(input(f"Gracz {player} podaję pierwsze pole: "))
    while a < 0:
        a = int(input("Podaj dodatnią liczbę: "))
    b = int(input(f"Gracz {player} podaję drugie pole: "))
    while b < 0:
        b = int(input("Podaj dodatnią liczbę: "))
    while field[a][b] == "X" or field[a][b] == "O":
        print("Nie możesz zagrać na polu przeciwnika")
        a = int(input(f"Gracz {player} podaję pierwsze pole: "))
        b = int(input(f"Gracz {player} podaję drugie pole: "))
    return a, b


try:
    game = 1
    while game <= 5:
        a, b = answer(1)
        field[a][b] = "X"
        for i in field:
            print(i)
        if is_win("X") is True:
            print("Gracz 1 wygrał")
            break

        if game == 5:
            print("Gracze zremisowali")
            break

        a, b = answer(2)
        field[a][b] = "O"
        for i in field:
            print(i)
        if is_win("0") is True:
            print("Gracz 2 wygrał")
            break

        game += 1


except IndexError:
    print("Wyszedłeś poza plansze")
except ValueError:
    print("Musisz podać liczbę od 0 do 2")
