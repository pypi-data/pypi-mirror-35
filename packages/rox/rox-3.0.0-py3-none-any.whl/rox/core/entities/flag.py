from rox.core.entities.variant import Variant


class Flag(Variant):
    FLAG_TRUE_VALUE = 'true'
    FLAG_FALSE_VALUE = 'false'

    def __init__(self, default_value=False):
        super(Flag, self).__init__(Flag.FLAG_TRUE_VALUE if default_value else Flag.FLAG_FALSE_VALUE, [Flag.FLAG_FALSE_VALUE, Flag.FLAG_TRUE_VALUE])

    def is_enabled(self, context):
        value = self.get_value(context=context)
        return self.is_enabled_from_string(value)

    def enabled(self, context, action):
        if self.is_enabled(context):
            action()

    def disabled(self, context, action):
        if not self.is_enabled(context):
            action()

    def is_enabled_from_string(self, value):
        return value == Flag.FLAG_TRUE_VALUE
