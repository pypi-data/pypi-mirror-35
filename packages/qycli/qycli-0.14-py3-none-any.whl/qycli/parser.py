# coding: utf-8 2018/9/4 14:45
import hmac
import sys
import time
import base64
import collections

from _sha256 import sha256
from pprint import pprint
from urllib import parse

from .globals import common_params, prefix


def utc_zero(utc_format='%Y-%m-%dT%H:%M:%SZ'):
    utc_0 = time.gmtime()
    return time.strftime(utc_format, utc_0)


class Parser(object):

    @staticmethod
    def replace_key(params):

        for key in list(params.keys()):
            value = params[key]
            # 如果是list类型，把instances转成instances.1
            if isinstance(value, list):
                n = len(value)
                for i in range(n):
                    params['{}.{}'.format(key, i+1)] = value[i].strip()
                # 删除key为instances的键值对
                del params[key]

    @classmethod
    def assemble_params(cls, action, params, conf_params):
        """构建get请求参数"""

        # 更换params中的一些key
        cls.replace_key(params)

        zone, access_key_id, secret_access_key = cls.get_valid_conf_values(params, conf_params)

        # 更新公共参数中的action, zone, access_key_id
        common_params = cls.update_common_params(action, zone, access_key_id)
        params.update(common_params)
        pprint(params, indent=4)

        # 获得签名后的url参数
        url_params = cls.get_params_signed(params, secret_access_key)
        return url_params

    @staticmethod
    def get_valid_conf_values(params, conf_params):
        # new_zone表示在命令行中设置的zone
        new_zone = params.get("zone", None)
        try:
            zone = conf_params["zone"]
            access_key_id = conf_params["access_key_id"]
            secret_access_key = conf_params["secret_access_key"]
        except KeyError as e:
            print("key: {} not in {}\nplease check your qy_config.yaml file".format(e, list(conf_params.keys())))

            sys.exit(-1)
        zone = new_zone if new_zone else zone
        return zone, access_key_id, secret_access_key

    @staticmethod
    def update_common_params(action, zone, access_key_id):
        """更新公共参数中的值"""
        new_params = common_params.copy()
        print("update_common_params", action)
        new_params["action"] = action
        new_params["time_stamp"] = utc_zero()
        new_params["access_key_id"] = access_key_id
        new_params["zone"] = zone
        return new_params

    @staticmethod
    def get_params_signed(params, secret_access_key):
        """获取签名后的"""
        items = sorted(params.items(), key=lambda item: item[0])
        # 对字典安key值排序
        ordered_params = collections.OrderedDict(items)
        # 生成url
        url_params = parse.urlencode(ordered_params).replace("+", "%20")
        # 待签名的字符串
        sign_string = prefix + url_params
        h = hmac.new(bytes(secret_access_key, 'utf-8'), digestmod=sha256)
        h.update(sign_string.encode('utf-8'))
        sign = base64.b64encode(h.digest()).strip()
        signature = parse.quote_plus(sign)
        # print(signature)
        return url_params + "&signature=" + signature
