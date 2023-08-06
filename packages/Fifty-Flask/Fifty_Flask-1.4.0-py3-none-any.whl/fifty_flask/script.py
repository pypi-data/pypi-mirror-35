import os
from flask_script import Server as BaseServer


class Server(BaseServer):
    def __init__(self, extra_files=None, **options):
        self.extra_files = extra_files or []
        super(Server, self).__init__(**options)

    def __call__(self, app, *args, **kwargs):
        if 'extra_files' not in self.server_options:
            config_files = (
                'config_default.py',
                'config_local.py',
                'config_test_default.py',
                'config_test_local.py'
            )

            self.extra_files.extend(os.path.join(app_path, config_file)
                                    for app_path in (app.root_path, app.instance_path)
                                    for config_file in config_files)

            self.server_options['extra_files'] = self.extra_files

        super(Server, self).__call__(app, *args, **kwargs)
