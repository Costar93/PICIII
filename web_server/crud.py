#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
import estructures

a = sys.argv[1]

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.route('/%s', methods=['GET'] % (a))
def get_posts():
    return jsonify({'posts': posts})

@app.route('/%s/<int:post_id>', methods=['GET'] % (a))
def get_task(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post[0]})

@app.route('/%s', methods=['POST'] % (a))
def create_post():
    if not request.json or not 'title' in request.json or not 'userId' in request.json or not 'body' in request.json:
        abort(400)
    post = {
        'id': posts[-1]['id'] + 1,
        'userId': request.json['userId'],
        'title': request.json['title'],
        'body': request.json['body'],
    }
    posts.append(post)
    return jsonify({'post': post}), 201

@app.route('/%s/<int:post_id>', methods=['PUT'] % (a))
def update_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    if not request.json:
        abort(400)
    post[0]['title'] = request.json.get('title', post[0]['title'])
    post[0]['body'] = request.json.get('body', post[0]['body'])
    return jsonify({'post': post[0]})
    </int:post_id>

@app.route('/%s/<int:post_id>', methods=['DELETE'] % (a))
def delete_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    posts.remove(post[0])
    return jsonify({'result': True})
    </int:post_id>
