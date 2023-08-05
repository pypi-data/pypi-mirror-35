# acidoseq

Studying Acidobacteria reads from a Nanopore metagenomic data-set | v1.01 | Python v3.5 

Author __Samantha C Pendleton__, Data Science MSc student at Aberystwyth University, [Twitter](https://twitter.com/sap218) | [GitHub](https://github.com/sap218)

The **GC** content of the Acidobacteria genomes are consistent with their placements, e.g. species in the same subdivision (above 60\% for group V fragments and roughly 10\% lower for group III fragments) are similar, displaying the diversity within the phylum [1].
The abundance of the subdivisions correlate with pH depends on the subdivisions: 1, 2, 3, 12, 13 have a negative relationship as pH increases, whilst 4, 6, 7, 10, 11, 16, 17, 18, 22, 25 are sparse in low pH and have a positive relationship as pH increases [2].

This package includes studying a collection of reads and gathering the ones assigned as Acidobacteria from a Kaiju output. There are various statistical information and GC plots. Futhermore, the group of unclassified Acidobacteria reads are visualised into subdivisons based on the pH level of the soil sample.

## Introduction
[**Kaiju**](http://kaiju.binf.ku.dk) output provides taxon ID and the corredponding sequence, my package outputs the Acidobacteria species alongside annotation, plots, and information on the unclassified reads.

###### Prerequisite
- FASTA format of all the reads.
- Kaiju output after extracting the two columns: sequence ID and NCBI taxIDs.

## Installation

**GitClone**

`https://github.com/sap218/acidoseq.git`

**Kaiju**

I used the Kaiju output: columns 2 and 3 which included sequence references and the NCBI taxons.

1. Filter the output with only classified labels	`$ awk '$1 == "C"' kaiju.out > kaijuC.out`
2. Cut the columns					`$ cut -f2,3 kaijuC.out > results.txt`
3. Converted the txt to csv (comma-delimted)		`$ sed 's/\s\+/,/g' results.txt > result_seqid_taxon.csv`

## Map
If you are unsure of the pH of your soil samples, you may want to use the map script first. All images will be in the output folder - default city is Aberystwyth.

Please **note**: due to the fact that the Earth is spherical and maps are 2-dimensional, there will be some distortion when plotting locations.

`$ python3 map.py --city Birmingham`

## Usage
CLI **needs** the Kaiju and FASTA files, all other options have defaults: e.g. pH = 5.

If plot style was entered incorrectly or none it will choose a random one.

Run like followed with **Linux** (find how to [run with other operating systems here](https://en.wikibooks.org/wiki/Python_Programming/Creating_Python_Programs)):

```
$ python3 acidoseq.py --help
Usage: acidoseq.py [OPTIONS]

Options:
  --taxdumptype TEXT  Study "ALL" or only unclassified "U"?
  --kaijufile TEXT    Place edited Kaiju (csv) in directory for ease.
  --fastapath TEXT    Place FASTA in directory for ease.
  --style TEXT        ['seaborn-bright', 'seaborn-poster', 'seaborn-white',
                      'bmh', 'seaborn-darkgrid', 'seaborn-pastel',
                      'grayscale', '_classic_test', 'ggplot', 'seaborn-
                      whitegrid', 'seaborn-dark', 'seaborn-muted', 'seaborn-
                      colorblind', 'seaborn-ticks', 'Solarize_Light2',
                      'seaborn-notebook', 'dark_background', 'fast',
                      'seaborn', 'fivethirtyeight', 'seaborn-paper', 'seaborn-
                      dark-palette', 'seaborn-talk', 'classic', 'seaborn-
                      deep']
  --plottype TEXT     "span" range of GC means OR "line" average mean GC
  --ph TEXT           pH of soil, use map script for assistance.
  --help              Show this message and exit.
```

**Example**

`$ python3 acidoseq.py --kaijufile result_seqid_taxon.csv --fastapath all.fa`

`$ python3 acidoseq.py --taxdumptype ALL --kaijufile result_seqid_taxon.csv --fastapath all.fa --style ggplot --plottype span --ph 4.92`

`$ python3 acidoseq.py --taxdumptype U --kaijufile result_seqid_taxon.csv --fastapath all.fa --style seaborn --plottype line --ph 7.14`

## Acknowledgements
* **Amanda Clare**, supervisor at Aberystwyth University, [Twitter](https://twitter.com/afcaber) | [GitHub](https://github.com/amandaclare)
* **Sam Nicholls**, postdoc at Birmingham University, [Twitter](https://twitter.com/samstudio8) | [GitHub](https://github.com/SamStudio8)

## Thank you! :seedling:

Don't hesitate to create an issue or make a suggestion!

###### Todo List
- [x] Make available
- [x] Improve descriptions and comments
- [x] Look into command line interface
- [x] Fix code to output unclassified subdivisions based on pH
- [ ] Alter code so the input file can be the original Kaiju output

###### References
[1] Quaiser, A., Ochsenreiter, T., Lanz, C., Schuster, S. C., Treusch, A. H., Eck, J., & Schleper, C. (2003). Acidobacteria form a coherent but highly diverse group within the bacterial domain: evidence from environmental genomics. Molecular microbiology, 50(2), 563-575.

[2] Eichorst, S. A., Breznak, J. A., & Schmidt, T. M. (2007). Isolation and characterization of soil bacteria that define Terriglobus gen. nov., in the phylum Acidobacteria. Applied and environmental microbiology, 73(8), 2708-2717.
