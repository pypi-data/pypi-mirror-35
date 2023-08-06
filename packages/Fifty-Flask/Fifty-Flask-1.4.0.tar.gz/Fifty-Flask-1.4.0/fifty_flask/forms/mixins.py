class CSRFControlMixin(object):
    """ Mixin to enable / disable csrf for a specific form at the class or instance level.
    """

    csrf_enabled = None

    def __init__(self, csrf_enabled=None, *args, **kwargs):
        if csrf_enabled is None:
            csrf_enabled = self.get_csrf_enabled(*args, **kwargs)
        super(CSRFControlMixin, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)

    def get_csrf_enabled(self, *args, **kwargs):
        return self.csrf_enabled


class CSRFDisabledMixin(CSRFControlMixin):
    """ Mixin to disable CSRF Tokens on a specific form
    """
    csrf_enabled = False
