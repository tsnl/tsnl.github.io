#!/usr/bin/env python3

import glob
import shutil
import os.path

import jinja2


TEMPLATE_DIRPATH = "template"
OUTPUT_DIRPATH = "public"


def main():
    bake_templates()
    copy_static_files()


def bake_templates():
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_DIRPATH)
    )
    template_env = {}

    input_filepath_list = glob.glob(f"{TEMPLATE_DIRPATH}/**/pub.*.j2", recursive=True)
    for template_filepath in input_filepath_list:
        template_filepath = os.path.relpath(template_filepath, TEMPLATE_DIRPATH)
        template_filename = os.path.basename(template_filepath)
        template = env.get_template(template_filepath)
        output = template.render(**template_env)
        output_dirpath = os.path.join(OUTPUT_DIRPATH, os.path.dirname(template_filepath))
        output_filename = template_filename[len("pub."):-len(".j2")]
        output_filepath = os.path.join(output_dirpath, output_filename)
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)
        print(output_filepath)
        with open(output_filepath, "w") as f:
            print(output, file=f)


def copy_static_files():
    pass


if __name__ ==  "__main__":
    main()
