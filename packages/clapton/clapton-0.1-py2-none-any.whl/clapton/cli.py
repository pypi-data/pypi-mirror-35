#!/usr/bin python
# -*- coding: utf-8 -*-

import argparse
import json
import os
import sys
import pkg_resources
import argcomplete
import traceback
import subprocess
from builtins import input
import json

import click
from click.exceptions import ClickException


def to_bool(string):
    if type(string) is bool:
        return string
    return True if string[0] in ["Y", "y"] else False

class CLI(object):
    
    def __init__(self):
        self.var_args = None
        self.command = None

    def command_dispatcher(self, args=None):
        desc = ('clapton,  a system to manage your DL4J dependencies from Python.\n')
        parser = argparse.ArgumentParser(description=desc)
        parser.add_argument(
            '-v', '--version', action='version',
            version=0.1,
            #version=pkg_resources.get_distribution("clapton").version,
            help='Print clapton version'
        )

        subparsers = parser.add_subparsers(title='subcommands', dest='command')
        subparsers.add_parser('init', help='Initialize clapton')

        argcomplete.autocomplete(parser)
        args = parser.parse_args(args)
        self.var_args = vars(args)

        if not args.command:
            parser.print_help()
            return

        self.command = args.command

        if self.command == 'init':
            self.init()
            return

    def init(self):

        click.echo(click.style(u"""\n      ___           ___       ___           ___           ___           ___           ___     
     /\  \         /\__\     /\  \         /\  \         /\  \         /\  \         /\__\    
    /::\  \       /:/  /    /::\  \       /::\  \        \:\  \       /::\  \       /::|  |   
   /:/\:\  \     /:/  /    /:/\:\  \     /:/\:\  \        \:\  \     /:/\:\  \     /:|:|  |   
  /:/  \:\  \   /:/  /    /::\~\:\  \   /::\~\:\  \       /::\  \   /:/  \:\  \   /:/|:|  |__ 
 /:/__/ \:\__\ /:/__/    /:/\:\ \:\__\ /:/\:\ \:\__\     /:/\:\__\ /:/__/ \:\__\ /:/ |:| /\__\\
 \:\  \  \/__/ \:\  \    \/__\:\/:/  / \/__\:\/:/  /    /:/  \/__/ \:\  \ /:/  / \/__|:|/:/  /
  \:\  \        \:\  \        \::/  /       \::/  /    /:/  /       \:\  /:/  /      |:/:/  / 
   \:\  \        \:\  \       /:/  /         \/__/     \/__/         \:\/:/  /       |::/  /  
    \:\__\        \:\__\     /:/  /                                   \::/  /        /:/  /   
     \/__/         \/__/     \/__/                                     \/__/         \/__/\n""", fg='blue', bold=True))

        click.echo(click.style("clapton", bold=True) + " manages your machine learning setup for easy deployments!\n")

        DEFAULT_INPUT_TYPE = 'text'
        DEFAULT_MODEL_TYPE = 'keras'
        DEFAULT_MODEL_PATH = ''
        DEFAULT_PREPROCESSING = 'n'
        DEFAULT_PREPROC_TYPE = ''
        DEFAULT_PREPROC_PATH = ''

        # Input type
        input_type = input("Which data type does your input have (default '%s'): " % DEFAULT_INPUT_TYPE) or DEFAULT_INPUT_TYPE

        # Model type
        model_type = input("Which ML library do you use for your model? (required): ") or DEFAULT_MODEL_TYPE
        model_type = model_type.lower()

        # Model path
        model_path = input("Where is your serialized model stored? (required): ") or DEFAULT_MODEL_PATH

        # Preprocessing
        preprocessing = input("Do you have a preprocessing step for your model? (default 'n') [y/n]: ") or DEFAULT_PREPROCESSING
        preprocessing = to_bool(preprocessing)
        preprocessing_type = DEFAULT_PREPROC_TYPE
        preprocessing_path = DEFAULT_PREPROC_PATH
        if preprocessing:
            # Preprocessing type
            preprocessing_type = input("With which library did you create your pre-processing? (required): ") or DEFAULT_PREPROC_TYPE
            # Preprocessing path
            preprocessing_path = input("Where is your serialized pre-processing stored? (required): ") or DEFAULT_PREPROC_PATH


        cli_out = {
                'input_type': input_type,
                'model_type': model_type,
                'model_path': model_path,
                'preprocessing': preprocessing,
                'preprocessing_type': preprocessing_type,
                'preprocessing_path': preprocessing_path
        }

        #validate_config(cli_out)
        formatted_json = json.dumps(cli_out, sort_keys=False, indent=2)

        click.echo("\nThis is your current settings file " + click.style("clapton_settings.json", bold=True) + ":\n")
        click.echo(click.style(formatted_json, fg="green", bold=True))

        confirm = input("\nDoes this look good? (default 'y') [y/n]: ") or 'yes'
        if not to_bool(confirm):
            click.echo("" + click.style("Please initialize clapton once again", fg="red", bold=True))
            return

        with open('clapton_settings.json', 'w') as f:
            f.write(formatted_json)


def handle():
    try:
        cli = CLI()
        sys.exit(cli.command_dispatcher())
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        click.echo(click.style("Error: ", fg='red', bold=True))
        traceback.print_exc()
        sys.exit()


def check_docker():
    devnull = open(os.devnull, 'w')
    try:
        subprocess.call(["docker", "--help"], stdout=devnull, stderr=devnull)
        click.echo(click.style("Docker is running, starting installation.", fg="green", bold=True))
    except:
        click.echo("" + click.style("Could not detect docker on your system. Make sure a docker deamon is running", fg="red", bold=True))
        raise Exception("Aborting installation, docker not found.")

if __name__ == '__main__':
    handle()
