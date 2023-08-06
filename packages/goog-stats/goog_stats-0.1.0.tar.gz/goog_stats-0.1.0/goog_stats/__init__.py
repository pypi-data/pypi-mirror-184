import typer
import time
import uuid
import os
from pathlib import Path

APP_NAME = "goog-stats"


class Stats(object):
    enabled: bool = False
    start_time: time
    working_dir_path = typer.get_app_dir(APP_NAME)
    user_id: str = str(uuid.uuid4())

    def __init__(self) -> None:
        print("starting stats collector")
        self.start_time = time.time()
        config_path: Path = Path(self.working_dir_path) / "config"
        if not os.path.exists(self.working_dir_path):
            os.makedirs(self.working_dir_path)
        if not config_path.is_file():
            print("creating config file")
            self.user_id = str(uuid.uuid4())
            with open(config_path, 'w+') as fp:
                fp.write(self.user_id)

    def enable_stat(self):
        self.enabled = True
        return

    def disable_stat(self):
        self.enabled = False

    def is_enabled(self):
        return self.enabled
