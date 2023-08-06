#!/usr/bin/env python
"""piomart

Usage:
  piomart.py info <genes>... [--offline -f FILE]
  piomart.py gtf [options]
  piomart.py json -f FILE [options]
  piomart.py dataframe <dataframe> [--columns=<args>... --offline -f FILE] [options]
  piomart.py -h | --help


Options:
  -h --help                      Display Help Options.
  --version                      Display version.
  -o FILE --output=FILE          Create output file with specifies name
  --columns=<args>...            specify columns to add to dataframe
  -u --unzip                     create unzipped the gz files
  -i  --interactive              Find out which files to download
  -r <INT> --release=<INT>       specify release versiopn
  -s SPECIES --species=SPECIES   specify species to download
  -v --verbose                   full info
  --offline
  -f F
ILE --file=FILE            input file
  --index                        specify index column in dataframe
 --infile

Columns:
  "Columns to specify and what information they contain"
  "seperate with commas IE --columns=source,object_type"
  "specifying "brief" will give gene name, biotype, and chromosome"


  source: ensembl_havana
  object_type: Gene
  logic_name: ensembl_havana_gene
  version: 13
  species: homo_sapiens danio_rerio etc
  description: Description of biotype
  display_name: name of gene
  assembly_name: GRCh38 GRCh37
  biotype: protein_coding
  end: 140924928
  seq_region_name: (chromosome)
  db_type: core comparitive genomics etc
  strand: -1 or 1
  id: ENSG00000157764
  start: 140719327
"""
from docopt import docopt
import pandas as pd
import requests
import sys
import json
from collections import defaultdict
import numpy as np
from .piomart_download import GetFiles


class CountsMatrix():

    def __init__(self, df, index=0):
        import pandas as pd
        self.df = pd.read_csv(
            df, sep=None, engine='python', index_col=index)
        # Make sure that the index column doesn't have duplicate values
        if self.df[self.df.index.duplicated()].shape[0] > 0:
            index = self.df[self.df.index.duplicated()].index.tolist()
            sys.stdout.write(("{}\n").format([_ for _ in index]))
            raise ValueError("Duplicate values in index")


