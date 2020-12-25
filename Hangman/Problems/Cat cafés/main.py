num_cats = 0
cafe = ''
while True:
    ip = input()
    if ip == 'MEOW':
        print(cafe)
        break
    else:
        ip = ip.split(" ")
        if int(ip[1]) > num_cats:
            cafe = ip[0]
            num_cats = int(ip[1])
