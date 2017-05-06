from main import UserStory


def import_database(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data


def import_database_objects(filename):
    data = import_database(filename)
    data = [d.replace('\n', '').split(',') for d in data]
    stories = [UserStory(*d) for d in data]
    return stories


def export_data(filename, data):
    with open(filename, 'w') as file:
        data = ''.join(data)
        file.write(data)

