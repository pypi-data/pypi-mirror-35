import argparse
from .fnr_core import load_keywords_to_be_replaced, find_and_replace

def parse_cla():
    parser = argparse.ArgumentParser()
    parser.add_argument("patient", help="Filename - The original input file containing the content that we would like to find and replace", type=str)
    parser.add_argument('-f', '--context-file', help="Filename - An input file containing set of key value pairs to find & replace. The placeholder keywords you're looking to replace should have curly braces {} around it", type=str)
    parser.add_argument("--in-place", help="Use if you would not like a new file to be generated and you want to just replace the text in the original file", action="store_true")

    return parser.parse_args()

def main():
    print('Hello, fnr!')
    args = parse_cla()

    # Get the mapping of items to be replaced
    context = {}
    try:
        context = load_keywords_to_be_replaced(args)
    except:
        print('Failed to load keyword mapping of values to be replaced')
        print('Exiting now...')
        exit()

    # Read in
    template = ''
    with open(args.patient, 'r') as in_file:
        template = in_file.read()

    # Write out
    out_file = (args.patient if args.in_place else 'newfile.out')
    with open(out_file, 'w') as out:
        out.write(find_and_replace(context, template))

if __name__ == '__main__':
    main()
