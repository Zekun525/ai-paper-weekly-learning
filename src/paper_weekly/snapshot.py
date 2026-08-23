import json
from datetime import datetime, timezone
from pathlib import Path

from paper_weekly.models import Paper


def save_snapshot(
    path: Path,
    papers: list[Paper],
    query: str,
) -> None:
    payload = {
        "query": query,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "papers": [
            {
                "id": paper.id,
                "title": paper.title,
                "authors": paper.authors,
                "abstract": paper.abstract,
                "published_at": paper.published_at,
                "url": paper.url,
            }
            for paper in papers
        ],
    }

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def load_snapshot(path: Path) -> list[Paper]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [Paper(**item) for item in payload["papers"]]