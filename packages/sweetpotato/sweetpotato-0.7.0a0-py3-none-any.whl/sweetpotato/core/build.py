"""
The `_access_check` and `_check_dependency` functions are essentially copies from
https://github.com/cookiecutter/whichcraft/blob/master/whichcraft.py#L20.

Todos:
    * Refactor + add platform command compatibility (windows, mac, etc).
    * Add docstrings for all classes & methods.
    * Add typing.
"""
import io
import json
import os
import pty
import subprocess
import sys
from typing import Literal, Optional

from sweetpotato.config import settings
from sweetpotato.core import js_utils
from sweetpotato.core.base_components import component_registry
from sweetpotato.core.interfaces import BaseRootComponent


class Build:
    """Contains actions for expo flow, dependency detection, app testing and publishing.

    Args:
        dependencies: User defined dependencies to replace inbuilt ones.
    """

    storage: dict[str, BaseRootComponent] = component_registry

    def __init__(self, dependencies: Optional[list[str]] = None) -> None:
        dependencies = (
            dependencies
            if dependencies
            else [
                "npm",
                "yarn",
                "expo",
            ]
        )
        for dependency in dependencies:
            if not self._check_dependency(dependency) and not self._install_dependency(
                dependency
            ):
                raise ImportError(f"Dependency package {dependency} not found.")

    @classmethod
    def write_files(cls) -> None:
        """Writes out .js files for application."""
        for _, content in cls.storage.items():
            cls._write_screen(content)
        cls._format_screens()

    @classmethod
    def run(cls, platform: Literal["ios", "android", "web", ""] = "") -> None:
        """Starts a React Native expo client through a subprocess.

        Args:
            platform: Platform for expo to run on.
        """

        cls.write_files()
        subprocess.run(
            f"cd {settings.REACT_NATIVE_PATH} && expo start --{platform}",
            shell=True,
            check=True,
        )

    @staticmethod
    def _write_screen(content: BaseRootComponent) -> None:
        """Writes screen contents to file with screen name as file name.

        Args:
            content: Component.
        """
        os.chdir(settings.REACT_NATIVE_PATH)
        with open(f"{content.package}", "w", encoding="utf-8") as file:
            file.write(js_utils.react_component(content))

    @staticmethod
    def publish(
        platform: Literal["ios", "android", "web"],
        staging: Literal["production", "preview"] = "preview",
    ) -> str:
        """Publishes app to specified platform / application store.

        Calls the `eas build` command with specified options.
        User will be prompted to log in if they are not already.

        Args:
            platform: Platform for app to be published on.
            staging: Staging environment for app, default preview.

        Todos:
            * Complete publishing logic for all platforms.
        """
        cmd = f"eas build -p {platform} --profile {staging}".split(" ")

        with open(f"{settings.REACT_NATIVE_PATH}/eas.json", "r+") as file:
            eas_conf = json.load(file)
            if platform == "ios":
                eas_conf["build"][staging][platform] = {"simulator": True}
            file.seek(0)
            json.dump(eas_conf, file)
            file.truncate()

        os.chdir(settings.REACT_NATIVE_PATH)

        with io.BytesIO() as script:

            def _read(file_d: int) -> bytes:
                """IO helper function."""
                data = os.read(file_d, 1024)
                script.write(data)
                return data

            pty.spawn(cmd, _read)
        result = script.getvalue().decode(encoding="utf-8")
        return result

    def show(self, verbose: bool = False) -> BaseRootComponent:
        """Returns .js rendition of application.

        Args:
            verbose: Whether to include extra details (imports, component count, etc).

        Returns:
            String rendition of application in .js format.

        Raises:
            NotImplementedError.

        Todo:
            Implement verbose argument.
        """
        if not verbose:
            return self.storage[settings.APP_COMPONENT]
        raise NotImplementedError

    @staticmethod
    def _format_screens() -> None:
        """Formats all .js files with the prettier.js package."""
        try:
            subprocess.run(
                f"cd {settings.REACT_NATIVE_PATH} && yarn prettier",
                shell=True,
                check=True,
                stdout=subprocess.DEVNULL,
            )

        except subprocess.CalledProcessError as error:
            sys.stdout.write(f"{error}\nTrying yarn install...\n")
            subprocess.run(
                f"cd {settings.REACT_NATIVE_PATH} && yarn install",
                shell=True,
                check=True,
                stdout=subprocess.DEVNULL,
            )

    @staticmethod
    def _install_dependency(dependency: str) -> None:
        """Prompts user to install js build dependencies if missing.

        Args:
            dependency: missing dependency.

        Todos:
            * Add rest of install logic.
        """
        sys.stdout.write(f"Build dependency {dependency} not found.\n")
        install = input("Would you like to install? (y/n): ") == "y"
        if install:
            raise NotImplementedError

    @staticmethod
    def _access_check(file: str, mode: int) -> bool:
        return (
            os.path.exists(file) and os.access(file, mode) and not os.path.isdir(file)
        )

    @classmethod
    def _check_dependency(
        cls,
        cmd: str,
        mode: int = os.F_OK | os.X_OK,
        path: Optional[str] = None,
    ) -> Optional[str]:
        if os.path.dirname(cmd):
            if cls._access_check(cmd, mode):
                return cmd
            return None
        if path is None:
            path = os.environ.get("PATH", os.defpath)
        if not path:
            return None
        path = path.split(os.pathsep)
        if sys.platform == "win32":
            if os.curdir not in path:
                path.insert(0, os.curdir)
            pathext = os.environ.get("PATHEXT", "").split(os.pathsep)
            if any(cmd.lower().endswith(ext.lower()) for ext in pathext):
                files = [cmd]
            else:
                files = [cmd + ext for ext in pathext]
        else:
            files = [cmd]
        seen = set()
        for directory in path:
            norm_dir = os.path.normcase(directory)
            if norm_dir not in seen:
                seen.add(norm_dir)
                for file in files:
                    name = os.path.join(directory, file)
                    if cls._access_check(name, mode):
                        return name
        return None
