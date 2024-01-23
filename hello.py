from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/metadata', methods=['POST'])
def get_metadata():
    if 'file' not in request.files or 'string' not in request.form:
        return jsonify({'error': 'Missing file or search_string parameter'}), 400

    file = request.files['file']
    string = request.form['string'].lower()

    if file.filename == '':
        return jsonify({'error': 'Empty file provided'}), 400

    content = file.read().decode('utf-8')

    metadata = {
        'length of whole text': len(content),
        'amount of alphanumeric symbols': sum(i.isalnum() for i in content),
        'number of occurrences of string': content.lower().count(string)
    }

    # isalnum +1 символ коли проходиться по файлу, якщо символ є буквою або цифрою

    return jsonify(metadata)


if __name__ == '__main__':
    app.run(debug=True)
