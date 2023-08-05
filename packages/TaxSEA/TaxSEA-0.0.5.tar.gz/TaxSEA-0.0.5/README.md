# Taxonomic Set Enrichment Analysis (TaxSEA)

### Description

A pipeline for continuous and discrete enrichment analyses of metagenomic profiling data.


## Installation

1. Install the TaxSEA database

The TaxSEA database can be obtained [here](https://github.com/abdohlman/TaxSEA-database). You will need to set the environment variable $TAXSEA_DB.

Add this line to your .bashrc or .bashprofile and re-start your terminal:
~~~
export TAXSEA_DB=/path/to/database/TaxSEA-database
~~~

2. Install TaxSEA

Via Github:
~~~
git clone https://github.com/abdohlman/TaxSEA.git
~~~

Via pip
~~~
pip install TaxSEA
~~~


Via anaconda:
~~~
coming soon
~~~


## Usage

~~~
TaxSEA [-h] -q [QUERY] [-o [OUTPUT_PATH]] [-f [FORMAT]] [-r [REFERENCE]] -m [MODE] [-b [BACKGROUND]] [-p] [-t [PLOT_FORMAT]] [-n] [-s [SEED]]
                 [-i [TERM_ID]]
~~~

optional arguments:
  `-h, --help`            show this help message and exit
  `-q [QUERY], --query [QUERY]`
                        Path to a query set to compute TaxSEA scores. If mode is continuous, a csv with taxa in rows and association statistics. If mode
                        is discrete, a list of taxa.
  `-o [OUTPUT_PATH], --output-path [OUTPUT_PATH]`
                        Where to output the results.
  `-f [FORMAT], --format [FORMAT]`
                        Format of taxa identifiers. Options include species name ("name") [DEFAULT], NCBI taxon id ("tax_id"), or taxonomy ("taxonomy").
  `-r [REFERENCE], --reference [REFERENCE]`
                        Reference group to search against (phenotypic, genotypic, biotic, abiotic).
  `-m [MODE], --mode [MODE]`
                        Mode to perform enrichment analysis (continuous/discrete/plot).
  `-b [BACKGROUND], --background [BACKGROUND]`
                        Background to use if mode is "discrete".
 ` -p, --plot-significant`
                        Create enrichment plots for significant results.
  `-n, --no-plot`         Do not create enrichment plots.
  `-s [SEED], --seed [SEED]`
                        Random seed to use for permutation analysis.
  `-i [TERM_ID], --term-id [TERM_ID]`
                        Term ID to generate an enrichment plot for (continuous plotting mode only).


### Examples

Continuous TaxSEA
~~~
TaxSEA -m continuous -r biotic -q ./examples/CRC_Dohlman2020.txt -o ./results/CRC_Dohlman2020/
~~~

Discrete TaxSEA
~~~
TaxSEA -m discrete -r biotic -q ./examples/discrete/HMP1.Gut.txt -b ./examples/discrete/HMP1.Gut.background.txt -o ./results/HMP1_Gut/
~~~

Generating TaxSEA enrichment plot for a specific term ID
~~~
TaxSEA -m plot -t EB-Disbiome-000186 -q ./examples/CRC_Dohlman2020.txt -o ./results/CRC_Dohlman2020/
~~~
