aiapi.pro 官方SDK包

使用方式
在http://aiapi.pro注册一个账户拿到一个Token后

from aiapi import request_api

authorization = "您的Token"
api_name = "api名称"
api_action = "api动作名称"
api_params = "参数"
request_api(authorization, api_name, api_action, api_params)

