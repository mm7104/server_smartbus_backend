from flask import Flask, request, jsonify
from firebase_admin import messaging
import firebase_admin
from firebase_admin import credentials
import boto3
import json
from googleapiclient import http
import requests
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv 
load_dotenv()
app=Flask(_name_)
client = boto3.client('cognito-idp', region_name='ap-south-1')
ClientId="5kdffi1qcpalk6ubac6nqp7gro"
cred=credentials.Certificate('/home/ubuntu/serviceaccount.json')

Database_url="postgres://smartbus_admin:iota2020@smart-bus02.cyfqca490urm.ap-south-1.rds.amazonaws.com:5432/postgres"
SSL_mode="require"


@app.route('/postgre', methods=["GET", "POST"])
def postgre():
       conn=psycopg2.connect(Database_url,sslmode=SSL_mode)
       cur=conn.cursor()
       cur.execute("SELECT notification from stations where id=1002")
       a=cur.fetchall()
       print(a)
       cur.close()
       conn.close()

       return "true"

       

@app.route('/signup', methods=["GET", "POST"])
def signup():
   try:
      content = json.loads(request.data)
      response = client.sign_up(
         ClientId=ClientId,
         Username=content['email'],
         Password=content['password'],
      )
      return "True"
   except client.exceptions.UsernameExistsException:
        return 'email Already Exists!'
   except client.exceptions.InvalidPasswordException as e:
        return ("Password validation error: the password should have an upper case, a lower case & a special character")
        
   except Exception as e:
        
        return str(e)

   
@app.route('/resend_confirmation',methods=["GET", "POST"])
def resend_confirmation():
  content = json.loads(request.data)

  response = client.resend_confirmation_code(
      ClientId=ClientId,
      Username=content['username'],
   )
  return response

@app.route('/login', methods=[ "POST"])
def login():
   try:
      content = json.loads(request.data)
      print(content)
      response = client.initiate_auth(
      ClientId=ClientId,   
      AuthFlow='USER_PASSWORD_AUTH',
      AuthParameters={
         'USERNAME': content['username'],
         'PASSWORD': content['password'],
         }
      )
      
      return {"result":"true"}

   except client.exceptions.UserNotConfirmedException:
      return 'User is not confirmed. Please check your mail.'
   except client.exceptions.UserNotFoundException:
      return 'User does not exist. Check again.'
   except client.exceptions.NotAuthorizedException:
      return 'Username/Password is incorrect'
   except Exception as e:
      print(str(e)+"exception")
      return str(e)
   
@app.route('/forgot_password',methods=["POST"])
def forgot_password():
   content = json.loads(request.data)
   response = client.forgot_password(
     ClientId=ClientId, 
     Username=content['username'],
     )

   return response
@app.route('/confirm_forgot_password',methods=["POST"])
def confirm_forgot_password():
   content = json.loads(request.data)

   response = client.confirm_forgot_password(
    ClientId=ClientId,  
    Username=content['username'],
    ConfirmationCode=content['code'],
    Password=content['password']
   )

   return response
@app.route('/change_password',methods=[ "POST"])
def change_password():
   content = json.loads(request.data)

   response = client.change_password(
       PreviousPassword=content['previousPassword'],
       ProposedPassword=content['newPassword'],
       AccessToken=content['accessToken']
   ) 

   return response
@app.route('/logout',methods=["POST"])
def logout():
   content = json.loads(request.data)
   response=client.global_sign_out(
      AccessToken=content['AccessToken']
   )
   return response


@app.route('/subscribe',methods=["GET", "POST"])
def subscribe():
   content = json.loads(request.data)
   registration_token=content["appid"]
   topic=content["topic"]
   firebase_admin.initialize_app(cred)
   response = messaging.subscribe_to_topic(registration_token, topic)
   
   print(response.success_count, 'tokens were subscribed successfully')
   return "TRUE"


@app.route('/unsubscribe',methods=["GET", "POST"])
def unsubscribe():
   content = json.loads(request.data)
   registration_token=content["appid"]
   topic=content["topic"]
   firebase_admin.initialize_app(cred)
   response = messaging.unsubscribe_from_topic(registration_token, topic)
   print(response.success_count, 'tokens were unsubscribed successfully')
   return "True"


@app.route('/notifaction',methods=["GET", "POST"])
def notifaction():
       topic = 'highScores'
       message = messaging.Message(
          data='req',
          topic=topic,
       )
       response = messaging.send(message)
       print('Successfully sent message:', response)
        
       
      





if _name=="main_":
    app.run(debug=True, host='0.0.0.0')
