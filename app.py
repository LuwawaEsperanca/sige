from flask import Flask

from blueprints.admin.views import main
from blueprints.user.views import user
from blueprints.guest.guest import guest

app = Flask(__name__)

app.secret_key = "12383@%@£§§½£½"

app.register_blueprint(main)
app.register_blueprint(user)
app.register_blueprint(guest)


if __name__ == '__main__':
    app.run(debug=True)