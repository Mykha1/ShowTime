def answer(result, err):
    if result == 0: return 'IP-адрес корректен.'
    if result == 1: return err + '— это не целое число'
    if result == 2: return err + ' превышает 255.'
    return 'Адрес — это четыре числа, разделённые точками.'


def check(i):
    value = 1
    if not i.isdigit():return value
    value = 2
    if int(i) > 255:return value
    return 0


ip_adress = input('Введите IP:').split('.')
value, num, i = len(ip_adress),'', 0
for num in ip_adress:
    if value != 4 and i == 0: break
    i += 1
    value = check(num)
    if value != 0: break
print(answer(value, num))


