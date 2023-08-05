import requests
from nauth_sdk.settings import settings
import time
from collections import namedtuple
nid = settings.get('nid', '')
nauth_host_location = settings.get('nauth_host_location', 'localhost')
nkey = settings.get('nkey', '')
sitename = settings.get('sitename', '')
name = 'nauth_sdk'
token_instance = namedtuple('token_instance', 'token expire')
token_persisted = {}
def _get_token(userid=None):
    data_dict = {'nkey': nkey, 'nid': nid}
    if userid is not None:
        data_dict['userid'] = userid
    res = requests.post(f"http://{nauth_host_location}/nauth/get_token", data=data_dict)
    if res.status_code == 200 or res.status_code == 201:
        return res.text
    else:
        return None
def get_token(userid=None):
    timestamp = time.time()
    if userid is None and token_persisted.get('generic') and timestamp < token_persisted.get('generic').expire:
        return token_persisted.get('generic').token
    generic_expired = token_persisted.get('generic') and timestamp >= token_persisted.get('generic').expire
    no_generic = token_persisted.get('generic') is None
    if userid is None and (generic_expired or no_generic):
        token = _get_token()
        expire = timestamp + 3000
        token_persisted['generic'] = token_instance(token, expire)
        return token
    if userid is not None:
        usertoken = token_persisted.get(userid)
        if usertoken and timestamp < usertoken.expire:
            return usertoken.token
        else:
            token = _get_token(userid)
            expire = timestamp + 3000
            token_persisted[userid] = token_instance(token, expire)
            return token
def patch_user(userid, d):
    token = get_token(userid)
    return send_account_request(token, d, 'user_patch')
def send_account_request(token, payload, func):
    headers = {
        'Authorization': 'Bearer ' + token,
    }
    res = requests.request('POST', f"http://{nauth_host_location}/accounts/{func}", headers=headers, data=payload)
    return res.text
def user_info(userid):
    token = get_token(userid)
    return send_account_request(token, {}, 'user_info')
def create_user(username, mail_or_mobile, password, repassword=''):
    token = get_token()
    if not repassword:
        repassword = password
    post_data = {'username': username,
                 'password': password,
                 're-password': repassword,
                 'mail_or_mobile': mail_or_mobile}
    return send_account_request(token, post_data, 'user_create')
def authenticate_user(user_identifier, password):
    token = get_token(user_identifier)
    payload = {'password': password}
    res = send_account_request(token, payload, 'user_authenticate')
    return res
