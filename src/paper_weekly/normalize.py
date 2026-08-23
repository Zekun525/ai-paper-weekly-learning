from datetime import datetime

from paper_weekly.models import Paper


def clean_text(value: str) -> str:
    return " ".join(value.split())


def normalize_date(value: str) -> str:
    normalized = value.strip().replace("Z", "+00:00")
    return datetime.fromisoformat(normalized).date().isoformat()


def normalize_papers(papers: list[Paper]) -> list[Paper]:
    by_id: dict[str, Paper] = {}

    for paper in papers:
        normalized = Paper(
            id=clean_text(paper.id),
            title=clean_text(paper.title),
            authors=[clean_text(author) for author in paper.authors],
            abstract=clean_text(paper.abstract),
            published_at=normalize_date(paper.published_at),
            url=clean_text(paper.url),
        )

        current = by_id.get(normalized.id)
        if current is None or normalized.published_at > current.published_at:
            by_id[normalized.id] = normalized

    return sorted(
        by_id.values(),
        key=lambda paper: (paper.published_at, paper.id),
        reverse=True,
    )