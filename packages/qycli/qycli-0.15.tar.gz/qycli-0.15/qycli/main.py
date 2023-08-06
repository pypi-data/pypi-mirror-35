# coding: utf-8 2018/9/3 15:20
import sys

from argparse import ArgumentParser

from qycli.command import get_cmd_obj

CMDS = ("RunInstances", "DescribeInstances", "TerminateInstances")


def bar():
    usage = ' %(prog)s <cmd> [parameters]\n\n' \
            + 'Here are valid cmds: [<{}>, <{}>, <{}>]'.format(*CMDS)

    parser = ArgumentParser(prog="qycli", usage=usage)
    parser.print_help()
    sys.exit(-1)


def check_args(args):
    if len(args) <= 1:
        print("QYCLI VERSION 0.10")
        bar()
    else:
        cmd = args[1]
        if cmd not in CMDS:
            bar()
            sys.exit(0)


def execute_cmd(cmd, params):
    command = get_cmd_obj(cmd)
    command.execute(params)


def main():
    args = sys.argv
    print(args)
    check_args(args)
    execute_cmd(args[1], args[2:])


if __name__ == '__main__':
    main()