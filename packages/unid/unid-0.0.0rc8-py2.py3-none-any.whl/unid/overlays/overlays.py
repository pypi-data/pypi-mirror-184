"""
unid 0.0.0rc8

a module designed to make unique identifiers
for variables and other constants

FUTURE FEATURES

    - communicative id manager (sockets)
    - more extensive overlays

TESTED ON

    - Python 3.11.1 (MacOS)
"""

__version__ = "0.0.0rc8"


TYPE_OVERLAY = "typeoverlay"
TYPE_BASEOVERLAY = "typebaseoverlay"  # base? nums


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
