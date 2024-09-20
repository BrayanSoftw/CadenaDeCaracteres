name = 'Brayan'
lastName = "Hormiga"
fullName = name + " " + lastName
print(fullName)
#Format String
price = 97
text3 = f"The price is {price: .2f} dollars "
print (text3)
#Math operation
text4 = f'La multiplicacion es {20 * 59}'
print (text4)
#String capitalize()
text5 = 'python es un lenguaje de alto nivel en programacion'
result1 = text5.capitalize()
print (result1)
#String casefold()
title = 'Cien Años de Soledad'
titleConvert = title.casefold()
print (titleConvert)
#String center()
fruit = 'banana'
textCenter = fruit.center(20, '*')
print(textCenter)
#String count()
title1 = 'I love apples, apple are my favorite fruit'
result2 = title1.count('apple')
print (result2)
#String endswith, COMPRUEBA SI HAY UN SIGNO DE PUNTUACION
text6 = 'Curso, fundamentos con Python.'
result3 = text6.endswith('.')
print(result3)
#String expandtabs
letter = 'F\tU\tP'
letterSpaces = letter.expandtabs(2)
print(letterSpaces)
#String Find
text7 = 'Hola, bienvenidos a Colombia.'
result4 = text7.find('bienvenidos')
print ("La cantidad es "+str(result4))
#Funcion title
text8 = 'welcome to my world'
result5 = text8.title()
print(result5)
#Funcion isalnum
alphanumeric = 'Python312'
result6 = alphanumeric.isalnum()
print(result6)
#Funcion Isalpha
letters = 'Space X'
result7 = letters.isalpha()
print(result7)
