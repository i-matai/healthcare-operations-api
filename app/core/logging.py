"""Minimal application logging configuration."""

import logging


def configure_logging(log_level: str) -> None:
    """Configure safe, process-level logging without request or domain data."""
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
