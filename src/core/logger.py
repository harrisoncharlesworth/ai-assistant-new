import logging
import sys
from typing import Any

import structlog

from core.config import settings

def setup_logging() -> structlog.BoundLogger:
    """Set up structured logging configuration."""
    
    # Set up standard logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.INFO,
    )

    # Configure structlog
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer()
        ],
        logger_factory=structlog.PrintLoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        cache_logger_on_first_use=True,
    )

    # Create logger instance
    logger: structlog.BoundLogger = structlog.get_logger()

    # Add environment context
    logger = logger.bind(
        app_name=settings.PROJECT_NAME,
        version=settings.VERSION,
        environment=settings.ENVIRONMENT
    )

    return logger

def get_logger() -> structlog.BoundLogger:
    """Get the configured logger instance."""
    return structlog.get_logger()

class LoggerMiddleware:
    """Middleware to add request logging."""

    def __init__(self, app: Any):
        self.app = app
        self.logger = get_logger()

    async def __call__(self, scope: dict, receive: Any, send: Any) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        self.logger.info(
            "request_started",
            path=scope.get("path", ""),
            method=scope.get("method", ""),
            client=scope.get("client", ("", ""))[0],
        )

        await self.app(scope, receive, send) 