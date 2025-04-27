from flask import Flask, request

app = Flask(__name__)
@app.route('/summa')
def summa():
    args = request.args
    luku1 = float(args.get("luku1"))
    if luku1%0:
        print("Luku on alkuluku")
    else:
        print("Luku ei ole alkuluku")
    return str(summa)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)