from flask import render_template,request,url_for,redirect
from app.register import bp
from app.extensions import db
from app.models.user import User
from app.models.credential import Credential

@bp.route('/register' , methods = ['GET','POST'])
def create():
   if request.method == 'GET':
        return url_for('register.index')
   
   if request.method == 'POST':
         first_name = request.form.get('first_name')
         last_name = request.form.get('last_name')
         dob= request.form.get('dob')
         age = request.form.get('age')
         gender = request.form.get('gender')
         address = request.form.get('address')
         phone = request.form.get('phone')
         add_phone = request.form.get('add_phone')
         email = request.form.get('email')
         adhaar = request.form.get('adhaar')
         password = request.form.get('password')

         user = User(first_name=first_name,last_name=last_name,dob=dob,age=age,gender=gender,address=address,phone=phone,add_phone=add_phone,email=email,adhaar=adhaar)
         db.session.add(user)
         
        # Create a Credential record with the password
         credential = Credential(password=password)
         db.session.add(credential)

         db.session.commit()

         return "Form data has been successfully saved."

