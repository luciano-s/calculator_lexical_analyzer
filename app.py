from flask import Flask, render_template
from src.tokens import Tokens
from src.validator import Validator
import sys


print(sys.path)

app = Flask(__name__, template_folder="src/templates")


@app.route("/")
def index():
    return render_template("index.html")


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