""" Quick Assess"""

import argparse
import shlex
import colorama
import readline, os
from base.utils.cli import (
    ArgumentParserError,
    MyArgumentParser,
    show,
    Cli,
    Command,
    exit_handler,
)
from assess.noc.app import noc_app
from assess.points.app import pt_app
from assess.solution.app import sl_app
from assess.app_client import client_app
from config import console
from dataclasses import dataclass


@dataclass()
class Client:
    PA=None
    SP=None
    PATH=[] # paths to immigration, exp: LMIA, WP,BCPNP,PR
    LAST_SOLUTIONS=[]
    SOLUTIONS=[]

client=Client()
cli = Cli()


def main_command(cmd):
    match cmd:
        case Command(command="clear" | "ls", tokens=[*keywords]):
            os.system(cmd.command)
        case Command(command="help" | "h", tokens=[*keywords]):
            main_parser().print_help()
        case Command(command="noc", tokens=[*keywords]):
            cli.command_chain.append("noc")
            noc_app(cli)
        case Command(command="pt", tokens=[*keywords]):
            cli.command_chain.append("pt")
            pt_app(cli)
        case Command(command="sl", tokens=[*keywords]):
            cli.command_chain.append("solution")
            sl_app(cli,client)
        case Command(command="client", tokens=[*keywords]):
            cli.command_chain.append("client")
            client_app(cli,client)
        case Command(command="", tokens=[*keywords]):
            pass
        case _:
            console.print(f"No such command: {cmd.command}", style="red")


def main_parser():
    parser = MyArgumentParser()
    parser.add_argument("command", choices=["exit", "noc", "pt", "pts"])
    return parser


def main():
    # Initialize colorama
    colorama.init()
    # Initialize readline
    readline.insert_text("")
    readline.redisplay()

    parser = main_parser()
    while True:
        cmd = cli.get_command()
        if cmd.command in ["e", "q", "quit", "exit"]:
            break
        main_command(cmd)

    colorama.deinit()


if __name__ == "__main__":
    main()
