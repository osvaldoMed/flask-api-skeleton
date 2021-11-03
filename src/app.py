from api import create_app
from config import Config as config

app = create_app(config)

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )