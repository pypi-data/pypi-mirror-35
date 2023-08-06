"""
Search a network configuration file

This module holds the primitives that make up a network configuration--configuration
lines and lists of lines.

To begin using `networkparse`, start with :module:`~parse`
"""
import re
from typing import List


class MultipleLinesError(Exception):
    """
    More than one line was found
    """


class NoLinesError(Exception):
    """
    No lines were found and at least one was expected
    """


class ConfigLine:
    """
    A line of a configuration file, which may or may not have children
    """

    # Config manager is used for checking style-specific questions
    config_manager = None

    # Parent block line (ie, might point to a line that's interface Eth1/1)
    parent = None

    line_number = None
    text = ""
    children = None

    def __init__(self, config_manager, parent, text, line_number=None, children=None):
        self.config_manager = config_manager  #: `ConfigBase` this line is using
        self.text = text  #: Text of line, without leading whitespace
        self.parent = (
            parent
        )  #: Parent of this line--could be a `ConfigBase` or another `ConfigLine`
        self.line_number = line_number  #: Line number in original configuration file
        self.children = (
            children or ConfigLineList()
        )  #: Children under this line, empty list if there are none

    def __repr__(self):
        return f"Line {self.line_number}: {self.text} ({len(self.children)} children)"

    @property
    def siblings(self):
        """
        Returns a :class:`~ConfigLineList` of all sibling lines

        Does not include this line in the list
        """
        siblings = self.parent.children.copy()
        siblings.remove(self)
        return siblings

    def tree_display(
        self,
        line_number: bool = False,
        initial_indent: int = 0,
        internal_indent: int = 0,
    ) -> str:
        """
        Print this line and child lines indented to show hierachy
        """
        start_str = " " * initial_indent
        if line_number:
            start_str += f"{self.line_number}: "

        start_str += " " * internal_indent

        lines = [f"{start_str}{self.text} ({len(self.children)} children)"]
        for c in self.children:
            lines.append(
                c.tree_display(
                    initial_indent=initial_indent,
                    line_number=line_number,
                    internal_indent=internal_indent + 2,
                )
            )
        return "\n".join(lines)

    def is_comment(self):
        """
        Returns true if line is a commment
        """
        return self.text.startswith(self.config_manager.comment_marker)


