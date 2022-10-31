import time

d = input('''Poll kiriting
Man
Woman
''')
def jinsi():
    if d.lower() == "man":
        for x in range(30):
            time.sleep(0.2)
            print("o'g'li")
    elif d.lower() == "woman":
        for x in range(30):
            time.sleep(0.2)
            print("qizi")
    else:
        print("Error")                


