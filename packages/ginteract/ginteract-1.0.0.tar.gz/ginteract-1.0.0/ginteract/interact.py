import io
import termios

import click
import inquirer


class Choices(click.Choice):
    def convert(self, value, param, ctx):
        for item in value.split():
            super().convert(item, param, ctx)
        return value

    def __repr__(self):
        return 'Choices(%r)' % list(self.choices)


def prompt(choices, message='Choice', current=None, multiple=False):
    if current:
        message = '{} [{}]'.format(message, current)

    cls = inquirer.Checkbox if multiple else inquirer.List
    question = [cls('key', message=message, choices=choices)]
    try:
        choice = inquirer.prompt(question)
        if choice is None:
            raise click.Abort
        choice = choice['key']
    except (termios.error, io.UnsupportedOperation):
        text = '{} ({})'.format(message, ', '.join(choices))
        if multiple:
            choice = click.prompt(text, default=choices[0], type=Choices(choices))
            choice = choice.split()
        else:
            choice = click.prompt(text, default=choices[0], type=click.Choice(choices))

    return choice
