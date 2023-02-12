import json
from datetime import datetime
from model import Note


DATABASE_NAME = 'notepad.json'


def write_to_database(data):
    with open(DATABASE_NAME, 'w', encoding='UTF-8') as base:
        json.dump(data, base, indent=2)


def get_notes_list():
    with open(DATABASE_NAME, 'r', encoding='UTF-8') as base:
        data = []
        try:
            data = json.load(base)
        except:
            print('party started\n')
        return data



def create_id_number(all_notes):
    id = 1
    for note in all_notes:
        if note['id'] >= id:
            id = note['id'] + 1
    return id


def create(title, text):
    all_notes = get_notes_list()
    id = create_id_number(all_notes)
    new_note = Note(id, title, text)
    all_notes.append(new_note.__dict__)
    write_to_database(all_notes)


def update_note(id, title, text):
    data = get_notes_list()
    is_updated, i = False, 0
    while not is_updated and i < len(data):
        if data[i]['id'] == id:
            data[i]['title'] = title
            data[i]['text'] = text
            data[i]['date'] = datetime.now().strftime("%d.%m.%Y %H:%M")
            is_updated = True
        i += 1
    if is_updated:
        write_to_database(data)
    else:
        print(f'note id = {id} 404')


def delete_note(id):
    data = get_notes_list()
    is_deleted, i = False, 0
    while not is_deleted and i < len(data):
        if data[i]['id'] == id:
            data.pop(i)
            is_deleted = True
        i += 1
    if is_deleted:
        print(f'id = {id} has been deleted')
        write_to_database(data)
    else:
        print(f'id = {id} 404')