from pathlib import Path

import pytest

from paper_weekly.arxiv_loader import ArxivEmptyResultError, ArxivXmlError, load_papers_from_arxiv_xml


def test_empty_arxiv_feed_raises(tmp_path: Path) -> None:
    xml_path = tmp_path / "empty.xml"
    xml_path.write_text(
        """\
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom"></feed>
""",
        encoding="utf-8",
    )

    with pytest.raises(ArxivEmptyResultError):
        load_papers_from_arxiv_xml(xml_path)


def test_broken_xml_raises(tmp_path: Path) -> None:
    xml_path = tmp_path / "broken.xml"
    xml_path.write_text("<feed><entry>", encoding="utf-8")

    with pytest.raises(ArxivXmlError):
        load_papers_from_arxiv_xml(xml_path)


def test_missing_link_raises(tmp_path: Path) -> None:
    xml_path = tmp_path / "missing-link.xml"
    xml_path.write_text(
        """\
<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2608.00001v1</id>
    <title>Broken entry</title>
    <summary>Missing alternate link</summary>
    <published>2026-08-18T00:00:00Z</published>
    <author><name>Tester</name></author>
  </entry>
</feed>
""",
        encoding="utf-8",
    )

    with pytest.raises(ArxivXmlError):
        load_papers_from_arxiv_xml(xml_path)