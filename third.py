from flask import Flask, send_from_directory, abort, jsonify

app = Flask(__name__)


@app.route('/images/<path:image_path>')
def get_image(image_path):
    try:
        image_directory = '/home/nastia/PycharmProjects/third_homework_backend'
        return send_from_directory(image_directory, image_path)

    except FileNotFoundError:
        abort(404, 'Nothing found')


@app.route('/')
def get_docs():
    documentation = {
        'endpoints': {
            '/images/<path:image_path>': {
                'method': 'GET',
                'description': 'Get images by specifying the path.',
                'example': '/images/flowers.png'
            },
            '/': {
                'method': 'GET',
                'description': 'Get documentation on all endpoints.'
            }
        }
    }
    return jsonify(documentation)


if __name__ == "__main__":
    app.run(debug=True)
