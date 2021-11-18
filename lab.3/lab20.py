'''
#20.1
def translate(text):
    vowel = ['А', 'О', 'Э', 'Е', 'И', 'Ы', 'У', 'Ё', 'Ю', 'Я',
             'а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я',
             ',', '.', '!', '?', '-']
    for x in text:
        if x in vowel:
            text = text.replace(x, '')
    print('translatedText == "' + ' '.join(text.split()) + '"')
'''

'''
#20.2
def setup_profile(name, vacationDates):
    global Name
    Name = name
    global date
    date = vacationDates


def print_application_for_leave():
    print('Заявление на отпуск в период', date + '.', Name)


def print_holiday_money_claim(amount):
    print('Прошу выплатить', amount, 'отпускных денег', Name)


def print_attorney_letter(toWhom):
    print('На время отпуска в период', date, 'моим заместителем назначается',
          toWhom + '.', Name)


setup_profile("Иван Петров", "1 июня – 20 июня")
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim("15 тысяч пиастров")
print_attorney_letter("Василий Васильев")
'''

'''
#20.3
messages = []
def print_only_new(message):
    if message not in messages:
        messages.append(message)
        print(message)
'''

'''
#20.5
def lucky(s):
    s = str(s)
    if sum([int(char) for char in s[:3]]) == sum([int(char) for char in s[-3:]]):
        return "Счастливый"
    else:
        return "несчастливый"


lastTicket = 123321
print(lucky(lastTicket))
'''
