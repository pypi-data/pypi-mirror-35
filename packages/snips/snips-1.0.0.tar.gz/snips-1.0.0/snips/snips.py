#!/usr/bin/python
# pylint: disable=missing-docstring

from __future__ import print_function

import click
import glob
import os
import pyperclip

SNIP_DIR = os.path.join(os.path.expanduser("~"), '.snips')


@click.group()
def cli():
    # case : default
    # snips python-test
    # Copy the content of python-test in clipboard
    if os.path.isdir(SNIP_DIR) == False:
        os.mkdir(SNIP_DIR)


@click.command(name='get', help='get snippet into clipboard')
@click.argument('snippet')
def get(snippet):
    print('hello2')
    # case : save
    # snips save python-test
    # Create a file python-test in ~/.snips
    # that contains the content of clip board
    with open(os.path.join(SNIP_DIR, snippet), 'rb') as snippet_file:
        content = snippet_file.read()

    pyperclip.copy(content)


@click.command(name='display', help='display a snippet')
@click.argument('snippet')
def display(snippet):
    # case : save
    # snips save python-test
    # Create a file python-test in ~/.snips
    # that contains the content of clip board
    printSnippet(snippet)

@click.command(name='edit', help='edit a snippet')
@click.argument('snippet')
def edit(snippet):
    # case : edit
    # snips edit python-test
    click.edit(filename=os.path.join(SNIP_DIR, snippet))

@click.command(name='save', help='save clipboard content as a snippet')
@click.argument('snippet')
def save(snippet):
    # case : save
    # snips save python-test
    # Create a file python-test in ~/.snips
    # that contains the content of clip board
    content = pyperclip.paste()
    with open(os.path.join(SNIP_DIR, snippet), 'wb') as snippet_file:
        snippet_file.write(content)


@click.command(name='remove', help='remove a snippet')
@click.argument('snippet')
def remove(snippet):
    # case : save
    # snips save python-test
    # Create a file python-test in ~/.snips
    # that contains the content of clip board
    os.remove(os.path.join(SNIP_DIR, snippet))


@click.command(name='list', help='list snippets available')
@click.argument('snippetpattern', default='')
@click.option('--display', '-d', is_flag=True, help='display snippets content')
def cli_list(snippetpattern, display):
    # case : list
    # snips list python
    # Get a list of all files that begins with
    # python
    os.chdir(SNIP_DIR)
    snippet_files = sorted(glob.glob('{0}*'.format(snippetpattern)))
    for snippet_file in snippet_files:
        if display:
            print('-----------')
            click.echo(click.style(snippet_file, fg="green"))
            print('-----------')
            printSnippet(snippet_file)
        else:
            print(snippet_file)

def printSnippet(snippet):
    with open(os.path.join(SNIP_DIR, snippet), 'rb') as snippet_file:
        content = snippet_file.read()

    print(content)

cli.add_command(get)
cli.add_command(display)
cli.add_command(edit)
cli.add_command(remove)
cli.add_command(save)
cli.add_command(cli_list)


if __name__ == '__main__':
    cli()
