calls = 0
def count_calls():
    global calls
    print(calls)

def string_info(a):
    string = len(a)
    global calls
    calls += 1
    print((string, a.upper(), a.lower()))

def is_contains(a, b=()):
    a = a.upper()
    c = [x.upper() for x in b]
    global calls
    calls += 1
    if a in c:
        print(True)
    else:
        print(False)


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
count_calls()
