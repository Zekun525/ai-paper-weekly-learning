from pathlib import Path

from paper_weekly.arxiv_loader import load_papers_from_arxiv_xml
from paper_weekly.models import Paper
from paper_weekly.normalize import normalize_papers
from paper_weekly.renderer import render_weekly_report
from paper_weekly.snapshot import load_snapshot, save_snapshot


ARXIV_XML = """\
<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:arxiv="http://arxiv.org/schemas/atom"
      xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2608.16100v1</id>
    <title>  TISC: A Text-Driven Image Semantic Communication System  </title>
    <updated>2026-08-17T03:16:37Z</updated>
    <published>2026-08-17T03:16:37Z</published>
    <summary>  First summary with  extra spaces.  </summary>
    <link href="https://arxiv.org/abs/2608.16100v1" rel="alternate" type="text/html"/>
    <author><name>Feifan Zhang</name></author>
    <author><name>Yuyang Du</name></author>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2608.16100v1</id>
    <title>TISC: A Text-Driven Image Semantic Communication System (revised)</title>
    <updated>2026-08-18T03:16:37Z</updated>
    <published>2026-08-18T03:16:37Z</published>
    <summary>Revised summary.</summary>
    <link href="https://arxiv.org/abs/2608.16100v1" rel="alternate" type="text/html"/>
    <author><name>Feifan Zhang</name></author>
    <author><name>Yuyang Du</name></author>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2608.15256v1</id>
    <title>  中文标题  </title>
    <updated>2026-08-16T03:16:37Z</updated>
    <published>2026-08-16T03:16:37Z</published>
    <summary>  含有 中文 与  多余空白  </summary>
    <link href="https://arxiv.org/abs/2608.15256v1" rel="alternate" type="text/html"/>
    <author><name>Lin Yin</name></author>
  </entry>
</feed>
"""


def test_arxiv_loader_reads_xml(tmp_path: Path) -> None:
    xml_path = tmp_path / "sample.xml"
    xml_path.write_text(ARXIV_XML, encoding="utf-8")

    papers = load_papers_from_arxiv_xml(xml_path)

    assert len(papers) == 3
    assert papers[0].title.strip() == "TISC: A Text-Driven Image Semantic Communication System"


def test_normalize_papers_is_stable_and_deduplicates() -> None:
    papers = [
        Paper("b", "  Older  ", [" A "], " x\n y ", "2026-08-01T00:00:00Z", " u "),
        Paper("a", " Newer ", [" B "], " z ", "2026-08-09T00:00:00Z", " v "),
        Paper("b", " Latest ", [" C "], " q ", "2026-08-05T00:00:00Z", " w "),
    ]

    first = normalize_papers(papers)
    second = normalize_papers(papers)

    assert first == second
    assert [paper.id for paper in first] == ["a", "b"]
    assert first[1].title == "Latest"


def test_snapshot_roundtrip_and_render(tmp_path: Path) -> None:
    papers = [
        Paper("a", "A paper", ["Author"], "Abstract", "2026-08-09", "https://example.com/a"),
        Paper("b", "B paper", ["作者"], "含有 中文", "2026-08-08", "https://example.com/b"),
    ]
    snapshot_path = tmp_path / "snapshot.json"

    save_snapshot(snapshot_path, papers, "semantic communication")
    restored = load_snapshot(snapshot_path)
    report = render_weekly_report(restored)

    assert snapshot_path.exists()
    assert len(restored) == 2
    assert "Semantic Communication Paper Weekly" in report
    assert "A paper" in report
    assert "B paper" in report
    assert "https://example.com/b" in report
