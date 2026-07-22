"""Compatibility entry point for tools that run from the repository root."""

from server.app import app, get_events as events
from server.models import Event

__all__ = ["app", "events", "Event"]
