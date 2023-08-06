"""WorkBench Application"""
from __future__ import annotations
from typing import Optional, TYPE_CHECKING, ClassVar

import logging
import mmap
import os
import pickle
import sys
import tempfile
import time
from argparse import ArgumentParser, Namespace

import wx
from appdirs import AppDirs

from .applicationWindow import ApplicationWindow
from .artprovider import Artprovider
from .document import DOC_SILENT

try:
    from git import GitCommandError, InvalidGitRepositoryError, Repo

    has_git = True
except ImportError:
    has_git = False

if TYPE_CHECKING:
    from wx.adv import AboutDialogInfo
    from .document.manager import DocumentManager
    from .applicationWindow import ApplicationWindow
    from .panelManager import PanelManager
    from .pluginManager import PluginManager

log = logging.getLogger(__name__)


class ExtChangeTestTimer(wx.Timer):
    """Timer for test of external changes"""

    def __init__(self, app):
        super().__init__()
        self.app: App = app

    def Notify(self):
        self.app.documentManager.testForExternalChanges(testAll=True)


class ListenAndLoadTimer(wx.Timer):
    def __init__(self, app):
        super().__init__()
        self.app: App = app

    def Notify(self):
        self.Stop()
        sharedMemory = self.app._sharedMemory
        sharedMemory.seek(0)
        if sharedMemory.read_byte() == ord("+"):  # available data
            data = sharedMemory.read(1024 - 1)
            sharedMemory.seek(0)
            sharedMemory.write_byte(
                ord("*")
            )  # finished reading, set buffer free marker
            sharedMemory.flush()
            args = pickle.loads(data)
            topWin = self.app.TopWindow
            for arg in args:
                if os.path.exists(arg):
                    topWin.documentManager.CreateDocument(arg, DOC_SILENT)
            if topWin.IsIconized():
                topWin.Iconize(False)
            else:
                topWin.Raise()
        self.Start(1000)


