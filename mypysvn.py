import pysvn 
import argparse

def set_default_username(username):
    return username

def set_default_password(password):
    return password

def get_log_message():
    return True ,log_message

def ssl_server_trust_prompt(trust_dict):
    return True, 3, True 

def get_login(realm, username, may_save):
    return True,username,password,True

parser = argparse.ArgumentParser("Testing PySVN")
parser.add_argument('-u', '--username', help= 'SVN Username')
parser.add_argument('-p', '--password', help= 'SVN Password')

args = parser.parse_args()
username = args.username
password = args.password
client = pysvn.Client()

client.set_default_username(username)
client.set_default_password(password)
client.callback_ssl_server_trust_prompt = ssl_server_trust_prompt
client.callback_get_login = get_login
client.callback_get_log_message = get_log_message



