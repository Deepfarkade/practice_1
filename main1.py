from flask import Flask

app = Flask(__name__) #constructor of the flask

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/my_name/<name>")
def print_name(name):
    return f"Happy Leaning {name} in Praxis BLR" 

if __name__ == "__main__":
    app.run(debug = True)