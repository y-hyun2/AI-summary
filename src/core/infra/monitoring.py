"""Monitoring stubs for InfoPilot core pipelines."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class Metric:
    name: str
    value: float
    labels: Dict[str, str]


class MonitoringClient:
    """Placeholder client for emitting metrics to an external system."""

    def emit(self, metric: Metric) -> None:
        # TODO: Connect to actual monitoring backend
        _ = metric
