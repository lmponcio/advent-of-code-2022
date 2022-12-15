# Input = terminal output
#   determine the total size of each directory
#       The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly
#   total disk space 70000000
#   need unused space of 30000000
# PART A QUESTION:
#   what is the toal size of the smallest directory that will allow for enough space?


import logging
from os.path import join, dirname

TOTAL_DISK = 70000000
NEEDED_SPACE = 30000000


def log_setup():
    handler_to_file = logging.FileHandler("log.log", "w")
    handler_to_file.setLevel(logging.DEBUG)
    handler_to_console = logging.StreamHandler()
    handler_to_console.setLevel(logging.ERROR)
    logging.basicConfig(
        handlers=[
            handler_to_file,
            handler_to_console,
        ],
        format="%(asctime)s: %(levelname)s %(filename)s %(lineno)s: %(message)s",
        level=logging.DEBUG,
    )


log_setup()


class SystemScanner:
    def __init__(self) -> None:
        self.wd = None
        self.dirs = {}  # dictionary containing the files of each dir
        self.parenthood = {}  # dictionary containing the parent relationships

    def get_wd(self):
        return self.wd

    def add_wd(self, dir_path):
        if dir_path not in self.dirs:
            logging.debug("    old dirs dict: %s", self.dirs)
            self.dirs[self.wd] = []
            logging.debug("    new dirs dict: %s", self.dirs)

    def change_wd(self, new_dir):
        logging.debug("    old wd: %s", scanner.get_wd())
        self.wd = new_dir
        logging.debug("    new wd: %s", scanner.get_wd())

    def change_wd_up(self):
        logging.debug("    old wd: %s", scanner.get_wd())
        self.wd = dirname(self.wd)
        logging.debug("    new wd: %s", scanner.get_wd())

    def add_file(self, file_size):
        logging.debug("    adding file: %s", file_size)
        self.dirs[self.wd].append(file_size)

    def _get_files_summary(self):
        dir_sums = {}
        for dir in self.dirs:
            this_sum = sum(self.dirs[dir])
            dir_sums[dir] = this_sum
        return dir_sums

    def _generate_parenthood(self):
        for dir in self.dirs:
            self.parenthood[dir] = []
            for other_dir in self.dirs:
                if dir == other_dir:
                    pass
                elif other_dir.startswith(dir) and len(other_dir) > len(dir):
                    self.parenthood[dir].append(other_dir)

    def get_summary(self):
        self._generate_parenthood()
        files_summary = self._get_files_summary()
        full_summary = files_summary
        dir_paths = list(files_summary.keys())
        for dir in self.parenthood:
            for child in self.parenthood[dir]:
                full_summary[dir] += files_summary[child]
        return full_summary


scanner = SystemScanner()
with open("day_07/input.txt") as file:
    for line in file:
        line = line.strip()
        logging.debug("%s", line)
        if line.startswith("$"):
            if line == "$ cd /":
                logging.debug("    to top directory")
                scanner.change_wd("/")
                scanner.add_wd("/")
            elif line == ("$ cd .."):
                logging.debug("    one dir up")
                scanner.change_wd_up()
            elif line.startswith("$ cd "):
                line = line.split(" ")
                this_dir_name = line[-1]
                full_path = join(scanner.wd, this_dir_name)
                scanner.change_wd(full_path)
                scanner.add_wd(full_path)
            elif line == "$ ls":
                logging.debug("    inspecting")
        elif line.startswith("dir"):
            pass
        else:
            size = int(line.split(" ")[0])
            scanner.add_file(size)


summary = scanner.get_summary()
available = TOTAL_DISK - summary["/"]
to_free = NEEDED_SPACE - available
sizes_list = list(summary.values())
size_to_remove = TOTAL_DISK  # start with a very high value
for size in sizes_list:
    if size > to_free and size < size_to_remove:
        size_to_remove = size


print("Answer:", size_to_remove)
# correct answer: 2086088
