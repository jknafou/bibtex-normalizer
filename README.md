# BibTeX Normalizer

A small Python program to normalize `.bib` files.

## Motivation

During my PhD, I've gathered an extensive collection of BibTeX entries in my bibliography. I've observed inconsistencies in the formatting of these entries, which might require manual adjustments depending on the citation style you want to apply. This program is designed to standardize the BibTeX formats and introduce some basic rules for capitalizing titles.

## Features

The core of this tool revolves around iterating through entries in a .bib file and applying normalization rules, with a particular focus on title formatting. The capitalize_title function encapsulates the logic for intelligent title capitalization, considering various linguistic and typographic conventions.


## Installation

1. **Clone the repository**:

```bash
git clone git@github.com:jknafou/bibtex-normalizer.git
```

2. **Navigate to the project directory**:
```bash
cd bibtex-normalizer/
```

3. (Option 1) **Install dependencies using Rye**:

```bash
rye sync
. .venv/bin/activate      # .\venv\Scripts\activate on Windows```
```

3. (Option 2) **Install dependencies using pip on a venv**:

```bash
python -m venv .venv
.venv/bin/activate      # .\venv\Scripts\activate on Windows```
pip install .
```

**One shot installation using pip+git on a venv**:

Here, skip step 1 & 2 and run the following commands:
```bash
python -m venv .venv
.venv/bin/activate      # .\venv\Scripts\activate on Windows```
pip install git+https://github.com/jknafou/bibtex-normalizer.git
```
## Usage

Normalize a `.bib` file:

```bash
bibtex-normalizer --input <input_file> --output <output_file>
```

### Demo
To test the program, you can use the provided example file `references.bib` by running the following command:

```bash
bibtex-normalizer
```

### Examples
1. **Specify both input and output files**:
```bash
bibtex-normalizer --input example.bib --output example_normalized.bib
```

2. **Use default output naming** (input filename + "_normalized" suffix):

```bash
bibtex-normalizer --input example.bib
```

## Contributing
We welcome contributions.