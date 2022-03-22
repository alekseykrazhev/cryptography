import math
import numpy as np

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_rus = ['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я','.',',',' ','?']


def move_enc(key, mes):
    if not check_move_key(key):
        print ('Invalid key!')
        quit(-1)
    enc = ''
    for i in mes:
        x = alphabet.index(i)
        y = (x + key) % 26
        i1 = alphabet[y]
        enc += i1
    return enc


def move_dec(key, mes):
    dec = ''
    for i in mes:
        y = alphabet.index(i)
        x = (y - key) % 26
        i1 = alphabet[x]
        dec += i1
    return dec


def is_perfect_square(n): return (n ** .5).is_integer() 


size = 0
def hill_key(text):
    if not is_perfect_square(len(text)):
        print('Invalid Hill key!')
        quit(-1)
    global size
    size = int(math.sqrt(len(text)))
    val = []
    for i in text:
        indx = alphabet_rus.index(i)
        val.append(indx)
    matrix = np.array(val).reshape(size, size)
    return matrix


def hill_enc(text, message):
    key = hill_key(text)

    parts = []
    part = []
    for i in range(1, len(message) + 1):
        a = message[i - 1]
        indx = alphabet_rus.index(a)
        part.append(indx)
        if i % 3 == 0:
            parts.append(part)
            part = []
    while len(part) < size:
        part.append(35)
    parts.append(part)
    parts_n = np.array(parts)

    enc = []
    for i in range(len(parts_n)):
        enc.append(parts_n[i].dot(key) % 37)
    
    enc_n = np.array(enc)
    encoded = ''
    for i in range(len(parts)):
        for j in enc_n[i]:
            a = alphabet_rus[j]
            encoded += a
    
    return encoded


def gcd_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)


def hill_dec(text, message):
    key = hill_key(text)

    parts = []
    part = []
    for i in range(1, len(message) + 1):
        a = message[i - 1]
        indx = alphabet_rus.index(a)
        part.append(indx)
        if i % 3 == 0:
            parts.append(part)
            part = []
    if not len(part) == 0: 
        while len(part) < 3:
            part.append(35)
        parts.append(part)
    parts_n = np.array(parts)

    k = round(np.linalg.det(key))

    d, x, y = gcd_extended(k, 37)
    
    det = 0
    if k < 0 and x > 0:
        det = x
    if k > 0 and x < 0:
        det = 37 + x
    if k > 0 and x > 0:
        det = x
    if k < 0 and x < 0:
        det = -x
    
    neg = np.linalg.inv(key)
    nn = neg * k
    for i in range(len(nn)):
        for j in range(len(nn[i])):
            nn[i][j] %= 37 * np.sign(nn[i][j])
    
    nn = nn.transpose()
    nn *= det
    for i in range(len(nn)):
        for j in range(len(nn[i])):
            nn[i][j] %= 37 * np.sign(nn[i][j])
    nn = nn.transpose()

    for i in range(len(nn)):
        for j in range(len(nn[i])):
            if nn[i][j] < 0:
                nn[i][j] += 37

    dec_part = []
    decoded = ''
    for i in range(len(parts_n)):
        dec_part.append(parts_n[i].dot(nn) % 37)
        
    dec_part_n = np.array(dec_part)
    for i in range(len(dec_part_n)):
        for j in dec_part_n[i]:
            decoded += alphabet_rus[round(j)]

    return decoded


def check_move_key(key):
    if key < 0 or key > 26:
        return False
    return True


'''
функция взлома простым подбором ключа
'''
def break_ceasar_selection(enc):
    dec = ''
    for j in range(26):
        dec = ''
        for i in range(len(enc)):
            y = alphabet.index(enc[i])
            indx = (y - j) % 26
            char = alphabet[indx]
            dec += char
        print('Decrypted: ', dec, ', key = ', j)
    return True

'''
Взлом шифра сдвига с применением частотного анализа
'''
def break_ceasar(enc):
    count = 0
    frequency = []

    for i in range(26):
        for j in enc:
            if j == alphabet[i]:
                count += 1
        count = count * 100 / len(enc)
        frequency.append(count)
        count = 0

    maximum = 0
    for i in range(25):
        if frequency[i+1] > frequency[i]:
            maximum = frequency[i+1]
    
    store_maxes = []
    for i in range(26):
        if frequency[i] == maximum:
            store_maxes.append(i)
    
    for i in store_maxes:
        key = abs(i - 4)
        dec_check = move_dec(key, enc)
        print(dec_check)
    
    answer = input('Is there what youre looking for? (y or n)')
    if answer == 'y':
        return True
    if answer == 'n':
        print('Starting a simple selection algorithm...')
        break_ceasar_selection(enc)
    else: 
        print('invalid input!')

    return False


if __name__ == '__main__':
    inp_key = open('key.txt', 'r')
    inp_mes = open('message.txt', 'r')
    out_encrypted = open('encrypted.txt', 'w')
    out_decrypted = open('decrypted.txt', 'w')

    key = int(inp_key.read())
    key_hill = 'АЛЬПИНИЗМ'
    message = inp_mes.readline()

    encrypted_m = move_enc(key, message)
    encrypted_h = hill_enc(key_hill, 'ЗАШИФРОВАННЫЙ ТЕКСТ')
    print('Hill encryption: ', encrypted_h)
    out_encrypted.write('First encryption result:\n\t')
    out_encrypted.write(encrypted_m)
    out_encrypted.write('\nSecond encryption result:\n\t')
    out_encrypted.write(encrypted_h)

    out_encrypted.close()

    decrypted_h = hill_dec(key_hill, encrypted_h)
    out_decrypted.write('Decryption results:\n\t')
    out_decrypted.write(move_dec(key, encrypted_m))
    print ('Hill decription: ', decrypted_h)

    out_decrypted.close()

    print('Trying to break Ceasar encryption...')
    break_ceasar(encrypted_m)
    print('Programm executed correctly!')
