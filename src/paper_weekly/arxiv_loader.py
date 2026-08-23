from pathlib import Path
import xml.etree.ElementTree as ET

from paper_weekly.models import Paper


ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


class ArxivXmlError(RuntimeError):
    pass


class ArxivEmptyResultError(ArxivXmlError):
    pass


def load_papers_from_arxiv_xml(path: Path) -> list[Paper]:
    try:
        root = ET.fromstring(path.read_text(encoding="utf-8"))
    except ET.ParseError as exc:
        raise ArxivXmlError(f"Failed to parse arXiv XML: {exc}") from exc

    papers: list[Paper] = []

    for entry in root.findall("atom:entry", ATOM_NS):
        authors = [
            author.findtext("atom:name", default="", namespaces=ATOM_NS).strip()
            for author in entry.findall("atom:author", ATOM_NS)
        ]
        link = entry.find("atom:link[@rel='alternate']", ATOM_NS)
        if link is None or not link.get("href"):
            raise ArxivXmlError("Entry is missing an alternate link")

        papers.append(
            Paper(
                id=entry.findtext("atom:id", default="", namespaces=ATOM_NS).strip(),
                title=entry.findtext("atom:title", default="", namespaces=ATOM_NS).strip(),
                authors=authors,
                abstract=entry.findtext("atom:summary", default="", namespaces=ATOM_NS).strip(),
                published_at=entry.findtext("atom:published", default="", namespaces=ATOM_NS).strip(),
                url=link.get("href", "").strip(),
            )
        )

    if not papers:
        raise ArxivEmptyResultError("arXiv XML returned no entries")

    return papers
