def bark(name, wheight):
    if wheight > 20 :
        print(name, " says WOOF ,WOOF")
    else :
        print(name, "says woof, woof") 

bark('Codie', 40)
bark('Sparky', 9)
bark('Jackson', 12)
bark('Fido', 65)
    

def get_attribute(query, default):
  question = query + ' [' + default + ']? '
  answer = input(question)
  if (answer == ''):
      answer = default
  print('You chose', answer)
  return answer
hair = get_attribute('What hair color', 'brown')
hair_length = get_attribute('What hair length', 'short')
eye = get_attribute('What eye color', 'blue')
gender = get_attribute('What gender', 'female')
glasses = get_attribute('Has glasses', 'no')
beard = get_attribute('Has beard', 'no')