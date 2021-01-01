from ams import create_app
from ams.models import *


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)