class EnsemblClient():

    def __init__(self, offline=False, json_file="", server='http://rest.ensembl.org', reqs_per_sec=15):
        self.offline = offline
        self.json_file = json_file
        self.server = server
        self.reqs_per_sec = reqs_per_sec
        self.req_count = 0
        self.last_req = 0

    def rest_request(self, ext=None, header=None, data=[]):
        import time

        if header is None:
            headers = {}

        if 'Content-Type' not in header:
            headers["Content-Type"] = "application/json"

        if ext is None:
            raise ValueError

        # check if we need to rate limit ourselves
        if self.req_count >= self.reqs_per_sec:
            delta = time.time() - self.last_req
            if delta < 1:
                time.sleep(1 - delta)
            self.last_req = time.time()
            self.req_count = 0

        if len(data) == 1:
            query = "".join([self.server, ext, data[0], "?"])
            self.r = requests.get(query, headers=header)
            self.req_count += 1

        elif len(data) > 1:
            gene_json = json.dumps({"ids": data})
            headers = {"Content-Type": "application/json", "Accept": "application/json"}
            query = "".join([self.server, ext])
            self.r = requests.post(query, headers=headers, data=gene_json)
            self.req_count += 1

        if not self.r.ok:
            self.r.raise_for_status()
            sys.exit()

            # #Too Many Requests
            # if self.r.status_code == 429:
            #     print("The error code was {}", code)
            #     print(retry = text["Retry-After"])
            # #     retry = self.r['Retry-After']
            # #     time.sleep(float(retry))
            # #     self.r
            # # #Gateway Timeout
            # # if self.r.status_code == 504:
            # #     pass
        else:
            decode = self.r.json()
            return(decode)

    def get_gene_info(self, gene=[], columns=[]):
        """ get information of a single gene or multiple genes
            returns dictionary or multiple dictionaries works with or without version names"""
        headers = {"Content-Type": "application/json"}
        ext = "/lookup/id/"
        #id necessary for merge
        if not columns:
            if len(gene) < 100:
                response = self.rest_request(ext, headers, gene)
                #final_dict = {k:v for k,v in response.items() if k in columns}
                return response
            elif len(gene) >= 1000:
                response = self.rest_request(ext, headers, gene)
                keys = response.keys()
                final_dict = {}
                for key in keys:
                    final_dict[key] = {k: v for k, v in response[key].items() if k in columns}
                return final_dict

        elif 'id' not in columns:
            columns.append('id')
            if len(gene) < 2:
                response = self.rest_request(ext, headers, gene)
                final_dict = {k: v for k, v in response.items() if k in columns}
                return final_dict
            elif len(gene) <= 1000:
                response = self.rest_request(ext, headers, gene)
                keys = response.keys()
                final_dict = {}
                for key in keys:
                    final_dict[key] = {k: v for k, v in response[key].items() if k in columns}
                return final_dict
        else:
            #respect 1000 gene limit
            length_list = len(gene)
            divisor = 2
            # #split list into arrays <= 1000
            while(length_list / divisor > 1000):
                divisor += 1
            gene_array = np.array_split(np.asarray(gene), divisor)
            final_dict = {}
            for array in gene_array:
                response = self.rest_request(ext, headers, array.tolist())
                keys = response.keys()
                for key in keys:
                    final_dict[key] = {k: v for k, v in response[key].items() if k in columns}

            return final_dict

    def gene_conversion(self,gene_list):
        from collections import defaultdict
        import pandas as pd
        with open(self.json_file) as f:
            data = json.load(f)
            info = []
            gene_dict = defaultdict(list)
            for val in gene_list:
                if val.startswith("ENS"):
                    #logic for genes with versions
                    if "." in val:
                        split = val.split(".")[0]
                        try:
                            json_gene_index = data["gene_id"][split]["gene_version"]
                            gene_version = split + "." + json_gene_index
                            #version in json doesn't match output from DE
                            if gene_version != val:
                                for k in data["gene_id"][split].keys():
                                    #append our original gene to make sure we can merge
                                    if k == "gene_id":
                                        gene_dict[k].append(val)
                                    elif k == "gene_name":
                                        gene_dict[k].append(val)
                                    else:
                                        gene_dict[k].append(False)
                            #versions are equal so append all info
                            else:
                                gene_info = data["gene_id"][split]
                                for k, v in gene_info.items():
                                    if k == "gene_id":
                                        #gene_id will contain original list of genes
                                        gene_dict[k].append(val)
                                    else:
                                        gene_dict[k].append(v)
                        #The versionless gene is not in the json file
                        except KeyError as e:
                            cols = ["gene_id", "gene_version"
                                    , "gene_name", "gene_source"
                                    , "gene_biotype", "seqname"
                                    , "source", "feature"
                                    , "start", "end"
                                    , "score", "strand", "frame"]

                            #usually means deprecation
                            for key in cols:
                                if key == "gene_id":
                                    gene_dict[key].append(val)
                                elif key == "gene_name":
                                    gene_dict[key].append(val + "_d")
                                else:
                                    gene_dict[key].append("deprecated")
                    else:
                        try:
                            gene_info = data["gene_id"][val]
                            for k,v in gene_info.items():
                                if k == "gene_id":
                                    #gene_id will contain original list of genes
                                    gene_dict[k].append(val)
                                else:
                                    gene_dict[k].append(v)
                        except KeyError as e:
                            cols = ["gene_id", "gene_version"
                                    , "gene_name", "gene_source"
                                    , "gene_biotype", "seqname"
                                    , "source", "feature"
                                    , "start", "end"
                                    , "score", "strand", "frame"]
                            for key in cols:
                                if key == "gene_id":
                                    gene_dict[key].append(val)
                                elif key == "gene_name":
                                    gene_dict[key].append(val + "_d")
                                else:
                                    gene_dict[key].append("deprecated")
        return pd.DataFrame(data=gene_dict)

    def quick_info(self, gene=[]):
        """ writes gene info to stdout"""
        if self.offline is True:
            df = self.gene_conversion(gene)
            index = df.index.values
            for val in index:
                sys.stdout.write("\n")
                if df.iloc[val,0] is False:
                    sys.stdout.write("{} does not have a record with matching version # in json file".format(df.loc[val, "gene_id"]))
                else:
                    row = df.iloc[val, :]
                    sys.stdout.write("{}\n".format(row))

        else:
            sys.stdout.write("\n")
            #bug in quickinfo for single gene
            gene_info = self.get_gene_info(gene)
            if len(gene) < 2:
                for key, val in gene_info.items():
                    if key == "display_name":
                        key = "Gene Name"
                    elif key == "seq_region_name":
                        key = "Chromosome"
                    out = "{}= {} \n".format(key,val)
                    sys.stdout.write(out)
            else:
                for key, val in gene_info.items():
                    sys.stdout.write("\n")
                    sys.stdout.write(key + "\n")
                    for k,v in val.items():
                        if k == "display_name":
                            k = "Gene Name"
                        elif k == "seq_region_name":
                            k = "Chromosome"
                        out = "{}= {} \n".format(k,v)
                        sys.stdout.write(out)

    def add_to_dataframe(self, dataframe, columns=[]):
        """ Return a dataframe with gene info appended"""
        counts = dataframe
        #so I can get the index back after the merge
        index_name = counts.index.name
        orig_columns = counts.columns.tolist()
        gene_list = counts.index.tolist()
        counts["ensembl_ids"] = gene_list
        total_columns = orig_columns + columns
        counts.reset_index(inplace=True, drop=False)
        if self.offline is True:
            json_df = self.gene_conversion(gene_list)
            # we don't want to lose the index in the merge
            merge_df = pd.merge(counts, json_df, left_on=["ensembl_ids"], right_on="gene_id", how="outer")
            merge_df.set_index(index_name, inplace=True)

        else:
            gene_dict = self.get_gene_info(counts["ensembl_ids"].tolist(), columns)
            ensembl_dict = defaultdict(list)
            #iterate through nested dictionary returned from response
            #and create a pandas df out of it
            for key, val in gene_dict.items():
                for k, v in val.items():
                    ensembl_dict[k].append(v)

            ensembl_df = pd.DataFrame(data=ensembl_dict)
            #do a full outer join and keep information from both dataframes
            merge_df = pd.merge(counts, ensembl_df, left_on=["ensembl_ids"], right_on="id", how="outer")
            merge_df.set_index(index_name, inplace=True)
            #id column is silently added for merge in get gene info function
            # if they don't want the id column this will remove it
        if not columns:
            return merge_df
        else:
            # merge_df.loc[:,"gene_id"] = merge_df.loc[:,"ensembl_ids"]
            return merge_df.loc[:, total_columns]

