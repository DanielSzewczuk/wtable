import os
import argparse
import prettytable as pt

def whois(domain):
    result = os.popen(f'whois {domain}').read()
    return result

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('domain', help='Domain name to look up')
    return parser.parse_args()

def create_table(result):
    table = pt.PrettyTable()
    table.field_names = ["Field", "Value"]

    # Split the WHOIS result into lines
    lines = result.splitlines()
    for line in lines:
        if ": " in line:
            key, value = line.split(": ", 1)
            table.add_row([key.strip(), value.strip()])

    return table

if __name__ == '__main__':
    args = get_arguments()
    result = whois(args.domain)
    table = create_table(result)
    print(table)
