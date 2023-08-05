"""Reset Config."""

from .base import Base, current_directory
from autolens import conf

config_path = "{}/config".format(current_directory)


class DownloadConfig(Base):
    """Reset Config!"""

    def run(self):
        if conf.is_config(config_path):
            if input("Are you sure? This will reset the state of your config. (y/n)\n").lower() != 'y':
                return
            conf.remove_config(config_path)
        conf.download_config(current_directory)
