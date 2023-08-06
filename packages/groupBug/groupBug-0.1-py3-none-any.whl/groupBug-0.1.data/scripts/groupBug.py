#!python
import sys
import os
import pandas as pd
from ete3 import NCBITaxa
from argparse import ArgumentParser, SUPPRESS
import copy
ncbi = NCBITaxa()
headers=['percentage','reads','reads_taxon','taxon','taxid','name']

def getSpecies(taxes):
    l=ncbi.get_lineage(taxes)
    r=ncbi.get_rank(l)
    s = ['species', 'species group','species subgroup']
    try:
        species = {'species':i for i in l if r[i] in s}['species']
    except:
        print(taxes, r)
        return 
    taxid2name = ncbi.get_taxid_translator([species])
    return taxid2name[species]

class kreportStats:
    def __init__(self,opts):
        self.domain=opts.domain
        self.saveName = opts.saveName
        self.topNum = opts.topNum
        self.suf = opts.suf
        self.descendants = ncbi.get_descendant_taxa(opts.domain,intermediate_nodes=True)

    def getDomain(self,kr):
        kr=kr
        sample=kr.split('/')[-1]#.rstrip('.fuge.kreport.txt') 
        df = pd.read_csv( kr,  sep='\t', names=headers )
        df['sample_name'] = sample.replace(self.suf,'') 
        domain=df.loc[(df['taxid'].isin(self.descendants)) & ( df['taxon'] == 'S') ]
        #domain=df.loc[(df['taxid'].isin(self.descendants)) & ( df['taxon'] == 'G') ]
        return domain

    def topN(self,df,n=5):
        tn=df.nlargest(n,'reads')
        sampleName=list(df['sample_name'])[0]
        tn.to_csv( '{0}_top_{1}_{2}_species.tsv'.format(sampleName, n, self.domain), sep='\t' )
        return tn

    def makePivot(self):
        df = self.all_samples
        p_all_samples = df.pivot(index='taxid',columns='sample_name',values='reads')

        # filter 
        p_all_samples['Total'] = p_all_samples.sum(axis=1)
        if self.topNum == None:
            self.topNum = 30
        p_all_samples =  p_all_samples.nlargest(self.topNum,'Total')
        p_all_samples.drop(['Total'],inplace=True, axis=1)
        p_all_samples['species'] = p_all_samples.index.map( getSpecies )
        #p_all_samples['species'] = p_all_samples.index.map( getGenus )
        p_all_samples = p_all_samples.fillna(0)
        p_all_samples.to_csv( '{0}_pivot.tsv'.format(self.domain), sep='\t' )
        self.p_all_samples=p_all_samples
 
    def visClutserMap(self):
        if self.saveName != None:
            import matplotlib as mpl
            mpl.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.colors import LogNorm
        import seaborn as sns; sns.set(color_codes=True)
        df=self.p_all_samples
        df=df.drop(['species'],axis=1)
        df = df[df.columns].astype(int)
        df.replace(0,0.1,inplace=True)
    
        ax = sns.clustermap(df,
                    cmap="Blues",
                    metric='euclidean',
                    method='centroid',
                    z_score=1,
                    #vmax=5000,
                    xticklabels='auto',
                    yticklabels=self.p_all_samples['species'],
                    figsize=(12, 8),
                    cbar_kws={'label': 'Z score'})
        plt.gcf().subplots_adjust(bottom=0.20,right=0.75,left=0,top=0.98)

        if self.saveName != None:
            plt.savefig(self.saveName)
        else:
            plt.show()
    
    def processFiles(self, files):
        tables=[]
        for f in files:
            d=self.getDomain(f)
            tables.append(d[['sample_name', 'reads', 'taxid', 'name' ]])
            if self.topNum != None:
                self.topN(d,self.topNum)
    
        all_samples = pd.concat( tables )
        all_samples['name'] = all_samples['name'].str.strip()
    
        all_samples.to_csv( '{0}_all_species.tsv'.format(self.domain), sep='\t' )
    
        all_samples['reads'] = all_samples['reads'].astype(int)
        self.all_samples=all_samples 
        
    def countTaxes(self,taxes):
        df=self.all_samples.loc[(self.all_samples['taxid'].isin(taxes))]
        df.to_csv( '{0}_specific_taxids.tsv'.format(self.domain), sep='\t' )
        df=df.pivot(index='taxid',columns='sample_name',values='reads')
        df['species'] = df.index.map( getSpecies )
        df = df.fillna(0)
        df.to_csv( '{0}_pivot_specific_taxids.tsv'.format(self.domain), sep='\t' )
        return df
        
        
    def run(self,opts):
        self.processFiles(opts.kraken_reports)
        self.makePivot()
        self.visClutserMap()
        if opts.taxids != None:
             self.countTaxes(opts.taxids)
    
    
if __name__ == '__main__':
    parser = ArgumentParser(description='cluster heatmap and information from kraken reports')
    parser.add_argument('-k', '--kraken_reports', required=True, nargs='+',
                             help='list of kraken style report files')
    parser.add_argument('-d', '--domain', required=False, default='bacteria',
                             help='Domain of life to display, bacteria, viruses etc')
    parser.add_argument('-t', '--taxids', required=False,nargs='+',default=None,
                             help='list of taxids to specifically count')
    parser.add_argument('-sv', '--saveName', required=False, default=None,
                             help='file name to save plot as')
    parser.add_argument('-n', '--topNum', required=False, default=None,
                             help='Number of discrete species to display')
    parser.add_argument('-suf', '--suf', required=False, default='',
                             help='suffix to delete from sample name')

    opts, unknown_args = parser.parse_known_args()
    ks=kreportStats(opts)
    ks.run(opts)
