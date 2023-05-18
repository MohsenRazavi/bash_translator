from deep_translator import GoogleTranslator as GT
from os import system
import time

system('clear')

lang = input('target lang (Fa/*): ')   
txt = input('>>> ')
if not lang:
    lang = 'fa'

while txt!='q':
    try:    
        print(GT(source='auto', target=lang).translate(txt))
    except:
        print('Some thing went wrong ...')
        break
    txt = input('\n>>> ')
