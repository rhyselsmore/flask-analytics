Flask Analytics
===============

Analytics Package. Definitely not for sending your data to PRISM. At all.

## Setup

Like so!

```
from flask import Flask
from flask_analytics import Analytics

app = Flask(__name__)
Analytics(app)

@app.route('/')
def index():
    return "woop!"

if __name__ == "__main__":
    app.debug = True
    app.run()
```