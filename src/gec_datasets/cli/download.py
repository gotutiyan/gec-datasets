import argparse
from gec_datasets import GECDatasets

def main(args):
    gec = GECDatasets(base_path=args.base_path)
    for i in args.ids:
        gec.load(i)

def cli_main():
    args = get_parser()
    main(args)

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base_path', required=True)
    parser.add_argument('--ids', nargs='+', required=True)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_parser()
    main(args)