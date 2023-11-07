from flask import render_template, url_for
from app.user import bp
from app.extensions import db
from app.models.user import User

@bp.route('/user')
def index():
    users = User.query.all()
    return render_template('user/index.html', users=users)
