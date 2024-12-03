from flask import Flask,render_template, request, redirect, url_for,session,flash, send_from_directory,send_file, jsonify
import requests

app = Flask(__name__, template_folder='code', static_folder='static')
@app.route('/ephedra')
def ephedra():
    return render_template('main.html')

@app.route('/')
def main():
    return render_template('Ephdrma.html')

@app.route('/donate')
def donate():
    return render_template('DONATEepH.html')

@app.route('/projects')
def projects():
    return render_template('frames.html')

@app.route('/about')
def about():
    return render_template('abouteph.html')


@app.route('/balance')
def get_balance():
    # Replace with the actual API for your wallet address
    wallet_address = "bc1q5kklnsu9c55v0uswszm3wwvf32v5srz3yqrut7"
    api_url = f"https://blockchain.info/q/addressbalance/{wallet_address}"

    try:
        response = requests.get(api_url)
        balance = response.json() / 1e8  # Convert satoshi to BTC if needed
    except Exception as e:
        balance = 0
    return jsonify(balance=balance)



@app.route('/prvpc')
def prvpc():
    return render_template('prv_pol.html')
if __name__ == '__main__':
    app.run(debug=True, port=8080)
