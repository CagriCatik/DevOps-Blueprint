# Git & Azure Repos Cheatsheet

A complete, beginner-friendly quick reference for working with **Azure Repos** (and Git in general). It starts from the core terms — **Branch, Clone, Commit, Fork, Pull, Pull Request, Push** — and gives you the **actual commands** for each, plus the Azure DevOps CLI (`az repos`) equivalents.

!!! note

    **Two ways to do almost everything:** the **Azure DevOps website** (point and click) and the **command line** (`git` + `az`). This page focuses on the commands, because they are the same whether you are on Windows, macOS, or Linux.

## The core terms at a glance

| Term | One-line meaning | Main command |
|---|---|---|
| **Branch** | An isolated line of work split off from `main`. | `git branch` / `git switch -c` |
| **Clone** | Make a full local copy of a remote repo. | `git clone <url>` |
| **Commit** | A saved group of changes in your local repo. | `git commit -m "..."` |
| **Fork** | A full personal copy of someone else's repo. | (UI) or `az repos` |
| **Pull** | Bring teammates' remote changes into your local repo. | `git pull` |
| **Pull Request (PR)** | Ask to merge your branch; team reviews first. | `az repos pr create` |
| **Push** | Upload your local commits to the remote repo. | `git push` |

---

## 1. First-time setup

Tell Git who you are (shows up in your commit history) and turn on helpers:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main      # new repos start on 'main'
git config --global pull.rebase false            # default merge behavior on pull
```

Install the **Azure DevOps CLI** extension (one-time), used for PRs and repo management:

```bash
az extension add --name azure-devops
az login                                         # sign in to Azure
az devops configure --defaults organization=https://dev.azure.com/<your-org> project=<your-project>
```

---

## 2. Clone — copy a repo to your machine

> **Clone:** creates a complete local copy of an existing Git repo, including all commits and branches, and remembers where it came from (the "remote").

```bash
# Get the URL from Azure Repos → Clone button
git clone https://dev.azure.com/<org>/<project>/_git/<repo>
cd <repo>
```

Authentication options (see [Creating an Azure Repo](5-Creating-Azure-Repo.md) for details):

```bash
# Using a Personal Access Token (PAT) embedded in the URL
git clone https://<PAT>@dev.azure.com/<org>/<project>/_git/<repo>

# Using SSH (after uploading your public key to Azure DevOps)
git clone git@ssh.dev.azure.com:v3/<org>/<project>/<repo>
```

!!! tip

    The recommended approach is **Git Credential Manager** — just run `git clone` with the HTTPS URL and a browser window will pop up to sign you in.

### Start a brand-new repo instead

```bash
git init                  # turn the current folder into a Git repo
git remote add origin https://dev.azure.com/<org>/<project>/_git/<repo>
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

## 3. The daily workflow (status → add → commit → push)

> **Commit:** a group of changes saved to your **local** repo.
> **Push:** uploads your saved commits to the **remote** repo.

```bash
git status                       # what changed? what's staged?
git add app/main.py              # stage one file
git add .                        # stage everything changed
git commit -m "Add health endpoint"
git push                         # upload commits to the current branch on the remote
```

First push of a **new** branch needs to set its remote tracking:

```bash
git push -u origin my-feature    # -u links local branch → remote branch
```

| Command | What it does |
|---|---|
| `git status` | Show changed, staged, and untracked files |
| `git add <file>` | Stage a specific file for the next commit |
| `git add -A` | Stage all changes (new, modified, deleted) |
| `git commit -m "msg"` | Save staged changes as a commit |
| `git commit -am "msg"` | Stage *tracked* files and commit in one step |
| `git push` | Upload commits to the remote |
| `git restore <file>` | Discard uncommitted changes in a file |
| `git restore --staged <file>` | Unstage a file (keep the changes) |

!!! tip

    **Write good commit messages.** Use the imperative mood: "Add login route", "Fix coverage gate" — as if completing the sentence "This commit will…".

---

## 4. Pull — get teammates' changes

> **Pull:** updates your local repo with changes others pushed to the remote.

