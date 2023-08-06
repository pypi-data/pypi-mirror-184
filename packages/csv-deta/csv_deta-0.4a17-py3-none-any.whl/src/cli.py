####
##
#
#

__version__ = "0.4a17"

import fire
from src import detacsv

# import detacsv


def main():
    fire.Fire(detacsv.DetaCsv)


if __name__ == "__main__":
    main()
