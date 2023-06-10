import random
from flask import Flask, request, jsonify
import random

app = Flask(__name__)


@app.route('/recur_payment', methods=['POST'])
def recur_payment():
    data = request.form
    amount = float(data.get('AMOUNT'))

    rrn = random.randint(1000000000, 9999999999)
    rc = '00' if random.random() < 0.8 else '99'
    rctext = 'Success' if rc == '00' else 'Insufficient Funds'

    response_data = {
        'AMOUNT': amount,
        'ORDER': data.get('ORDER'),
        'RRN': rrn,
        'RC': rc,
        'RCTEXT': rctext
    }

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(debug=True)