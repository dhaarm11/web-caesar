from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <form method="post" >
        <label for="rot">Rotate By:</label>
        <input type="text" name="rot" value="0"/>
        <textarea type="text" name="text">{0}</textarea>
        <input type="submit" value="Submit Query"/>
    </form>
</html>
"""

header ="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <form method="post" >
        <label for="rot">Rotate By:</label>
        <input type="text" name="rot" value="0"/>       
        <textarea type="text" name="text">"""
footer="""        
        </textarea>
        <input type="submit" value="Submit Query"/>
    </form>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    rot = int(rot)
    
    encrypted = rotate_string(text , rot)

    content = form.format(encrypted)
    return content

@app.route("/")
def index():
    encrypted = ""
    content = form.format(encrypted)

    return content

app.run()