from dataclasses import dataclass


@dataclass(frozen=True)
class Paper:
    id: str
    title: str
    authors: list[str]
    abstract: str
    published_at: str
    url: str