================
Working offline
================


Downloading the gtf file
~~~~~~~~~~~~~~~~~~~~~~~~~

To download the gtf file use the `gtf` command. To create the json file  needed the gtf file needs to be unzipped

  piomart gtf --species homo_sapiens -u

While this is all you need to download and unzip over ftp the gtf file, it is a good idea to specify the release as well to ensure reproducibility, using the `--release <ver>` option. If no release is specified, the data is pulled from the http://ftp.ensembl.org/pub/current_gtf/ directory which is updated every time a new release is published.

Creating the json file
~~~~~~~~~~~~~~~~~~~~~~

After the gtf file for the species of interest is download, it's time to use to create the json file which is parsed to get the gene symbols and other information. The json file that is created contains two nested objects. The first allows you to access information using Ensembl ids as the keys. The second using gene symbols as keys. The information can be easily by loading in the file and indexing into either object.


  with open(self.json_file) as f:
    data = json.load(f)

  gene_id_dict = data["gene_id"]

  gene_name_dict = data["gene_name"]

The command 

  piomart json -f Homo_sapiens.GRCh38.93.gtf -o homo_sapiens.json

Will parse the gtf file and create the json file `homo_sapiens.json` if no output file is specified `.json` will be added to the input file creating Homo_sapiens.GRCh38.93.gtf.json so it is recommended to specify an output.

Using the info Command
~~~~~~~~~~~~~~~~~~~~~~
The quick command is useful for getting information on on one or two genes. Using our previously downloaded `homo_sapiens.json`

  piomart info ENSG00000278384 --offline -f homo_sapiens.json

will produce the output in the terminal

  gene_id         ENSG00000278384

  gene_version                  1

  gene_name            AL354822.1

  gene_source             ensembl

  gene_biotype     protein_coding

  seqname              GL000218.1

  source                  ensembl

  feature                    gene

  start                     51867

  end                       54893

  score                         .

  strand                        -

  frame                         .


Any number of genes can be specified using spaces. All offline functionality requires the parameter `--offline -f <jsonfile>`


Appending data to a csv file using dataframe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When used in offline mode the `dataframe` command will append up to all the information for each gene in the gtf file. The most common way to use it

  piomart dataframe MyCsv.csv --offline -f homo_sapiens.json --columns=gene_name,gene_id -o Mycsv_with_symbols.csv

piomart assumes that the index column is the first column, and that that column contains Ensembl ids.
if the first column is not the index column. It can be specified with --index using either the column name, or integer.