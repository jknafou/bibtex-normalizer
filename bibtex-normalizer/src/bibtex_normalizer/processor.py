import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bibdatabase import as_text
from typing import Dict
import re
from .capitalizer import capitalize_title
from .capitalizer import dynamic_bounding_pattern

# Declare global variable
global month_dict
month_dict = {}

def process_bibtex_file(input_path: str, output_path: str) -> None:
    global month_dict
    parser = BibTexParser(common_strings=True, interpolate_strings=False)

    with open(input_path, 'r') as f:
        bib_db = bibtexparser.load(f, parser=parser)
    
    month_dict = {value: key for key, value in bib_db.strings.items()}

    processed_entries = [
        process_entry(entry, bib_db.strings)
        for entry in bib_db.entries
    ]
    
    with open(output_path, 'w') as f:
        f.write("\n\n".join(processed_entries))

def process_entry(entry: Dict, strings: Dict) -> str:
    lines = [
        f"@{entry['ENTRYTYPE']}{{{entry['ID']},",
        *[format_field(k, v, strings) for k, v in entry.items() 
         if k not in ('ENTRYTYPE', 'ID')],
        "}"
    ]
    return "\n".join(lines)

def format_field(key: str, value: str, strings: Dict) -> str:
    global month_dict
    if isinstance(value, str):
        cleaned_value = extract_content(value)
    else:
        cleaned_value = month_dict[value.get_value()]
    if key == "title":
        cleaned_value = capitalize_title(cleaned_value)
    return f'    {key} = {{{cleaned_value}}},'

def extract_content(text: str) -> str:
        bounding_chars = [("\"", "\""), ("{", "}"), ("[", "]")]
        while True:
            breaking_count = 0
            for bc in bounding_chars:
                left_pattern, right_pattern = bc[0], bc[1]
                pattern = dynamic_bounding_pattern(left_pattern, right_pattern)
                bounding_chars = [("\"", "\""), ("{", "}"), ("[", "]")]
                match = re.match(pattern, text)
                if match:
                    text = match.group(1)
                else:
                    breaking_count += 1
            if breaking_count == len(bounding_chars):
                break
        return text.strip()