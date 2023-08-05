from collections import namedtuple

from rox.core.logging.logging import Logging

ImpressionArgs = namedtuple('ImpressionArgs', ['reporting_value', 'experiment', 'context'])


class ImpressionInvoker:
    def __init__(self, internal_flags, custom_property_repository, device_properties, analytics_client, is_roxy):
        self.internal_flags = internal_flags
        self.custom_property_repository = custom_property_repository
        self.device_properties = device_properties
        self.analytics_client = analytics_client
        self.is_roxy = is_roxy

        self.impression_handlers = []

    def invoke(self, reporting_value, client_experiment, context):
        try:
            # TODO Implement analytics logic
            pass
        except Exception as ex:
            Logging.get_logger().error('Failed to send analytics', ex)

        self.raise_impression_event(ImpressionArgs(reporting_value, client_experiment, context))

    def register_impression_handler(self, handler):
        self.impression_handlers.append(handler)

    def raise_impression_event(self, args):
        for handler in self.impression_handlers:
            handler(args)
