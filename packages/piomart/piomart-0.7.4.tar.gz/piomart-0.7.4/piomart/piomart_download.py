from ftplib import FTP


class GetFiles():

    def __init__(self, species="homo_sapiens", wd='', url="ftp.ensembl.org"):
        self.species = species.lower()
        if not wd:
            self.wd = "pub/current_gtf/"

        else:
            if wd.startswith("release"):
                self.wd = "pub/" + wd + "/gtf/"
            else:
                wd = "release-" + wd
                self.wd = "pub/" + wd + "/gtf/"
        self.url = url

    def download_ftp(self, files=False):
        """downloads current gtf files for that species"""
        conn = FTP(self.url)
        conn.login()

        #species directory
        conn.cwd("".join([self.wd, self.species]))
        species_files = conn.nlst()
        species_dict = {}
        #create dictionary of all files in directory except readme and CHECKSUMS
        for idx,item in enumerate(species_files):
            if item == species_files[-1] or item == species_files[0]:
                pass
            else:
                species_dict[idx-1] = item

        species_dict[len(species_dict)] = "All Files"

        open_file = open('CHECKSUMS', 'wb')
        file_name = "CHECKSUMS"
        conn.retrbinary('RETR ' + file_name, open_file.write)
        open_file.close()

        if files is False:
            #just download the regular gtf.gz file
            file_name = species_dict[len(species_dict) - 2]
            open_file = open(file_name, 'wb')
            conn.retrbinary('RETR ' + file_name, open_file.write)
            conn.quit()
            open_file.close()
            return [file_name]
        else:
            print("\n")
            print("\n")
            print(species_dict)
            print("\n")
            print("\n")
            file_list = []
            done = False
            file_names = []
            while done is not True:
                answer = int(input("enter the number associated with file "))
                if species_dict[answer] == "All Files":
                    species_dict.pop(answer, None)
                    file_list = [_ for _ in species_dict.keys()]
                    break
                else:
                    file_list.append(answer)
                    again = input("Another file y/n ")
                    if again == "y":
                        continue
                    else:
                        done = True

            for val in file_list:
                file_name = species_dict[val]
                file_names.append(file_name)
                open_file = open(file_name, 'wb')
                conn.retrbinary('RETR ' + file_name, open_file.write)
                open_file.close()
            conn.quit()
            return file_names

    def unzip(self, files=False):
        """open all of the gz files and unzip them"""
        import gzip
        if files is False:
            file_list = self.download_ftp()
        else:
            file_list = self.download_ftp(files)
        for files in file_list:
            with gzip.open(files, 'rb') as f:
                file_content = f.read()
                with open(files.strip('.gz'), 'wb') as outfile:
                    outfile.write(file_content)

    def parse_gtf(self, gtffile, filename=""):
        import pandas as pd
        import json
        import warnings

        colnames = ["seqname", "source", "feature"
                    ,"start", "end","score", "strand"
                    ,"frame", "attribute"]

        df = pd.read_csv(gtffile, sep="\t", header=None, names=colnames, dtype=object, comment="#")
        index = df.index.tolist()
        ens_dict = {}
        gene_name_dict = {}

        for val in index:
            values = df.iloc[val, :]
            line = values["attribute"]
            line_strip = line.strip().split(" ")
            stript = [_.split("\t") for _ in line_strip]
            #create list in order key,val key,val based on attributes field
            clean_line = [_[0].strip('"').strip(';').strip('"') for _ in stript]
            dict_1 = dict(zip(clean_line[::2], clean_line[1::2]))
            #gtf file has annotations from multiple sources
            if dict_1["gene_id"] in ens_dict:
                pass
            else:
                for col in colnames:
                    #already parsed attribute column
                    if col == "attribute":
                        pass
                    else:
                        #add info of seqname, source etc to dict
                        dict_1[col] = values[col]
                #ens_dict keys are ensemble ids
                #gene_name_dict keys are gene symbols
                ens_dict[dict_1["gene_id"]] = dict_1
                try:
                    gene_name_dict[dict_1["gene_name"]] = dict_1
                except KeyError:
                    warnings.warn("gene names missing from gtf file")
                    continue

        #takes 92 seconds to do this so save to json
        gtf_json = json.dumps({"gene_id":ens_dict, "gene_name":gene_name_dict})
        #if filename doesn't exist
        if not filename:
            filename = gtffile + ".json"
        with open(filename, 'w') as f:
            f.write(gtf_json)
