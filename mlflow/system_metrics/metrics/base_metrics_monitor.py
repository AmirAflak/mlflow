"""Base class of system metrics monitor."""
import abc
from collections import defaultdict


class BaseMetricsMonitor(abc.ABC):
    """Base class of system metrics monitor."""

    def __init__(self):
        self._metrics = defaultdict(list)

    @abc.abstractmethod
    def collect_metrics(self):
        """Method to collect metrics.

        Sublcass should implement this method to collect metrics and store in `self._metrics`.
        """
        pass

    @abc.abstractmethod
    def aggregate_metrics(self):
        """Method to aggregate metrics.

        Sublcass should implement this method to aggregate the metrics and return it in a dict.
        """
        pass

    @property
    def metrics(self):
        return self._metrics

    def clear_metrics(self):
        self._metrics.clear()
