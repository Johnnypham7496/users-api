import pathlib
import connexion    
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


basedir = pathlib.Path(__file__).parent.resolve()
connexion_app = connexion.App(__name__, specification_dir=basedir)


app = connexion_app.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(basedir / 'db/local_sqlite/people.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)