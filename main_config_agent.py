import os
from toolbox.config_agent.config_agent import ConfigAgent

current_path = os.path.dirname(__file__)
config_folder = os.path.join(current_path, 'toolbox\config_agent')
# config_filename = 'config.ini'
config_filename = 'config.toml'
config_path = os.path.join(config_folder, config_filename)


def main():
    config = ConfigAgent(config_path=config_path, category_prefix="cat")
    pass


if __name__ == "__main__":
    main()