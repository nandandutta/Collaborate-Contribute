import requests
import configparser
import logger
import traceback
import urllib
config = configparser.ConfigParser()
config.read('settings.ini')

access_token = config['LinkedIn']['Access_Token']
organization_id = config['LinkedIn']['Organization_Id']

# LinkedIn Text Post
def linkedin_text_post(message):
    try:
        url = "https://api.linkedin.com/v2/ugcPosts"
        headers = {'Content-Type': 'application/json',
                'X-Restli-Protocol-Version': '2.0.0',
                'Authorization': 'Bearer ' + access_token}
        post_data = {"author": "urn:li:organization:"+organization_id,
                    "lifecycleState": "PUBLISHED",
                    "specificContent": {"com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {"text": message},
                        "shareMediaCategory": "NONE"}},
                    "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}}
        response = requests.post(url, headers=headers, json=post_data)
        return response.json()
    except:
        logger.error("Could not post to linkedin : " +
                     traceback.format_exc())
        return "FAIL"
    
    
    
## LinkedIn Image & Text Post
def post_upload_image(message, file):
    try:

        headers = {'Content-Type': 'application/octet-stream',
                'X-Restli-Protocol-Version': '2.0.0',
                'Authorization': 'Bearer ' + access_token}
        data = {
            "author": "urn:li:organization:"+organization_id,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": message},
                    "shareMediaCategory": "IMAGE",
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
        }
        if file:
            r = requests.post("https://api.linkedin.com/v2/assets?action=registerUpload", json={
                "registerUploadRequest": {
                    "recipes": ["urn:li:digitalmediaRecipe:feedshare-image"],
                    "owner":"urn:li:organization:144284",
                    "serviceRelationships": [
                        {
                            "relationshipType": "OWNER",
                            "identifier": "urn:li:userGeneratedContent",
                        }
                    ],
                }
            },
                headers=headers)
            j = r.json()
            asset = j["value"]["asset"]
            url = j["value"]["uploadMechanism"]
            url = url["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]
            r = requests.put(url, data=open(file, "rb"), headers=headers)
            data["specificContent"]["com.linkedin.ugc.ShareContent"]["shareMediaCategory"] = "IMAGE"
            data["specificContent"]["com.linkedin.ugc.ShareContent"]["media"] = [
                {"status": "READY", "media": asset, "title": {"text": message}}]
        r = requests.post("https://api.linkedin.com/v2/ugcPosts",json=data, headers=headers)
        return r.json()
    except:
        logger.error("Could not post to linkedin : " +
                     traceback.format_exc())
        return "FAIL"

## LinkedIn Video Post
def post_upload_video(file,message):
    try:
        headers = {'Content-Type': 'application/octet-stream',
                'X-Restli-Protocol-Version': '2.0.0',
                'Authorization': 'Bearer ' + access_token}
        data = {
            "author": "urn:li:organization:"+organization_id,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text":"test"},
                    "shareMediaCategory": "VIDEO"
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
        }
        if file:
            r = requests.post("https://api.linkedin.com/v2/assets?action=registerUpload", json={
                "registerUploadRequest": {
                    "recipes": ["urn:li:digitalmediaRecipe:feedshare-video"],
                    "owner": f"urn:li:organization:+organization_id",
                    "serviceRelationships": [
                        {
                            "relationshipType": "OWNER",
                            "identifier": "urn:li:userGeneratedContent",
                        }
                    ],
                }
            },
                headers=headers)
            j = r.json()
            print(r)
            asset = j["value"]["asset"]
            url = j["value"]["uploadMechanism"]
            url = url["com.linkedin.digitalmedia.uploading.MediaUploadHttpRequest"]["uploadUrl"]
            r = requests.put(url, data=open(file, "rb"), headers=headers)
            data["specificContent"]["com.linkedin.ugc.ShareContent"]["shareMediaCategory"] = "VIDEO"
            data["specificContent"]["com.linkedin.ugc.ShareContent"]["media"] = [
                {"status": "READY", "media": asset}]
        r = requests.post("https://api.linkedin.com/v2/ugcPosts",json=data, headers=headers)
        return r.json()
    except:
        logger.error("Could not post to linkedin : " +
                     traceback.format_exc())
        return "FAIL"

# LinkedIn #DATA RETRIEVAL

def get_data_on_linkedin(post_id):
    try:
        url = "https://api.linkedin.com/v2/socialActions/"
        query_string=urllib.parse.quote("urn:li:share:"+post_id)
        web=url+query_string
        headers = {'Content-Type': 'application/json',
           'X-Restli-Protocol-Version': '2.0.0',
           'Authorization': 'Bearer ' + access_token}
        response = requests.get(web, headers=headers)
        return response
    except:
        logger.error("Could not get data from twitter : " +
                     traceback.format_exc())
        return "FAIL"
