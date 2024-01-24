from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=["GET"])
def het_ip_user():
    with open('info_users.txt', 'a+', encoding='utf-8') as f:
        if request.remote_addr not in f:
            f.write(f'{request.remote_addr} \n')
    return jsonify({'Your ip': request.remote_addr}), 200




if __name__ == '__main__':
    app.run(debug=True)