from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hey():
#     return f'Hello from Flask!'

# the below code worked well
# @app.get('/home')
# def getting_get():
#     return "Hey, it's Robin I was wondering if GET request works"


# testing Post request ## it was ... [ ]
@app.route('/add_friend', methods=['GET'])
def new_friend():
    name = " Josphert Mumo"
    return f'This was a crazy dude back in school{name}'