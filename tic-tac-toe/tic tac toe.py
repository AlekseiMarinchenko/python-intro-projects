import random
field = ['-' for i in range(9)]
nomer_hoda_igroka = random.randint(0, 1)
if nomer_hoda_igroka == 0:
    player_symbol = 'x'
    Ai_symbol = 'o'
else:
    player_symbol = 'o'
    Ai_symbol = 'x'
def end(field):
    if field[0] == field[1] == field[2] != '-':
        return True
    if field[3]==field[4]==field[5] != '-':
        return True
    if field[6]==field[7]==field[8] != '-':
        return True
    if field[0]==field[3]==field[6] != '-':
        return True
    if field[1]==field[4]==field[7] != '-':
        return True
    if field[2]==field[5]==field[8] != '-':
        return True
    if field[0]==field[4]==field[8] != '-':
        return True
    if field[2]==field[4]==field[6] != '-':
        return True
    return False
def pustota(aifield, x):
    if aifield[x] == '-':
        return True
    return False
def pole(field):
    print(*field[0:3])
    print(*field[3:6])
    print(*field[6:9])
def player_turn(field):
    n = int(input())
    if field[n] != '-':
        print('поле занято, выберите другое')
        return player_turn(field)
    field[n] = player_symbol
def AI_turn(field):
    c = 0
    if c == 0:
        if (field[0] == field[1] == Ai_symbol or field[0] == field[2] == Ai_symbol or field[2] == field[1] == Ai_symbol) and '-' in field[0:3]:
            for i in range(3):
                if pustota(field, i):
                    field[i] = Ai_symbol

        elif( field[3] == field[4] == Ai_symbol or field[3] == field[5] == Ai_symbol or field[4] == field[5] == Ai_symbol) and (field[3] == '-' or field[4]=='-' or field[5]=='-'):
            for i in range(3, 6):
                if pustota(field, i):
                    field[i] = Ai_symbol

        elif (field[6] == field[7] == Ai_symbol or field[6] == field[8] == Ai_symbol or field[7] == field[8] == Ai_symbol) and (field[6] == '-' or field[7]=='-' or field[8]=='-'):
            for i in range(6, 9):
                if pustota(field, i):
                    field[i] = Ai_symbol

        elif (field[0] == field[3] == Ai_symbol or field[0] == field[6] == Ai_symbol or field[3] == field[6] == Ai_symbol) and (field[0] == '-' or field[3]=='-' or field[6]=='-'):
            for i in [0, 3, 6]:
                if pustota(field, i):
                    field[i] = Ai_symbol

        elif (field[1] == field[4] ==Ai_symbol or field[1] == field[7] == Ai_symbol or field[4] == field[7] == Ai_symbol) and (field[1] == '-' or field[4]=='-' or field[7]=='-'):
            for i in [1, 4, 7]:
                if pustota(field, i):
                    field[i] = Ai_symbol

        elif (field[2] == field[5] == Ai_symbol or field[2] == field[8] == Ai_symbol or field[5] == field[8] == Ai_symbol) and (field[2] == '-' or field[5]=='-' or field[8]=='-'):
            for i in [2, 5, 8]:
                if pustota(field, i):
                    field[i] = Ai_symbol

        elif (field[2] == field[4] == Ai_symbol or field[2] == field[6] == Ai_symbol or field[4] == field[6] == Ai_symbol) and (field[2] == '-' or field[4]=='-' or field[6]=='-'):
            for i in [2, 4, 6]:
                if pustota(field, i):
                    field[i] = Ai_symbol

        elif (field[0] == field[4] == Ai_symbol or field[0] == field[8] == Ai_symbol or field[4] == field[8] == Ai_symbol) and (field[0] == '-' or field[4]=='-' or field[8]=='-'):
            for i in [0, 4, 8]:
                if pustota(field, i):
                    field[i] = Ai_symbol
        else:
            if (field[0] == field[1] == player_symbol or field[0] == field[2] == player_symbol or field[2] == field[1] == player_symbol)and (field[0] == '-' or field[1]=='-' or field[2]=='-'):
                for i in range(3):
                    if pustota(field, i):
                        field[i] = Ai_symbol
            elif (field[3] == field[4] == player_symbol or field[3] == field[5] == player_symbol or field[4] == field[5] == player_symbol)and (field[3] == '-' or field[4]=='-' or field[5]=='-'):
                for i in range(3, 6):
                    if pustota(field, i):
                        field[i] = Ai_symbol
            elif (field[6] == field[7] == player_symbol or field[6] == field[8] == player_symbol or field[7] == field[8] == player_symbol) and (field[6] == '-' or field[7]=='-' or field[8]=='-'):
                for i in range(6, 9):
                    if pustota(field, i):
                        field[i] = Ai_symbol
            elif (field[0] == field[3] == player_symbol or field[0] == field[6] == player_symbol or field[3] == field[6] == player_symbol)and (field[0] == '-' or field[3]=='-' or field[6]=='-'):
                for i in [0, 3, 6]:
                    if pustota(field, i):
                        field[i] = Ai_symbol
            elif (field[1] == field[4] == player_symbol or field[1] == field[7] == player_symbol or field[4] == field[7] == player_symbol) and (field[1] == '-' or field[4]=='-' or field[7]=='-'):
                for i in [1, 4, 7]:
                    if pustota(field, i):
                        field[i] = Ai_symbol
            elif (field[2] == field[5] == player_symbol or field[2] == field[8] == player_symbol or field[5] == field[8] == player_symbol) and (field[2] == '-' or field[5]=='-' or field[8]=='-'):
                for i in [2, 5, 8]:
                    if pustota(field, i):
                        field[i] = Ai_symbol
            elif (field[2] == field[4] == player_symbol or field[2] == field[6] == player_symbol or field[4] == field[6] == player_symbol) and (field[2] == '-' or field[4]=='-' or field[6]=='-'):
                for i in [2, 4, 6]:
                    if pustota(field, i):
                        field[i] = Ai_symbol
            elif (field[0] == field[4] == player_symbol or field[0] == field[8] == player_symbol or field[4] == field[8] == player_symbol) and (field[0] == '-' or field[4]=='-' or field[8]=='-'):
                for i in [0, 4, 8]:
                    if pustota(field, i):
                        field[i] = Ai_symbol
            else:
                k = []
                for i in range(9):
                    if field[i] == '-':
                        k.append(i)
                field[random.choice(k)] = Ai_symbol
print('Введите "старт" для начала игры')
if input()=='старт':
    if nomer_hoda_igroka == 0:
        print('Ты ходишь первый')
        print("Ты играешь за крестики")
    else:
        print('Компуктер ходит первый')
        print('Ты играешь за нолики')
    print('Координаты поля имеют вид:')
    print('0','1','2')
    print('3','4','5')
    print('6','7','8')
    print()
    pole(field)
    print()
    c = 0
    for i in range(9):
        c += 1
        if (i + nomer_hoda_igroka)%2==0:
            print('Введите координату')
            player_turn(field)
            pole(field)
            print()
            if end(field):
                print('Повезло-повезло')
                break
        else:
            AI_turn(field)
            pole(field)
            if end(field):
                print('Тебя даже эта железка обыграла!')
            print()
    if c == 9:
        print('Ничья')
else:
    print('это не старт(((')