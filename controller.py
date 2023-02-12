from view import menu, get_note_id, get_note_text, show_in_console
from datebase import create, get_notes_list, update_note, delete_note


def add_new():
    try:
        title, text = get_note_text()
        create(title, text)
        print('sucssess')
    except:
        print('addition error')


def view_all():
    try:
        all_notes = get_notes_list()
        show_in_console(all_notes)
    except:
        print('view error')


def edit():
    try:
        id = get_note_id()
        title, text = get_note_text()
        update_note(id, title, text)
        print('update sucssess')
    except:
        print('edition error')


def delete_note_by_id():
    try:
        id = get_note_id()
        delete_note(id)
    except:
        print('deliting error\n')



COMMANDS_LIST = {
    '1': add_new,
    '2': view_all,
    '3': edit,
    '4': delete_note_by_id,
    '5': exit,
}


def start():
    is_running = True
    while is_running:
        command = menu()
        if command == '5':
            is_running = False
        else:
            try:
                COMMANDS_LIST[command]()
            except:
                print("application error\n")