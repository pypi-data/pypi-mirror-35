""" Entry point for `tsrc init` """
import argparse
import os

from path import Path
import ui

import tsrc.workspace


def main(args: argparse.Namespace) -> None:
    workspace_path = args.workspace_path or os.getcwd()
    workspace = tsrc.workspace.Workspace(Path(workspace_path))
    ui.info_1("Configuring workspace in", ui.bold, workspace_path)
    manifest_options = tsrc.workspace.options_from_args(args)
    workspace.configure_manifest(manifest_options)
    workspace.load_manifest()
    workspace.clone_missing()
    workspace.set_remotes()
    workspace.copy_files()
    ui.info("Done", ui.check)
