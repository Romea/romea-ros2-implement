#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import sys

from romea_common_meta_bringup.script_parameters import (
    configuration_file_generation_parameters_from_cli,
)
from romea_implement_meta_bringup.meta_description import generate_yaml_configuration_file_str
from romea_implement_meta_bringup.meta_description import ImplementMetaDescription


def main():
    parameters = configuration_file_generation_parameters_from_cli("implement")
    extended = parameters.pop_bool("extended") == "true"
    meta_description_file_path = parameters.pop_str("meta_description_file_path", required=True)
    meta_description = ImplementMetaDescription(meta_description_file_path)
    print(generate_yaml_configuration_file_str(meta_description, extended))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
