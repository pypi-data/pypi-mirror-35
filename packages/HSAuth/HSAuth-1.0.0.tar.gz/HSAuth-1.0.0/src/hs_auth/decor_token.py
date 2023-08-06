#!/usr/bin/python
# -*- coding: utf-8 -*-¬
from flask import request, jsonify
import requests
from functools import wraps


def token_required(func):
    # token验证装饰器
    @wraps(func)
    def decorator(*args, **kwargs):
        if request.method == 'GET':
            grant_type = request.args.get('grant_type')
            auth_token = request.args.get('auth_token')
            key_url = 'http://127.0.0.1:5001/hs_auth/app_verify_token/'
            json_params = {'grant_type': grant_type, 'auth_token': auth_token, 'app_id': ''}
            res = requests.post(url=key_url, json=json_params,
                                headers={"Content-type": "application/json", "Accept": "*/*"})
            if res.text:
                return res.text
            return func(*args, **kwargs)
        raise RuntimeError('Verify failed')

    return decorator
