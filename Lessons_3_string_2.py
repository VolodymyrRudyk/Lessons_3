S = 'A\nB\tC'               #\n - це кінець строки, а \t - це табуляція
print(S)

print(len(S))               #\n i \t є тільки одним символом
print(ord('\n'))            #\n - це один символ, який кодується як десятиричне значення 10

S = 'A\0B\0C'               #\0 - це байт з двійковими нулями, не завершує строку
print(S)

print(len(S))

msg = """                                       
aaaaaaaaaaaaaa
bbbbb'''bbbbbbbbbbb""bbbbbbbbbb'bbbbb
cccccccccccc
"""                                         #""" - такі лапки довзволяють виводити все так як написав програміст
print(msg)