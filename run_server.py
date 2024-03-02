# run application
from main import create_app
from models import db

app = create_app()
db.create_all(app)
app.run(port=8888, debug=True)
