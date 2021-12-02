from flask import Flask, render_template, request
from helpers import find_result, points

app: Flask = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


# @app.route('/all-results')
# def all_results():
#     return render_template('all-results.html', users=users)


# @app.route('/user<usernumber>')
# def display_user(usernumber: str):
#     return render_template('user.html', user=users[int(usernumber)])


@app.route("/index", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        sort_points = sorted(points.items(), key=lambda x: x[1], reverse= True)

        winner: str = find_result(sort_points)
        return render_template("../index.html", winner=winner)
    return render_template("../index.html")


if __name__ == '__main__':
    app.run(debug=True)
