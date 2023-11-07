from app.auth import bp
from flask import render_template,request,redirect,url_for,session
from werkzeug.security import check_password_hash
from app.models.credential import Credential
from app.models.user import User

@bp.route('/auth', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        print("Username:", username)
        print("Password:", password)

        
        credential = Credential.query.filter_by(username=username).first()
        
        if credential and check_password_hash(credential.password, password):
            session['user_id'] = credential.user_id
            
            return redirect(url_for('base'))
        
        else:
            return "Invalid login credentials"

    return render_template('login.html')

