from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder="templates")


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        expression = request.form["pizzo"]
        result = eval(expression)
        return render_template("simple_calculator.html", pizzo=f"Result is {result}")
    return render_template("simple_calculator.html")


@app.route("/display_data")
def show_data():
    df = pd.read_csv("static/bacteria_train.csv")
    data_html = df.to_html(classes="data")

    plt.scatter(df.Perc_population, df.Spreading_factor)
    plt.xlabel("Perc Population")
    plt.ylabel("Spreading Factor")
    plt.title("Bacteria Data")
    plt.savefig("static/plot.png")
    return render_template("analytics.html", data=data_html)


@app.route("/jonathan")
def hello_jonathan():
    return "Hello Jonathan"


@app.route("/<string:name>")
def hello_name(name):
    # return f"Hello {name}"
    return render_template("home.html", some_name=name)


@app.route("/<string:name>/<int:age>")
def hello_age(name, age):
    return f"Hello {name}. You are {age} years old."


@app.route("/some_post", methods=["POST"])
def some_post():
    print(request.data)
    return "Got what you sent me"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
