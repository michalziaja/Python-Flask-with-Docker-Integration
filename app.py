import random
import string
from flask import Flask, render_template, request

app = Flask(__name__)

def generate_password(word, num_digits, add_special):
    password = ""
    mappings = {
        'a': ['@', '4', 'a', 'A'],
        'b': ['8', 'B'],
        'c': ['(', 'c', 'C'],
        'd': ['d', 'D'],
        'e': ['3', '€'],
        'f': ['F', 'f'],
        'g': ['g', 'G'],
        'h': ['H', '#'],
        'i': ['!', '1'],
        'j': ['J', 'j'],
        'k': ['k', 'K'],
        'l': ['l', 'L'],
        'm': ['M', 'm'],
        'n': ['n', 'N'],
        'o': ['0', 'O'],
        'p': ['P', 'p'],
        'q': ['Q', 'q'],
        'r': ['R', 'r'],
        's': ['$', '5', 'S', 's'],
        't': ['T', '+', 't'],
        'u': ['U', 'u'],
        'v': ['\/', 'V', 'v'],
        'w': ['VV', 'w', 'W'],
        'x': ['x', 'X'],
        'y': ['y', 'Y'],
        'z': ['7', 'z', 'Z']
    }

    if num_digits > 0:
        digits = ''.join(random.choice(string.digits) for _ in range(num_digits))
        password += digits + "."

    for char in word:
        if char.lower() in mappings:
            options = mappings[char.lower()]
            password += random.choice(options)
        else:
            password += char

    if add_special == "on": 
        password += random.choice([".", "!", "?"])

    return password

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_word = request.form["word"]
        input_num_digits = int(request.form["num_digits"])
        add_special = request.form.get('add_special')

        password = generate_password(input_word, input_num_digits, add_special)
        return render_template("result.html", password=password)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