class ConfigLineList:
    """
    A searchable list of :class:`~ConfigLine` s

    This class acts like a standard Python list, so indexed access via `[]`,
    `len()`, etc. all work. See the Python 3 documentation on `list`_ for more
    methods.

    This class may not hold only `ConfigLine` items from the same parent--it can
    store *any* `ConfigLine`, so be aware that iterating through a `ConfigLineList`
    does not necessarily mean all items have the same parent. In particular, after
    running :func:`~filter` or :func:`~flatten` the returned list will
    be a mixture of parents.

    .. _list: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
    """

    def __init__(self, lines: List[ConfigLine] = None):
        self.lines = lines or []

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, index):
        return self.lines[index]

    def __setitem__(self, index, line):
        self.lines[index] = line

    def __delitem__(self, index):
        del self.lines[index]

    def __iter__(self):
        return iter(self.lines)

    def __getattr__(self, name):
        """
        Defers all failing calls to list
        """
        return getattr(self.lines, name)

    def __str__(self):
        return self.tree_display(line_number=True)

    def __repr__(self):
        return str(self)

    def copy(self):
        """
        Create a copy of this list
        """
        return ConfigLineList(self.lines.copy())

    def tree_display(self, line_number: bool = False, initial_indent: int = 0):
        """
        Print all lines in list with indents to show hierachy

        Despite the name, remember that the top-level items may not all have the
        same parent and may in fact display the same item multiple times.

        See `ConfigLine`'s :func:`~ConfigLine.tree_display` for more details on parameters.
        """
        if not self.lines:
            return (" " * initial_indent) + "(empty line list)"

        lines = []
        for line in self.lines:
            lines.append(
                line.tree_display(
                    initial_indent=initial_indent, line_number=line_number
                )
            )
        return "\n".join(lines)

    def one(self) -> ConfigLine:
        """
        Returns the single ConfigLine in list

        Raises :class:`~MultipleLinesError` if there is more than one item in list.
        Raises :class:`~NoLinesError` if there are no items in list. Use
        :func:`~one_or_none` to return None if there are no items
        """
        item = self.one_or_none()
        if item is None:
            raise NoLinesError()
        return item

    def one_or_none(self) -> ConfigLine:
        """
        Returns the single ConfigLine in list

        Raises :class:`~MultipleLinesError` if there is more than one item in list. Returns
        None if there are no items in list. Use :func:`~one` to raise an exception
        if there are no items
        """
        if len(self) == 0:
            return None
        elif len(self) > 1:
            raise MultipleLinesError()
        else:
            return self[0]

    def flatten(self, depth: int = None) -> List:
        """
        Return a ConfigLineList of all of this list *and* the children

        If `depth` is None, returns all children, recursing as deeply as needed into the
        hierarchy (technically, limited to 500). Otherwise, flattens only the top
        `depth` levels.

        For example, say you have the structure:

        - level 1

            - level 2

                - level 3

        `flatten(depth=None)` returns:

        - level 1
        - level 2
        - level 3

        `flatten(depth=1)` returns:

        - level 1
        - level 2

            - level 3
        """
        if depth is None:
            depth = 500

        flattened = ConfigLineList()
        for line in self.lines:
            flattened.append(line)

            if depth > 0:
                flattened.extend(line.children.flatten(depth=depth - 1))
        return flattened

    def filter(
        self,
        regex: str,
        full_match: bool = None,
        invert: bool = False,
        search_depth: int = 0,
        skip_comments: bool = True,
    ) -> List:
        """
        Find all lines that match the regex

        See `filter_children()` for explanation of parameters

        If `invert` is True, excludes matched items from the list.

        Returns a new ConfigLineList with the filtered items. Returns an empty list
        if none are found.
        """
        if not self.lines:
            return ConfigLineList()

        if full_match is None:
            full_match = self.lines[0].config_manager.full_match

        compiled = re.compile(regex)
        if full_match and not invert:
            match_func = compiled.fullmatch
        elif full_match and invert:
            match_func = lambda t: not compiled.fullmatch(t)
        elif not full_match and not invert:
            match_func = compiled.search
        elif not full_match and invert:
            match_func = lambda t: not compiled.search(t)

        starting_list = self
        if search_depth != 0:
            starting_list = self.flatten(depth=search_depth)

        matches = ConfigLineList()
        for s in starting_list:
            if not (skip_comments and s.is_comment()) and match_func(s.text):
                matches.append(s)

        return matches

    def exclude(self, regex: str, **kwargs) -> List:
        """
        Calls `filter()` with `invert` = `True`

        See `filter()` for argument descriptions. Comments will still not be included
        unless `skip_comments` is False.
        """
        return self.filter(regex=regex, invert=True, **kwargs)

    def filter_with_child(
        self,
        child_regex: str,
        full_match: bool = None,
        invert: bool = False,
        search_depth: int = 0,
        skip_comments: bool = True,
    ) -> List:
        """
        Find all lines that have a *child* that matches the given regex.

        For example, if this list has these items (children shown as well):

        - child 1
        - child 2
        - child 3

            - child 4
            - child 5

        - child 6

            - child 7

                - child 8
                - child 9

        Then `filter_with_child("child 4")` will return the list:

        - child 3

            - child 4
            - child 5

        If `search_depth` is not 0, the child does not need to be a direct descendent.
        See `filter()`'s `depth` argument for more details. Given the example above,
        `filter_with_child("child 8", search_depth=None)` will return the list:

        - child 6

            - child 7

                - child 8
                - child 9
        """
        real_match = ConfigLineList()
        for match in self.lines:
            if match.children.flatten(depth=search_depth).filter(
                regex=child_regex, full_match=full_match
            ):
                real_match.append(match)

        return real_match

    def filter_without_child(
        self,
        child_regex: str,
        full_match: bool = None,
        invert: bool = False,
        search_depth: int = 0,
        skip_comments: bool = True,
        skip_childless: bool = False,
    ) -> List:
        """
        Find all lines that do not have a child that matches the given regex.

        Follows the symmatics of `filter_children()`, see that function for more
        details.

        If `skip_childless` is False (the default), a line that has no children
        will always be matched by this function.
        """
        real_match = ConfigLineList()
        for match in self.lines:
            if skip_childless and not match.children:
                continue

            if not match.children.flatten(depth=search_depth).filter(
                regex=child_regex, full_match=full_match
            ):
                real_match.append(match)

        return real_match
