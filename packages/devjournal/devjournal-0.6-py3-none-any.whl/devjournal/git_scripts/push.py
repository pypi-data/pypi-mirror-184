from git.repo import Repo

from devjournal.constants import entries_directory

from ..config import get_config


def push():
    remote_branch = get_config().remote_branch
    repo = Repo(entries_directory())
    repo.git.add(".")
    # TODO: change commit message here to time stamp or something
    repo.git.commit(message="devjournal commit")
    local_branch_name = repo.head.reference.name
    repo.git.push("--set-upstream", "origin", f"{local_branch_name}:{remote_branch}")


if __name__ == "__main__":
    push()
