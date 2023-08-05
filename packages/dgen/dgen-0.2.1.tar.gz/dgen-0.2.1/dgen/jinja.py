from jinja2 import Environment, select_autoescape


def create_env(loader):
    return Environment(
        block_start_string='[%',
        block_end_string='%]',
        variable_start_string='[[',
        variable_end_string=']]',
        comment_start_string='[#',
        comment_end_string='#]',
        autoescape=select_autoescape(['html', 'xml']),
        loader=loader
    )
