from pathlib import Path
import xml.etree.ElementTree as ET

from paper_weekly.models import Paper


ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def load_papers_from_arxiv_xml(path: Path) -> list[Paper]:
    root = ET.fromstring(path.read_text(encoding="utf-8"))
    papers: list[Paper] = []

    for entry in root.findall("atom:entry", ATOM_NS):
        authors = [
            author.findtext("atom:name", default="", namespaces=ATOM_NS).strip()
            for author in entry.findall("atom:author", ATOM_NS)
        ]
        url = entry.find("atom:link[@rel='alternate']", ATOM_NS).get("href", "")

        papers.append(
            Paper(
                id=entry.findtext("atom:id", default="", namespaces=ATOM_NS).strip(),
                title=entry.findtext("atom:title", default="", namespaces=ATOM_NS).strip(),
                authors=authors,
                abstract=entry.findtext("atom:summary", default="", namespaces=ATOM_NS).strip(),
                published_at=entry.findtext("atom:published", default="", namespaces=ATOM_NS).strip(),
                url=url,
            )
        )

    return papers