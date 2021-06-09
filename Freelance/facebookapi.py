# This file provides functions to post data on facebook
import facebook
from logger import Logger
import traceback
import json
import requests
from flask import jsonify
import configparser
config = configparser.ConfigParser()
config.read('settings.ini')

token = config['Facebook']['ACCESS_TOKEN_FB']
logger = Logger("POP").get()

# FACEBOOK POST CREATE ONLY TEXT
def post_on_facebook(message):
    try:
        graph = facebook.GraphAPI(token)
        data=graph...........................
        logger.debug("Posted message successfully on facebook")
        return data
    except:
        logger.error("Could not post message to facebook : " +
                     traceback.format_exc())
        return "FAIL"

# FACEBOOK POST CREATE IMAGE & TEXT or only IMAGE NEEDS ONLI PATH ON READ MODE AND TEXT IF AVAILABLE
def image_post_on_facebook(path,message):
    try:
        graph = facebook.GraphAPI(token)
        postid = graph.put_photo(image=open(path,"rb"), message=message)
        logger.debug("Image Posted successfully on facebook")
        return postid

    except:
        logger.error("Could not post message to facebook : " +
                     traceback.format_exc())
        return "FAIL"

# FACEBOOK POST CREATE VIDEO & TEXT or only IMAGE NEEDS ONLI PATH ON READ MODE AND TEXT IF AVAILABLE

def put_video(video_url, page_id,title, access_token):
    .
    ..
    ...
    ...
    ...
    
    #     return facebook_video_id
    # else:
    #     print("Facebook upload error: {0}".format(r.text))

def video_post_on_facebook(video_url, page_id,title, access_token):
    try:
        postid = put_video(video_url, page_id,title, access_token)
        logger.debug("Video Posted successfully on facebook")
        #return postid
    except:
        logger.error("Could not post Video to facebook : " +
                     traceback.format_exc())
    return postid


# DELETE FACEBOOK POST NEEDS ONLI POST ID
def delete_message_on_facebook():
    try:
        graph = facebook.GraphAPI(token)
        graph.delete_object()
        logger.debug("Deleted post successfully on facebook")
        return "SUCCESS"
    except:
        logger.error("Could not delete post to facebook : " +
                     traceback.format_exc())
        return "FAIL"

# COMMENT ON FACEBOOK POST NEEDS ONLI POST ID
def comment_message_on_facebook():
    try:
        graph = facebook.GraphAPI(token)
        graph.put_object()
        logger.debug("Commented on a post successfully on facebook")
        return "SUCCESS"
    except:
        logger.error("Could not comment post to facebook : " +
                     traceback.format_exc())
        return "FAIL"

# DELETE COMMENTS ON FACEBOOK POST NEEDS ONLI COMMENT ID
def delete_comment_on_facebook():
    try:
        graph = facebook.GraphAPI(token)
        graph.delete_object()
        logger.debug("Delete comment successfully on facebook")
        return "SUCCESS"
    except:
        logger.error("Could not delete comment to facebook : " +
                     traceback.format_exc())
        return "FAIL"
# COMMENT LIKE ON FACEBOOK POST NEEDS ONLI COMMENT ID
def comment_like_message_on_facebook():
    try:
        graph = facebook.GraphAPI(token)
        graph.put_like()
        logger.debug("Commented on a message successfully on facebook")
        return "SUCCESS"
    except:
        logger.error("Could not delete message to facebook : " +
                     traceback.format_exc())

# LIKE FACEBOOK POST NEEDS ONLI POST ID
def like_message_on_facebook():
    try:
        graph = facebook.GraphAPI(token)
        graph.put_like()
        logger.debug("Like on message successfully on facebook")
        return "SUCCESS"
    except:
        logger.error("Could not like on message to facebook : " +
                     traceback.format_exc())
        return "FAIL"


# def get_post(post_id):
#     graph = facebook.GraphAPI(access_token=token, version="2.11")
#     post = graph.get_object(id=post_id, fields='message,reactions.type(LIKE).limit(0).summary(total_count),shares,comments')
#     print('Title - ', post['message'])
#     print('Total likes - ', post['reactions'])
#     print('Total Share - ', post['shares'])
#     # #print('Recent Comment - ', post['comments']['data'][0]['message'])
#     #print('Total Comments - ', len(post['comments']))
#     # for i in post['comments']['data']:
#     #     print('Comments - ', i['message'])
    
# Get post data using POST ID
def get_data_on_facebook(post_id):
    try:
        token = config['Facebook']['ACCESS_TOKEN_FB']
        graph = facebook.GraphAPI(access_token=token, version="2.11")
        post = graph.get_object(id=post_id, fields='reactions.type(LIKE).limit(0).summary(total_count),comments,shares')
        return post
    except:
        logger.error("Could not get data from facebook : " +
                     traceback.format_exc())
        return "FAIL"

# Get comments data using POST ID : Note this end point has limitation 5/day calls
def get_post_comments(post_id):
    try:
        graph = facebook.GraphAPI(access_token=token, version="2.11")
        comments_all = graph.get_all_connections(id=post_id, connection_name='comments')
        return comments_all
    except:
        logger.error("Could not get data from facebook : " +
                     traceback.format_exc())
        return "FAIL"




if __name__ == '__main__':
    main()
