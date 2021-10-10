# Built using vscode-ext

import sys
import vscode
from random import*
items = ['rock','paper','scissors']
rules = {'rock':'scissors','scissors':'paper','paper':'scissors'}
Rock_Paper_Scissors = vscode.Extension(name="Rock,Paper,Scissors", display_name="Rock,Paper,Scissors", version="0.1.0")

@Rock_Paper_Scissors.event
def on_activate():
    return f"The Extension '{Rock_Paper_Scissors.name}' has started"
@Rock_Paper_Scissors.command()
def rock():
    p_i = 'rock'
    computer = choice(items)
    if p_i == computer:
        vscode.window.show_info_message(f'We Drew')
    elif rules[p_i] == computer:
        vscode.window.show_info_message(f'You Won i chose {computer}')
    else:
        vscode.window.show_info_message(f'I Won i chose {computer}')

@Rock_Paper_Scissors.command()
def paper():
    p_i = 'paper'
    computer = choice(items)
    if p_i == computer:
        vscode.window.show_info_message(f'We Drew')
    elif rules[p_i] == computer:
        vscode.window.show_info_message(f'You Won i chose {computer}')
    else:
        vscode.window.show_info_message(f'I Won i chose {computer}')

@Rock_Paper_Scissors.command()
def scissors():
    p_i = 'scissors'
    computer = choice(items)
    if p_i == computer:
        vscode.window.show_info_message(f'We Drew')
    elif rules[p_i] == computer:
        vscode.window.show_info_message(f'You Won i chose {computer}')
    else:
        vscode.window.show_info_message(f'I Won i chose {computer}')



def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()
