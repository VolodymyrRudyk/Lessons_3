S = 'spam'

print(dir(S))                           #вивід на екран справки

print(S + 'NI!')                        #Конкатинація
print(S.__add__('NI!'))                 #також конкатинація строк

print(help(S.replace))                  #справка по встроєній функції replace