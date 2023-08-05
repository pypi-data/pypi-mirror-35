import unittest

from rox.core.configuration.models.experiment_model import ExperimentModel
from rox.core.impression.impression_invoker import ImpressionInvoker, ImpressionArgs
from rox.core.impression.models.experiment import Experiment
from rox.core.impression.models.reporting_value import ReportingValue

try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock


class ImpressionInvokerTests(unittest.TestCase):
    def test_will_set_impression_invoker_empty_invoke_not_throwing_exception(self):
        internal_flags = Mock()
        impression_invoker = ImpressionInvoker(internal_flags, None, None, None, False)
        impression_invoker.invoke(None, None, None)

    def test_will_test_impression_invoker_invoke_and_parameters(self):
        internal_flags = Mock()
        impression_invoker = ImpressionInvoker(internal_flags, None, None, None, False)

        context = {'obj1', 1}

        reporting_value = ReportingValue('name', 'vaue')

        original_experiment = ExperimentModel('id', 'name', 'cond', True, None, set())
        experiment = Experiment(original_experiment)

        is_impression_raised = {'raised': False}

        def on_impression(e):
            self.assertEqual(reporting_value, e.reporting_value)
            self.assertEqual(experiment, e.experiment)
            self.assertEqual(context, e.context)

            is_impression_raised['raised'] = True

        impression_invoker.register_impression_handler(on_impression)
        impression_invoker.invoke(reporting_value, experiment, context)

        self.assertTrue(is_impression_raised['raised'])

    def test_experiment_constructor(self):
        original_experiment = ExperimentModel('id', 'name', 'cond', True, None, {'name1'})
        experiment = Experiment(original_experiment)

        self.assertEqual(experiment.name, original_experiment.name)
        self.assertEqual(experiment.identifier, original_experiment.id)
        self.assertEqual(experiment.is_archived, original_experiment.is_archived)
        self.assertTrue('name1' in original_experiment.labels)

    def test_reporting_value_constructor(self):
        reporting_value = ReportingValue('pi', 'ka')

        self.assertEqual('pi', reporting_value.name)
        self.assertEqual('ka', reporting_value.value)

    def test_impression_args_constructor(self):
        context = {'obj1': 1}
        reporting_value = ReportingValue('name', 'value')

        original_experiment = ExperimentModel('id', 'name', 'cond', True, None, set())
        experiment = Experiment(original_experiment)

        impression_args = ImpressionArgs(reporting_value, experiment, context)

        self.assertEqual(reporting_value, impression_args.reporting_value)
        self.assertEqual(experiment, impression_args.experiment)
        self.assertEqual(context, impression_args.context)

    def test_will_not_invoke_analytics_when_flag_is_off(self):
        pass
        # TODO Implement analytics logic

    def test_will_not_invoke_analytics_when_is_roxy(self):
        pass
        # TODO Implement analytics logic

    def test_will_invoke_analytics(self):
        pass
        # TODO Implement analytics logic

    def test_will_invoke_analytics_with_bad_distinct_id(self):
        pass
        # TODO Implement analytics logic
