import argparse

def setup_parser():
    parser = argparse.ArgumentParser(
        description="Normalize BibTeX files: capitalize titles"
    )
    
    parser.add_argument('-I', '--input', 
                       type=str, 
                       default="./bibliography/references.bib",
                       help="Input BibTeX file path")
    
    parser.add_argument('-O', '--output',
                       type=str, 
                       help="Output file path (by default, add '_normalized' to the input file name)")
    
    parser.add_argument('-V', '--verbose',
                       action="store_true",
                       help="Enable verbose output")
    
    return parser