from flask import Flask
# from markupsafe from escape



app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    return f'user {username}'

@app.route('/post/<int:post_id>/<string:post_head>')
def post(post_id,post_head):
    # return 'post %d' % escape(post_id)
    return f'post {post_id} and post {post_head}'

@app.route('/path/<path:subpath>')
def show_post(subpath):
    return f'path {subpath}'

if __name__ == '__main__':
    app.debug = True
    app()