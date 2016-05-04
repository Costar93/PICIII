#!flask/bin/python
from flask import Flask, jsonify, abort, make_response
import estructures

comments = [
{
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
  },
  {
    "postId": 1,
    "id": 2,
    "name": "quo vero reiciendis velit similique earum",
    "email": "Jayne_Kuhic@sydney.com",
    "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"
  },
  {
    "postId": 1,
    "id": 3,
    "name": "odio adipisci rerum aut animi",
    "email": "Nikita@garfield.biz",
    "body": "quia molestiae reprehenderit quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"
  },
  ]

  @app.errorhandler(404)
  def not_found(error):
      return make_response(jsonify({'error': 'Not found'}), 404)

  @app.errorhandler(400)
  def bad_request(error):
      return make_response(jsonify({'error': 'Bad request'}), 400)

  @app.route('/comments', methods=['GET'])
  def get_posts():
      return jsonify({'comments': comments})

  @app.route('/comments/<int:comment_id>', methods=['GET'])
  def get_task(comment_id):
      comment = [comment for comment in comments if comment['id'] == comment_id]
      if len(comment) == 0:
          abort(404)
      return jsonify({'comment': comment[0]})

#Falten opcions
