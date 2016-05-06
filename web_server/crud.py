#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from estructures import posts, comments, albums, photos, todos, users


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

#GET

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify({'posts': posts})

@app.route('/comments', methods=['GET'])
def get_comments():
    return jsonify({'comments': comments})

@app.route('/albums', methods=['GET'])
def get_albums():
    return jsonify({'albums': albums})

@app.route('/photos', methods=['GET'])
def get_photos():
    return jsonify({'photos': photos})

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

#GET ID

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_task(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    return jsonify({'post': post[0]})

@app.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = [comment for comment in comments if comment['id'] == comment_id]
    if len(comment) == 0:
        abort(404)
    return jsonify({'comment': comment[0]})

@app.route('/albums/<int:album_id>', methods=['GET'])
def get_album(album_id):
    album = [album for album in albums if album['id'] == album_id]
    if len(album) == 0:
        abort(404)
    return jsonify({'album': album[0]})

@app.route('/photos/<int:photo_id>', methods=['GET'])
def get_photo(photo_id):
    photo = [photo for photo in photos if photo['id'] == photo_id]
    if len(photo) == 0:
        abort(404)
    return jsonify({'photo': photo[0]})

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = [todo for todo in todos if todo['id'] == todo_id]
    if len(todo) == 0:
        abort(404)
    return jsonify({'todo': todo[0]})

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

#POST


@app.route('/posts', methods=['POST'])
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

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    if not request.json:
        abort(400)
    post[0]['title'] = request.json.get('title', post[0]['title'])
    post[0]['body'] = request.json.get('body', post[0]['body'])
    return jsonify({'post': post[0]})

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    posts.remove(post[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