```bash
git pull                         # fetch + merge remote changes into your branch
git fetch                        # download remote changes WITHOUT merging (safer to inspect first)
git fetch --all --prune          # update all remotes and delete stale remote branches
```

`git pull` is really two steps: `git fetch` (download) + `git merge` (combine).

---

## 5. Branch — isolate your work

> **Branch:** keeps its own history of commits so you can work on a feature or bug fix without affecting `main` or other people's work.

```bash
git branch                       # list local branches (* marks current)
git branch -a                    # list local + remote branches
git switch -c feature/cart       # create AND switch to a new branch
git switch main                  # switch to an existing branch
git branch -d feature/cart       # delete a merged branch (safe)
git branch -D feature/cart       # force-delete an unmerged branch
git push origin --delete feature/cart   # delete the branch on the remote
```

!!! note

    `git switch` (and `git restore`) are the modern, clearer replacements for the older `git checkout`, which did both jobs. `git checkout -b feature/cart` still works if you prefer it.

### Keeping a branch up to date with `main`

```bash
git switch feature/cart
git merge main                   # bring main's latest changes into your branch
# OR, for a cleaner linear history:
git rebase main                  # replay your commits on top of the latest main
```

---

## 6. Merging & resolving conflicts

```bash
git switch main
git merge feature/cart           # merge a branch into the current branch
```

When Git can't auto-merge, you get a **conflict**:

```bash
git status                       # lists files "both modified"
# Open each file, look for the markers, and edit to the desired result:
#   <<<<<<< HEAD
#   your version
#   =======
#   their version
#   >>>>>>> feature/cart
git add <resolved-file>          # mark each conflict resolved
git commit                       # finish the merge
# (or abort and start over:)
git merge --abort
```

---

## 7. Pull Request — propose & review changes

> **Pull Request (PR):** lets your team review your branch, leave comments, and approve or reject it **before** it merges into `main`. This is the heart of collaboration in Azure Repos.

Typical flow:

```bash
git switch -c feature/cart
# ...make changes, commit...
git push -u origin feature/cart
```

Then create the PR — either in the **Azure DevOps website** (Repos → Pull requests → New) or from the CLI:

```bash
# Create a PR from your branch into main
az repos pr create \
  --repository <repo> \
  --source-branch feature/cart \
  --target-branch main \
  --title "Add shopping cart" \
  --description "Implements the cart route and tests"

# Manage PRs from the terminal
az repos pr list --status active
az repos pr show --id <pr-id>
az repos pr set-vote --id <pr-id> --vote approve
az repos pr update --id <pr-id> --status completed   # complete (merge) the PR
```

| Vote value | Meaning |
|---|---|
| `approve` | Looks good, merge it |
| `approve-with-suggestions` | OK, but consider my comments |
| `wait-for-author` | Author needs to make changes |
| `reject` | Do not merge |

!!! tip

    Branch policies can **require** PRs (and passing CI builds + reviewers) before anything merges to `main`. See [Azure Repos Permissions & Policies](../5-Security-in-Azure-DevOps/4-Azure-Repos-Permissions-and-Policies.md).

---

## 8. Fork — your own copy of a repo

> **Fork:** a complete copy of a repo (all files, commits, branches). It behaves as if someone cloned the original and pushed it into a new, empty repo. Changes are **not** shared back unless a pull request carries them.

Forking is usually done in the **Azure DevOps website** (Repos → ⋯ → Fork). After forking, you clone *your fork* and add the original as an "upstream" remote so you can pull in updates:

```bash
git clone <your-fork-url>
cd <repo>
git remote add upstream <original-repo-url>
git fetch upstream
git merge upstream/main          # sync your fork with the original
```

When ready, push to your fork and open a PR **from the fork into the original** repo.

