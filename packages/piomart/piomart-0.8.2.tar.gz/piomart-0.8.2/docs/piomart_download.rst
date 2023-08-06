``gtf`` - Downloading gtf files
================================

Piomart supports the downloading of gtf files from the ensembl database.
A common usecase is downloading the Homo_sapiens.GRCh38.93.gtf.gz from ensembl.
This can be done by specifying

  python piomart.py gtf --species homo_sapiens

  python piomart.py gtf --species homo_sapiens --release release-93 -iu

The above command is a more complex use case. here we specify the specif release we want for our gtf file.
-u tells piomart to unzip the resulting .gz file that is downloaded. -i is an interactive feature. Some analyses require a special version of the gtf. abinitio, chr, chr_patch_hapl_scaff, etc. -i will present youwith all the files in the gtf ftp directory for your species. You can download all of them, or pick (one at a time) which files you would like to download 


{0: 'Homo_sapiens.GRCh38.93.abinitio.gtf.gz', 1: 'Homo_sapiens.GRCh38.93.chr.gtf.gz', 2: 'Homo_sapiens.GRCh38.93.chr_patch_hapl_scaff.gtf.gz', 3: 'Homo_sapiens.GRCh38.93.gtf.gz', 4: 'All Files'}
