from flask import Flask
# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
@app.route('/')
def hello():
    a = '                                 Hello Person!'
    a += '\n'
    a += ('                    Please type in a fake news source here:\n')
    a += ("----------------------------------------------------------------" + '\n')
    a += ("         |                                                                |\n")
    a += ("         |                                                                |\n")
    a += ("----------------------------------------------------------------" + '\n')
    a += '\n'
    a += ('                        Thanks for playing! :)\n')
    a += '\n'
    a += ('                 Made by Ian, Brendan, Gordon, Kevin\n')
                
    b = '<center><h1>Please enter a URL you wish to check</h1><br/><input placeholder="http:://www.example.com/"/></center>'
    """Return a friendly HTTP greeting."""
    return b

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
