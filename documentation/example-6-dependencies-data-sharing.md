# example-6-dependencies-data-sharing.yml

## Purpose
This workflow demonstrates how multiple jobs can share data using artifacts.
It shows a pipeline where one job creates a file, uploads it, and later jobs download and update the same artifact.

## Trigger
- `push` to any branch.

## Jobs and flow
- `job1`
  - Runs on `ubuntu-latest`.
  - Creates `shared-file.txt` containing data.
  - Uploads the file with `actions/upload-artifact@v3` using `name: shared-data`.
- `job2`
  - Depends on `job1` via `needs: job1`.
  - Downloads the artifact with `actions/download-artifact@v3`.
  - Reads the file and appends processing output.
  - Re-uploads the updated artifact under the same name.
- `job3`
  - Depends on `job2` via `needs: job2`.
  - Downloads the updated artifact.
  - Finalizes and prints the contents of the shared file.

## Key concepts
- `needs` creates explicit job dependencies and enforces execution order.
- Artifacts are the standard way to pass files between jobs in GitHub Actions.
- Each job runs on a fresh runner, so artifacts are required to move data between jobs.

## Use cases
- Multi-stage pipelines that build, test, and package artifacts.
- Data transformation workflows where output from one job is input to the next.
- Scenarios where temporary files must be persisted between jobs.
