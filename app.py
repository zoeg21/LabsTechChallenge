from flask import Flask, render_template

app = Flask(__name__)


@app.route('/zeg2103', methods=['GET'])
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
