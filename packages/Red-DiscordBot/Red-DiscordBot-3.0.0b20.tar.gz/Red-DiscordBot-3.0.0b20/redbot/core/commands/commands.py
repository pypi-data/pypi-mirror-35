"""Module for command helpers and classes.

This module contains extended classes and functions which are intended to
replace those from the `discord.ext.commands` module.
"""
import inspect
from typing import TYPE_CHECKING

from discord.ext import commands

from .errors import ConversionFailure
from ..i18n import Translator

if TYPE_CHECKING:
    from .context import Context

__all__ = ["Command", "GroupMixin", "Group", "command", "group"]

_ = Translator("commands.commands", __file__)


class Command(commands.Command):
    """Command class for Red.

    This should not be created directly, and instead via the decorator.

    This class inherits from `discord.ext.commands.Command`.
    """

    def __init__(self, *args, **kwargs):
        self._help_override = kwargs.pop("help_override", None)
        super().__init__(*args, **kwargs)
        self.translator = kwargs.pop("i18n", None)

    @property
    def help(self):
        """Help string for this command.

        If the :code:`help` kwarg was passed into the decorator, it will
        default to that. If not, it will attempt to translate the docstring
        of the command's callback function.
        """
        if self._help_override is not None:
            return self._help_override
        if self.translator is None:
            translator = lambda s: s
        else:
            translator = self.translator
        command_doc = self.callback.__doc__
        if command_doc is None:
            return ""
        return inspect.cleandoc(translator(command_doc))

    @help.setter
    def help(self, value):
        # We don't want our help property to be overwritten, namely by super()
        pass

    @property
    def parents(self):
        """
        Returns all parent commands of this command.

        This is a list, sorted by the length of :attr:`.qualified_name` from highest to lowest.
        If the command has no parents, this will be an empty list.
        """
        cmd = self.parent
        entries = []
        while cmd is not None:
            entries.append(cmd)
            cmd = cmd.parent
        return sorted(entries, key=lambda x: len(x.qualified_name), reverse=True)

    async def do_conversion(
        self, ctx: "Context", converter, argument: str, param: inspect.Parameter
    ):
        """Convert an argument according to its type annotation.

        Raises
        ------
        ConversionFailure
            If doing the conversion failed.

        Returns
        -------
        Any
            The converted argument.

        """
        # Let's not worry about all of this junk if it's just a str converter
        if converter is str:
            return argument

        try:
            return await super().do_conversion(ctx, converter, argument, param)
        except commands.BadArgument as exc:
            raise ConversionFailure(converter, argument, param, *exc.args) from exc
        except ValueError as exc:
            # Some common converters need special treatment...
            if converter in (int, float):
                message = _('"{argument}" is not a number.').format(argument=argument)
                raise ConversionFailure(converter, argument, param, message) from exc

            # We should expose anything which might be a bug in the converter
            raise exc


class GroupMixin(commands.GroupMixin):
    """Mixin for `Group` and `Red` classes.

    This class inherits from :class:`discord.ext.commands.GroupMixin`.
    """

    def command(self, *args, **kwargs):
        """A shortcut decorator that invokes :func:`.command` and adds it to
        the internal command list.
        """

        def decorator(func):
            result = command(*args, **kwargs)(func)
            self.add_command(result)
            return result

        return decorator

    def group(self, *args, **kwargs):
        """A shortcut decorator that invokes :func:`.group` and adds it to
        the internal command list.
        """

        def decorator(func):
            result = group(*args, **kwargs)(func)
            self.add_command(result)
            return result

        return decorator


class Group(GroupMixin, Command, commands.Group):
    """Group command class for Red.

    This class inherits from `Command`, with :class:`GroupMixin` and
    `discord.ext.commands.Group` mixed in.
    """

    def __init__(self, *args, **kwargs):
        self.autohelp = kwargs.pop("autohelp", True)
        super().__init__(*args, **kwargs)

    async def invoke(self, ctx):
        view = ctx.view
        previous = view.index
        view.skip_ws()
        trigger = view.get_word()
        if trigger:
            ctx.subcommand_passed = trigger
            ctx.invoked_subcommand = self.all_commands.get(trigger, None)
        view.index = previous
        view.previous = previous

        if ctx.invoked_subcommand is None or self == ctx.invoked_subcommand:
            if self.autohelp and not self.invoke_without_command:
                await self._verify_checks(ctx)
                await ctx.send_help()

        await super().invoke(ctx)


# decorators


def command(name=None, cls=Command, **attrs):
    """A decorator which transforms an async function into a `Command`.

    Same interface as `discord.ext.commands.command`.
    """
    attrs["help_override"] = attrs.pop("help", None)
    return commands.command(name, cls, **attrs)


def group(name=None, **attrs):
    """A decorator which transforms an async function into a `Group`.

    Same interface as `discord.ext.commands.group`.
    """
    return command(name, cls=Group, **attrs)
