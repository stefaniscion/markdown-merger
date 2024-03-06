import argparse
from pathlib import Path

def get_file_content(file_path: Path):
    with open(file_path, 'r') as file_handler:
        return file_handler.read()

parser = argparse.ArgumentParser(description='Merges a folder of markdowns in a single markdown.')
parser.add_argument(
    'path', 
    metavar='D', 
    type=Path, 
    help='path of directory containing the markdowns to be merged'
)
args = parser.parse_args()

output_path = Path("output.md")

if args.path.is_dir():
    output_handler = open(output_path, "w")
    for file_path in sorted(args.path.iterdir()):
        if file_path.suffix == '.md':
            file_content = get_file_content(file_path)
            file_content += "\n\n"
            if file_content:
                output_handler.write(file_content)
else:
    print("The path is not a directory")