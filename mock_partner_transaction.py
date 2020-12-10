from flask import Flask
from flask import request, jsonify
import mock, time

app = Flask(__name__)

BRINKSPAY_CONTEXT = "/brinkspay/v1/ewallet"

@app.route("/", methods = ['GET'])
@app.route("{}".format(BRINKSPAY_CONTEXT), methods = ['GET'])
def default_health_brinkspay():
    result = mock.return_health()
    return jsonify(result)

@app.route("/transaction", methods = ['POST'])
@app.route("{}/transaction".format(BRINKSPAY_CONTEXT), methods = ['POST'])
def partner_transaction_brinkspay():
    data = request.get_json(force=True)
    result = mock.return_transaction(data)
    for i in range(6): 
      time.sleep(10)
      print("{} segundos".format((i+1)*10))
    return jsonify(result)

@app.route("/payments/internal-payment", methods = ['POST', 'DELETE'])
@app.route("{}/payments/internal-payment".format(BRINKSPAY_CONTEXT), methods = ['POST', 'DELETE'])
def internal_payment():
    result = mock.return_internal_payment()
    return jsonify(result)

@app.route("/accounts/<accountId>", methods = ['GET'])
@app.route("{}/accounts/<accountId>".format(BRINKSPAY_CONTEXT), methods = ['GET'])
def accounts(accountId):
    result = mock.return_accounts()
    return jsonify(result)
