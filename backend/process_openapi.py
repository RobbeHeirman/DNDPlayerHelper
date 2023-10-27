import argparse
import json
import sys

from uvicorn.importer import import_from_string


def create_parser():
    parser = argparse.ArgumentParser(prog="extract-openapi.py")
    parser.add_argument("--app", help='App import string. Eg. "main:app"', default="src.main:app")
    parser.add_argument("--app-dir", help="Directory containing the app", default=None)
    parser.add_argument("--out", help="Output file ending in .json or .yaml", default="../frontend/openapi.json")
    return parser


def extract_open_api(args):
    if args.app_dir is not None:
        print(f"adding {args.app_dir} to sys.path")
        sys.path.insert(0, args.app_dir)

    print(f"importing app from {args.app}")
    app = import_from_string(args.app)
    return app.openapi()


def process_open_api(openapi_content):
    for path_data in openapi_content["paths"].values():
        for operation in path_data.values():
            if "tags" not in operation.keys():
                continue
            tag = operation["tags"][0]
            operation_id = operation["operationId"]
            to_remove = f"{tag}-"
            new_operation_id = operation_id[len(to_remove):]
            operation["operationId"] = new_operation_id
    return openapi_content


def main():
    parser = create_parser()
    args = parser.parse_args()
    extract_open_api(args)
    openapi = extract_open_api(args)
    openapi = process_open_api(openapi)
    with open(args.out, "w") as f:
        json.dump(openapi, f, indent=2)
    print(f"spec written to {args.out}")


if __name__ == "__main__":
    main()
