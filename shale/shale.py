import yaml
from jinja2 import Environment, FileSystemLoader, Template
import argparse
import sys
import os.path
import re


def usage():
    print "shale.py < --stage stage> < --config config.yml> <--file file1> [--file file2] ... [--file fileN]"

def env_override(value, key):
  return os.getenv(key, value)

def run():


    parser = argparse.ArgumentParser(description='Config variables subsitatution utility')
    parser.add_argument('--stage', type=str, required=True,
                    help='the stage [dev,test,prod] from which to find substitution tokens')

    parser.add_argument('--config', type=str, required=True, metavar='config.yml',
                        help='configuration yaml file from which to read subtitution tokens')

    parser.add_argument('--file', action='append', metavar='file.cfg.tpl [--file file2.cfg.tpl] ...', required=True,
                        help='a file on which to do token substitution. Must be of type .tpl')

    args = parser.parse_args()

    ENV = Environment(loader=FileSystemLoader('./'))
    ENV.filters['env_override'] = env_override

    config = args.config




    if not os.path.isfile(config):
        print "Config file \"" + config + "\" does not exist. Exiting..."
        sys.exit(-1)

    with open(config) as file:
        dictionary =  yaml.load(file)

    if args.stage not in dictionary:
        print "Stage \"" + args.stage + "\" does not exist in " + config
        sys.exit(-1)

    vals = dictionary['default']
    vals.update(dictionary[args.stage])

    for templateFile in args.file:
        print "Processing templateFile " + templateFile

        if not os.path.isfile(templateFile):
            print "File \"" + templateFile + "\" does not exist. Skipping..."
            continue


        template = ENV.get_template(templateFile)
        output = template.render(vals)

        outputFile = re.sub('\.tpl$', '', templateFile)

        # to save the results
        with open(outputFile, "wb") as fh:
            fh.write(output)



if __name__ == "__main__":
    run()
