import json
from pathlib import Path

from paper_weekly.models import Paper


def load_papers(path: Path) -> list[Paper]:
    raw_items = json.loads(path.read_text(encoding="utf-8"))
    return [Paper(**item) for item in raw_items]