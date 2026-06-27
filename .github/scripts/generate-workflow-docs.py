import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS_DIR = REPO_ROOT / ".github" / "workflows"
DOCS_DIR = REPO_ROOT / "documentation"


def load_yaml(file_path: Path) -> Optional[Dict[str, Any]]:
    if file_path.stat().st_size == 0:
        return None
    try:
        with file_path.open("r", encoding="utf-8") as fp:
            return yaml.safe_load(fp)
    except yaml.YAMLError:
        return None


def format_trigger(on_value: Any) -> List[str]:
    if on_value is None:
        return ["No trigger is defined for this workflow."]
    if isinstance(on_value, str):
        return [f"- `{on_value}`"]
    if isinstance(on_value, list):
        return [f"- `{item}`" for item in on_value]
    if isinstance(on_value, dict):
        lines: List[str] = []
        for event, config in on_value.items():
            if event == "schedule" and isinstance(config, list):
                lines.append("- `schedule` with the following cron entry(ies):")
                for cron_item in config:
                    lines.append(f"  - `{cron_item.get('cron')}`")
            elif isinstance(config, list):
                lines.append(f"- `{event}` with values: {config}")
            elif isinstance(config, dict):
                values = ", ".join(sorted(config.keys()))
                lines.append(f"- `{event}` with configuration: {values}")
            else:
                lines.append(f"- `{event}`")
        return lines
    return [f"- Unrecognized trigger format: `{type(on_value).__name__}`"]


def format_steps(steps: Any) -> List[str]:
    lines: List[str] = []
    if not steps:
        return ["- No steps defined."]
    for step in steps:
        if not isinstance(step, dict):
            continue
        name = step.get("name") or step.get("id") or "Unnamed step"
        condition = step.get("if")
        uses = step.get("uses")
        run = step.get("run")
        if uses:
            lines.append(f"- **{name}**: uses `{uses}`{f' if `{condition}`' if condition else ''}.")
        elif run:
            run_preview = run.strip().splitlines()[0].replace('`', '\`')
            lines.append(
                f"- **{name}**: runs shell commands starting with `{run_preview}`{f' if `{condition}`' if condition else ''}."
            )
        else:
            lines.append(f"- **{name}**: step with no `run` or `uses` field.")
    return lines


def format_job(job_name: str, job_data: Any) -> List[str]:
    lines: List[str] = [f"### `{job_name}`"]
    if not isinstance(job_data, dict):
        lines.append("- Invalid job definition.")
        return lines
    runs_on = job_data.get("runs-on")
    needs = job_data.get("needs")
    lines.append(f"- Runs on `{runs_on}`." if runs_on else "- Runner not specified.")
    if needs:
        if isinstance(needs, list):
            needs_list = ", ".join(f"`{item}`" for item in needs)
        else:
            needs_list = f"`{needs}`"
        lines.append(f"- Depends on {needs_list}.")
    lines.append("- Steps:")
    lines.extend(format_steps(job_data.get("steps")))
    return lines


def generate_doc(workflow_path: Path, workflow_data: Optional[Dict[str, Any]]) -> str:
    title = workflow_data.get("name") if isinstance(workflow_data, dict) else None
    if not title:
        title = workflow_path.stem.replace("-", " ").title()

    lines: List[str] = [f"# {workflow_path.name}", "", f"## {title}", ""]

    if workflow_data is None:
        lines.extend(
            [
                "## Status",
                "This workflow file is empty or could not be parsed.",
                "Add jobs and steps to the YAML file and re-run the generator.",
                "",
                "## Notes",
                "- This documentation file is generated automatically.",
                "- Empty or malformed workflow YAML files do not generate a detailed summary.",
            ]
        )
        return "\n".join(lines)

    lines.extend(["## Trigger", ""])
    lines.extend(format_trigger(workflow_data.get("on")))
    lines.append("")

    concurrency = workflow_data.get("concurrency")
    if concurrency:
        lines.extend(["## Concurrency", ""])
        if isinstance(concurrency, dict):
            group = concurrency.get("group")
            cancel = concurrency.get("cancel-in-progress")
            if group:
                lines.append(f"- `group: {group}`")
            if cancel is not None:
                lines.append(f"- `cancel-in-progress: {cancel}`")
        else:
            lines.append(f"- `concurrency` is defined as `{concurrency}`.")
        lines.append("")

    jobs = workflow_data.get("jobs")
    if jobs and isinstance(jobs, dict):
        lines.extend(["## Jobs", ""])
        for job_name, job_data in jobs.items():
            lines.extend(format_job(job_name, job_data))
            lines.append("")
    else:
        lines.extend(["## Jobs", "", "- No jobs defined.", ""])

    lines.extend(
        [
            "## Key concepts",
            "",
            "- This documentation is auto-generated from the workflow YAML file.",
            "- Review the workflow file to customize the trigger, jobs, and steps.",
            "",
            "> This file is generated automatically by `.github/scripts/generate-workflow-docs.py`.",
        ]
    )

    return "\n".join(lines)


def main() -> int:
    if not WORKFLOWS_DIR.exists():
        print(f"Workflows directory not found: {WORKFLOWS_DIR}")
        return 1
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    changed_files = []
    for workflow_file in sorted(WORKFLOWS_DIR.glob("*.yml")):
        workflow_data = load_yaml(workflow_file)
        content = generate_doc(workflow_file, workflow_data)
        target_path = DOCS_DIR / f"{workflow_file.stem}.md"
        if target_path.exists():
            existing = target_path.read_text(encoding="utf-8")
            if existing == content:
                continue
        target_path.write_text(content, encoding="utf-8")
        changed_files.append(str(target_path.relative_to(REPO_ROOT)))

    if changed_files:
        print("Generated or updated documentation for:")
        for file_name in changed_files:
            print(f"- {file_name}")
    else:
        print("No documentation changes were necessary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