class App(wx.App):
    """Implements the main application object"""

    # modes for external changes test
    EXT_CHANGE_TEST_ON_REQUEST: ClassVar[int] = 0
    EXT_CHANGE_TEST_ON_ACTIVATE: ClassVar[int] = 1
    EXT_CHANGE_TEST_ON_TIMER: ClassVar[int] = 2
    TopWindow: ApplicationWindow

    _post_init_queue = []

    def __init__(
        self,
        about: Optional[AboutDialogInfo] = None,
        pluginDir: Optional[str] = None,
        redirect: bool = False,
        debug: int = 1,
        iconName: Optional[str] = None,
    ):
        """Constructor

        Args:
            about (wx.adv.AboutDialogInfo): Application info with name, vendor, version etc.
        """
        self._debug: bool = debug
        self.about: Optional[AboutDialogInfo] = about
        self.iconName: Optional[str] = iconName
        self._argumentParser: Optional[ArgumentParser] = None
        self.arguments: Optional[Namespace] = None
        self._extChangeMode: int = self.EXT_CHANGE_TEST_ON_REQUEST
        self.extChangeTimerInterval: int = 60
        self.folder: str = os.path.dirname(sys.argv[0])
        self.sharedDataDir: str = ""
        self.privateDataDir:str = ""
        self.enterMainLoop: bool = False
        if about:
            self.dirs = AppDirs(about.Name, about.Vendor)
            self.sharedDataDir = os.path.join(self.dirs.site_data_dir, "shared")
            self.privateDataDir = self.dirs.user_data_dir
        if self.folder not in sys.path:
            sys.path.insert(0, self.folder)
        if pluginDir and os.path.isdir(pluginDir):
            self.pluginDir = pluginDir
        else:
            self.pluginDir = os.path.join(self.folder, "plugin")
        wx.App.__init__(self, redirect, useBestVisual=True)

    def OnPreInit(self):
        if self.about:
            self.arguments = self.argumentParser.parse_args(sys.argv[1:] + [""])
        wx.App.OnPreInit(self)
        if self.about:
            self.AppName: str = self.about.Name
            self.VendorName: str = self.about.Vendor
            self.instanceChecker = wx.SingleInstanceChecker(
                "%s-%s" % (self.AppName, wx.GetUserId())
            )

    def OnInit(self):
        if hasattr(sys, "frozen") and sys.frozen:
            self.SetAssertMode(wx.APP_ASSERT_SUPPRESS)
        wx.ArtProvider.Push(Artprovider())
        self.config: wx.ConfigBase = self.Traits.CreateConfig()
        self.globalObjects = []
        self.SetTopWindow(ApplicationWindow(self.iconName))
        if self.about:
            self.enterMainLoop: bool = True
            # self.config: wx.ConfigBase = self.Traits.CreateConfig()
            self.prepareSingleInstanceConfig()
            if self.enterMainLoop:
                self.globalObjects = [
                    "__builtins__",
                    "__doc__",
                    "__file__",
                    "__name__",
                    "app",
                    "wx",
                    # "shell",
                ]
                self.prepareSharedDataFolder()
                self.preparePrivateDataFolder()
                # self.SetTopWindow(ApplicationWindow(self.iconName))
                self.TopWindow.Show(True)
                self.RunPostInitQueue()
                # set up external changes test
                self.extChangeTimer = ExtChangeTestTimer(self)
                self.extChangeTimerInterval = self.config.ReadInt(
                    "/Application/ExtChanges/Timer", self.extChangeTimerInterval
                )
                self.extChangeMode = self.config.ReadInt(
                    "/Application/ExtChanges/Mode", self.EXT_CHANGE_TEST_ON_REQUEST
                )
        return True

    def InitLocale(self):
        """
        Try to ensure that the C and Python locale is in sync with wxWidgets locale.
        This is a Windows only problem.
        """
        self.ResetLocale()
        import locale

        try:
            loc, enc = locale.getlocale()
        except ValueError:
            loc = enc = None
        # Try to set it to the same language as what is already set in the C locale
        info = wx.Locale.FindLanguageInfo(loc) if loc else None
        if info:
            self._initial_locale = wx.Locale(info.Language)
        else:
            # otherwise fall back to the system default
            self._initial_locale = wx.Locale(wx.LANGUAGE_DEFAULT)
        try:
            locale.setlocale(locale.LC_ALL, self._initial_locale.Locale)
        except locale.Error:
            # this does not work on Mac, ignore it.
            pass

    def MainLoop(self):
        """
        Execute the main GUI event loop.
        """
        if self.enterMainLoop:
            # execute startup script
            if (
                self.config.ReadBool("/Application/Start/Script/execute", False)
                and self.arguments.start_script_exec
            ):
                self.executeScript(
                    self.config.Read("/Application/Start/Script/path", "")
                )
            # open documents passed as command line arg
            for docPath in self.arguments.document:
                if os.path.exists(docPath):
                    self.TopWindow.documentManager.CreateDocument(docPath, DOC_SILENT)
            # execute script passed as command line arg
            if self.arguments.scriptPath:
                self.executeScript(self.arguments.scriptPath)
            self.enterMainLoop = False
            super().MainLoop()

    def __repr__(self) -> str:
        return '<Application: "%s" by %s>' % (self.AppName, self.VendorName)

    def on_ACTIVATE_APP(self, event) -> None:
        if event.Active:
            self.TopWindow.documentManager.testForExternalChanges(testAll=True)

    @property
    def extChangeMode(self) -> int:
        """
        Mode how external changes in documents should be checked.
        """
        return self._extChangeMode

    @extChangeMode.setter
    def extChangeMode(self, value: int):
        assert value in (
            self.EXT_CHANGE_TEST_ON_REQUEST,
            self.EXT_CHANGE_TEST_ON_ACTIVATE,
            self.EXT_CHANGE_TEST_ON_TIMER,
        )
        if value != self._extChangeMode:
            if self._extChangeMode == self.EXT_CHANGE_TEST_ON_ACTIVATE:
                self.Unbind(wx.EVT_ACTIVATE_APP, handler=self.on_ACTIVATE_APP)
            elif self._extChangeMode == self.EXT_CHANGE_TEST_ON_TIMER:
                self.extChangeTimer.Stop()
            if value == self.EXT_CHANGE_TEST_ON_ACTIVATE:
                self.Bind(wx.EVT_ACTIVATE_APP, self.on_ACTIVATE_APP)
            elif value == self.EXT_CHANGE_TEST_ON_TIMER:
                self.extChangeTimer.Start(self.extChangeTimerInterval * 1000)
            self._extChangeMode = value

    @property
    def argumentParser(self) -> ArgumentParser:
        if not self._argumentParser:
            self._argumentParser = ArgumentParser(
                self.AppName, description=self.about.Description
            )
            self._argumentParser.add_argument(
                "document",
                type=str,
                nargs="+",
                help="Documents to open",
            )
            self._argumentParser.add_argument(
                "-x",
                "--eXecute",
                type=str,
                # required=False,
                dest="scriptPath",
                help="Execute a script after documents are loaded, if any",
            )
            self._argumentParser.add_argument(
                "-s",
                "--noStartupscript",
                action="store_false",
                default=True,
                # required=False,
                dest="start_script_exec",
                help="Don't exceute the startup script, even if enabled in the apps preferences",
            )
        return self._argumentParser

    @property
    def pluginManager(self) -> PluginManager:
        """The plugin manager of the running application"""
        return self.TopWindow.pluginManager

    @property
    def panelManager(self) -> PanelManager:
        """The panel manager of the running application"""
        return self.TopWindow.panelManager

    @property
    def documentManager(self) -> DocumentManager:
        """The document manager of the running application"""
        return self.TopWindow.documentManager

    def prepareSingleInstanceConfig(self) -> None:
        self.allowMultipleInstances = self.config.ReadBool(
            "/Application/Start/MultipleInstances", False
        )
        if not self.allowMultipleInstances:
            # create shared memory temporary file
            if wx.Platform == "__WXMSW__":
                tfile = tempfile.TemporaryFile(prefix="ag", suffix="tmp")
                fno = tfile.fileno()
                self._sharedMemory = mmap.mmap(fno, 1024, "shared_memory")
            else:
                tfile = open(
                    os.path.join(
                        tempfile.gettempdir(),
                        tempfile.gettempprefix()
                        + self.GetAppName()
                        + "-"
                        + wx.GetUserId()
                        + "AGSharedMemory",
                    ),
                    "w+b",
                )
                tfile.write(b"*")
                tfile.seek(1024)
                tfile.write(b" ")
                tfile.flush()
                fno = tfile.fileno()
                self._sharedMemory = mmap.mmap(fno, 1024)
            if (
                hasattr(self, "instanceChecker")
                and self.instanceChecker.IsAnotherRunning()
            ):
                data = pickle.dumps(sys.argv[1:])
                sharedMemory = self._sharedMemory
                while True:
                    sharedMemory.seek(0)
                    marker = sharedMemory.read_byte()
                    if marker == 0 or chr(marker) == "*":  # available buffer
                        sharedMemory.seek(0)
                        sharedMemory.write_byte(ord("-"))  # set writing marker
                        sharedMemory.write(
                            data
                        )  # write files we tried to open to shared memory
                        sharedMemory.seek(0)
                        sharedMemory.write_byte(ord("+"))  # set finished writing marker
                        sharedMemory.flush()
                        break
                    else:
                        time.sleep(1)  # give enough time for buffer to be available
                self.enterMainLoop = False
            else:
                self.listenAndLoadTimer = ListenAndLoadTimer(self)
                self.listenAndLoadTimer.Start(250)

    def prepareSharedDataFolder(self) -> None:
        cfg = self.config
        cfgPath = cfg.GetPath()
        cfg.SetPath("/Application/SharedData/")
        folder = cfg.Read("Dir", self.sharedDataDir)
        url = cfg.Read("URL", "")
        pull_on_start = cfg.ReadBool("PullOnStart", False)
        if folder:
            if not os.path.isdir(folder):
                try:
                    os.makedirs(folder)
                except PermissionError:
                    folder = ""
            self.sharedDataDir = folder
            if has_git and url and folder:
                try:
                    repo = Repo(folder)
                except InvalidGitRepositoryError:
                    repo = Repo.init(folder)
                if not repo.remotes:
                    remote = repo.create_remote("origin", url)
                else:
                    try:
                        remote = repo.remote(name="origin")
                    except ValueError:
                        remote = repo.create_remote("origin", url)
                urls = [u for u in remote.urls]
                old_url = None
                if url not in urls:
                    if len(urls) == 1:
                        old_url = urls[0]
                    remote.set_url(url, old_url)
                if pull_on_start:
                    self.pullSharedData()
        cfg.SetPath(cfgPath)

    def pullSharedData(self) -> None:
        if has_git:
            if self.sharedDataDir:
                try:
                    repo = Repo(self.sharedDataDir)
                except InvalidGitRepositoryError:
                    wx.LogError(f"{self.sharedDataDir} is not a valid GIT repo")
                    return
                try:
                    remote = repo.remote(name="origin")
                except ValueError:
                    wx.LogError(f"{self.sharedDataDir} has no valid remote 'origin'")
                    return
                try:
                    remote.pull("master")
                    wx.LogStatus(f"{remote} pulled")
                except GitCommandError as e:
                    wx.LogError(f"{e}")
        else:
            wx.LogWarning(" GIT not available\n\nShared Data will not be pulled!")

    def preparePrivateDataFolder(self) -> None:
        cfg = self.config
        cfgPath = cfg.GetPath()
        cfg.SetPath("/Application/PrivateData/")
        folder = cfg.Read("Dir", self.privateDataDir)
        if not os.path.isdir(folder):
            os.makedirs(folder)
        self.privateDataDir = folder
        cfg.SetPath(cfgPath)

    def MacOpenFiles(self, fileNames) -> None:
        docManager = self.documentManager
        if docManager:
            for filename in fileNames:
                docManager.CreateDocument(filename, DOC_SILENT)

    # def MacNewFile(self):
    #     docManager = self.documentManager
    #     if docManager:
    #         docManager.CreateDocument(None, DOC_NEW)

    def AddPostInitAction(self, action) -> None:
        """
        Add actions to the post init queue.

        This is intended for plug-in initialization which require an existing
        application window.

        Args:
            action (funtion): Function which takes the app instance as paramerter
                when callend by `App.RunPostInitQueue`
        """
        self._post_init_queue.append(action)

    def RunPostInitQueue(self) -> None:
        """
        Execute the queued post init actions
        """
        while self._post_init_queue:
            action = self._post_init_queue.pop(0)
            # print(action)
            try:
                action(self)
            except:
                print(
                    "Can't execute post init action '%s' from module '%s'"
                    % (action.func_name, action.__module__)
                )
                print(sys.exc_info())

    def executeScript(self, scriptPath: str) -> None:
        """
        Execute a Python script located at scriptPath in the name space
        of the running app.
        """
        if os.path.isfile(scriptPath):
            del_name = False
            import __main__

            global_vars = __main__.__dict__
            if "__name__" not in global_vars:
                global_vars["__name__"] = "__main__"
                del_name = True
            with open(scriptPath) as scriptFile:
                code = compile(scriptFile.read(), scriptPath, "exec")
                exec(code, __main__.__dict__)
            if del_name and "__name__" in global_vars:
                del global_vars["__name__"]
