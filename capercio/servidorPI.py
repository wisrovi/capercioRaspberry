from flask import Flask, request
import os


# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


def invocarCerrarNavegador():
    print("cerrando quesito")
    os.system("pkill chromium & exit")

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded        
    if request.method == 'POST':
        print("solicitud POST")
        datoControl = request.form['namePost']
        if datoControl[:1] == "N":
            invocarCerrarNavegador()    
    return '''
    <!doctype html>
	<h1>Servidor POST PI</h1>
    '''
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)
    