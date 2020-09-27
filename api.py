import flask 

app= flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/',methods=['GET'])
def home():
    return "<H1>Hello Work Welcome to Flask Based Api </H1>"

app.run()
