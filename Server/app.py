import flask
from lib import TeachersCharacters


app = flask.Flask('character-server', template_folder='templates')
teachers_characters = TeachersCharacters("data_base.txt")


@app.route('/')
def home():
    return flask.render_template("home.html")


@app.route('/comment', methods=['get'])
def to_comment():
    return flask.render_template("comment.html")


@app.route('/create-comment', methods=['post'])
def create_comment():
    name = flask.request.form['name']
    comment = flask.request.form['comment']
    mark = flask.request.form['mark']
    teachers_characters.create_comment(name, comment)
    teachers_characters.create_mark(name, mark)
    return flask.redirect(flask.url_for('home'))


@app.route('/get_characters', methods=['get'])
def get_most_common_characters():
    return flask.render_template("get_characters.html", messages=[])


@app.route('/account', methods=['post'])
def to_demonstrate():
    name = flask.request.form['name']
    return flask.render_template(
        "get_characters.html",
        messages=teachers_characters.get_most_common_comments(name)
    )


def main():
    try:
        teachers_characters.load()
        app.run('localhost', port=8000)
    finally:
        teachers_characters.dump()


if __name__ == '__main__':
    main()
