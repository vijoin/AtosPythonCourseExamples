from flask import Flask, jsonify

app = Flask(__name__)

context = {
        'title': 'Home',
        'posts': [
            {
                'author': {'username': 'Jhon'},
                'body': 'Beautiful day in Portland!',
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie was so cool!',
            },
        ]
               }

@app.route('/')
def hello_world():
    #return "Hello World"
    return jsonify(context)

if __name__ == '__main__':
    app.run(port=8080)