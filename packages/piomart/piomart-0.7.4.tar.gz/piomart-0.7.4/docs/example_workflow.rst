=========================================
Example Workflow Offline
=========================================


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

  piomart offline -f Homo_sapiens.GRCh38.93.gtf -o homo_sapiens.json

Will parse the gtf file and create the json file `homo_sapiens.json` if no output file is specified `.json` will be added to the input file creating Homo_sapiens.GRCh38.93.gtf.json so it is recommended to specify an output.

Using the Quick Command
~~~~~~~~~~~~~~~~~~~~~~~
The quick command is useful for getting information on on one or two genes. Using our previously downloaded `homo_sapiens.json`

  piomart quick ENSG00000278384 --offline -f homo_sapiens.json

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

Currently, the csv file must contain the gene information as the first column. And it will not be returned in the appended dataframe, so always specify gene_id to get the genes back. If gene versions are specified with the ids, information about the genes is only appended if the version is an exact match. If not the gene_name will just be returned as the original gene that was queried. All other columns will contain `False` as their value. There is one special case. If gene versions are not specified with the ids, then if the id does not exist in the gtf file, the gene_id is returned with _d (deprecated) appended to the end to alert the user. The values in the field will also be deprecated.