from flask import Flask, render_template # pip3 install flask
app = Flask(__name__)

@app.route("/")
#@app.route("/home")
def home():
    #return "Hello from Flask!"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

