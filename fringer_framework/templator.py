from jinja2 import Environment, FileSystemLoader


def render(template_name, folder='templates', static_url='/static/', **kwargs):
    env = Environment()
    env.loader = FileSystemLoader(folder)
    env.globals['static'] = static_url
    template = env.get_template(template_name)
    return template.render(**kwargs)

# /static/new_app/my_image.jpg

# {% load staticfiles %}
# src = "{% static "new_app/my_image.jpg" %}"
