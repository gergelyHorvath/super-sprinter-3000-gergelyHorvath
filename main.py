from flask import Flask, render_template, request, redirect
import data_manager


app = Flask(__name__)


class UserStory:
    def __init__(self, storytitle, userstory, acceptcrit, business, time, status):
        self.storytitle = storytitle
        self.userstory = userstory
        self.acceptcrit = acceptcrit
        self.business = business
        self.time = time
        self.status = status


@app.route('/')
def root():
    stories = data_manager.import_database_objects(filename)
    return render_template('list.html', stories=stories)


@app.route('/story')
def new_entry():
    default = UserStory('', '', '', '100', '2.5', 'Review')
    return render_template('form.html', story=default, string=' -Add new Story', idx='0', button='Create')


@app.route('/story/<idx>')
def edit_user_story(idx):
    story_to_edit = data_manager.import_database_objects(filename)[int(idx) - 1]
    return render_template('form.html', story=story_to_edit, string=' -Edit Story', idx=idx, button='Update')


@app.route('/modify/<idx>')
def write_new_entry(idx):
    new_entry = ','.join(request.args.values()) + '\n'
    data = data_manager.import_database(filename)
    if idx == '0':
        data.append(new_entry)
    else:
        data[int(idx) - 1] = new_entry
    data_manager.export_data(filename, data)
    return redirect('/')


@app.route('/delete/<idx>')
def delete(idx):
    data = data_manager.import_database(filename)
    data.pop(int(idx) - 1)
    data_manager.export_data(filename, data)
    return redirect('/')


if __name__ == '__main__':
    filename = 'database.csv'
    app.run()
