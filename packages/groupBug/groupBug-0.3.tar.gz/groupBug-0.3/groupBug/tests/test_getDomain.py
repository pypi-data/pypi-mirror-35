import unittest
import os,shutil
from groupBug.groupBug import *
from argparse import ArgumentParser, SUPPRESS

modules_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(modules_dir, 'data')
basedir = os.path.join(data_dir, 'reports/')

files = os.listdir( basedir )
files = ['{0}{1}'.format(basedir,i) for i in files]

# args
parser = ArgumentParser(description='cluster heatmap and information from kraken reports')
parser.add_argument('-k', '--kraken_reports', required=False, nargs='+',default=files,
                         help='list of kraken style report files')
parser.add_argument('-d', '--domain', required=False, default='bacteria',
                         help='Domain of life to display, bacteria, viruses etc')
parser.add_argument('-t', '--taxids', required=False,nargs='+',default=None,
                         help='list of taxids to specifically count')
parser.add_argument('-sv', '--saveName', required=False, default='clustermap.pdf',
                         help='file name to save plot as')
parser.add_argument('-n', '--topNum', required=False, default=None,
                         help='Number of discrete species to display')
parser.add_argument('-suf', '--suf', required=False, default='',
                         help='suffix to delete from sample name')
opts, unknown_args = parser.parse_known_args()


class testGetDomain(unittest.TestCase):

    def setUp(self):
        self.ks = kreportStats( opts )

    def testGetDomain(self):
        kr = os.path.join(basedir, '312a_kreport_score_150.txt' )
        print(kr)
        d = self.ks.getDomain( kr )
        print(d.iloc[0]['percentage'])
        assert d.iloc[0]['percentage'] == 1.57

    def test_processFiles(self):
        self.ks.processFiles( files )
        print(len(self.ks.all_samples))
        assert len(self.ks.all_samples) > 1600

    def test_makePivot(self):
        self.ks.processFiles( files )
        self.ks.makePivot()
        print(len(self.ks.p_all_samples))
        assert (len(self.ks.p_all_samples)) == 30

    def test_visClutserMap(self):
        self.ks.processFiles( files )
        self.ks.makePivot()
        self.ks.visClutserMap()

    def test_countTaxes(self):
        self.ks.processFiles( files )
        df = self.ks.countTaxes(['1280'])
        print(df)
        print(df.iloc[0]['229a_kreport_score_150.txt'])
        assert df.iloc[0]['229a_kreport_score_150.txt'] == 872

    def test_topN(self):
        kr = os.path.join(basedir, '312a_kreport_score_150.txt' )
        print(kr)
        d = self.ks.getDomain( kr )
        print( d['reads'] )
        tn = self.ks.topN( d,n=5 )
        print(tn.iloc[0])
        assert tn.iloc[0]['reads'] == 14021

    def tearDown(self):
        try:
            os.unlink('{0}_all_species.tsv'.format(opts.domain))
            os.unlink('{0}_pivot.tsv'.format(opts.domain))
            os.unlink('clustermap.pdf')
            os.unlink('bacteria_pivot_specific_taxids.tsv')
            os.unlink('bacteria_specific_taxids.tsv')
            os.unlink('312a_kreport_score_150.txt_top_5_bacteria_species.tsv')

        except:
            pass

