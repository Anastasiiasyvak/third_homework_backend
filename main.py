from flask import Flask, request, jsonify
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

def parse_url(URL):
    try:
        parsed_url = urlparse(URL)
        scheme = parsed_url.scheme
        domain = parsed_url.netloc
        path_steps = parsed_url.path.strip('/').split('/')
        query_params = parse_qs(parsed_url.query)

        return {
            'scheme': scheme,
            'domain': domain,
            'path steps': path_steps,
            'query params': query_params
        }
    except Exception as e:
        return {'error': f'Invalid URL. {str(e)}'}


@app.route('/get_info_about_url', methods=['POST'])
def get_info_about_url():
    try:
        data = request.get_json()
        url = data.get('url', '')

        if not url:
            return jsonify({'error': 'URL not provided in the request'}), 400

        url_info = parse_url(url)

        return jsonify(url_info)

    except Exception as e:
        return jsonify({'error': f'An error occurred. {str(e)}'}), 500


if __name__=="__main__":
    app.run(debug=True)



