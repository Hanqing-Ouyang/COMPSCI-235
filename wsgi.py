"""App entry point."""
from hello import create_app
from flask import request
from flask import url_for

app = create_app()

def print_urls_for_views():
    with app.test_request_context():
        print('URL for index view:', url_for('index'))
        print('URL for hello view:', url_for('hello'))
        print('URL for show_user_profile view:', url_for('show_user_profile'),username='edsheeran')
        print('URL for show_post view:', url_for('show_post'), post_id=6)
        print('URL for show_subpath view:', url_for('show_subpath'), subpath='abc/def')
        print('URL for shows_news view:', url_for('shows_news'))
        print('URL for greeting view:', url_for('greeting'), name='bob')

def print_request_info():
    with app.test_request_context('greeting?name=bob', method='GET'):
        print('request path:', request.path)
        print('request HTTP method', request.method)
        print('request query parameter for name', request.args.get('name'))
    with app.test_request_context('hello?name=bob', method='GET'):
        print('request path:', request.path)
        print('request HTTP method', request.method)
        print('request query parameter for name', request.args.get('name'))

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
