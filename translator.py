from deep_translator import GoogleTranslator as GT
from os import system
import time

system('clear')

lang = input()   
txt = input('>>> ')

while txt!='q':
    try:    
        print(GT(source='auto', target=lang).translate(txt))
    except:
        print('Some thing went wrong ...')
        break
    txt = input('\n>>> ')
