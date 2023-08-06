import os

from dataclasses import dataclass
from typing import List

__all__ = ['parse', 'parse_user_settings']


COMMAND_NAMES = {
        '0x10000001': 'Delete',
        '0x10000002': 'Insert',
        '0x10000003': 'Mark',
        '0x10000004': 'Remove',
        '0x10000005': 'Cue Marker',
        '0x10000006': 'Replace',
        '0x10000007': 'Right',
        '0x10000008': 'Left',
        '0x10000009': 'Swap',
        '0x1000000A': 'Unmark',
        '0x1000000B': 'Play',
        '0x1000000C': 'Stop',
        '0x1000000D': 'Reverse',
        '0x1000000E': 'Reverse Nudge',
        '0x1000000F': 'Forward Nudge',
        '0x10000010': 'Remove Cue Marker',
        '0x10000011': 'Switch',
        '0x10000012': 'Join',
        '0x10000015': 'Start',
        '0x10000017': 'Backtime',
        '0x1000001B': 'End',
        '0x1000001C': 'Jog',
        '0x1000001D': 'Mark segment end',
        '0x1000001E': 'Trim In',
        '0x1000001F': 'Trim Out',
        '0x10000025': 'Undo',
        '0x10000027': 'Trim Last Out',
        '0x10000028': 'Trim Next In',
        '0x1000002D': 'Redo',
        '0x1000002E': 'Fill',
        '0x34000001': 'Jog Left',
        '0x34000002': 'Jog Right',
        }


@dataclass
class Key:
    code: int
    ctrl: bool = False
    alt: bool = False
    shift: bool = False
    cmd: bool = False
    special: bool = False
    char: str = None

    @classmethod
    def from_code(cls, code):
        modifier = (code & 0xFFFF0000) >> 16
        keycode = code & 0xFFFF
        shift = bool(modifier & 0x100)
        control = bool(modifier & 0x200)
        alt = bool(modifier & 0x400)
        command = bool(modifier & 0x010)
        special = bool(modifier & 0x800)

        return cls(
                code=keycode, shift=shift, ctrl=control,
                alt=alt, cmd=command, char=chr(keycode),
                special=special)


class Command:
    @classmethod
    def factory(cls, code, tap, hold=None):
        return cls(
                code=code, name=COMMAND_NAMES.get(code) or code,
                tap=Key.from_code(tap),
                hold=Key.from_code(hold) if hold else None)


@dataclass
class ConsoleCommand(Command):
    code: int
    name: str
    tap: Key
    hold: Key = None


@dataclass
class GlobalCommand(Command):
    code: str
    name: str
    tap: Key
    hold: Key = None


@dataclass
class Preferences:
    commands: List[Command]


def parse(path):
    import re
    import enum

    RE_SECTION = re.compile(r'^\[(.+)\]$')
    STATES = enum.Enum('STATES', 'search keys end')
    FORMAT = enum.Enum('FORMAT', 'unknown prefs usersettings')

    state = STATES.search
    rows = []

    file_format = FORMAT.unknown

    with open(path, 'r') as fh:
        for line in fh.readlines():
            line = line.strip()
            match = RE_SECTION.match(line)
            if match:
                section = match[1]
                if section in (
                        'KeyAssignments2', 'Configuration\\MappingManager2'):
                    state = STATES.keys
                    if section == 'KeyAssignments2':
                        file_format = FORMAT.prefs
                    else:
                        file_format = FORMAT.usersettings
                else:
                    if state == STATES.keys:
                        break
            elif state is STATES.keys and line:
                rows.append(line)

    commands = []
    cmdtypes = {
            'ConsoleMapper': ConsoleCommand,
            'GlobalCommands': GlobalCommand,
            }

    if file_format == FORMAT.unknown:
        raise ValueError('Unknown file format')

    if file_format == FORMAT.prefs:
        def parse_row(row):
            enabled, kind, code, key1, key2, key3, tap, *rest = row.split(':')
            return enabled, kind, code, key1, key2, key3, tap
    else:
        def parse_row(row):
            kind, code, key1, key2, key3, tap, enabled = row.split(':')
            enabled = enabled[1:] if enabled else ''
            return enabled, kind, code, key1, key2, key3, tap

    for row in rows:
        enabled, kind, code, key1, key2, key3, tap = parse_row(row)
        enabled = (enabled.lower() or '') == 'true'
        tap = (tap.lower() or '') == 't'
        key1 = int(key1, 16) if key1 else None
        key2 = int(key2, 16) if key2 else None
        key3 = int(key3, 16) if key3 else None
        code = re.sub('^"(.+)"$', '\\1', code)

        if enabled:
            try:
                factory = cmdtypes[kind].factory
            except KeyError:
                continue
            else:
                if tap:
                    key, hold = key3, key2
                else:
                    key, hold = key1, None
                commands.append(factory(code, key, hold))

    p = Preferences(commands=commands)
    return p


def parse_user_settings(path=None):
    path = path or os.path.expanduser('~/Lightworks/UserSettings.txt')
    return parse(path)
