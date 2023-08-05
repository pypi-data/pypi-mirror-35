from flask import Flask, render_template, send_from_directory
import json
from movielst import config
from web.forms import SettingsForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'not really secret but still a really useless secret key for this use case'


def main():
    app.run(debug=False)


@app.route('/')
def index():
    with open(config.get_setting('Index', 'location') + 'movies.json', 'r') as file:
        data = json.loads(file.read())

    return render_template('home.html', movie_list=data)


@app.route('/movie/<variable>')
def movie(variable):
    with open(config.get_setting('Index', 'location') + 'movies.json', 'r') as file:
        data = json.loads(file.read())
    i = 0
    list = {}
    for datas in data:
        if datas["title"] == variable:
            list["title"] = datas["title"]
            list["genre"] = datas["genre"]
            list["imdb"] = datas["imdb"]
            list["runtime"] = datas["runtime"]
            list["tomato"] = datas["tomato"]
            list["year"] = datas["year"]
            list["awards"] = datas["awards"]
            list["cast"] = datas["cast"]
            list["director"] = datas["director"]
        i += 1
    return render_template('movie.html', list=list)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    form = SettingsForm()
    form.log_level_field.default = config.get_setting('General', 'log_level')
    form.log_location_field.default = config.get_setting('General', 'log_location')
    form.location_field.default = config.get_setting('Index', 'location')
    form.use_external_api_field.default = config.get_setting('API', 'use_external_api')
    form.omdb_api_key_field.default = config.get_setting('API', 'OMDb_API_key')
    form.tmdb_api_key_field.default = config.get_setting('API', 'TMdb_API_key')
    if form.validate_on_submit():
        config.update_config('General', 'log_level', form.log_level_field.data)
        config.update_config('General', 'log_location', form.log_location_field.data)
        config.update_config('Index', 'location', form.location_field.data)
        config.update_config('API', 'use_external_api', form.use_external_api_field.data)
        config.update_config('API', 'OMDb_API_key', form.omdb_api_key_field.data)
        config.update_config('API', 'TMdb_API_key', form.tmdb_api_key_field.data)
    form.process()
    return render_template('settings.html', form=form)


@app.route('/movie/play/<variable>')
def play(variable):
    return send_from_directory('/', variable)


if __name__ == '__main__':
    main()
