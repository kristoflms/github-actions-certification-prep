# Basic Git Commands

## `git status`
Show the current branch and working tree status.

Example:
```bash
git status
```

Use this to see:
- modified files
- files staged for commit
- current branch name
- untracked files

## `git add`
Stage changes for commit.

Examples:
```bash
git add file.txt
git add .
```

- `git add .` stages all tracked and modified files in the current directory.
- Use it when you are ready to include changes in the next commit.

## `git commit`
Record staged changes in a new commit.

Example:
```bash
git commit -m "Add new README section"
```

- `-m` sets the commit message.
- This creates a new commit from the staged snapshot.

## `git branch`
List branches or create a new branch.

Examples:
```bash
git branch
git branch feature/new-feature
```

- `git branch` lists local branches.
- `git branch <name>` creates a new branch from the current commit.

## `git checkout`
Switch branches.

Example:
```bash
git checkout development
```

- Use this to move your working tree to an existing branch.
- If you want to create and switch in one step, use `git checkout -b <branch>`.

## `git checkout -b`
Create a new branch and switch to it.

Example:
```bash
git checkout -b feature/login-form
```

- Useful when starting new work from the current branch.

## `git log`
Show recent commit history.

Example:
```bash
git log --oneline
```

- `--oneline` shows each commit in a single line.
- Use this to inspect recent commits and verify history.
