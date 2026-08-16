from pathlib import Path

from paper_weekly.loader import load_papers
from paper_weekly.renderer import render_weekly_report


def main() -> None:
    project_root = Path.cwd()
    sample_path = project_root / "data" / "samples" / "papers.json"
    report_path = project_root / "reports" / "sample-weekly.md"

    papers = load_papers(sample_path)
    report = render_weekly_report(papers)

    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")

    print(f"Wrote {len(papers)} papers to {report_path}")