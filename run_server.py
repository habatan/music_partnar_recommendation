# run application
from club_activity_app.app import create_app

app = create_app()
app.run(port=8888)
