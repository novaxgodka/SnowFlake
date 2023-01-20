
class SnowFlake:
    def __init__(self, s):   # Инициализация параметра s (сторона квадрата)
        self.square_side = s
        if int(self.square_side) % 2 != 0: # Проверка корректности данных
            self.square_side = int(s)
        else:
            raise ValueError('Ошибка! Число четное и/или не целое, повторите попытку!!!') # Выдает ошибку, если данные некорректны

    def thaw(self, n): # Создание метода таяния
        if n > (self.square_side//2):
            print('Снежинка расстаяла полностью')
        else:
            self.square_side -= n
            print(f'Снежинка расстаяла на {n} и теперь равна {self.square_side}')

    def freeze(self, n): # Создание метода заморозки
        self.square_side = n*2 + self.square_side
        print(f'Снежинка стала размером {self.square_side}')

    def show(self): # Создание метода показа квадрата, в методе выполняется добавление скелета снежинки в матрицу и дальнейший ее вывод
        meridian = int(((self.square_side - 1) / 2) + 1)
        start_step = 1
        snow_str = ''
        snow_matrix = []
        for j in range(1, meridian+1):
            for i in range(1, meridian):
                if i == start_step:
                    snow_str = snow_str + '*'
                else:
                    snow_str = snow_str + '-'
            snow_matrix.append([snow_str+'*'+snow_str[::-1]])
            snow_str = ''
            start_step += 1
        new_snow_matrix = []
        for i in snow_matrix[::-1]:
            new_snow_matrix.append(i)
        snow_matrix = snow_matrix + new_snow_matrix[1:]
        for j in snow_matrix:
            print(j[0])

    def __str__(self):   #уточнение стороны квадрата
        return f'На данный момент, сторона квадрата равна {self.square_side}'


inputing_snow_size = input('Привет! для создания снежинки, введи пожалуйста размер стороны квадрата, только есть '
                           'условние, число должно быть нечетным и целым...\nВведи число - ')
snow = SnowFlake(inputing_snow_size)
client_input = ''
while client_input != 'Stop':
    print('')
    print('#'*10)
    client_input = input('Что сделаем со снежинкой? Напиши "thaw", что бы подогреть снежинку и она немного расстает;\n'
                   'Напиши "freeze", что бы подморозоить снежинку;\n'
                   'Напиши "show", что бы посмотреть как выглядит снежинка;\n'
                   'Напиши "snow", что бы узнать, какого размера сейчас снежинка;\n'
                   'И наконец, если хочешь выйти из программы, напиши "Stop"!\n'
                         'Твой выбор - ')
    if client_input == "thaw":
        print('')
        print('#' * 10)
        print('')
        snow.thaw(n=int(input('На сколько подогреем снежинку? ')))
    elif client_input == "freeze":
        print('')
        print('#' * 10)
        print('')
        snow.freeze(n=int(input('На сколько заморозим снежинку? ')))
    elif client_input == "show":
        print('')
        print('#' * 10)
        print('')
        snow.show()
    elif client_input == "Stop":
        print('')
        print('#' * 10)
        print('')
        print('Пока!')
    elif client_input == "snow":
        print('')
        print('#' * 10)
        print('')
        print(snow)
