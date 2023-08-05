"""
unid 0.0.0rc9

a module designed to make unique identifiers
for variables and other constants

FUTURE FEATURES

    - communicative id manager (sockets)
    - more extensive overlays
    - allow multiple base-? overlays

TESTED ON

    - Python 3.11.1 (MacOS)
"""

__version__ = "0.0.0rc9"

# module imports
import os
import pathlib

# inner imports
import overlays


HOME_PATH = pathlib.Path.home()  # computer's home path
PACKAGE_ROOT = os.path.join(HOME_PATH, ".unid")  # package data storage location

# overlays
TYPE_OVERLAY = "typeoverlay"
TYPE_BASEOVERLAY = "typebaseoverlay"  # base? nums


"""OVERLAYS"""
class PipelineStructuringError(Exception):
    pass


class OverlayPipeline:
    """
    Allow multiple overlays to be overlayed
    on an ID manager.
    """

    def __init__(self, overlays=[]):
        """
        Initialize overlay pipeline

        overlays -- list of overlays to apply
        """
        self.overlays = overlays

    def _overlay(self, num):
        """Apply each of the overlays"""
        for overlay in self.overlays:
            num = overlay._overlay(num)
        return num


class Overlay:
    TYPE = TYPE_OVERLAY

    def __init__(self):
        pass

    def _overlay(num):
        pass


class BinaryOverlay(Overlay):
    TYPE = TYPE_BASEOVERLAY

    def _overlay(num):
        return bin(num)


class Base10Overlay(Overlay):
    TYPE = TYPE_BASEOVERLAY

    def _overlay(num):
        return int(num)


class OctalOverlay(Overlay):
    TYPE = TYPE_BASEOVERLAY

    def _overlay(num):
        return oct(num)


class HexadecimalOverlay(Overlay):
    TYPE = TYPE_BASEOVERLAY

    def _overlay(num):
        return hex(num)


# pointers
Base2Overlay = BinaryOverlay  # pointer to binary function
Base8Overlay = OctalOverlay  # pointer to octal function
Base16Overlay = HexadecimalOverlay  # pointer to hexadecimal function


"""ID MANAGERS"""


class IDManager():
    """
    A system for creating unique
    IDs.
    """

    def __init__(self, overlay=overlays.Base10Overlay):
        """
        Initialize an ID Manager

        system -- ID generation system
        """
        self._curid = -1  # integer curid
        self.curid = -1  # overlayed curid
        self.overlay = overlay  # should be callable

    def __iter__(self):
        return self

    def __next__(self):
        return self.new

    def _apply_overlay(self):
        self._curid = int(self._curid)
        self.curid = self.overlay._overlay(self._curid)

    @property
    def new(self):
        """Generate new ID"""
        self._curid += 1
        self._apply_overlay()
        return self.curid

    def reset(self):
        """Reset ID counter"""
        self._curid = -1


class PersistentIDManager(IDManager):
    """
    A system for creating unique IDs
    that will persist through program
    restarts and loads.
    """

    def __init__(self, name, system=None):
        """
        Generate a new persistent ID
        system.

        name -- name of ID system
        system -- type of IDs to generate
        """

        super().__init__()

        self.name = name

        # either make new idmanager or load previous
        self._generate_persistent_dir()

    def _generate_persistent_dir(self):
        """
        Create a persistent directory
        for persistent data.
        """

        # generate the persistent directory for persistent data
        if not os.path.exists(PACKAGE_ROOT):
            os.mkdir(PACKAGE_ROOT)

        # generate persistent file
        self.file_path = os.path.join(PACKAGE_ROOT, "%s.id" % (self.name))
        if not os.path.exists(self.file_path):
            # make an ID file, does not exist currently
            with open(self.file_path, "w") as f:
                f.write("-1")
        else:
            # file already exists, load file's information
            with open(self.file_path, "r") as f:
                self._curid = int(f.read())


    @property
    def new(self):
        """Generate new ID"""
        self._curid += 1
        with open(self.file_path, "w") as f:
            self._apply_overlay()
            f.write(str(self._curid))
        return self._curid

    def reset(self):
        """Reset ID counter"""
        self._curid = -1
        self._apply_overlay()
        with open(self.file_path, "w") as f:
            f.write(str(self._curid))

