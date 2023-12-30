from flask import Flask,render_template,request, url_for
app = Flask(__name__)

todos = ['default']

@app.route("/")
def hello_world():
    return render_template('index.html',todos=todos)

@app.route("/addTodo",methods=["POST"])
def addTodo():
    todos.append(request.form.get('todo'))
    return render_template('index.html',todos=todos)

@app.route("/deleteTodo", methods=["POST"])
def deleteTodo():
    if request.method == "POST":
        todo = request.form.get("todo")
        todos.remove(todo)
        return render_template('index.html',todos=todos)


app.run(debug=True)