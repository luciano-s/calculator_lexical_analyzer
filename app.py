from flask import Flask, render_template, request
from src.tokens import Tokens
from src.validator import Validator
import sys


app = Flask(__name__, template_folder="src/templates")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        expression = request.form['expression']
        tokens = Tokens()
        validated_lexems = list(map(
            lambda d: (
            list(d.keys()).pop(), list(d.values()).pop(), 'Yes' if list(d.values()).pop() is not None else 'No'),
            tokens.split_token(expression.replace(' ', ''))
        ))
        return render_template("index.html", validated_lexems=validated_lexems)

@app.route("/valid-lexems/<expression>")
def valid_lexems(expression=None):
    if expression == None:
        return render_template("error.html")
    tokens = Tokens()
    validated_lexems = list(map(
        lambda d: (list(d.keys()).pop(), list(d.values()).pop(), 'Yes'  if list(d.values()).pop() is not None else 'No'),
        tokens.split_token(expression)
    ))

    return render_template("table.html", validated_lexems=validated_lexems)


if __name__ == '__main__':
    app.run(debug=True)