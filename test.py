from flask import Flask
import boto3
from dotenv import load_dotenv
load_dotenv()
app=Flask(__name__)
@app.route('/')
def signup():
   username = 'aa7995@srmist.edu.in'
   password = 'Amish123@'

   client = boto3.client('cognito-idp', region_name='ap-south-1')
   response = client.sign_up(
      ClientId="7911ht17hg4t102ttseql68lm3",
      Username=username,
      Password=password,
   )
   return response
@app.route('/resend_confirmation')
def resend_confirmation():
  username = 'aa7995@srmist.edu.in'

  client = boto3.client('cognito-idp', region_name='ap-south-1')
  response = client.resend_confirmation_code(
    ClientId="7911ht17hg4t102ttseql68lm3",
    Username=username,
   )
  return response

@app.route('/login')
def login():
   username = 'aa7995@srmist.edu.in'
   password = 'Amish1234@'

   client = boto3.client('cognito-idp', region_name='ap-south-1')
   response = client.initiate_auth(
    ClientId="7911ht17hg4t102ttseql68lm3",
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': username,
        'PASSWORD': password
      }
    )
   return response
@app.route('/forgot_password')
def forgot_password():
   username = 'aa7995@srmist.edu.in'

   client = boto3.client('cognito-idp', region_name='ap-south-1')
   response = client.forgot_password(
     ClientId="7911ht17hg4t102ttseql68lm3",
     Username=username
     )

   return response
@app.route('/confirm_forgot_password')
def confirm_forgot_password():
   username = 'aa7995@srmist.edu.in'
   confirm_code = '528010'
   password = 'Amish12@'

   client = boto3.client('cognito-idp', region_name='ap-south-1')
   response = client.confirm_forgot_password(
    ClientId="7911ht17hg4t102ttseql68lm3",
    Username=username,
    ConfirmationCode=confirm_code,
    Password=password
   )

   return response
@app.route('/change_password')
def change_password():
   access_token = 'eyJraWQiOiI2bThnR3k3aHZHTEhpbEV1MzUwdzlLYUtqS1c0d05VbFJDdlJCRHp6cmxrPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2NWNmN2RjYy1kMDVjLTQ4NDUtYmE5Ny01YmExYTA4OWFkMmEiLCJldmVudF9pZCI6IjJmMTM3NjBmLTNlNjctNDc1ZC05NDJjLTQ0ZGQ0OTRlYTRmNCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2MTY0NDM3MTUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aC0xLmFtYXpvbmF3cy5jb21cL2FwLXNvdXRoLTFfaFhHeWVpTmlhIiwiZXhwIjoxNjE2NDQ3MzE1LCJpYXQiOjE2MTY0NDM3MTUsImp0aSI6ImVhYzI2NDA0LWM3OTctNDYyMi1iZjAxLTlmMjk4NTVmMzA3YSIsImNsaWVudF9pZCI6Ijc5MTFodDE3aGc0dDEwMnR0c2VxbDY4bG0zIiwidXNlcm5hbWUiOiI2NWNmN2RjYy1kMDVjLTQ4NDUtYmE5Ny01YmExYTA4OWFkMmEifQ.LDLtvdJuRCERLcvMN1qQq6UeDtSUVKauh4CVItkpxzmOKvkV8HjfQtqxEYz5kovErP8bjyV0GUVe8dcl2VgwayBOqUiCxCUjAt76Ap1yrHNfiS4GJt-X1OGuWj88x0bD8hHVzRqI0o6d2zyUPe70kJcOt6oYjzoNxFfTScdEZNvwsAXyVlcyFzeCZm470VqvIH_slTGuV5p2P0IMpGWDBy_W3aS--7OUZgsQpk-K_unYLMEKgN3xlvDfClawRHObEW9ikLznhelY8q7MDGNx9EAzO0VpXhZKY3rSgVe8mYvSdbrmSSZyOJow5W63FkT8ryoRkpAZIW6-kEwpqRepNw'
   previous_password = 'Amish12@'
   new_password = 'Amish1234@'

   client = boto3.client('cognito-idp', region_name='ap-south-1')
   response = client.change_password(
       PreviousPassword=previous_password,
       ProposedPassword=new_password,
       AccessToken=access_token
   ) 

   return response
@app.route('/logout')
def logout():
   access_token = 'eyJraWQiOiI2bThnR3k3aHZHTEhpbEV1MzUwdzlLYUtqS1c0d05VbFJDdlJCRHp6cmxrPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2NWNmN2RjYy1kMDVjLTQ4NDUtYmE5Ny01YmExYTA4OWFkMmEiLCJldmVudF9pZCI6IjA1ZjRkOWVhLWZkMWYtNDlhNS1iYWQxLTE3N2RlYjA3MjM4OSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2MTY0ODM5MjksImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aC0xLmFtYXpvbmF3cy5jb21cL2FwLXNvdXRoLTFfaFhHeWVpTmlhIiwiZXhwIjoxNjE2NDg3NTI5LCJpYXQiOjE2MTY0ODM5MjksImp0aSI6IjdmNjdhOTExLWYzY2YtNDgxZC04ODQ1LTY0NTQ1ODc4MjUyNyIsImNsaWVudF9pZCI6Ijc5MTFodDE3aGc0dDEwMnR0c2VxbDY4bG0zIiwidXNlcm5hbWUiOiI2NWNmN2RjYy1kMDVjLTQ4NDUtYmE5Ny01YmExYTA4OWFkMmEifQ.KVY47ySUN-w4bYrwc8o2K_ZUiUjUjwNnwlZWFedurwZrQv8xzbCFBaprY7pFfOiDZFGkLZ0_hFHsY6IyZEns3xQf9wdq6K6ivLB7u5i8VfDsk4mLqieYXlFRE-fddKmuMcHMA7xs_NUNiw3eFHbrarJ8Xh5l_ayxSn7FhJAsyVOQQXRxbWEUewlT0u9Q9WsVJuDOXW9T4kQkdnpiAI9VGSdl0wHGTtWEwgRlRp1hRCHtLn7HCapRnISB4GEidwdgt4AQLOK0L2ITuM_BThOfJhAmC56ghcZyxH1m68llqdnjWwQMkB8p4qKdwt4cQ8-8Gvt-13jnhA7EfvQ_tZhNvg'
   client = boto3.client('cognito-idp', region_name='ap-south-1')
   response=client.global_sign_out(
      AccessToken=access_token
   )
   return response




if __name__=="__main__":
    app.run()