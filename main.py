from flask import flask

app = Flask(__name__)
app.config['DEBUG'] = True

def form():

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px san-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        
    </body>
</html>                    


@app.route("/")
def index():
    return "Hello World"

app.run()    