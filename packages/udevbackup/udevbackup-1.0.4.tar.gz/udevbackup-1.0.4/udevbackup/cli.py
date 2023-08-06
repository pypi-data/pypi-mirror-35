import argparse
import glob
from configparser import ConfigParser

from termcolor import cprint

from udevbackup.rule import Config, Rule


def load_config(config_dir):
    config_filenames = glob.glob("%s/*.ini" % config_dir)
    parser = ConfigParser()
    parser.read(config_filenames, encoding='utf-8')
    config_section = Config.section_name
    kwargs = Config.load(parser, config_section)
    config = Config(**kwargs)
    for section in parser.sections():
        if section == config_section:
            continue
        kwargs = Rule.load(parser, section)
        rule = Rule(config, section, **kwargs)
        config.register(rule)
    return config


def main():
    """

    Returns:
      * :class:`int`: 0 in case of success, != 0 if something went wrong

    """
    parser = argparse.ArgumentParser(description="Run script when targetted external devices are connected")
    parser.add_argument("command", choices=("show", "run", "help"))
    parser.add_argument(
        "--config-dir",
        "-C",
        default="/etc/udevbackup",
        help="Configuration directory (default: /etc/udevbackup)",
    )
    parser.add_argument(
        "--no-fork",
        action="store_true",
        default=False,
        help="do not fork",
    )
    args = parser.parse_args()
    return_code = 0  # 0 = success, != 0 = error
    try:
        config = load_config(args.config_dir)
    except ValueError as e:
        cprint("Unable to load udevbackup configuration: %s" % e, "red")
        config = None
    if not config:
        return_code = 1
    elif args.command == "show":
        config.show()
    elif args.command == "run":
        config.run(fork=not args.no_fork)
    elif args.command == "help":
        Config.show_rule_file()
        cprint("Create one or more .ini files in %s." % args.config_dir)
        cprint("Yellow lines are mandatory.")
        Config.print_help(Config.section_name)
        cprint("")
        Rule.print_help("example")
    return return_code


if __name__ == "__main__":
    import doctest

    doctest.testmod()
