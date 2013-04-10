# -*- coding: utf-8 *-*
from rauth.service import OAuth1Service
import webbrowser


class yahooSessionManager:

    def __init__(self, consumerKey, consumerSecret, name):
        self.consumer_key = consumerKey
        self.consumer_secret = consumerSecret
        self.name = name
        #lint:disable
        self.request_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
        self.request_token_url = 'https://api.login.yahoo.com/oauth/v2/get_request_token'
        self.access_token_url = 'https://api.login.yahoo.com/oauth/v2/get_token'
        self.authorize_url = 'https://api.login.yahoo.com/oauth/v2/request_auth'
        self.base_url = 'http://fantasysports.yahooapis.com/'
        self.session = None
        #lint:enable

    def getSession(self):
        if (not self.session):
            yahoo = OAuth1Service(
                consumer_key=self.consumer_key,
                consumer_secret=self.consumer_secret,
                name=self.name,
                request_token_url=self.request_token_url,
                access_token_url=self.access_token_url,
                authorize_url=self.authorize_url,
                base_url=self.base_url)

            params = {'params': {'oauth_callback':
                    'http://andyjmeyers.blogspot.com/'}}
            request_token, request_token_secret = yahoo.get_request_token(
                    **params)
            authorize_url = yahoo.get_authorize_url(request_token)

            print 'Visit this URL in your browser: ' + authorize_url
            webbrowser.open(authorize_url)
            pin = raw_input('Enter PIN from browser: ')

            self.session = yahoo.get_auth_session(request_token,
                                   request_token_secret,
                                   method='POST',
                                   data={'oauth_verifier': pin})
        return self.session


if __name__ == "__main__":
    sessionMgr = yahooSessionManager(
        'key',
        'secret',
        'yahoo')

    print(sessionMgr.getSession())

