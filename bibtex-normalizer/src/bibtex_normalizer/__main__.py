from .cli import setup_parser
from .processor import process_bibtex_file

def main():
    parser = setup_parser()
    args = parser.parse_args()
    
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
