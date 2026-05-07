import gec_datasets
import argparse
import pprint

def main():
    pprint.pprint(gec_datasets.available())

def cli_main():
    main()

if __name__ == '__main__':
    main()