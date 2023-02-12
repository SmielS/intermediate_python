from datetime import datetime


COMMANDS_LIST = {
    '1': 'add new',
    '2': 'view all',
    '3': 'edit',
    '4': 'delete',
    '5': 'exit',
}


def menu():
    print('select a menu item\n')
    for key, value in COMMANDS_LIST.items():
        print(f'{key} - {value}')
    print()
    while True:
        choice = input('enter a number: ')
        if choice in COMMANDS_LIST:
            return choice
        else:
            print('try again\n')


def get_note_id():
    while True:
        id = input('enter id: ')
        try:
            return int(id)
        except:
            print(f'{id} is not number. Try again')


def get_note_text():
    title_required, text_required = True, True
    while title_required:
        title = input('Enter head ')
        if title:
            title_required = False
    while text_required:
        text = input('enter body ')
        if text:
            text_required = False
    return title, text


def print_note(note):
    print(f'ID: {note["id"]}\n{note["title"].upper()}\n{note["text"]}\nupdate time:{note["date"]}')


def show_in_console(data):
    if isinstance(data, list):
        for note in data:
            print_note(note)
            print()
    if isinstance(data, dict):
        print_note(data)
    print()