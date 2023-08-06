"""
    ____          ____                __               __
   / __ \\ __  __ / __ \\ _____ ____   / /_ ___   _____ / /_
  / /_/ // / / // /_/ // ___// __ \\ / __// _ \\ / ___// __/
 / ____// /_/ // ____// /   / /_/ // /_ /  __// /__ / /_
/_/     \\__, //_/    /_/    \\____/ \\__/ \\___/ \\___/ \\__/
       /____/

Made With ❤️ By Ghoul & Marci
"""

import os
import time

import psutil
import win32gui

from typing import Any
from win32process import GetWindowThreadProcessId

from ..constants import Lists
from ..utils.webhook import Webhook


class AntiProcess:
    def __init__(
            self,
            webhook: Webhook,
            logger: Any,
            exit: bool,
            report: bool) -> None:
        self.webhook: Webhook = webhook
        self.logger: Any = logger
        self.exit: bool = exit
        self.report: bool = report

    def CheckProcessList(self) -> None:
        while True:
            try:
                time.sleep(0.7)
                for process in psutil.process_iter():
                    if any(
                        process_name in process.name().lower()
                        for process_name in Lists.BLACKLISTED_PROGRAMS
                    ):
                        try:
                            self.logger.info(
                                f"{process.name} Process Was Running")
                            if self.report:
                                self.webhook.send(
                                    f"Anti-Debug Program: `{process.name()}` was detected running on the system.",
                                    "Anti Process",
                                )
                            process.kill()
                            if self.exit:
                                os._exit(1)
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            pass
            except BaseException:
                pass

    def CheckWindowNames(self) -> None:
        while True:
            try:
                time.sleep(0.7)
                window_name: str = win32gui.GetWindowText(
                    win32gui.GetForegroundWindow()
                )
                if window_name in Lists.BLACKLISTED_WINDOW_NAMES:
                    self.logger.info(f"{window_name} Found")
                    if self.report:
                        self.webhook.send(
                            f"Found `{window_name}` in Window Names", "Anti Process")
                    if self.exit:
                        os._exit(1)
            except (RuntimeError, NameError, TypeError, OSError) as error:
                self.webhook.send(f"Error!: ```yaml\n{error}\n```")
                pass

    def CheckWindows(self) -> None:
        def winEnumHandler(hwnd, ctx) -> None:
            if win32gui.GetWindowText(hwnd).lower(
            ) in Lists.BLACKLISTED_WINDOW_NAMES:
                pid: tuple[int, int] = GetWindowThreadProcessId(hwnd)
                if isinstance(pid, int):
                    try:
                        psutil.Process(pid).terminate()
                    except BaseException:
                        pass
                else:
                    for process in pid:
                        try:
                            psutil.Process(process).terminate()
                        except BaseException:
                            pass
                self.logger.info(f"{win32gui.GetWindowText(hwnd)} Found")
                if self.report:
                    self.webhook.send(
                        f"Debugger Open: {win32gui.GetWindowText(hwnd)}",
                        "Anti Process")
                if self.exit:
                    os._exit(1)

        while True:
            win32gui.EnumWindows(winEnumHandler, None)
