"""
Parse a network configuration file

To begin using `networkparse`, typically an subclass of :class:`~ConfigBase` will be
instantiated with the text of the configuration file. Currently, `networkparse` has
support for:

- Cisco IOS: :class:`~ConfigIOS`
- Cisco NX-OS: :class:`~ConfigNXOS`
"""
import re
from collections import namedtuple
from typing import List
from .core import ConfigLineList, ConfigLine


class ConfigBase(ConfigLineList):
    """
    Common configuration base operations

    `ConfigBase` is really just a specialized :class:`~ConfigLineList`
    that can hold some settings and act like a :class:`~ConfigLine`
    in terms of having a parent (`None`) and children.

    Refer to :class:`~ConfigLineList` for filtering and searching options
    after you've parsed a configuration file.
    """

    # If an algorithm is walking up a tree of `.parent`s, making it easy to
    # simply watch for None
    parent = None

    # Defaults to ! as the comment marker, following Cisco convention
    # If more complex comment checking is needed override is_comment()
    comment_marker = None

    # Defaults to True to prevent a search from also matching the "no" version
    # of the line.
    full_match = True

    original_lines = None

    def __init__(
        self,
        name="Network Config",
        original_lines: List[str] = None,
        comment_marker: str = "!",
        full_match_default: bool = True,
    ):
        """
        Configures settings used by :class:`~ConfigLine` methods

        In addition, subclasses should verride this to parse the configuration file
        into :class:`~ConfigLine`s. See :class:`~ConfigIOS`
        for an example of this.
        """
        super().__init__()
        self.name = name
        self.comment_marker = comment_marker
        self.full_match = (
            full_match_default
        )  #: Default setting for `full_match` in `filter`
        self.original_lines = original_lines or []  #: Original configuration lines

    @property
    def children(self) -> ConfigLineList:
        """
        Allow for use of ".children" for consistency with :class:`~ConfigLine`

        Returns `self`, which is already a :class:`~ConfigLineList`. It
        is likely cleaner to not use this. I.E.:

        .. code:: python

            config = ConfigIOS(running_config_contents)

            # Prefer this, typically
            config.filter("interface .+")

            # Only use this if it looks clearer in context
            config.children.filter("interface .+")
        """
        return self


class ConfigIOS(ConfigBase):
    """
    Parses Cisco IOS-style configuration into common config format

    Supported command output:

    - `show running-config`
    - `show running-config all`
    - `show startup-config`

    See :class:`~ConfigBase`
    """

    def __init__(self, config_content):
        """
        Break all lines up into tree
        """
        super().__init__(
            name="IOS Config",
            original_lines=config_content.splitlines(),
            comment_marker="!",
        )

        parent_stack = {0: self}
        last_line = None
        last_indent = 0
        for lineno, line in enumerate(self.original_lines):
            # Determine our config depth and compare to the previous line's depth
            # The top-level config is always on the stack, so account for that
            matches = re.match(r"^(?P<spaces>\s*)", line)
            new_indent = len(matches.group("spaces"))

            if new_indent > last_indent:
                # Need to change parents to the last item of our current parent
                parent_stack[new_indent] = last_line

            curr_parent = parent_stack[new_indent]
            last_indent = new_indent
            last_line = ConfigLine(
                config_manager=self,
                parent=curr_parent,
                text=line.strip(),
                line_number=lineno,
            )
            curr_parent.children.append(last_line)


class ConfigNXOS(ConfigIOS):
    """
    Parses Cisco NX-OS-style configuration into common config format

    Presently defers entirely to :class:`~ConfigIOS`
    """


class ConfigJunos(ConfigBase):
    """
    Parses a Juniper OS (Junos)-style configuration into common config format

    Supported command outputs are:

    - `show configuration`
    - `save`

    """

    def __init__(self, config_content):
        """
        Break all lines up into tree
        """
        super().__init__(
            name="Junos Config",
            original_lines=config_content.splitlines(),
            comment_marker="#",
        )

        parent_stack = [self]
        last_line = None
        for lineno, line in enumerate(self.original_lines):
            curr_parent = parent_stack[-1]

            command = True
            block_start = False
            block_end = False
            modified_line = line.strip()
            if modified_line.endswith(";"):
                command = True
            elif modified_line.endswith("{"):
                block_start = True
            elif modified_line.endswith("}"):
                block_end = True

            if block_start or block_end or command:
                modified_line = modified_line[:-1]

            if not block_end:
                last_line = ConfigLine(
                    config_manager=self,
                    parent=curr_parent,
                    text=modified_line.strip(),
                    line_number=lineno,
                )
                curr_parent.children.append(last_line)

            # Change indent?
            if block_start:
                parent_stack.append(last_line)
            elif block_end:
                parent_stack.pop()
