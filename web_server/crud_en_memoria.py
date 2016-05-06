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

@app.route('/comments', methods=['POST'])
def create_comment():
    if not request.json or not 'postId' in request.json or not 'name' in request.json or not 'email' in request.json or not 'body' in request.json:
        abort(400)
    comment = {
        'id': comments[-1]['id'] + 1,
        'postId': request.json['postId'],
        'name': request.json['name'],
        'email': request.json['email'],
        'body': request.json['body'],
    }
    comments.append(comment)
    return jsonify({'comment': comment}), 201

@app.route('/albums', methods=['POST'])
def create_album():
    if not request.json or not 'userId' in request.json or not 'title' in request.json:
        abort(400)
    album = {
        'id': albums[-1]['id'] + 1,
        'userId': request.json['userId'],
        'title': request.json['title'],
    }
    albums.append(album)
    return jsonify({'album': album}), 201

@app.route('/photos', methods=['POST'])
def create_photo():
    if not request.json or not 'albumId' in request.json or not 'title' in request.json or not 'url' in request.json or not 'thumbnailUrl' in request.json:
        abort(400)
    photo = {
        'id': photos[-1]['id'] + 1,
        'albumId': request.json['albumId'],
        'title': request.json['title'],
        'url': request.json['url'],
        'thumbnailUrl': request.json['thumbnailUrl'],
    }
    photos.append(photo)
    return jsonify({'photo': photo}), 201

@app.route('/todos', methods=['POST'])
def create_todo():
    if not request.json or not 'userId' in request.json or not 'title' in request.json or not 'completed' in request.json:
        abort(400)
    todo = {
        'id': todos[-1]['id'] + 1,
        'userId': request.json['userId'],
        'title': request.json['title'],
        'completed': request.json['completed'],
    }
    todos.append(todo)
    return jsonify({'todo': todo}), 201

#Falta users pero es molt llarg xdd

#PUT

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

@app.route('/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    comment = [comment for comment in comments if comment['id'] == comment_id]
    if len(comment) == 0:
        abort(404)
    if not request.json:
        abort(400)
    comment[0]['name'] = request.json.get('name', comment[0]['name'])
    comment[0]['email'] = request.json.get('email', comment[0]['email'])
    comment[0]['body'] = request.json.get('body', comment[0]['body'])
    return jsonify({'comment': comment[0]})

@app.route('/albums/<int:album_id>', methods=['PUT'])
def update_album(album_id):
    album = [album for album in albums if album['id'] == album_id]
    if len(album) == 0:
        abort(404)
    if not request.json:
        abort(400)
    album[0]['title'] = request.json.get('title', album[0]['title'])
    return jsonify({'album': album[0]})

@app.route('/photos/<int:photo_id>', methods=['PUT'])
def update_photo(photo_id):
    photo = [photo for photo in photos if photo['id'] == photo_id]
    if len(photo) == 0:
        abort(404)
    if not request.json:
        abort(400)
    photo[0]['title'] = request.json.get('title', photo[0]['title'])
    photo[0]['url'] = request.json.get('url', photo[0]['url'])
    photo[0]['thumbnailUrl'] = request.json.get('thumbnailUrl', photo[0]['thumbnailUrl'])
    return jsonify({'photo': photo[0]})

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = [todo for todo in todos if todo['id'] == todo_id]
    if len(todo) == 0:
        abort(404)
    if not request.json:
        abort(400)
    todo[0]['title'] = request.json.get('title', todo[0]['title'])
    return jsonify({'todo': todo[0]})

#Falta users que es molt llarg

#DELETE

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = [post for post in posts if post['id'] == post_id]
    if len(post) == 0:
        abort(404)
    posts.remove(post[0])
    return jsonify({'result': True})

@app.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    comment = [comment for comment in comments if comment['id'] == comment_id]
    if len(comment) == 0:
        abort(404)
    comments.remove(comment[0])
    return jsonify({'result': True})

@app.route('/albums/<int:album_id>', methods=['DELETE'])
def delete_album(album_id):
    album = [album for album in albums if album['id'] == album_id]
    if len(album) == 0:
        abort(404)
    albums.remove(album[0])
    return jsonify({'result': True})

@app.route('/photos/<int:photo_id>', methods=['DELETE'])
def delete_photo(photo_id):
    photo = [photo for photo in photos if photo['id'] == photo_id]
    if len(photo) == 0:
        abort(404)
    photos.remove(photo[0])
    return jsonify({'result': True})

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = [todo for todo in todos if todo['id'] == todo_id]
    if len(todo) == 0:
        abort(404)
    todos.remove(todo[0])
    return jsonify({'result': True})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
