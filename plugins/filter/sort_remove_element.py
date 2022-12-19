def sort_remove_element(items, reverse, keep_count=0):
    if len(items) < keep_count:
        return []
    else:
        return [
            item
            for item in sorted(items, reverse=reverse)[keep_count:]
        ]


class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            'sort_remove_element': sort_remove_element,
        }
