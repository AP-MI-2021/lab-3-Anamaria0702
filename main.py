def show_menu():
    print("1. Citire date")
    print("2. Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sunt pare")
    print("3. Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele au acelasi numar de divizori")
    print("4. Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sunt palindroame")
    print("5. Iesire")

def read_list():
    lst=[]
    lst_str = input("Dati numerele separate prin spatiu:")
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def is_even():
    '''
    Determina daca numarul dat este par
    :param n: numarul dat
    :return: daca este par returneaza True daca nu este par returneaza False
    '''
    if n % 2 == 0:
        return True
    return False

def test_is_even():
    assert is_even(5) == False
    assert is_even(4) == True
    assert is_even(8) == True
    assert is_even(7) == False

def get_even():
    '''
    Determina daca toate numerele sunt pare
    :param lst: lista de numere
    :return: o lista cu numere pare
    '''
    result = []
    for num in lst:
        if is_even(num):
            result.append(num)
    return result

def get_longest_all_even(lst):
    '''
    Determina cea mai lunga subsecventa a unei liste cu proprietatea ca toate numerele sunt pare
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''
    nr = len(lst)
    result = []
    for st in range(nr):
        for dr in range(st, nr):
            all_even = True
            for num in lst[st:dr + 1]:
                if num % 2 != 0:
                    all_even = False
                    break
            if all_even:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result

def test_get_longest_all_even():
    assert get_longest_all_even([1,4,5,6,8,10]) == [6,8,10]
    assert get_longest_all_even([ 100 , 122 , 154 ,211]) == [100,122,154]
    assert get_longest_all_even([50,60,70,71,88]) == [50,60,70]

def is_nr_div(n):
    '''
    Determina numarul de divizori al numarului dat
    :param n: Numarul dat
    :return: Variabila k care returneaza numarul total de divizori al numarului.
    '''
    k = 0
    x = n
    for i in range (1 , x + 1):
        if x % i == 0:
            k = k+1
    return k

def test_is_nr_div():
    assert is_nr_div(11) == 2
    assert is_nr_div(8) == 4
    assert is_nr_div(5) == 2

def get_nr_div(lst):
    '''
    Determina daca toate numerele au acelasi numar de divizori
    :param lst: O lista cu numere
    :return: O lista cu numerele care au acelasi numar de divizori
    '''
    result = []
    for num in lst:
        if is_nr_div(num):
            result.append(num)
    return result

def get_longest_same_div_count(lst):
    '''
    Determina cea mai lunga subsecventa in care numerele au acelasi numar de divizori
    :param lst: Lista in care se cauta subsecventa
    :return: Subsecventa gasita
    '''
    nr = len(lst)
    result = []

    for st in range(nr):
        for dr in range(st, nr):
            k=is_nr_div(lst[st])
            all_same_div_count= True
            for num in lst[st:dr + 1]:
                if is_nr_div(num)!=k:
                    all_same_div_count = False
                    break
            if all_same_div_count:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result

def test_get_longest_same_div_count():
    assert get_longest_same_div_count([7 , 5, 2 , 3 , 80]) == [7,5,2,3]
    assert get_longest_same_div_count([12,45, 2,]) == [12,45]
    assert get_longest_same_div_count([14,8, 3, 202]) == [14,8]

def is_palindrome(n):
    '''
    Determina daca numarul dat este palindrom
    :return: True daca este palindrom si false daca nu este palindrom
    '''
    inv = 0
    x = n
    ogl = 0
    while n != 0:
        ogl = ogl * 10 + n % 10
        n = n // 10
    if x == ogl:
        return True
    elif x != ogl:
        return False

def test_is_palindrome():
    assert is_palindrome(1) == True
    assert is_palindrome(25) ==False
    assert is_palindrome(9779) == True
    assert is_palindrome(323) == True

def get_palindrome():
    '''
    Determina numerele care sunt palindroame din lista
    :param lst: O lista de numere
    :return: O lista cu numere palindrome
    '''
    result = []
    for num in lst:
        if is_palindrome(num):
            result.append(num)
    return result

def get_longest_all_palindromes(lst):
    '''
    Determina cea mai lunga subsecventa in care numerele sunt palindroame
    :param lst: Lista in care se cauta subsecventa
    :return: Subsecventa gasita
    '''
    nr = len(lst)
    result = []
    for st in range(nr):
        for dr in range(st, nr):
            all_palindrome = True
            for num in lst[st:dr + 1]:
                if is_palindrome(num) == False:
                    all_palindrome = False
                    break
            if all_palindrome:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([252,727,989 ,1,3]) == [252,727,989,1,3]
    assert get_longest_all_palindromes([31, 424,9889,200]) == [424,9889]
    assert get_longest_all_palindromes([ 1,3,2, 252,722]) == [1,3,2,252]

def main():
    lst=[]
    while True:
        show_menu()
        cmd=input("Comanda: ")
        if cmd == "1":
            lst = read_list()
        elif cmd == "2":
            print(get_longest_all_even(lst))
        elif cmd == "3":
            print(get_longest_same_div_count(lst))
        elif cmd == "4":
            print(get_longest_all_palindromes(lst))
        elif cmd == "5":
            break
        else:
            print("Comanda invalida.")


if __name__ == '__main__':
    main()