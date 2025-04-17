from flask import Flask, render_template

app = Flask(__name__)

users = {
    1: {"name": "Ala", "age": 22},
    2: {"name": "Bartek", "age": 25},
    3: {"name": "Celina", "age": 30}
}


@app.route("/")
def hello():
    return render_template('home.html')


@app.route("/about")
def about():
    return "About us<br><a href='/'>Back</a>"


@app.route("/users")
def user_list():
    links = ""
    for id, user in users.items():
        links += f"<li><a href='/user/{id}'>{user['name']}</a></li>"
    return f"<h2>Users list</h2><ul>{links}</ul><br><a href='/'>Back</a>"


@app.route("/user/<int:user_id>")
def user_details(user_id):
    user = users.get(user_id)
    if user:
        return f"<h2>User: {user['name']}</h2><p>Age: {user['age']}</p><br><a href='/users'>Back</a>"
    else:
        return "User does not exist <br><a href='/users'>Back</a>"


if __name__ == "__main__":
    app.run(debug=True)