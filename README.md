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
cd bibtex-normalizer/bibtex-normalizer
```

3. **Install dependencies using Rye**:

```bash
rye sync
```


## Usage

Normalize a `.bib` file:

```bash
rye run bibtex-normalizer --input <input_file> --output <output_file>
```

### Demo
To test the program, you can use the provided example file `references.bib` by running the following command:

```bash
rye run bibtex-normalizer
```

### Examples
1. **Specify both input and output files**:
```bash
rye run bibtex-normalizer --input example.bib --output example_normalized.bib
```

2. **Use default output naming** (input filename + "_normalized" suffix):

```bash
rye run bibtex-normalizer --input example.bib
```

## Contributing
We welcome contributions.