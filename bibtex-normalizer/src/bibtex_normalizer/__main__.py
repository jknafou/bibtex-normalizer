from .cli import setup_parser
from .processor import process_bibtex_file
import os

def main():
    parser = setup_parser()
    args = parser.parse_args()

    if args.output is None:
        input_name, input_ext = os.path.splitext(args.input)
        args.output = f"{input_name}_normalized{input_ext}"
    
    if args.verbose:
        print(f"Processing {args.input} → {args.output}")
    
    try:
        process_bibtex_file(args.input, args.output)
        print(f"Successfully processed {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise SystemExit(1) from e

if __name__ == "__main__":
    main()
