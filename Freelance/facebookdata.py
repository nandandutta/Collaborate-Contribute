import facebook
import configparser
config = configparser.ConfigParser()
config.read('settings.ini')

token = config['Facebook']['ACCESS_TOKEN_FB']
page_id = config['Facebook']['PAGE_ID']

# FACEBOOK POST CREATE ONLY TEXT


# def Get_post_on_facebook():
#     graph = facebook.GraphAPI(access_token=token, version="2.11")
#     posts_all = graph.get_all_connections(id=page_id, connection_name='feed')
#     for ind, post in enumerate(posts_all):
#         print(ind, post)

# # graph = facebook.GraphAPI(access_token=token, version="2.11")
# # posts_all= graph.get_all_connections(id=page_id,connection_name='feed')
# # for ind, post in enumerate(posts_all):
# #     print(ind, post)


# def get_post(post_id):
#     graph = facebook.GraphAPI(access_token=token, version="2.11")
#     post = graph.get_object(
#         id=post_id, fields='message,reactions.type(LIKE).limit(0).summary(total_count),shares,comments')
#     # print('Title - ', post['message'])
#     # print('Total likes - ', post['reactions'])
#     # print('Total Share - ', post['shares'])
#     # print('Recent Comment - ', post['comments']['data'][0]['message'])
#     # print('Total Comments - ', len(post['comments']['data']))
#     # for i in post['comments']['data']:
#     #     print('Comments - ', i['message'])


# def get_post_comments(post_id):
#     graph = facebook.GraphAPI(access_token=token, version="2.11")
#     comments_all = graph.get_all_connections(
#         id=post_id, connection_name='comments')
#     for ind, post in enumerate(comments_all):
#         print(ind, post)


from flask import Flask, request, make_response, jsonify, render_template
from pprint import pprint

VERIFICATION_TOKEN = token

app = Flask(__name__)


@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/callback', methods=['GET', 'POST'])
def callback_function():
	if request.method == 'GET':
		hub_verify_token = request.args['hub.verify_token']
		hub_challenge = request.args['hub.challenge']
		if hub_verify_token == VERIFICATION_TOKEN:
			print("Verified")
		else:
			print("Verification Failed")
		return hub_challenge
	else:
		pprint(request) #Request (Response Code)
		pprint(request.get_json()) #dictionary
		return make_response("Response OK", 200)


if __name__ == '__main__':
	app.run() #'0.0.0.0', port=8080