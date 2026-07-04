from flask import request, jsonify, Flask
import string
import secrets
from flask_cors import CORS

import random
import string

app = Flask(__name__)
CORS(app)

@app.route('/aleatory-password', methods=['GET'])
def generated_pasword():
    pasword_finish = ""
    pasword_finish_count = []
    aleatory_numbers = random.choices(range(30,40))

    while aleatory_numbers[0] != len(pasword_finish_count):
        selecction_object_aleatory = random.choices(range(1,4))

        match selecction_object_aleatory[0]:
            case 1:
                letra = str(random.choice(string.ascii_letters))
                pasword_finish_count.append(letra[0])
                pasword_finish += letra[0]
                continue
            case 2:
                numbers =  str(int(random.random()*10))
                pasword_finish_count.append(numbers[0])
                pasword_finish += numbers[0]
                continue
            case 3:
                symbols = string.punctuation
                symbols_seleted = random.choice(symbols)
                pasword_finish_count.append(symbols_seleted)
                pasword_finish += symbols_seleted
                continue

    return jsonify({"result": pasword_finish})


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)


import os

if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=puerto)
