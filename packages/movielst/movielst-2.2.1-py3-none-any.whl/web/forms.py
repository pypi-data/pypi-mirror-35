from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SettingsForm(FlaskForm):
    log_level_field = StringField('Log level')
    log_location_field = StringField('Log location')
    location_field = StringField('Index location')
    use_external_api_field = StringField('External API')
    omdb_api_key_field = StringField('OMDb API key')
    tmdb_api_key_field = StringField('TMDb API key')
    submit = SubmitField('Save')