def main(argv=sys.argv):
    args = docopt(__doc__, version='piomart 0.7.4')
    if args["info"]:
        if len(args["<genes>"]) == 1:
            import os
            if os.path.isfile(args["<genes>"][0]) is True:
                gene_list = []
                with open(args["<genes>"][0], "r") as f:
                    for line in f.readlines():
                        gene_list.append(line.strip("\n"))
            else:
                gene_list = args["<genes>"]
        else:
            gene_list = args["<genes>"]

        if args["--offline"]:
            EnsemblClient(True, args["--file"]).quick_info(gene_list)
        else:
            EnsemblClient().quick_info(gene_list)

    if args["dataframe"]:
        if args["--index"]:
            try:
                index_col = int(args["--index"])
            except ValueError as e:
                index_col = int(args["--index"])
            df = CountsMatrix(args["<dataframe>"], index=index_col).df
        else:
            df = CountsMatrix(args["<dataframe>"]).df
        if args["--offline"]:
            func = EnsemblClient(True, args["--file"])
            if args["--columns"]:
                column_list = "".join(args["--columns"]).split(",")
                df = func.add_to_dataframe(df, column_list)
            else:
                df = func.add_to_dataframe(df)
        else:
            if args["--columns"]:
                column_list = "".join(args["--columns"]).split(",")
                df = EnsemblClient().add_to_dataframe(df, column_list)
            else:
                df = EnsemblClient().add_to_dataframe(df)

        if args["--output"]:
            df.to_csv(args["--output"], sep=",", index=True)
        else:
            print(df)

    if args["gtf"]:
        if args["--species"]:
            args["--species"] = args["--species"].lower()
            if args["--release"]:
                func = GetFiles(args["--species"], args["--release"])
                if args["--unzip"]:
                    if args["-i"]:
                        func.unzip(True)
                    else:
                        func.unzip()
                else:
                    if args["-i"]:
                        func.download_ftp(True)
                    else:
                        func.download_ftp()
            else:
                func = GetFiles(args["--species"])
                if args["--unzip"]:
                    if args["-i"]:
                        func.unzip(True)
                    else:
                        func.unzip()
                else:
                    if args["-i"]:
                        func.download_ftp(True)
                    else:
                        func.download_ftp()

    if args["json"]:
        if args["--output"]:
            filename = args["--output"]
            GetFiles().parse_gtf(args["--file"], filename)
        else:
            GetFiles().parse_gtf(args["--file"])


if __name__ == '__main__':
    main()
