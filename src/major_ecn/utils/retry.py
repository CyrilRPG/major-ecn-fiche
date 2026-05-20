"""Retry asynchrone avec backoff exponentiel pour les erreurs API transitoires."""

from __future__ import annotations

import asyncio
import random
from collections.abc import Awaitable, Callable
from typing import TypeVar

from major_ecn.utils.logger import get_logger

T = TypeVar("T")

# Codes HTTP considérés comme transitoires (méritent un nouvel essai).
_TRANSIENT_STATUS = {408, 409, 429, 500, 502, 503, 504}


def _is_transient(exc: BaseException) -> bool:
    """Détermine si une exception API justifie une nouvelle tentative."""
    status = getattr(exc, "status_code", None)
    if isinstance(status, int) and status in _TRANSIENT_STATUS:
        return True
    name = type(exc).__name__.lower()
    if any(token in name for token in ("ratelimit", "timeout", "connection", "apistatus",
                                       "internalserver", "overloaded", "apiconnection")):
        return True
    return isinstance(exc, (asyncio.TimeoutError, ConnectionError))


async def retry_async(
    func: Callable[[], Awaitable[T]],
    *,
    attempts: int = 2,
    base_delay: float = 2.0,
    label: str = "appel API",
) -> T:
    """Exécute `func` avec retry sur erreur transitoire (backoff exponentiel).

    `attempts` est le nombre TOTAL d'essais (1 essai initial + retries).
    Conforme à la spec : 1 nouvel essai par défaut sur 429/500/timeout.
    """
    logger = get_logger()
    last_exc: BaseException | None = None

    for attempt in range(1, attempts + 1):
        try:
            return await func()
        except BaseException as exc:  # noqa: BLE001 — on filtre ensuite
            last_exc = exc
            if attempt >= attempts or not _is_transient(exc):
                raise
            delay = base_delay * (2 ** (attempt - 1)) + random.uniform(0, 0.5)
            logger.warning(
                "[yellow]%s : échec transitoire (%s) — nouvel essai dans %.1fs "
                "(%d/%d)[/yellow]",
                label, type(exc).__name__, delay, attempt, attempts - 1,
            )
            await asyncio.sleep(delay)

    assert last_exc is not None  # pragma: no cover — boucle garantit une exception
    raise last_exc
