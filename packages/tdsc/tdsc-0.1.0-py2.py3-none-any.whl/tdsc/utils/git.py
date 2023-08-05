import subprocess
import functools


@functools.lru_cache(maxsize=1)
def git_available():
    """
    Indicates whether ``git`` is available on the system.

    Result is cached by functools.lru_cache
    """

    return (
        subprocess.call(
            ["git", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        == 0
    )


def run_git(*args, **kwargs):
    """Shallow wrapper to run ``git`` with given arguments, return exit code."""
    args = ["git"] + list(args)

    return subprocess.call(args, **kwargs)
