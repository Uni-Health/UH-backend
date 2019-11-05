import json
from flask import Flask, request, render_template, jsonify
from sqlalchemy.ext import mutable

app = Flask(__name__, static_url_path='/dist')
app.config.from_pyfile(os.path.abspath('app.cfg'))
db = SQLAlchemy(app)

# class for parse json file into db
class JsonEncodedDict(db.TypeDecorator):
    impl = db.Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return '{}'
        else:
            return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return {}
        else:
            return json.loads(value)

mutable.MutableDict.associate_with(JsonEncodedDict)