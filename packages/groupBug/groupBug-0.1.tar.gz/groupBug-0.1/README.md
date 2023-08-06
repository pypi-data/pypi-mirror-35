[![coverage report](https://gitlab.com/ModernisingMedicalMicrobiology/groupBug/badges/master/coverage.svg)](https://gitlab.com/ModernisingMedicalMicrobiology/groupBug/commits/master)
[![pipeline status](https://gitlab.com/ModernisingMedicalMicrobiology/groupBug/badges/master/pipeline.svg)](https://gitlab.com/ModernisingMedicalMicrobiology/groupBug/commits/master)

# groupBug

Clustering heatmap tool for kraken-style reports. Takes kraken style reports in text file format from eithr Kraken or Centrifuge (use centrifuge-kreport.pl). Produces a clustermap using seaborn of top species (default) using z scores for the heatmap and euclidean centroid clustering for the dendrograms.

This work was inspired by the excellent hclust script available for metaphlan analysis, see here https://bitbucket.org/biobakery/biobakery/wiki/metaphlan2#rst-header-create-a-heatmap-with-hclust2. And Pavian see here, https://github.com/fbreitwieser/pavian.

This work was funded by NIHR Biomedical Research Centre at Oxford University Hospitals NHS Foundation Trust and the University of Oxford.

## Installation 

From github
```
git clone https://gitlab.com/ModernisingMedicalMicrobiology/groupBug
cd groupBug
sudo python3 setup.py install
```


## Usage

Command line options are as follows.
```
usage: groupBug.py [-h] -k KRAKEN_REPORTS [KRAKEN_REPORTS ...] [-d DOMAIN]
                   [-t TAXIDS [TAXIDS ...]] [-sv SAVENAME] [-n TOPNUM]
                   [-suf SUF]

cluster heatmap and information from kraken reports

optional arguments:
  -h, --help            show this help message and exit
  -k KRAKEN_REPORTS [KRAKEN_REPORTS ...], --kraken_reports KRAKEN_REPORTS [KRAKEN_REPORTS ...]
                        list of kraken style report files
  -d DOMAIN, --domain DOMAIN
                        Domain of life to display, bacteria, viruses etc
  -t TAXIDS [TAXIDS ...], --taxids TAXIDS [TAXIDS ...]
                        list of taxids to specifically count
  -sv SAVENAME, --saveName SAVENAME
                        file name to save plot as
  -n TOPNUM, --topNum TOPNUM
                        Number of discrete species to display
  -suf SUF, --suf SUF   suffix to delete from sample name
```

For example, use this command to display the top bacterial species.
```
groupBug.py -k kreports/* 
```

This will prodcuce a chart like this.
![](plots/PJI_ONT_zscores.pdf_bacteria_z_score_columns.png)

The file names are used as sample labels along the x axis. To remove suffixes, use the -suf options like such.

```
groupBug.py -k reports/* -suf _kreport_score_150.txt
```

This will prodcuce a chart like this.
![](plots/PJI_ONT_zscores_shortname.png_bacteria_z_score_columns.png)
