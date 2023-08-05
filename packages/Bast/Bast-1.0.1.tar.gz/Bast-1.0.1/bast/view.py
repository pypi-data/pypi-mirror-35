"""
    Bast Web Framework
    (c) Majiyagbe Oluwole <oluwole564@gmail.com>

    For full copyright and license information, view the LICENSE distributed with the Source Code
"""

import os
from jinja2 import Environment, FileSystemLoader, TemplateNotFound, select_autoescape


def script(js_file):
    """
    Returns a route to the JS folder. Renders the JS file in the js folder
    Error 404 is seen in the server log if not found
    :param js_file:
    :return:
    """
    if 'http' in js_file:
        return '<script type="text/javascript" src="' + js_file + '"></script>'
    return '<script type="text/javascript" src="/script/' + js_file + '"></script>'


def css(css_file):
    """
    Returns a route to the CSS File and renders it to the server
    Error 404 is seen in the server log if not found
    :param css_file:
    :return:
    """
    if 'http' in css_file:
        return '<link rel="stylesheet" href="' + css_file + '">'
    return '<link rel="stylesheet" href="/css/' + css_file + '">'


def image(image_file, alt_name="image"):
    """
    Returns a route to the image file and renders it to the server
    Error 404 is thrown in server log if not found
    :param alt_name:
    :param image_file:
    :return:
    """
    if 'http' in image_file:
        return '<img src="' + image_file + '" alt="' + alt_name + '">'
    return '<img src="/images/' + image_file + '" alt="' + alt_name + '">'


# def session():
#     return


class TemplateRendering:
    """
    Base class to load the template directory from the OS Environment TEMPLATE_FOLDER variable
    """

    dict_object = {}

    def __init__(self):
        self.dict_object = {}

    def add_(self, key, _dict_):
        self.dict_object[key] = _dict_
        return self

    def render_template(self, template_name, **kwargs):
        template_dir = os.environ['TEMPLATE_FOLDER']

        env = Environment(loader=FileSystemLoader(template_dir))

        env.globals['css'] = css
        env.globals['script'] = script

        self.dict_object.update(**kwargs)

        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        content = template.render(self.dict_object)
        return content

    @classmethod
    def render_exception(cls, **kwargs):
        template_dir = os.path.dirname(os.path.realpath(__file__)) + "/exception"
        print(template_dir)
        env = Environment(loader=FileSystemLoader(template_dir))

        try:
            template = env.get_template('exception.html')
        except TemplateNotFound:
            raise TemplateNotFound('exception.html')
        content = template.render(**kwargs)
        return content
