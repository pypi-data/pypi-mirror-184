#!/usr/bin/env python3

import argparse
import csv
import datetime
import getpass
import logging
import os
import pathlib
import re
import sys
import yaml

from types import TracebackType
from typing import ItemsView, KeysView, List, Optional, Type

import pylast

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


class UsernameError(Exception):
    def __init__(self, msg: Optional[str] = None,
                 *, username: Optional[str] = None) -> None:
        self.msg = msg
        self.username = username


class FileDoesntExistError(Exception):
    def __init__(self, filepath: pathlib.Path) -> None:
        self.filepath = filepath


class ScrobblingEntries:
    def __init__(self, scrobbling_log_path: pathlib.Path) -> None:
        self.entries = []

        with scrobbling_log_path.open() as tsv:
            line = 0
          
            for str_line in csv.reader(tsv, dialect="excel-tab"):
                line += 1

                # Skip 4 first lines. 
                if line < 4:
                    continue

                artist = str_line[0]
                album = str_line[1]
                track_name = str_line[2]
                track_number = str_line[3]
                duration = int(str_line[4])

                unix_timestamp = str_line[6]       
                unix_timestamp = datetime.datetime.fromtimestamp(int(unix_timestamp))
                local_tz = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
                unix_timestamp = unix_timestamp.replace(tzinfo=local_tz).astimezone(tz=datetime.timezone.utc)

                if str_line[5] == "S":
                    logging.debug(f"Skipped track '{artist} — {track_name}' from album '{album}' at {unix_timestamp}")
                    continue
                  
                self.entries.append({"artist": artist,
                                     "album": album,
                                     "title": track_name,
                                     "track_number": track_number,
                                     "timestamp": unix_timestamp,
                                     "duration": duration})

    def recalculate_timestamp(self, upto: str):
        timestamp = int(datetime.datetime.fromisoformat(upto).timestamp())

        for entry in reversed(self.entries):
            timestamp -= entry["duration"]
            entry["timestamp"] = timestamp


class Credentials:
    def __init__(self, filepath: pathlib.Path) -> None:
        self.creds, self.default_username = self._load_file(filepath)
        self._cred_file_path = filepath

    def __getitem__(self, username: str) -> str:
        return self.creds[username]

    def __setitem__(self, username: str, password: str) -> None:
        return self.add_credentials(username, password)

    def __delitem__(self, username: str) -> None:
        if username not in self.creds:
             raise UsernameError(f"Username {username} doesn't exist",
                                 username=username)

        del self.creds[username]
        if username == self.default_username:
            self.default_username = None

    def __contains__(self, username: str) -> bool:
        return username in self.creds

    def __len__(self) -> int:
        return len(self.creds)

    def items(self) -> ItemsView[str, str]:
        return self.creds.items()

    def __enter__(self) -> "Credentials":
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> Optional[bool]:
        self._save_file(self._cred_file_path)

    def _load_file(self, filepath: Optional[pathlib.Path] = None) -> dict[str, str]:
        if filepath is None:
            filepath = self._cred_file_path

        if not filepath.exists():
            raise FileDoesntExistError(filepath)

        creds = dict()
        default_username = None
        with filepath.open("r") as file:
            config = yaml.load(file, Loader=Loader)
            if config is not None and "users" in config:
                users_info = config["users"]
            else:
                return creds, default_username

            for user in users_info:
                creds[user["username"]] = user["password_hash"]

            if "common" in config:
                common_config = config["common"]
                if "default_username" in common_config:
                    default_username = common_config["default_username"]

        return creds, default_username

    def _save_file(self, filepath: Optional[pathlib.Path] = None) -> None:
        if filepath is None:
            filepath = self._cred_file_path

        structure = dict()
        structure["users"] = dest = list()
        structure["common"] = dict()

        for username, password_hash in self.creds.items():
            dest.append({
                "username": username,
                "password_hash": password_hash
            })
        if len(structure["users"]) == 0:
            del structure["users"]    

        if self.default_username is not None:
            structure["common"]["default_username"] = self.default_username
        else:
            del structure["common"]

        if len(structure) > 0:
            yaml.dump(structure, filepath.open("w"))
        else:
            filepath.open("w").close() 

    def add_credentials(self, username: str, password: str):
        if not is_md5(password):
            password = pylast.md5(password)

        self.creds[username] = password

    def usernames(self) -> KeysView[str]:
        return self.creds.keys()

    def save(self, filepath: Optional[pathlib.Path] = None) -> None:
        if filepath is None:
            filepath = self._cred_file_path

        self._save_file(filepath)

 
