from git import GitCommandError
from git.repo import Repo
from rich import print

from devjournal.constants import entries_directory

from .config import get_config


def is_repo_defined():
    return bool(get_config().remote_repo_url)


def get_origin(remote_repo_url: str):
    repo = Repo.init(entries_directory())
    if repo.remotes:
        repo.delete_remote(repo.remotes[0])
    return repo.create_remote("origin", remote_repo_url)


def _indent(text: str, spaces=2):
    return " " * spaces + text.replace("\n", "\n" + " " * spaces)


def pull_rebase():
    config = get_config()
    remote_branch = config.remote_branch
    remote_repo_url = config.remote_repo_url
    try:
        get_origin(remote_repo_url).pull(rebase=True, refspec=remote_branch)
    except GitCommandError as e:
        command = " ".join(e.command)
        message = e.stderr.replace("stderr:", "").strip()
        print(
            f"[red]Error:[/red] Git command '{command}' failed with error message {message}"
        )
        print("[blue]Config file:[/blue]")
        print(_indent(config.text))


def push():
    remote_branch = get_config().remote_branch
    repo = Repo(entries_directory())
    repo.git.add(".")
    # TODO: change commit message here to time stamp or something
    repo.git.commit(message="devjournal commit")
    local_branch_name = repo.head.reference.name
    repo.git.push("--set-upstream", "origin", f"{local_branch_name}:{remote_branch}")
