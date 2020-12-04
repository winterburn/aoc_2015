from hashlib import md5


input = 'yzbqklnj'
number = 0
while True:
    hex = md5()
    hex.update(f'{input}{number}'.encode('utf-8'))
    if hex.hexdigest()[:6] == '000000':
        break
    number += 1
print(number)