class UI:
    def __init__(self) -> None:
        pass

    def add_username(self, username: str,
                     config_file: pathlib.Path) -> None:
        password = getpass.getpass(f"Last.fm password for {username}: ")
       
        if not config_file.exists():
            config_file.parent.mkdir()
            config_file.touch() 
 
        with Credentials(config_file) as credentials:
            credentials[username] = pylast.md5(password)

    def edit_username(self, username: str, credentials: Credentials) -> int:
        if username not in credentials:
            print(f"Username '{username}' doesn't exist")
            return 5
 
        password = getpass.getpass(f"Last.fm password for {username}: ")
        credentials[username] = password

        return 0


def is_md5(datastring: str) -> bool:
    result = re.findall(r"([a-fA-F\d]{32})", datastring)
    if len(result) > 0 and result[0] == datastring: 
        return True
    else:
        return False


def scrobble(scrobbling_file: pathlib.Path, config_file: pathlib.Path,
             *, recalculate_time: Optional[str] = None,
             username: Optional[str] = None) -> int:
    scrobbling_entries = ScrobblingEntries(scrobbling_file)

    if  recalculate_time is not None:
        scrobbling_entries.recalculate_timestamp(recalculate_time)

    credentials = Credentials(config_file)

    password = None
    if username is not None and username in credentials:
        password = credentials[username]
    elif username is not None and username not in credentials:
        print(f"Username '{username}' not in config file. Exit...", file=sys.stderr)
        return 5
    elif username is None and len(credentials) > 1:
        if credentials.default_username is None:
            print("More than one username in config file. Choose one. Exit... ", file=sys.stderr)
            return 5
        else:
            username = credentials.default_username
    elif username is None and len(credentials) == 0:
        print("No usernames in config File. Exit...", file=sys.stderr)
        return 5
    else:
        for username_config, password_config in credentials.items():
            username = username_config
            password = password_config
            break

    API_KEY = "b4dee23dca93e13434b8f0fda47c20a4"
    API_SECRET = "e9201a666af7871ec5e27602d37edc60"

    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=username, password_hash=password)
    network.scrobble_many(scrobbling_entries.entries)

    return 0

#  homedir = os.path.expanduser("~")
#  credsfile = '{}/.config/pyapplier/saved_creds'.format(homedir)



def parse_args(args: List[str]) -> argparse.Namespace:
    argparser = argparse.ArgumentParser()

    subcommands = argparser.add_subparsers(help="Subcommands", dest="subcommand")
    
    subcommand_creds = subcommands.add_parser("creds")
    subcommand_scrobble = subcommands.add_parser("scrobble")
    
    subcommand_creds_subparsers = subcommand_creds.add_subparsers(help="Creds subcommands",
                                                                  dest="subcommand_creds")
    subcommand_creds_list = subcommand_creds_subparsers.add_parser("list")
    subcommand_creds_edit = subcommand_creds_subparsers.add_parser("edit")
    subcommand_creds_edit.add_argument("username", action="store")
    subcommand_creds_add = subcommand_creds_subparsers.add_parser("add")
    subcommand_creds_add.add_argument("username", action="store")
    subcommand_creds_del = subcommand_creds_subparsers.add_parser("del")
    subcommand_creds_del.add_argument("username")
    subcommand_creds_del = subcommand_creds_subparsers.add_parser("set-default-username")
    subcommand_creds_del.add_argument("username")

    subcommand_scrobble.add_argument("-f", "--file", required=True, type=pathlib.Path)
    subcommand_scrobble.add_argument("-r", "--recalculate", required=False, action="store")   
    subcommand_scrobble.add_argument("-u", "--username", required=False, action="store")   
 
    return argparser.parse_args(args[1:])


def main(args: Optional[List[str]] = None) -> int:
    if args is None:
        args = sys.argv

    config_file = pathlib.Path.home() / ".config" / "krautcat" / "scrobbler.yaml" 
    ns = parse_args(args) 

    ui = UI()

    if ns.subcommand == "scrobble":
        return(scrobble(ns.file, config_file, recalculate_time=ns.recalculate,
                        username=username))
        
    if ns.subcommand == "creds":
        if ns.subcommand_creds == "list":
            with Credentials(config_file) as credentials:
                for username in credentials.usernames():
                    print(f"{username}")
        elif ns.subcommand_creds == "edit":
            with Credentials(config_file) as credentials:
                return ui.edit_username(ns.username, credentials)         
        elif ns.subcommand_creds == "add":
            ui.add_username(ns.username, config_file)
        elif ns.subcommand_creds == "del":
            with Credentials(config_file) as credentials:
                del credentials[ns.username]
        elif ns.subcommand_creds == "set-default-username":
            with Credentials(config_file) as credentials:
                if ns.username in credentials:
                    credentials.default_username = ns.username
                else:
                    print(f"Username '{ns.username}' doesn't exist in credentials file. Exit...", file=sys.stderr)
                    return 5
 

if __name__ == "__main__":
    exit(main(sys.argv))
