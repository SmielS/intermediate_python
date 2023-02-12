from view import menu, get_note_id, get_note_text, show_in_console, get_date
from datebase import create, get_notes_list, update_note, delete_note


def add_new():
    try:
        title, text = get_note_text()
        create(title, text)
        print('sucssess\n')
    except:
        print('addition error\n')


def view_all():
    try:
        all_notes = get_notes_list()
        show_in_console(all_notes)
    except:
        print('view error\n')


def edit():
    try:
        id = get_note_id()
        title, text = get_note_text()
        update_note(id, title, text)
        print('update sucssess\n')
    except:
        print('edition error\n')


def delete_note_by_id():
    try:
        id = get_note_id()
        delete_note(id)
    except:
        print('deliting error\n')

def view_by_date():
    try:
        date = get_date()
        filtered_notes = [note for note in get_notes_list() if note['date'].startswith(date)]
        if filtered_notes:
            show_in_console(filtered_notes)
        else:
            print(f'{date} 404\n')
    except:
        print('by_date error\n')


COMMANDS_LIST = {
    '1': add_new,
    '2': view_all,
    '3': view_by_date,
    '4': edit,
    '5': delete_note_by_id,
    '6': exit,
}


def start():
    is_running = True
    while is_running:
        command = menu()
        if command == '6':
            is_running = False
        else:
            try:
                COMMANDS_LIST[command]()
            except:
                print("application error\n")