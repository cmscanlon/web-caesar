from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

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
            <form action="" method="POST">
                <div>
                    <label for="rotation">Rotate By:</label>
                    <input type="text" name="rot" value='0' />
                </div>
                <div>
                    <textarea type="text" name="text"> </textarea>
                    <br>
                    <input type="submit" />
                </div>    
            </form>
        </body>
</html>                    
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form["text"]
    rot = request.form["rot"]
    #encrypted = ''
    encrypted = rotate_string(text, int(rot))   

    return encrypted

app.run()    
