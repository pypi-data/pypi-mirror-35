from fifty_flask.views.generic import FlashMixin, FormView
from flask import session
from tests.forms import PersonForm
from tests.mixins import AppMixin
from unittest import TestCase


class FlashFormView(FormView):
    form_cls = PersonForm


class FlashTests(AppMixin, TestCase):
    def setUp(self):
        super(FlashTests, self).setUp()
        self.form = PersonForm(csrf_enabled=False)

    def test_invalid_flash_nothing(self):
        fm = FlashMixin()
        self.assertEquals((None, None), fm.get_flash_invalid_message(self.form))
        fm.flash_valid(self.form)
        self.assertNotIn('_flashes', session)

    def test_valid_flash_nothing(self):
        fm = FlashMixin()
        self.assertEquals((None, None), fm.get_flash_valid_message(self.form))
        fm.flash_invalid(self.form)
        self.assertNotIn('_flashes', session)
