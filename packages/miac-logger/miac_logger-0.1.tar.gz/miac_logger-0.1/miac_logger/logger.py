import os
from datetime import datetime


class BaseLogger:
    """Basic class. Use it for initialization new object logger()"""

    # Levels to write to file
    _LEVELS = ['WARNING', 'ERROR', ]

    def __init__(self, path_to_log_file: str = os.getcwd(), log_file_name: str = 'app.log', current_file: str = None):
        self.level = None
        self.message = None
        self.current_file = current_file
        self.path_to_log_file = path_to_log_file
        self.log_file_name = log_file_name

    def set_levels(self, *args) -> None:
        """Set levels to write it to DB or file ('WARNING', 'ERROR', 'INFO', 'DEBUG')
            Default values is ['WARNING', 'ERROR', ]
            Example: logger.set_levels('INFO', 'DEBUG')
        """
        for arg in args:
            if arg not in self._LEVELS:
                self._LEVELS.append(arg)

    def del_levels(self, *args) -> None:
        """Delete levels to write it to DB or file ('WARNING', 'ERROR', 'INFO', 'DEBUG')
            Default values is ['WARNING', 'ERROR', ]
            Example: logger.del_levels('INFO', 'DEBUG')
        """
        for arg in args:
            if arg in self._LEVELS:
                self._LEVELS.pop(self._LEVELS.index(arg))

    def _write_to_file(self):
        with open(f'{self.path_to_log_file}\\{self.log_file_name}', 'a', encoding='utf-8') as f:
            f.write(
                f'[{datetime.now().strftime("%d.%m.%Y %H:%M:%S")}][{self.level}][{self.current_file}] {self.message}\n'
            )

    def _dispatcher(self, level, message):
        self.level = level
        self.message = message
        if level in self._LEVELS:
            self._write_to_file()
            print(f'[{self.level}] {self.message}')
        else:
            print(f'[{self.level}] {self.message}')

    def debug(self, message: str):
        level = 'DEBUG'
        self._dispatcher(level, message)

    def info(self, message: str):
        level = 'INFO'
        self._dispatcher(level, message)

    def warning(self, message: str):
        level = 'WARNING'
        self._dispatcher(level, message)

    def error(self, message: str):
        level = 'ERROR'
        self._dispatcher(level, message)
