from __future__ import annotations

import logging
import os
import sys
from typing import TYPE_CHECKING, Optional

import wx
import wx.aui as aui
from wx.lib.dialogs import ScrolledMessageDialog

from .dialog.preferences import PreferencesDialog
from .document.manager import DocumentManager
from .panelManager import PanelManager
from .pluginManager import PluginManager
from .scripting import MacroMenu  # , makeMergedMacroTree

if TYPE_CHECKING:
    from .application import App

log = logging.getLogger(__name__)


class FileDropTarget(wx.FileDropTarget):
    @property
    def app(self) -> App:
        return wx.GetApp()

    def OnDropFiles(self, x, y, filenames):
        wx.CallAfter(self.app.TopWindow.documentManager.openDocuments, filenames)
        return True


class ApplicationWindow(wx.Frame):
    """Implementation of the main application window"""

    def __init__(self, iconName=None):
        self._panelManager: Optional[PanelManager] = None
        self._pluginManager: Optional[PluginManager] = None
        self._documentManager: Optional[DocumentManager] = None
        self._toolbarEdit: Optional[aui.AuiToolBar] = None
        self._showTooltip: bool = False
        app: App = wx.GetApp()
        title: str = ""
        self.about = about = app.about
        parent = None
        id = wx.ID_ANY
        if about:
            title = about.Name
        pos = wx.DefaultPosition
        size = wx.DefaultSize
        style = wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL
        name = "ApplicationWindow"
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)
        self.SetIcon(iconName)
        self._externalTools = []
        self._menubar = wx.MenuBar()
        self.CreateStatusBar(3, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.loadConfig()
        self.editMenu = wx.Menu()
        self.buildEditMenu()
        self.scriptsMenu = None
        self.buildScriptsMenu()
        self.extraMenu = wx.Menu()
        self.buildExtraMenu()
        self.helpMenu = wx.Menu()
        self.buildHelpMenu()
        self.documentManager.initTemplates()
        self.panelManager.initPanels()
        self._menubar.Append(self.documentManager.menu, "&File")
        self._menubar.Append(self.editMenu, "&Edit")
        self._menubar.Append(self.panelManager.menu, "&View")
        self._menubar.Append(self.scriptsMenu, "&Scripts")
        self._menubar.Append(self.extraMenu, "E&xtra")
        self._menubar.Append(self.helpMenu, "&Help")
        self.SetMenuBar(self._menubar)

        # =================================================================================
        self.SetDropTarget(FileDropTarget())
        # =================================================================================

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Bind(wx.EVT_MENU, self.on_edit_undo, id=wx.ID_UNDO)
        self.Bind(wx.EVT_MENU, self.on_edit_redo, id=wx.ID_REDO)
        self.Bind(wx.EVT_MENU, self.on_edit_copy, id=wx.ID_COPY)
        self.Bind(wx.EVT_MENU, self.on_edit_cut, id=wx.ID_CUT)
        self.Bind(wx.EVT_MENU, self.on_edit_paste, id=wx.ID_PASTE)
        self.Bind(wx.EVT_MENU, self.on_edit_select_all, id=wx.ID_SELECTALL)
        self.Bind(wx.EVT_MENU, self.on_find, id=wx.ID_FIND)
        self.Bind(
            wx.EVT_MENU, self.on_find_next, id=self.editMenu.FindItem("Find Next")
        )
        self.Bind(wx.EVT_MENU, self.on_replace, id=wx.ID_REPLACE)
        self.Bind(wx.EVT_MENU, self.on_edit_preferences, id=wx.ID_PREFERENCES)
        self.Bind(wx.EVT_MENU, self.on_help_about, id=wx.ID_ABOUT)
        self.Bind(
            wx.EVT_MENU,
            self.on_help_about_plugin,
            id=self.helpMenu.FindItem("About Plugins"),
        )
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_edit_undo, id=wx.ID_UNDO)
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_edit_redo, id=wx.ID_REDO)
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_edit_copy, id=wx.ID_COPY)
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_edit_cut, id=wx.ID_CUT)
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_edit_paste, id=wx.ID_PASTE)
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_edit_select_all, id=wx.ID_SELECTALL)
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_find, id=wx.ID_FIND)
        self.Bind(
            wx.EVT_UPDATE_UI,
            self.on_update_find_next,
            id=self.editMenu.FindItem("Find Next"),
        )
        self.Bind(wx.EVT_UPDATE_UI, self.on_update_replace, id=wx.ID_REPLACE)
        self.Bind(wx.EVT_SYS_COLOUR_CHANGED, self.on_sys_colour_chnaged)

    def __repr__(self):
        if self.about:
            return '<Application Window of "%s">' % self.about.Name
        return "<Application Window>"

    # -----------------------------------------------------------------------------
    # Properties
    # -----------------------------------------------------------------------------

    @property
    def app(self) -> App:
        return wx.GetApp()

    @property
    def config(self) -> wx.ConfigBase:
        return self.app.config

    @property
    def pluginManager(self) -> PluginManager:
        """The plugin manager of the running application"""
        if not self._pluginManager:
            self._pluginManager = PluginManager()
        return self._pluginManager

    @property
    def panelManager(self) -> PanelManager:
        """The panel manager of the running application"""
        if not self._panelManager:
            self._panelManager = PanelManager(self)
        return self._panelManager

    @property
    def documentManager(self) -> DocumentManager:
        """The document manager of the running application"""
        if not self._documentManager:
            self._documentManager = DocumentManager(self)
            self.PushEventHandler(self._documentManager)
        return self._documentManager

    @property
    def editToolbar(self) -> aui.AuiToolBar:
        if not self._toolbarEdit:
            menu = self.editMenu
            self._toolbarEdit = tb = aui.AuiToolBar(
                self.TopLevelParent,
                wx.ID_ANY,
                wx.DefaultPosition,
                wx.DefaultSize,
                wx.aui.AUI_TB_HORZ_LAYOUT
                | wx.aui.AUI_TB_PLAIN_BACKGROUND
                | wx.NO_BORDER,
            )
            tb.SetToolBitmapSize(wx.Size(16, 16))
            lastItem = menu.MenuItems[0]
            for item in menu.MenuItems:
                if item.IsSeparator() and not lastItem.IsSeparator():
                    pass
                elif item.IsSubMenu():
                    continue
                elif item.Bitmap.IsOk() and item.Id != wx.ID_EXIT:
                    if lastItem.IsSeparator():
                        tb.AddSeparator()
                    tb.AddTool(
                        item.Id,
                        item.ItemLabelText,
                        item.Bitmap,
                        item.Help,
                        wx.ITEM_NORMAL,
                    )
                lastItem = item
            tb.Realize()
        return self._toolbarEdit

    @property
    def showTooltip(self) -> bool:
        return self._showTooltip

    @showTooltip.setter
    def showTooltip(self, value):
        self._showTooltip = bool(value)
        wx.ToolTip.Enable(self._showTooltip)

    @property
    def externalTools(self):
        return self._externalTools

    # -----------------------------------------------------------------------------
    # public methods
    # -----------------------------------------------------------------------------

    def SetIcon(self, iconName=None) -> None:
        if iconName:
            super().SetIcon(wx.ArtProvider.GetIcon(iconName, wx.ART_FRAME_ICON))

    def buildEditMenu(self) -> None:
        mnu = self.editMenu
        # undo/redo
        item = wx.MenuItem(
            mnu, wx.ID_UNDO, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL
        )
        item.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_UNDO, wx.ART_MENU))
        mnu.Append(item)
        item = wx.MenuItem(
            mnu, wx.ID_REDO, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL
        )
        item.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_REDO, wx.ART_MENU))
        mnu.Append(item)
        mnu.AppendSeparator()
        # copy/cut/paste
        item = wx.MenuItem(
            mnu, wx.ID_COPY, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL
        )
        item.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_MENU))
        mnu.Append(item)
        item = wx.MenuItem(
            mnu, wx.ID_CUT, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL
        )
        item.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_CUT, wx.ART_MENU))
        mnu.Append(item)
        item = wx.MenuItem(
            mnu, wx.ID_PASTE, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL
        )
        item.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_MENU))
        mnu.Append(item)
        mnu.AppendSeparator()
        # select all
        item = wx.MenuItem(
            mnu, wx.ID_SELECTALL, "Select All\tCtrl+A", "Select all", wx.ITEM_NORMAL
        )
        item.SetBitmap(wx.ArtProvider.GetBitmap("SELECT_ALL", wx.ART_MENU))
        mnu.Append(item)
        mnu.AppendSeparator()

        # find/replace
        item = wx.MenuItem(
            mnu, wx.ID_FIND, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL
        )
        item.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FIND, wx.ART_MENU))
        mnu.Append(item)

        item = wx.MenuItem(mnu, wx.ID_ANY, "Find Next\tF3", "Find next", wx.ITEM_NORMAL)
        item.SetBitmap(wx.ArtProvider.GetBitmap("FIND_NEXT", wx.ART_MENU))
        mnu.Append(item)

        item = wx.MenuItem(
            mnu, wx.ID_REPLACE, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL
        )
        item.SetBitmap(wx.ArtProvider.GetBitmap("REPLACE", wx.ART_MENU))
        mnu.Append(item)

        mnu.AppendSeparator()

        self.menu_edit_preferences = wx.MenuItem(
            mnu, wx.ID_PREFERENCES, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL
        )
        mnu.Append(self.menu_edit_preferences)

    def buildScriptsMenu(self) -> None:
        macroFolders = []
        if self.about:
            macroFolders.append(
                os.path.join(
                    self.config.Read(
                        "/Application/SharedData/Dir", self.app.sharedDataDir
                    ),
                    "Macro",
                )
            )
            macroFolders.append(
                os.path.join(
                    self.config.Read(
                        "/Application/PrivateData/Dir", self.app.privateDataDir
                    ),
                    "Macro",
                ),
            )
        for macroFolder in macroFolders:
            if not os.path.isdir(macroFolder):
                os.makedirs(macroFolder)
            modulesPath = os.path.join(macroFolder, "_Modules")
            if os.path.isdir(modulesPath):
                if modulesPath not in sys.path:
                    sys.path.insert(0, modulesPath)
        self.scriptsMenu = MacroMenu(folderList=macroFolders)

    def buildExtraMenu(self) -> None:
        mnu = self.extraMenu
        if mnu.MenuItemCount == 0:
            mnu.AppendSeparator()
            item = wx.MenuItem(
                mnu, wx.ID_ANY, "Configure", "Configure external tools", wx.ITEM_NORMAL
            )
            mnu.Append(item)
            self.Bind(wx.EVT_MENU, self.on_externalToolConfigure, item, item.Id)
        if mnu.MenuItemCount > 2:
            for i in reversed(range(0, mnu.MenuItemCount - 2)):
                item = mnu.MenuItems[i]
                self.Unbind(wx.EVT_MENU, item, item.Id)
                mnu.DestroyItem(item)
        for i, tool in enumerate(self.externalTools):
            item = wx.MenuItem(
                mnu, wx.ID_ANY, tool["name"], tool["name"], wx.ITEM_NORMAL
            )
            mnu.Insert(i, item)
            self.Bind(wx.EVT_MENU, self.on_externalTool, item, item.Id)

    def buildHelpMenu(self) -> None:
        mnu = self.helpMenu
        self.menu_help_about = wx.MenuItem(
            mnu, wx.ID_ABOUT, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL
        )
        self.menu_help_about.SetBitmap(wx.ArtProvider.GetBitmap("ABOUT", wx.ART_MENU))
        mnu.Append(self.menu_help_about)
        about_plugins = wx.MenuItem(mnu, wx.ID_ANY, "About Plugins")
        mnu.Append(about_plugins)

    def loadConfig(self) -> None:
        config = self.config
        __ = wx.ConfigPathChanger(config, "/Window/")
        x = config.ReadInt("x", -1)
        y = config.ReadInt("y", -1)
        self.Position = (x, y)
        width = config.ReadInt("width", 800)
        height = config.ReadInt("height", 600)
        self.Size = (width, height)
        self.showTooltip = config.ReadBool("showTooltip", True)
        config.SetPath("/Application/")
        self._externalTools = eval(config.Read("ExternalTools", "[]"))

    def saveConfig(self) -> None:
        config = self.config
        __ = wx.ConfigPathChanger(config, "/Window/")
        x, y = self.Position
        config.WriteInt("x", x)
        config.WriteInt("y", y)
        width, height = self.Size
        config.WriteInt("width", width)
        config.WriteInt("height", height)
        config.WriteBool("showTooltip", self.showTooltip)
        self.panelManager.saveConfig()

    # -----------------------------------------------------------------------------
    # Event handler
    # -----------------------------------------------------------------------------

    def on_sys_colour_chnaged(self, event):
        """
        prevent colour changes if screenpresso is used to make a screenshot
        """
        dockArtColours = (
            "AUI_DOCKART_BACKGROUND_COLOUR",
            "AUI_DOCKART_BORDER_COLOUR",
            "AUI_DOCKART_SASH_COLOUR",
            "AUI_DOCKART_GRIPPER_COLOUR",
            "AUI_DOCKART_ACTIVE_CAPTION_COLOUR",
            "AUI_DOCKART_ACTIVE_CAPTION_GRADIENT_COLOUR",
            "AUI_DOCKART_ACTIVE_CAPTION_TEXT_COLOUR",
            "AUI_DOCKART_INACTIVE_CAPTION_COLOUR",
            "AUI_DOCKART_INACTIVE_CAPTION_GRADIENT_COLOUR",
            "AUI_DOCKART_INACTIVE_CAPTION_TEXT_COLOUR",
        )
        cfg = self.app.config
        cfgPath = cfg.GetPath()
        cfg.SetPath("/Window/Panels")
        setColour = self.panelManager.ArtProvider.SetColour
        for artColour in dockArtColours:
            setColour(getattr(aui, artColour), wx.Colour(cfg.ReadInt(artColour)))
        self.panelManager.Update()
        cfg.SetPath(cfgPath)

    def on_close(self, event):
        if self._documentManager.Clear(not event.CanVeto()):
            self.saveConfig()
            self._panelManager.UnInit()
            self.PopEventHandler(True)
            self.app.SetAssertMode(wx.APP_ASSERT_SUPPRESS)
            self.Destroy()
        else:
            event.Veto()

    # === Undo/Redo ===
    def on_edit_undo(self, event):
        self.FindFocus().Undo()

    def on_update_edit_undo(self, event: wx.UpdateUIEvent):
        widget = self.FindFocus()
        if widget:
            if widget.Name == "wxWebView":
                event.Enable(False)
                return
            if widget and hasattr(widget, "CanUndo"):
                try:
                    event.Enable(widget.CanUndo())
                except:
                    event.Enable(False)
                return
        event.Enable(False)

    def on_edit_redo(self, event):
        self.FindFocus().Redo()

    def on_update_edit_redo(self, event: wx.UpdateUIEvent):
        widget = self.FindFocus()
        if widget:
            if widget.Name == "wxWebView":
                event.Enable(False)
                return
            if hasattr(widget, "CanRedo"):
                try:
                    event.Enable(widget.CanRedo())
                except:
                    event.Enable(False)
                return
        event.Enable(False)

    # === Copy/Cut/Paste ===
    def on_edit_copy(self, event):
        self.FindFocus().Copy()

    def on_update_edit_copy(self, event: wx.UpdateUIEvent):
        widget = self.FindFocus()
        if widget:
            if widget.Name == "wxWebView":
                event.Enable(False)
                return
            if hasattr(widget, "CanCopy"):
                event.Enable(widget.CanCopy())
                return
        event.Enable(False)

    def on_edit_cut(self, event):
        self.FindFocus().Cut()

    def on_update_edit_cut(self, event):
        widget = self.FindFocus()
        if widget:
            if widget.Name == "wxWebView":
                event.Enable(False)
                return
            if hasattr(widget, "CanCut"):
                event.Enable(widget.CanCut())
                return
        event.Enable(False)

    def on_edit_paste(self, event):
        self.FindFocus().Paste()

    def on_update_edit_paste(self, event: wx.UpdateUIEvent):
        widget = self.FindFocus()
        if widget:
            if widget.Name == "wxWebView":
                event.Enable(False)
                return
            if hasattr(widget, "CanPaste"):
                event.Enable(widget.CanPaste())
                return
        event.Enable(False)

    def on_edit_select_all(self, event):
        widget = self.FindFocus()
        widget.SelectAll()
        event.Skip()

    def on_update_edit_select_all(self, event: wx.UpdateUIEvent):
        widget = self.FindFocus()
        if widget and hasattr(widget, "SelectAll"):
            event.Enable(True)
        else:
            event.Enable(False)

    # === Find/Replace ===
    def on_find(self, event):
        widget = self.FindFocus()
        widget.doFind()

    def on_update_find(self, event: wx.UpdateUIEvent):
        widget = self.FindFocus()
        if widget and hasattr(widget, "CanFind"):
            event.Enable(widget.CanFind())
        else:
            event.Enable(False)

    def on_find_next(self, event):
        widget = self.FindFocus()
        widget.doFindNext()

    def on_update_find_next(self, event: wx.UpdateUIEvent):
        widget = self.FindFocus()
        if widget and hasattr(widget, "CanFindNext"):
            event.Enable(widget.CanFindNext())
        else:
            event.Enable(False)

    def on_replace(self, event):
        widget = self.FindFocus()
        widget.doReplace()

    def on_update_replace(self, event: wx.UpdateUIEvent):
        widget = self.FindFocus()
        if widget and hasattr(widget, "CanReplace"):
            event.Enable(widget.CanReplace())
        else:
            event.Enable(False)

    def on_edit_preferences(self, event):
        prefDlg = PreferencesDialog(self)
        prefDlg.ShowModal()
        prefDlg.Destroy()

    def on_externalTool(self, event):
        menuItem = self.MenuBar.FindItemById(event.GetId())
        for tool in self.externalTools:
            if tool["name"] == menuItem.ItemLabelText:
                from .tools import startfile  # The wx.App object must be created first!

                oldDir = os.getcwd()
                if os.path.isdir(tool["folder"]):
                    os.chdir(tool["folder"])
                startfile(tool["cmd"])
                os.chdir(oldDir)
                return
        wx.LogError(f"Tool not found {menuItem.ItemLabelText}")

    def on_externalToolConfigure(self, event):
        prefDlg = PreferencesDialog(self)
        for i in range(prefDlg.book.PageCount):
            if prefDlg.book.GetPageText(i) == "External Tools":
                prefDlg.book.SetSelection(i)
                break
        prefDlg.ShowModal()
        prefDlg.Destroy()

    def on_help_about(self, event):
        wx.adv.AboutBox(self.app.about)

    def on_help_about_plugin(self, event):
        message = "Plugin version info\n============================\n"
        for pluginName in sorted(self.pluginManager, key=str.lower):
            plugin = self.pluginManager[pluginName]
            if hasattr(plugin, "__version__"):
                message += f"{pluginName:20}\t{plugin.__version__}\n"
        dlg = ScrolledMessageDialog(self, message, "About Plugins")
        dlg.ShowModal()
        dlg.Destroy()
