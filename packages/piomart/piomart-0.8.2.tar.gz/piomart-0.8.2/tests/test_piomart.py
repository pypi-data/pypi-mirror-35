import sys
import os
import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
import numpy as np
path = os.path.abspath('../')
sys.path.append(path)
from piomart.piomart import EnsemblClient as pio
from piomart.piomart import CountsMatrix

class TestQueries(unittest.TestCase):
    def setUp(self):
        self.test_dict = {"ENSG00000157764": {"source": "ensembl_havana",
                                          "object_type": "Gene",
                                          "logic_name": "ensembl_havana_gene",
                                          "version": 13,
                                          "species": "homo_sapiens",
                                          "description": "B-Raf proto-oncogene, serine/threonine kinase [Source:HGNC Symbol;Acc:HGNC:1097]",
                                          "display_name": "BRAF",
                                          "assembly_name": "GRCh38",
                                          "biotype": "protein_coding",
                                          "end": 140924928,
                                          "seq_region_name": "7",
                                          "db_type": "core",
                                          "strand": -1,
                                          "id": "ENSG00000157764",
                                          "start": 140719327},
                      "ENSG00000248378": {
                          "source": "havana",
                          "object_type": "Gene",
                          "logic_name": "havana",
                          "version": 1,
                          "species": "homo_sapiens",
                          "display_name": "AC022447.1",
                          "assembly_name": "GRCh38",
                          "biotype": "lincRNA",
                          "end": 31744451,
                          "seq_region_name": "5",
                          "db_type": "core",
                          "strand": -1,
                          "id": "ENSG00000248378",
                          "start": 31743988
                      }
        }
        self.mart_export = pd.read_csv("mart_export.txt", sep="\t")
        self.mart_export.rename(columns={"Gene stable ID version":"id","Gene start (bp)":"start"
                                         ,"Gene end (bp)":"end","Gene name":"display_name"
                                         ,"Chromosome/scaffold name":"seq_region_name"},inplace=True)

        self.columns = ["source", "object_type", "logic_name"]

    def test_get_gene_info(self, gene=["ENSG00000157764", "ENSG00000248378"], columns=[]):
        """Test with no columns specified"""

        info_dict = pio().get_gene_info(gene, columns)
        assert self.test_dict == info_dict, "{} does not equal {}".format(self.test_dict, info_dict)

    def test_get_gene_info_get_filter(self, gene=["ENSG00000157764"]):
        """Test get http request with a single gene"""
        #return single dict with only keys of interest
        if "id" not in self.columns:
            self.columns.append(id)

        get_dict = {k: v for k, v in self.test_dict["ENSG00000157764"].items() if k in self.columns}

        info_dict = pio().get_gene_info(gene, self.columns)
        #added id for merging in dataframe so don't forget to remove it
        info_dict.pop("id", None)
        assert get_dict == info_dict, "{} does not equal {}".format(get_dict, info_dict)

    def test_get_gene_info_post_filter(self, gene=["ENSG00000157764", "ENSG00000248378"]):
        """Test post http request with a list of genes"""
        keys = self.test_dict.keys()

        post_dict = {}
        for key in keys:
            post_dict[key] = {k: v for k, v in self.test_dict[key].items() if k in self.columns}

        info_dict = pio().get_gene_info(gene, self.columns)

        #self.columns gets id added to it
        self.columns = ["source", "object_type", "logic_name"]
        #added id for merging in dataframe so don't forget to remove it
        info_dict_keys = info_dict.keys()
        comparison_dict = {}
        for key_info in info_dict_keys:
            comparison_dict[key_info] = {k: v for k, v in info_dict[key_info].items() if k in self.columns}
        assert post_dict == comparison_dict, "{} does not equal {}".format(post_dict, comparison_dict)

    def test_add_to_dataframe(self):

        self.mart_export = self.mart_export.drop("Gene stable ID", axis=1)
        colnames = self.mart_export.columns.tolist()
        self.mart_export.set_index("id", inplace=True)

        #get back dataframe with same values as mart_export
        in_df = CountsMatrix("test_deseq.csv").df
        df = pio().add_to_dataframe(in_df, colnames)

        #returns index of the values the match mart export
        subset_df = df.loc[:, colnames]
        subset_df.set_index("id", inplace=True)
        comparison_df = subset_df.loc[self.mart_export.index.tolist(), :].copy()
        comparison_df["seq_region_name"] = comparison_df["seq_region_name"].astype(np.int64)

        assert_frame_equal(self.mart_export, comparison_df)

    def test_offline_add_to_dataframe(self):
        """testing the offline dataframe function"""

        self.mart_export.set_index("id", inplace=True)
        #no gene id with ver in gtf file
        conver_dict = {"Gene stable ID":"gene_id","Gene start (bp)":"start"
                       ,"Gene end (bp)":"end", "display_name":"gene_name"
                       ,"seq_region_name":"seqname"}
                       #,"Chromosome/scaffold name":"seqname"}
        self.mart_export = self.mart_export.rename(columns=conver_dict)
        colnames = self.mart_export.columns.tolist()
        self.mart_export.loc[:, "gene_id"] = self.mart_export.index.tolist()

        #get back dataframe with same values as mart_export
        in_df = CountsMatrix("test_deseq.csv").df
        func = pio(True, "homo_sapiens.json")
        df = func.add_to_dataframe(in_df, colnames)
        df["id"] = df.loc[:, "gene_id"]
        df.set_index("id", drop=True, inplace=True)

        subset_df = df.loc[:, colnames]
        comparison_df = subset_df.loc[self.mart_export.index.tolist(), :].copy()

        #Sometimes I hate pandas
        self.mart_export.iloc[:, 1] = self.mart_export.iloc[:, 1].astype("int64")
        self.mart_export.iloc[:, 2] = self.mart_export.iloc[:, 2].astype("int64")
        self.mart_export.iloc[:, 4] = self.mart_export.iloc[:, 4].astype(str)

        comparison_df.iloc[:, 1] = comparison_df.iloc[:, 1].astype("int64")
        comparison_df.iloc[:, 2] = comparison_df.iloc[:, 2].astype("int64")
        comparison_df.iloc[:, 4] = comparison_df.iloc[:, 4].astype(str)

        assert_frame_equal(self.mart_export, comparison_df)

    def test_duplicate_index(self):
        #make sure the counts matrix doesn't have duplicate values int it
        with self.assertRaises(ValueError):
            CountsMatrix("duplicate_values.csv", "index")

    def test_offline_add_to_dataframe_no_ids(self):
        """testing the offline dataframe function"""

        mart_df = pd.read_csv("ensembl_no_versions.tsv", sep="\t")
        mart_df.rename(columns={"Gene stable ID":"gene_id", "Gene name":"gene_name"}, inplace=True)
        mart_df["X"] = mart_df.loc[:, "gene_id"]
        mart_df.set_index("X", inplace=True)

        colnames = mart_df.columns.tolist()
        in_df = CountsMatrix("no_version.csv", "X").df
        func = pio(True, "homo_sapiens.json")
        df = func.add_to_dataframe(in_df, colnames)
        comparison_df = df.loc[mart_df.index.tolist(), colnames]
        assert_frame_equal(mart_df, comparison_df)

    def test_no_index_name(self):
        """make sure dataframes have default values"""
        import pandas as pd
        df = CountsMatrix("no_index_name.csv").df
        assert df.index.name == "id_index", "the default index name isn't being added"

    def test_no_inexact(self):
        """Assert that removing versions still produces expected result"""
        import pandas as pd
        #annotated_df = CountsMatrix("no_versions_annotated.csv").df
        annotated_df = CountsMatrix("no_ver_dep_par_annotated.csv").df

        counts = CountsMatrix("inexact_test_df.csv", 0, True).df
        #counts = CountsMatrix("adj_onset_deseq2_results.csv", 0, True).df
        #counts.to_csv("no_versions_inexact.csv", sep=",",index=True)
        func = pio(True, "homo_sapiens.json")
        counts_df = func.add_to_dataframe(counts)

        assert_frame_equal(counts_df, annotated_df)


if __name__ == '__main__':
    unittest.main()
