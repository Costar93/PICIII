from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    if request.method== "GET":
        name = {'first_name':'francesc', 'surname':'guitart'}
        return '''
        
        <h2>Hello! ''' + name['first_name'] + ''' ''' + name['surname'] + ''' </h2>
        
        
        '''

if __name__ == '__main__':
    app.run('0.0.0.0')
