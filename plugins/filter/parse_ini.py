import configparser


def parse_ini(init_content, section, name, default):
    config = configparser.RawConfigParser()
    try:
        config.read_string(init_content)
    except configparser.MissingSectionHeaderError:
        try:
            config.read_string(f'[DEFAULT]\n{init_content}')
        except Exception as e:
            ValueError(f'Could not parse the file: {str(e)}')
    
    try:
        config_section = config[section]
    except Exception:
        config_section = {}
    
    return config_section.get(name, default)


class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            'parse_ini': parse_ini,
        }
