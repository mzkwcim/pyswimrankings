import json
from pathlib import Path


def load_config(path: Path | None = None) -> dict:
    """
    Load configuration from a JSON file.

    Args:
        path: Optional path to config file. Defaults to config.json next to this module.

    Returns:
        Configuration dictionary.
    """
    if path is None:
        path = Path(__file__).with_name("config.json")

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open(encoding="utf-8") as f:
        return json.load(f)