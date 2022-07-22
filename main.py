field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def is_win(num):
    if field[0][0] == num and field[0][1] == num and field[0][2] == num:
        return True
    elif field[0][0] == num and field[1][0] == num and field[2][0] == num:
        return True
    elif field[0][0] == num and field[1][1] == num and field[2][2] == num:
        return True
    elif field[1][0] == num and field[1][1] == num and field[1][2] == num:
        return True
    elif field[2][0] == num and field[2][1] == num and field[2][2] == num:
        return True
    elif field[2][0] == num and field[1][1] == num and field[0][2] == num:
        return True
    elif field[0][1] == num and field[1][1] == num and field[2][1] == num:
        return True
    elif field[0][2] == num and field[1][2] == num and field[2][2] == num:
        return True


def answer(player):
    while True:
        try:
            a = int(input(f"Gracz {player} podaję pierwsze pole: "))
            print(a)
            while a < 0 or a > 2:
                a = int(input(f"Gracz {player} podaję poprawne pole: "))
            break
        except ValueError:
            print("Podaj liczbę w przedziale 0:2: ")
        except IndexError:
            print("Podaj liczbę w przedziale 0:2: ")
    while True:
        try:
            b = int(input(f"Gracz {player} podaję drugie pole: "))
            print(b)
            while b < 0 or b > 2:
                b = int(input(f"Gracz {player} podaję poprawne pole: "))
            break
        except ValueError:
            print("Podaj liczbę w przedziale 0:2: ")
        except IndexError:
            print("Podaj liczbę w przedziale 0:2: ")
    return a, b


def taken_place(a, b):
    if field[a][b] == "X" or field[a][b] == "O":
        return True
    else:
        return False


game = 1
while game <= 5:
    a, b = answer(1)
    while taken_place(a, b) is True:
        print("Poprawne miejsce podaj")
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
    while taken_place(a, b) is True:
        print("Poprawne miejsce podaj")
        a, b = answer(2)

    field[a][b] = "O"

    for i in field:
        print(i)

    if is_win("O") is True:
        print("Gracz 2 wygrał")
        break

    game += 1








