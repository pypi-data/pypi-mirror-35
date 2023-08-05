import unittest

from concurrent import futures

from rox.core.core import Core

try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock


class CoreTests(unittest.TestCase):
    def test_will_check_core_setup_when_options_with_roxy(self):
        sdk_settings = Mock()
        device_props = Mock()
        rox_options = Mock()
        rox_options.roxy_url = 'http://site.com'

        c = Core()
        task = c.setup(sdk_settings, device_props, rox_options)
        futures.wait([task])

    def test_will_check_core_setup_when_no_options(self):
        sdk_settings = Mock()
        device_props = Mock()

        c = Core()
        task = c.setup(sdk_settings, device_props, None)
        futures.wait([task])
