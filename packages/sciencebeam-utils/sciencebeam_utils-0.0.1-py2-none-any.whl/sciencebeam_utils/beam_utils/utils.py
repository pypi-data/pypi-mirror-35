import logging
from random import getrandbits

import apache_beam as beam
from apache_beam.metrics.metric import Metrics


def get_logger():
    return logging.getLogger(__name__)


def Spy(f):
    def spy_wrapper(x):
        f(x)
        return x
    return spy_wrapper


def MapSpy(f):
    return beam.Map(Spy(f))


def MapOrLog(fn, log_fn=None, error_count=None):
    if log_fn is None:
        log_fn = lambda e, x: get_logger().warning(
            'caught exception (ignoring item): %s, input: %.100s...',
            e, x, exc_info=e
        )
    error_counter = (
        Metrics.counter('MapOrLog', error_count)
        if error_count
        else None
    )

    def wrapper(x):
        try:
            yield fn(x)
        except Exception as e: # pylint: disable=broad-except
            if error_counter:
                error_counter.inc()
            log_fn(e, x)
    return beam.FlatMap(wrapper)


LEVEL_MAP = {
    'info': logging.INFO,
    'debug': logging.DEBUG
}


def Count(name, counter_value_fn):
    counter = Metrics.counter('Count', name)

    def wrapper(x):
        counter.inc(counter_value_fn(x) if counter_value_fn else 1)
        return x
    return name >> beam.Map(wrapper)


class GroupTransforms(beam.PTransform):
    """
    Convenience method to allow a PTransform for grouping purpose
    to be defined using a lambda function.
    (Completely unrelated to GroupBy transforms)
    """

    def __init__(self, expand_fn):
        super(GroupTransforms, self).__init__()
        self.expand_fn = expand_fn

    def expand(self, pcoll):  # pylint: disable=W0221
        return self.expand_fn(pcoll)


def TransformAndCount(transform, counter_name, counter_value_fn=None):
    return GroupTransforms(lambda pcoll: (
        pcoll |
        transform |
        "Count" >> Count(counter_name, counter_value_fn)
    ))


def _identity(x):
    return x


def TransformAndLog(transform, log_fn=None, log_prefix='', log_value_fn=None, log_level='info'):
    if log_fn is None:
        if log_value_fn is None:
            log_value_fn = _identity
        log_level = LEVEL_MAP.get(log_level, log_level)

        log_fn = lambda x: get_logger().log(
            log_level, '%s%.50s...', log_prefix, log_value_fn(x)
        )

    return GroupTransforms(lambda pcoll: (
        pcoll |
        transform |
        "Log" >> MapSpy(log_fn)
    ))


def random_key():
    return getrandbits(32)


def PreventFusion(key_fn=None, name="PreventFusion"):
    """
    Prevents fusion to allow better distribution across workers.

    See:
    https://cloud.google.com/dataflow/service/dataflow-service-desc#preventing-fusion

    TODO Replace by: https://github.com/apache/beam/pull/4040
    """
    if key_fn is None:
        key_fn = lambda _: random_key()
    return name >> GroupTransforms(lambda pcoll: (
        pcoll |
        "AddKey" >> beam.Map(lambda x: (key_fn(x), x)) |
        "GroupByKey" >> beam.GroupByKey() |
        "Ungroup" >> beam.FlatMap(lambda element: element[1])
    ))
