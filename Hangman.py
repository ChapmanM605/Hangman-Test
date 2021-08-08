import random

def replace_char_at_index(org_str, index, replacement):
    new_str = org_str
    if index < len(org_str):
        new_str = org_str[0:index] + replacement + org_str[index + 1:]
    return new_str

start = 0
f = open('word_list.txt', 'r')
file_data = f.read()
source_words = list(map(str, file_data.split()))
f.close()
question = (random.choice(source_words))

length = len(question)

str = ""
user_display = str.ljust(length, '*')
print ('Lets go, here is your word:', user_display)

while '*' in user_display and start <= 6:
    guess = input("Please enter your next guess: ")

    if guess in question:
        result1 = []
        for i in range(len(question)):
            if (question[i] == guess):
                result1.append(i)
                for index in result1:
                    user_display = replace_char_at_index(user_display, index, guess)
        print ('Well done! You are smashing it! Your word remains:', user_display)
    else:
        start += 1
        print ('Unlucky! Your word remains:', user_display)

if start >= 6:
    print('You lose')
elif '*' not in user_display:
    print ('Congratulations you win')
