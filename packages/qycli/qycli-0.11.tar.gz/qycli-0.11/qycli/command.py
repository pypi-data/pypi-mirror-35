# coding: utf-8 2018/9/4 13:38
import os
import sys

from yaml import load, Loader
from argparse import ArgumentParser

from . import BASE_DIR
from . import ArgumentInfo
from .globals import conf_file_name
from .parser import Parser
from .httpcli import HttpClient


def get_cmd_obj(cmd):
    """获取命令行类对象"""
    cmd_obj = globals().get(cmd, None)
    return cmd_obj


class BaseCMD(object):
    args_parser = ArgumentParser(prog="qycli", usage="%(prog)s <cmd> [parameters]")

    cmd = ""

    params = {}

    list_params = ()
    other_params = ()

    argument_infos = []

    @classmethod
    def set_conf_option(cls):
        default_path = os.path.join(BASE_DIR, conf_file_name)
        cls.args_parser.add_argument(
            "-f", "--config", dest="conf_file", action="store",
            type=str, default=default_path, help="config file of your access keys"
        )

    @classmethod
    def get_conf_params(cls, args):
        """获得配置文件中的参数"""
        options = cls.args_parser.parse_args(args)
        # print("get_conf_params", options)
        conf_path = options.conf_file
        conf_params = cls.load_conf(conf_path)
        return conf_params

    @classmethod
    def load_conf(cls, conf_path):
        """加载配置文件"""
        try:
            with open(conf_path, encoding="utf-8") as f:
                conf_dict = load(f, Loader=Loader)
                return conf_dict
        except FileNotFoundError as e:
            print("'{}' is not existed\nplease use -f conf_path config your qy_config.yaml file".format(conf_path))
            cls.args_parser.print_help()
            sys.exit(-1)

    @classmethod
    def set_options(cls, args):

        args_parser = cls.args_parser
        for info in cls.argument_infos:
            args_parser.add_argument(info.shot_name, info.full_name, dest=info.dest,
                                     action=info.action, type=info.type, default=info.default,
                                     help=info.help)
        # 把从命令行获取参数args设置到parmas中去
        cls._set_params(args)

    @classmethod
    def _set_params(cls, args):
        params = cls.params
        option = cls.args_parser.parse_args(args)
        print("_set_params", option)

        # 给list类型参数赋值
        for key in cls.list_params:
            value = getattr(option, key, "")
            # 如果参数不为空字符串，则变成list
            if value:
                params[key] = list(map(lambda x: x.strip(), value.strip().split(",")))

        # 给非list类型参数赋值
        for key in cls.other_params:
            params[key] = getattr(option, key, "")

        print("_set_params", params)

    @classmethod
    def get_url_params(cls, args):
        """将命令行传入的option参数args转换成url路径后面要传入的params"""

        cls.set_conf_option()
        # 设置参数到params变量中去，此时的params不包含公共参数
        cls.set_options(args)
        conf_params = cls.get_conf_params(args)
        print("conf_params", conf_params)
        params = Parser.assemble_params(cls.cmd, cls.params, conf_params)
        return params

    @classmethod
    def execute(cls, args):
        params = cls.get_url_params(args)
        # print("params: ", params)
        http_client = HttpClient()
        http_client.send_request(params)


class DescribeInstances(BaseCMD):
    cmd = "DescribeInstances"

    list_params = ("instances", "status", "image_id", "instance_type", "tags")
    other_params = ("search_word", "verbose", "offset", "limit", "zone")

    argument_infos = [
        ArgumentInfo("-i", "--instances", dest="instances", action="store",
                     type=str, default="", help='IDs of hosts'),

        ArgumentInfo("-s", "--status", dest="status", action="store",
                     type=str, default="", help='status of hosts'),

        ArgumentInfo("-im", "--image_id", dest="image_id", action="store",
                     type=str, default="", help='the image id of host'),

        ArgumentInfo("-t", "--instance_type", dest="instance_type", action="store",
                     type=str, default="", help="types of your hosts"),

        ArgumentInfo("-sw", "--search_word", dest="search_word", action="store",
                     type=str, default="", help="search by words"),

        ArgumentInfo("-v", "--verbose", dest="verbose", action="store",
                     type=int, default=0, help="verbose messages"),

        ArgumentInfo("-o", "--offset", dest="offset", action="store",
                     type=int, default=0, help='offset of data'),

        ArgumentInfo("-l", "--limit", dest="limit", action="store",
                     type=int, default=20, help="length of data"),

        ArgumentInfo("-tg", "--tags", dest="tags", action="store",
                     type=str, default="", help="IDs of tags"),

        ArgumentInfo("-z", "--zone", dest="zone", action="store",
                     type=str, default=None, help="the ID of zone"),
    ]


class RunInstances(BaseCMD):
    cmd = "RunInstances"

    list_params = ()
    other_params = ("image_id", "instance_type", "login_mode", "login_passwd", "zone")

    argument_infos = [
        ArgumentInfo("-im", "--image_id", dest="image_id", action="store",
                     type=str, default="", help="the image id of host"),

        ArgumentInfo("-t", "--instance_type", dest="instance_type", action="store",
                     type=str, default="", help="types of your hosts"),

        ArgumentInfo("-l", "--login_mode", dest="login_mode", action="store",
                     type=str, default="", help="SSH or password"),

        ArgumentInfo("-p", "--login_passwd", dest="login_passwd", action="store",
                     type=str, default="", help="login by password"),

        ArgumentInfo("-z", "--zone", dest="zone", action="store",
                     type=str, default=None, help="the ID of zone"),
    ]


class TerminateInstances(BaseCMD):
    cmd = "TerminateInstances"

    list_params = ("instances",)
    other_params = ("direct_cease", "zone")

    argument_infos = [
        ArgumentInfo("-i", "--instances", dest="instances", action="store",
                     type=str, default="", help='IDs of hosts'),

        ArgumentInfo("-d", "--direct_cease", dest="direct_cease", action="store",
                     type=int, default=0, help="destroy host"),

        ArgumentInfo("-z", "--zone", dest="zone", action="store",
                     type=str, default=None, help="the ID of zone"),
    ]


if __name__ == '__main__':
    DescribeInstances.execute([
        # "-i", "i-pryj70hk, i-i076i6zm",
        # "-z", "pek3",
        # "-h"
    ])
