from flask import Flask,render_template
app = Flask(__name__)

todos = ['default']

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/addTodo",methods=["GET"])
def addTodo():
    todos.append(2)


@app.route("/deleteTodo",methods=["DELETE"])
def deleteTodo():
    return "deleted"

app.run()