!!! note

    **Fork vs Branch:** use a **branch** for your own day-to-day work inside a repo you can write to. Use a **fork** when you want an independent copy (e.g., contributing to a repo you don't own).

---

## 9. Undoing things (the safety net)

| Goal | Command | Notes |
|---|---|---|
| Discard changes in a file | `git restore <file>` | Loses uncommitted edits |
| Unstage a file | `git restore --staged <file>` | Keeps the edits |
| Fix the last commit message | `git commit --amend -m "new msg"` | Only before pushing |
| Add a forgotten file to last commit | `git add f && git commit --amend --no-edit` | Only before pushing |
| Undo last commit, keep changes | `git reset --soft HEAD~1` | Changes stay staged |
| Undo last commit, unstage changes | `git reset HEAD~1` | Changes stay in files |
| Throw away last commit entirely | `git reset --hard HEAD~1` | ⚠️ Destroys changes |
| Safely undo a pushed commit | `git revert <commit>` | Creates a new "undo" commit |

!!! warning

    Avoid `git reset --hard` and **force-push** (`git push --force`) on shared branches like `main` — they rewrite history and can destroy teammates' work. Use `git revert` for anything already pushed. Prefer `git push --force-with-lease` if you ever must force-push your own feature branch.

### Stash — park changes without committing

```bash
git stash                        # shelve your uncommitted changes
git stash list                   # see stashed entries
git stash pop                    # re-apply the latest stash and remove it
git stash drop                   # delete a stash
```

---

## 10. Inspecting history

```bash
git log --oneline --graph --all  # compact visual history of all branches
git log -p <file>                # history with the actual diffs for a file
git show <commit>                # everything that changed in one commit
git diff                         # unstaged changes vs last commit
git diff --staged                # staged changes vs last commit
git diff main..feature/cart      # differences between two branches
git blame <file>                 # who last changed each line
```

---

## 11. Tags (mark releases)

```bash
git tag                          # list tags
git tag -a v1.0.0 -m "First release"   # create an annotated tag
git push origin v1.0.0           # push one tag
git push origin --tags           # push all tags
git tag -d v1.0.0                # delete a local tag
```

!!! tip

    Tags are how you mark a specific commit as "the version we released". In Azure Repos you can restrict who may create tags — see the security module.

---

## 12. Remotes

```bash
git remote -v                    # show remote URLs
git remote add origin <url>      # add a remote named 'origin'
git remote set-url origin <url>  # change a remote's URL
git remote rename origin azure   # rename a remote
```

---

## 13. Azure DevOps CLI (`az repos`) quick reference

Manage Azure Repos without leaving the terminal:

```bash
# Repositories
az repos list --output table
az repos create --name my-new-repo
az repos show --repository my-repo

# Branches & policies
az repos ref list --repository my-repo --filter heads          # list branches
az repos policy list --branch main --repository my-repo

# Pull requests (see section 7 for more)
az repos pr create --title "..." --source-branch feature/x --target-branch main
az repos pr list --status active --output table

# Import an existing Git repo into Azure Repos
az repos import create --git-source-url https://github.com/user/repo.git --repository my-repo
```

---

## 14. A typical feature, start to finish

```bash
# 1. Start from an up-to-date main
git switch main
git pull

# 2. Branch off for your feature
git switch -c feature/health-endpoint

# 3. Work, then save your progress
git add .
git commit -m "Add /health endpoint and test"

# 4. Share your branch
git push -u origin feature/health-endpoint

# 5. Open a PR for review
az repos pr create --title "Add health endpoint" \
  --source-branch feature/health-endpoint --target-branch main

# 6. After approval + green CI, the PR merges into main.
#    Then clean up locally:
git switch main
git pull
git branch -d feature/health-endpoint
```

---

## Beginner gotchas

!!! danger "Caution"

    - **"Commit" is local; "push" is remote.** A commit alone does not share anything — you must `push`.
    - **Always `git pull` before you start** so you build on the latest code and avoid conflicts.
    - **Never commit secrets** (passwords, PATs, keys) or junk (`.venv/`, `__pycache__/`). Add a Python [`.gitignore`](https://github.com/github/gitignore/blob/main/Python.gitignore) early.
    - **`reset --hard` and `push --force` are destructive** on shared branches — reach for `git revert` instead.

!!! tip

    **References:**

    - [Azure Repos Git documentation (Microsoft)](https://learn.microsoft.com/en-us/azure/devops/repos/git/)
    - [Git command reference](https://git-scm.com/docs)
    - [az repos CLI reference (Microsoft)](https://learn.microsoft.com/en-us/cli/azure/repos)
