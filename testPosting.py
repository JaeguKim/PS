#!/usr/bin/python3
# coding: utf-8

# ### Python code to auto post to blogger
# @author Ramachandran K <ramakavanan@gmail.com>
# 

import sys
import os
import pickle
from google.auth import client
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# ##### Adding the blog id and scope of the blogger. 
# The scope will play the major rolw. It will generate the feasibility to work through the API.

BLOG_ID = "403444661419-bs9vaidd4k84kvtsv9vqmjneoulc49s9.apps.googleusercontent.com"
SCOPES = ['https://www.googleapis.com/auth/blogger', 'https://www.googleapis.com/auth/drive.file']


# #### Function to generatet the blogger and drive service
# Here we are using the pickle to store and retrive the credential file. The pickle will store the data in bytes. 
# The normal human cant read that pickle file.

def get_blogger_service_obj():

    creds = None
    if os.path.exists('auth_token.pickle'):
        with open('auth_token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('auth_token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    blog_service = build('blogger', 'v3', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)
    return drive_service,blog_service


drive_handler, blog_handler = get_blogger_service_obj()


# # ### Function to get the blog information 

# def get_blog_information(api_handler=None, blog_max_posts=3):
#     try:
#         if not api_handler:
#             return None
#         blogs = api_handler.blogs()
#         resp = blogs.get(blogId=BLOG_ID, maxPosts=blog_max_posts, view='ADMIN').execute()
#         for blog in resp['posts']['items']:
#             print('The blog title : \'%s\'  and url : %s' % (blog['title'], blog['url']))
#     except Exception as ex:
#         print(str(ex))

# get_blog_information(blog_handler)

# import json

# data = {
#     'content': '<b> Welcome ! </b> <br/> This is my first automated post through API.',
#     'title':'Python post sample',
#     'labels' : ['First Post'],
#     'blog': {
#         'id': BLOG_ID, # The identifier of the Blog that contains this Post.
#       },
# }

# posts = blog_handler.posts()
# res = posts.insert(blogId=BLOG_ID, body=data, isDraft=True, fetchImages=True).execute()


# # #### Printing response from the server 
# print(res)
