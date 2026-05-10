#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import sys

from romea_common_meta_bringup.script_parameters import (
    device_urdf_description_generation_parameters_from_cli,
)
from romea_implement_meta_bringup.meta_description import (
    generate_xml_urdf_description_str,
)
from romea_implement_meta_bringup.meta_description import ImplementMetaDescription


def main():

    parameters = device_urdf_description_generation_parameters_from_cli("implement")
    mode = parameters.pop_str("mode", required=True)
    robot_namespace = parameters.pop_str("robot_namespace", required=True)
    meta_description_file_path = parameters.pop_str("meta_description_file_path", required=True)
    meta_description = ImplementMetaDescription(meta_description_file_path, robot_namespace)

    print(generate_xml_urdf_description_str(mode, meta_description))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
