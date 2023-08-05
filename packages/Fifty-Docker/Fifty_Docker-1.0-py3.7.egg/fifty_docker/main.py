#!/usr/bin/env python
import click
import json
import os
import yaml
from jinja2 import Environment, FileSystemLoader


@click.command()
@click.option('-t', '--template', type=click.Path(exists=True, dir_okay=False, resolve_path=True),
              help='The Jinja template to render')
@click.option('-o', '--output_file', type=click.Path(dir_okay=False, resolve_path=True),
              help='The output location of the rendered template',)
@click.option('-d', '--default_context', type=click.Path(exists=True, dir_okay=False),
              help='The default context variables to load (YAML)')
def render_template(template, output_file, default_context=None, json_env=True):
    context = load_jinja_context(default_context=default_context, json_env=json_env)
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        jinja_env = Environment(loader=FileSystemLoader(searchpath="/"), trim_blocks=True)
        with open(output_file, 'w') as f:
            jinja_template = jinja_env.get_template(template)
            f.write(jinja_template.render(context))
        return True
    except Exception as e:
        print(e)
        return False


def load_jinja_context(default_context=None, json_env=True):
    context = {}
    if default_context:
        context.update(load_default_context_from_yaml(default_context))

    for k, v in os.environ.items():
        try:
            context[k] = json.loads(str(v)) if json_env else v
        except:
            context[k] = v
    return context


def load_default_context_from_yaml(path):
    with open(path, 'r') as f:
        return yaml.load(f)


if __name__ == '__main__':
    render_template()
