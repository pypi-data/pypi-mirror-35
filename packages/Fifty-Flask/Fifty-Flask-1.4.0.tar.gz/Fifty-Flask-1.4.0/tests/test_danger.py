from datetime import datetime
from fifty_flask.danger import decode_timed_token, decode_token, get_timed_token, get_token
from itsdangerous import BadPayload, BadSignature, SignatureExpired
from tests.mixins import AppMixin
from unittest import TestCase


salt = 'salt'
expected_payload_tokens = (
        ('hi', 'ImhpIg.zThxSJtMtwwo823OIkxdXchFuu8'),
        (True, 'dHJ1ZQ.C84uq5QZPPn6-ygc-SJ52z1TImE'),
        ({'a': 'b'}, 'eyJhIjoiYiJ9.cEIRCFD3_r4snHsMQOqCkkVGct4'),
        (123, 'MTIz.3IrfesgYDcv_x4mvCHzYgU1AAWA'),
        (['a', 'b'], 'WyJhIiwiYiJd.TncD2vx_WmCqvEoloY2efkCl100')
        )


class DangerTests(AppMixin, TestCase):
    def setUp(self):
        super(DangerTests, self).setUp()
        self.app.config['ITSDANGEROUS_SECRET'] = 'its-so-secret'

    def test_get_token(self):
        """Encoded payloads should match the expected token values.
        """
        for payload, expected_token in expected_payload_tokens:
            self.assertEqual(expected_token, get_token(payload, salt))

    def test_decode_token(self):
        """Decoded tokens should match the expected payload values.
        """
        for expected_payload, token in expected_payload_tokens:
            self.assertEqual(expected_payload, decode_token(token, salt))

    def test_decode_bad_signature_token(self):
        """Invalid tokens should raise BadSignature.
        """
        with self.assertRaises(BadSignature):
            decode_token('invalid-token', salt)

    def test_decode_timed_token_with_wrong_serializer(self):
        """A timed token should not be able to be decoded with a non-timed serializer.
        """
        with self.assertRaises(BadPayload):
            decode_token(get_timed_token('i-am-timed', salt), salt)

    def test_decode_timed_token(self):
        """A timed token should deserialize to the expected payload and a datetime timestamp.
        """
        expected_payload = 'time me'
        timed_token = get_timed_token(expected_payload, salt)
        payload, timestamp = decode_timed_token(timed_token, salt)
        self.assertEqual(expected_payload, payload)
        self.assertIsInstance(timestamp, datetime)

    def test_decode_timed_token_only_return_payload(self):
        """A timed token should deserialize to the expected payload, excluding the datetime
        timestamp.
        """
        expected_payload = {'return': 'to sender'}
        timed_token = get_timed_token(expected_payload, salt)
        payload = decode_timed_token(timed_token, salt, return_timestamp=False)
        self.assertEqual(expected_payload, payload)

    def test_decode_timed_token_ok_max_age(self):
        """A timed token should successfully decode if it hasn't expired.
        """
        expected_payload = 'so fresh'
        timed_token = get_timed_token(expected_payload, salt)
        payload, timestamp = decode_timed_token(timed_token, salt, max_age=60)
        self.assertEqual(expected_payload, payload)
        payload = decode_timed_token(timed_token, salt, max_age=60, return_timestamp=False)
        self.assertEqual(expected_payload, payload)

    def test_decode_timed_token_expired_max_age(self):
        """A timed token should raise SignatureExpired when it has expired.
        """
        payload = 'so old'
        timed_token = get_timed_token(payload, salt)
        with self.assertRaises(SignatureExpired):
            decode_timed_token(timed_token, salt, max_age=-1)

    def test_decode_timed_token_expired_max_age_without_timestamp(self):
        """A timed token should raise SignatureExpired when it has expired, even if we tell it to
        not return the timestamp.
        """
        payload = 'so old'
        timed_token = get_timed_token(payload, salt)
        with self.assertRaises(SignatureExpired):
            decode_timed_token(timed_token, salt, max_age=-1, return_timestamp=False)
