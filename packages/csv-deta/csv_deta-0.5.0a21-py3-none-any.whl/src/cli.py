####
##
#
#

__version__ = "0.5.0-alpha-21"

import fire
from src import detacsv

# import detacsv


def main():
    fire.Fire(detacsv.DetaCsv)


if __name__ == "__main__":
    main()
