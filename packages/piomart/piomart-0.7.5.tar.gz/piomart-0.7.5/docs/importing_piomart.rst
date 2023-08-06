`module` - importing piomart 
============================
it is possible to piomart in a script or notebook.

  from piomart.piomart import EnsembleClient as pio
  
The function `add_to_dataframe` takes a pandas dataframe, and a list of colnames which correspond to
the names of the columns in a gtf file as well as the values in the attribute column. So long as the index column is the gene ids, `add_to_dataframe` will append the gene symbols. If the symbol's version doesn't match the version in the gtf file, then the Ensembl id is used instead of the gene symbol. If the gene symbol without the id is not in the gtf file, this usually means it is deprecated. Therefore the Ensembl id
is used, and "_d" is appended to it to give the user an indication that they should check out the id


if you have you have a counts matrix you would like to add gene name information to, you can
add it to the dataframe by creatinga  small function that looks like this.

  def add_gene_info(dataframe, columns=[]):
      func = pio(True, "homo_sapiens.json")   
      df = func.add_to_dataframe(dataframe
                                 ,columns)
      df.set_index("gene_name",drop=True,inplace=True)
      return df

and then passing the df with the column of interest to the function

   df = add_gene_info(my_df, ["gene_name"])

which will change the dataframe as shown below.


| gene_ids   | sample_1 | sample_2 | sample_3 |
|------------+----------+----------+----------|
| ENSG000001 |      100 |      200 |      300 |
| ENSG000002 |      200 |      100 |      300 |
| ENSG000003 |      200 |      400 |      300 |
| ENSG000004 |      300 |      400 |      100 |


| gene_ids   | sample_1 | sample_2 | sample_3 | gene_name  |
|------------+----------+----------+----------|------------|
| ENSG000001 |      100 |      200 |      300 | GENE1      |
| ENSG000002 |      200 |      100 |      300 | GENE2      |
| ENSG000003 |      200 |      400 |      300 | GENE3      |
| ENSG000004 |      300 |      400 |      100 | GENE4      |

`func = pio(True, "homo_sapiens.json")` tells piomart that you
want to use it offline, with the homo_sapiens.json file
(created using the `gtf` and `json` command)

`df = func.add_to_dataframe(dataframe,columns)` simply passes your dataframe
(indexed to ensembl ids!) and columns of interest to the add_to_dataframe method of
the ensembl client class.