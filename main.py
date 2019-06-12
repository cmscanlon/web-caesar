from flask import Flask

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
            <form action="" method="post">
                <label for="rotation">Rotate By:</label>
                <input type="text" name="rot" id="rotation" default value="0" />
                <textarea name="text"> </textarea>
                <input type="submit" />
            </form>
        </body>
</html>                    
"""

@app.route("/")
def index():
    return form

app.run()    