from paper_weekly.models import Paper


def render_weekly_report(papers: list[Paper]) -> str:
    lines = ["# Semantic Communication Paper Weekly", ""]

    for index, paper in enumerate(papers, start=1):
        authors = ", ".join(paper.authors)
        lines.extend(
            [
                f"## {index}. {paper.title}",
                "",
                f"- ID: {paper.id}",
                f"- Authors: {authors}",
                f"- Published: {paper.published_at}",
                f"- Link: {paper.url}",
                "",
                paper.abstract,
                "",
            ]
        )

    return "\n".join(lines)