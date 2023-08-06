import logging

from blessings import Terminal


class Simple(logging.Formatter):
    """
    Fancy, colorised log output adding ANSI escape codes to the log output.

    :params show_threads: Whether to display thread names or not.
    :params show_exc: Whether to display tracebacks or not.

    .. note:: This formatter *suppresses* tracebacks by default! Remember that
        is is meant to give a concise, readable output. If you need to see
        tracebacks on the console, you can override this setting useing
        \*show_exc\*.
    """

    @staticmethod
    def basicConfig(show_exc=True, show_threads=False, *args, **kwargs):
        '''
        Convenience method to have a one-liner set-up.

        Both *show_exc* and *show_threads* are directly passed to
        :py:class:`~.Simple`. The remaining *args* and *kwargs* are passed on to
        :py:func:`logging.basicConfig`.

        After returning from :py:func:`logging.basicConfig`, it will fetch the
        *stderr* and *stdout* handlers and replace the formatter.

        The function also returns a list of all handlers which have been
        modified. This is useful if you want to modify the handlers any further
        (for example using :py:class:`~gouge.filters.ShiftingFilter`).
        '''
        logging.basicConfig(*args, **kwargs)
        root = logging.getLogger()
        output = []
        for handler in root.handlers:
            if (hasattr(handler, 'stream') and
                    hasattr(handler.stream, 'name') and
                    handler.stream.name in ('<stderr>', '<stdout>')):
                handler.setFormatter(Simple(show_exc, show_threads))
                output.append(handler)
        return output

    def __init__(self, show_exc=False, show_threads=False, *args, **kwargs):
        logging.Formatter.__init__(self, *args, **kwargs)
        self.show_threads = show_threads
        self.show_exc = show_exc
        self.term = Terminal()

    def format(self, record):
        if record.levelno <= logging.DEBUG:
            colorize = self.term.bold_black
        elif record.levelno <= logging.INFO:
            colorize = self.term.cyan
        elif record.levelno <= logging.WARNING:
            colorize = self.term.yellow
        elif record.levelno <= logging.ERROR:
            colorize = self.term.bold_red
        else:
            colorize = self.term.bold_yellow_on_red

        record.message = record.getMessage()
        record.asctime = self.formatTime(record, self.datefmt)

        message_items = [
            '{t.green}{asctime}{t.normal}',
            '{levelcolor}{levelname:<10}{t.normal}',
            '{t.bold}[{name}]{t.normal}',
            '{message}',
        ]
        if self.show_threads:
            message_items.insert(0, '{threadName:<10}')

        message_template = ' '.join(message_items)

        if self.show_exc:
            if record.exc_info:
                # Cache the traceback text to avoid converting it multiple times
                # (it's constant anyway)
                if not record.exc_text:
                    record.exc_text = self.formatException(record.exc_info)

            if record.exc_text:
                message_template += '\n{t.red}{exc_text}{t.normal}'

        return message_template.format(
            t=self.term,
            levelcolor=colorize,
            **vars(record))
