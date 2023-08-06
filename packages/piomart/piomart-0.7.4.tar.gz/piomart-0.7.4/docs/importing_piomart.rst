`module` - using piomart as a module
===============================
it is possible to piomart in a script.The class with the relevant information is provided

  from piomart.piomart import EnsembleClient as pio
  class EnsembleClient():
  
      def  __init__(self,offline=False,json_file="",server='http://rest.ensembl.org',reqs_per_sec=15):
          self.offline = offline
          self.json_file = json_file

The function `add_to_dataframe` takes a pandas dataframe, and a list of colnames which correspond to
the names of the columns in a gtf file as well as the values in the attribute column. So long as the index column is the gene ids, `add_to_dataframe` will append the gene symbols. If the symbol's version doesn't match the version in the gtf file, then the Ensembl id is used instead of the gene symbol. If the gene symbol without the id is not in the gtf file, this usually means it is deprecated. Therefore the Ensembl id
is used, and "_d" is appended to it to give the user an indication that they should check out the id


if you have a counts matrix 

  def add_gene_info(dataframe, columns=[]):
      func = pio(True, "homo_sapiens.json")   
      df = func.add_to_dataframe(dataframe
                                 ,columns)
      df.set_index("gene_name",drop=True,inplace=True)
      return df

df = add_gene_info(my_df,["gene_name"])

| gene_ids   | sample_1 | sample_2 | sample_3 |
|------------+----------+----------+----------|
| ENSG000001 |      100 |      200 |      300 |
| ENSG000002 |      200 |      100 |      300 |
| ENSG000003 |      200 |      400 |      300 |
| ENSG000004 |      300 |      400 |      100 |


| gene_ids   | sample_1 | sample_2 | sample_3 |
|------------+----------+----------+----------|
| GENE1      |      100 |      200 |      300 |
| GENE2      |      200 |      100 |      300 |
| GENE3      |      200 |      400 |      300 |
| GENE4      |      300 |      400 |      100 |

    def add_to_dataframe(self,dataframe,columns=[]):
        """ Return a dataframe with gene info appended"""


