"""Journalisation : console stylée (rich) + fichier `logs/run_<timestamp>.log`."""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler

from major_ecn.config import LOGS_DIR

console: Console = Console()


def setup_logging(verbose: bool = False, logs_dir: Path = LOGS_DIR) -> tuple[logging.Logger, Path]:
    """Configure le logger applicatif.

    Renvoie le logger et le chemin du fichier de log de ce run.
    """
    logs_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = logs_dir / f"run_{timestamp}.log"

    logger = logging.getLogger("major_ecn")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    logger.propagate = False

    # Handler console (rich) — niveau ajustable.
    console_handler = RichHandler(
        console=console,
        rich_tracebacks=True,
        show_path=False,
        markup=True,
        show_time=False,
    )
    console_handler.setLevel(logging.DEBUG if verbose else logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(message)s"))

    # Handler fichier — tout est tracé, en clair.
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)-8s | %(name)s | %(message)s")
    )

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger, log_path


def get_logger() -> logging.Logger:
    """Renvoie le logger applicatif (à utiliser après `setup_logging`)."""
    return logging.getLogger("major_ecn")
