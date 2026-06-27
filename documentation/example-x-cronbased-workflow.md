# example-x-cronbased-workflow.yml

## Purpose
This workflow shows how to schedule jobs using a cron expression.
It is useful for recurring tasks such as periodic checks, cleanup, or scheduled automation.

## Trigger
- `schedule` with cron: `*/2 * * * *`
  - Runs every 2 minutes.

## Jobs and steps
- `scheduled-job`
  - Runs on `ubuntu-latest`.
  - Executes a simple shell command to print a message.

## Key concepts
- `schedule` is a GitHub Actions event that triggers workflows on a time schedule.
- Cron syntax in GitHub Actions uses the standard UNIX cron format.
- Scheduled workflows are useful when you need automation independent of repository events.

## Considerations
- GitHub may enforce minimum schedule frequencies or quotas for scheduled workflows.
- Keep scheduled jobs efficient to avoid consuming unnecessary runner minutes.
- Use scheduled workflows for maintenance, periodic testing, or data refresh tasks.
