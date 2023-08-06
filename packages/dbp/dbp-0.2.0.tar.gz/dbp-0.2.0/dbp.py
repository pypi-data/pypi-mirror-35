"""Simple program to manage gbp-docker container lifecycle."""

__version__ = "0.2.0"

import argparse
import logging
import os
import shutil
import sys

from pathlib import Path
from subprocess import run, PIPE, DEVNULL
from typing import List

PWD = Path.cwd()
UID = os.getuid()
GID = os.getgid()
USER = os.getenv("USER")

CONTAINER_NAME = "{}-dbp-{}".format(USER, PWD.stem)
IMAGE = "opxhub/gbp"


L = logging.getLogger("dbp")
L.addHandler(logging.NullHandler())


def container_exists() -> bool:
    """Returns true if our dbp container can be inspected"""
    p = run(["docker", "inspect", CONTAINER_NAME], stdout=DEVNULL, stderr=DEVNULL)
    return p.returncode == 0


def container_running(dist: str) -> bool:
    """Returns true if our dbp container is running"""
    p = run(
        ["docker", "inspect", CONTAINER_NAME, "--format={{.State.Running}}"],
        stdout=PIPE,
        stderr=DEVNULL,
    )
    return p.returncode == 0 and "true" in str(p.stdout)


def buildpackage(dist: str, target: Path, sources: str, gbp_options: str) -> int:
    """Runs gbp buildpackage --git-export-dir=pool/{dist}-amd64/{target}

    Container must already be started.
    """
    if not target.exists():
        L.error("Build target `{}` does not exist".format(target))
        return 1

    cmd = [
        "docker",
        "exec",
        "-it",
        "--user=build",
        "-e=UID={}".format(UID),
        "-e=GID={}".format(GID),
        "-e=EXTRA_SOURCES={}".format(sources),
        CONTAINER_NAME,
        "build",
        target.stem,
        gbp_options,
    ]

    proc = run(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    return proc.returncode


def docker_run(dist: str, sources: str, dev=True) -> int:
    if container_exists():
        L.warning("Container already exists.")
        return 0

    cmd = [
        "docker",
        "run",
        "-d",
        "-it",
        "--name={}".format(CONTAINER_NAME),
        "--hostname={}".format(dist),
        "-v={}:/mnt".format(PWD),
        "-v={}/.gitconfig:/etc/skel/.gitconfig:ro".format(Path.home()),
        "-e=UID={}".format(UID),
        "-e=GID={}".format(GID),
        "-e=EXTRA_SOURCES={}".format(sources),
    ]

    if dev:
        cmd = cmd + ["{}:{}-dev".format(IMAGE, dist)]
    else:
        cmd = cmd + ["{}:{}".format(IMAGE, dist), "bash", "-l"]

    proc = run(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    return proc.returncode


def docker_shell(dist: str, sources: str, command=None) -> int:
    """Runs bash in a development container

    Uses (and starts if necessary) any matching pre-existing dbp container.
    """
    if container_exists():
        cmd = [
            "docker",
            "exec",
            "-it",
            "--user=build",
            "-e=UID={}".format(UID),
            "-e=GID={}".format(GID),
            "-e=EXTRA_SOURCES={}".format(sources),
            CONTAINER_NAME,
            "bash",
            "-l",
        ]
        if not container_running(dist):
            docker_start(dist)
    else:
        cmd = [
            "docker",
            "run",
            "--rm",
            "-it",
            "--name={}".format(CONTAINER_NAME),
            "--hostname={}".format(dist),
            "-v={}:/mnt".format(PWD),
            "-v={}/.gitconfig:/etc/skel/.gitconfig:ro".format(Path.home()),
            "-e=UID={}".format(UID),
            "-e=GID={}".format(GID),
            "-e=EXTRA_SOURCES={}".format(sources),
            "{}:{}-dev".format(IMAGE, dist),
            "bash",
            "-l",
        ]

    if command is not None:
        cmd = cmd + ["-c", command]
    proc = run(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    return proc.returncode


def docker_start(dist: str) -> int:
    """Runs docker start and returns the return code"""
    cmd = ["docker", "start", CONTAINER_NAME]
    proc = run(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    return proc.returncode


def pull_images(dist: str) -> int:
    """Runs docker pull for both build and development images and returns the return code"""
    cmd = ["docker", "pull", "{}:{}".format(IMAGE, dist)]
    proc = run(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    if proc.returncode != 0:
        return proc.returncode

    cmd = ["docker", "pull", "{}:{}-dev".format(IMAGE, dist)]
    proc = run(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    return proc.returncode


def remove_container() -> int:
    """Runs docker rm -f for the dbp container"""
    if container_exists():
        cmd = ["docker", "rm", "-f", CONTAINER_NAME]
        proc = run(cmd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
        return proc.returncode

    L.warning("Container does not exist.")
    return 1


def cmd_build(args: argparse.Namespace) -> int:
    rc = 0
    remove = True

    if container_exists():
        remove = False
    else:
        rc = docker_run(args.dist, args.extra_sources, dev=False)
        if rc != 0:
            L.error("Could not run container")
            return rc

    for t in args.targets:
        if not container_running(args.dist):
            rc = docker_start(args.dist)
            if rc != 0:
                L.error("Could not start stopped container")
                break

        rc = buildpackage(args.dist, t, args.extra_sources, args.gbp)
        if rc != 0:
            L.error("Could not build package {}".format(t.stem))
            break

    if remove:
        remove_container()

    return 0


def cmd_pull(args: argparse.Namespace) -> int:
    return pull_images(args.dist)


def cmd_rm(args: argparse.Namespace) -> int:
    remove_container()
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    return docker_run(args.dist, args.extra_sources, dev=True)


def cmd_shell(args: argparse.Namespace) -> int:
    return docker_shell(args.dist, args.extra_sources, args.command)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)

    # general arguments
    parser.add_argument("--version", "-V", action="store_true", help="print program version")
    parser.add_argument(
        "--verbose", "-v", help="-v for info, -vv for debug", action="count", default=0
    )
    parser.add_argument(
        "--dist", "-d", help="Debian distribution", default=os.getenv("DIST", "stretch")
    )
    parser.add_argument(
        "--extra-sources",
        "-e",
        help="Apt-style sources",
        default=os.getenv("EXTRA_SOURCES", ""),
    )

    sps = parser.add_subparsers(help="commands")

    # build subcommand
    build_parser = sps.add_parser("build", help="run gbp buildpackage")
    build_parser.add_argument(
        "targets", nargs="+", type=Path, help="directories to build"
    )
    build_parser.add_argument(
        "--gbp", "-g", default="", help="additional git-buildpackage options to pass"
    )
    build_parser.set_defaults(func=cmd_build)

    # pull subcommand
    pull_parser = sps.add_parser("pull", help="pull latest images")
    pull_parser.set_defaults(func=cmd_pull)

    # rm subcommand
    rm_parser = sps.add_parser("rm", help="remove workspace container")
    rm_parser.set_defaults(func=cmd_rm)

    # run subcommand
    run_parser = sps.add_parser("run", help="run development container in background")
    run_parser.set_defaults(func=cmd_run)

    # shell subcommand
    shell_parser = sps.add_parser("shell", help="launch development environment")
    shell_parser.add_argument("--command", "-c", help="command to run noninteractively")
    shell_parser.set_defaults(func=cmd_shell)

    args = parser.parse_args()

    if args.version:
        print("dbp {}".format(__version__))
        return 0

    # set up logging
    logging.basicConfig(
        format="[%(levelname)s] %(message)s", level=10 * (3 - min(args.verbose, 2))
    )

    # check for prereqs
    if shutil.which("docker") is None:
        L.error("Docker not found in PATH. Please install docker.")
        sys.exit(1)

    # read sources from ./extra_sources and ~/.extra_sources
    if args.extra_sources == "":
        extra_sources = [Path("extra_sources"), Path.home() / ".extra_sources"]
        for s in extra_sources:
            if s.exists():
                args.extra_sources = s.read_text()
                break

    if args.extra_sources != "":
        L.info("Loaded extra sources:\n{}".format(args.extra_sources))

    # print help if no subcommand specified
    if getattr(args, "func", None) is None:
        parser.print_help()
        return 0

    # run subcommand
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
