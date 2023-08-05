# -*- coding: utf-8 -*-

__version__ = "0.0.4"

import os
import sys
import pickle
import numpy as np
import pandas as pd
import argparse

from .gmt_tools import *

from matplotlib import gridspec
import matplotlib.pyplot as plt
from scipy.stats import fisher_exact
from statsmodels.stats.multitest import multipletests, fdrcorrection
from datetime import datetime

import time

with warnings.catch_warnings():
	warnings.simplefilter("ignore")
	from ete3 import NCBITaxa

# warnings.simplefilter("ignore")

os.environ["PYTHONWARNINGS"] = "default"

DBPATH = os.environ.get('TAXSEA_DB')
# except: DBPATH = './gmts/'
# DBPATH = '/Users/dohlman/Documents/MSEA_project/TaxSEA-database'


level1_dict = dict(zip(
	# ['phenotypic','genotypic','biotic','abiotic'],
	['cellular','molecular','biotic','abiotic'],
	['intrinsic','intrinsic','extrinsic','extrinsic']
))

CONTINUOUS_COL_ORDER = [
	'term','feature','source',
	'overlap','ES','p_value','q_value',
	'leading_edge_taxnames','leading_edge_taxids'
]

DISCRETE_COL_ORDER = [
	'term','feature','database','level2','level1',
	'odds_ratio','fisher_p','fisher_fdr','length'
]

class EnrichmentResult:
	def __init__(self,feature,source,level1,level2,reference_set_library,enrichment_scores):
		self.feature = feature
		self.source = source
		self.level1 = level1
		self.level2 = level2
		self.reference_set_library = reference_set_library
		self.enrichment_scores = enrichment_scores

	# def get_database(self):
	#     return self.database
	# def get_traits(self):
	# return list(enrichment_scores.keys())

	def index(self):
		return list(self.reference_set_library.keys())

	def get_term(self, ix):
		return self.enrichment_scores[ix].term

	def ES(self, ix):
		return self.enrichment_scores[ix].ES

	def ES_arg(self, ix):
		return self.enrichment_scores[ix].ES_arg

	def RES(self, ix):
		return self.enrichment_scores[ix].RES

	def tag(self, ix):
		return self.enrichment_scores[ix].tag


	def correct_multiple_tests(self):

		p_values = [ self.enrichment_scores[ix].p_value if self.enrichment_scores[ix].p_value else 1 for ix in self.index() ]

		q_values = dict(zip(self.index(), fdrcorrection(p_values)[1]))

		for ix in self.index():
			self.enrichment_scores[ix].q_value = q_values[ix]


	def get_table(self):

		df = pd.DataFrame([[
			self.enrichment_scores[ix].term,
			self.feature,
			self.source,
			self.enrichment_scores[ix].ES,
			self.enrichment_scores[ix].p_value,
			self.enrichment_scores[ix].overlap,
			# ','.join(self.enrichment_scores[ix].leading_edge),
			self.enrichment_scores[ix].leading_edge

			# ','.join(ncbi_taxid_from_name_lst(self.enrichment_scores[ix].leading_edge)),
		] for ix in self.index()],
			index=self.index(),
			columns=['term','feature','source','ES','p_value','overlap','leading_edge_taxids'] #,'leading_edge_taxnames']
		)
		df.index.name = 'term_id'

		df['leading_edge_taxnames'] = [
			','.join(ncbi_name_from_taxid_lst(lst)) if type(lst)==list else None for lst in df.leading_edge_taxids
		]

		df['leading_edge_taxids'] = [
			','.join([str(x) for x in lst]) if type(lst)==list else None for lst in df.leading_edge_taxids
		]

		return df


class EnrichmentScore:
	def __init__(self, term_id, term): #, ES, ES_arg, RES, tag, pvalue):
		self.term_id = term_id
		self.term = term
		self.ES = None
		self.ES_arg = None
		self.RES = None
		self.tag = None
		self.p_value = None
		self.q_value = None
		self.leading_edge = None
		self.overlap = None

	def compute_enrichment_path(self, query, reference_set, p=1):

		# Get set sizes
		N = len(query)
		N_h = len(reference_set)
		N_m = N - N_h
		    
		# Indicator (1 if in query, else 0)
		tag = np.array((query.index.isin(reference_set)).astype(int))

		# Weight each species by log2FC (default p = 1)
		corr = np.array(abs(query['change']**p))

		# Normalization parameters for step size
		sum_corr_tag = sum(corr[tag==1])
		norm_tag = 1/sum_corr_tag
		norm_no_tag = 1/N_m

		# Compute walk using cumulative sum
		RES = ((tag * corr * norm_tag) - ((1 - tag) * norm_no_tag)).cumsum()

		RES = [0.0] + list(RES)
		min_RES = np.min(RES)
		max_RES = np.max(RES)

		# Return absolute max
		if max_RES > abs(min_RES):
		    ES = max_RES
		    ES_arg = np.argmax(RES)
		else:
		    ES = min_RES
		    ES_arg = np.argmin(RES)
		    
		# return ES, ES_arg, RES, tag
		self.ES = ES
		self.ES_arg = ES_arg
		self.RES = RES
		self.tag = tag
		self.overlap = sum(tag)

		return self

	def compute_pvalue(self, query, n_items, num_permutations=1000, pnorm=1):

		monte_carlo = np.array([
			self.compute_enrichment_path(query, np.random.choice(query.index, n_items), p=pnorm).ES
			for n in range(num_permutations)
		])

		self.p_value = sum(abs(np.array(monte_carlo)) > abs(self.ES))/float(num_permutations)
		return self

	def compute_leading_edge(self, query):

		ix_tag = query.loc[self.tag==1].index.values

		if self.ES > 0:
		    ix_edge = query.iloc[:self.ES_arg].index.values
		elif self.ES < 0:
		    ix_edge = query.iloc[self.ES_arg:].index.values

		ix_edge = np.intersect1d(ix_tag, ix_edge).astype(int)

		self.leading_edge = list(ix_edge)
		return self


	def get_figure(self,query):

		ntaxa = len(query)
		pad = 0.01*ntaxa
		    
		fig = plt.figure(figsize=(5,4))

		gs = gridspec.GridSpec(3, 1, height_ratios=[3, 1, 2]) 
		gs.update(hspace=0)

		# Enrichment score path
		ax = plt.subplot(gs[0])

		plt.plot(range(len(self.RES)),self.RES, color='red')
		plt.plot([0, len(self.RES)], [0, 0], color='gray', zorder=-1)
		ax.set_xticklabels([])

		plt.title(self.term)
		plt.ylabel('Enrichment Score')
		plt.xlim(-pad, ntaxa + pad)

		# Overlap / tags
		ax = plt.subplot(gs[1])


		for m,t in enumerate(self.tag):
			if t != 1: continue
			# plt.plot([m,m],[0,2],color='black')
			plt.plot([m+1,m+1],[0,2],color='black')

		plt.xlim(-pad, ntaxa + pad)
		ax.set(xticks=[], yticks=[], xticklabels=[], yticklabels=[])
		plt.ylim(0, 1)
		plt.ylabel('Hits')

		# Differential abundance
		ax = plt.subplot(gs[2])     

		y = query.values.flatten()
		ax.fill_between(range(ntaxa), 0, y, color='gray')
		plt.xlim(-pad, ntaxa + pad)
		# plt.yticks([-1,0,1,2])
		plt.ylabel('Log2FC')

		plt.tight_layout()

		return fig


	def get_table(self, query):

		df = pd.DataFrame(query)

		df['tag'] = self.tag
		df['running_enrichment_score'] = self.RES[1:]
		df['name'] = ncbi_name_from_taxid_lst(query.index)

		return df



def search_reference_continuous(query, reference_set_library, min_overlap=5, num_permutations=1000, pnorm=1):

	# id2name, reference_set_library = get_microbe_set_library(database, gmt_fname)

	n = 0
	enrichment_scores = {}
	# enrichment_path = {}

	for term_id in reference_set_library.keys():

		reference_set = reference_set_library[term_id]
		nrecords = len(reference_set)

		# if nrecords < min_overlap:
		# 	pass
		# 	enrichment_scores[trait] = EnrichmentScore(0, None, None, None)
		# 	continue
			
		reference_set = np.intersect1d(query.index.values, reference_set)

		ES_obj = EnrichmentScore(term_id, terms_dict.loc[term_id,'term'])

		# print(ES_obj)

		if len(reference_set) < min_overlap:

			enrichment_scores[term_id] = ES_obj

		else: 
			n += 1

			ES_obj.compute_enrichment_path(query, reference_set, p=pnorm)
			ES_obj.compute_pvalue(query, len(reference_set), num_permutations=num_permutations, pnorm=pnorm)
			ES_obj.compute_leading_edge(query)

			enrichment_scores[term_id] = ES_obj

	return enrichment_scores


def search_reference_discrete(query, background, reference_set_library, min_overlap=1):

	query = set(query).intersection(set(background))

	trait_ids = reference_set_library.keys()

	result = pd.DataFrame(index=trait_ids,columns=['odds_ratio','fisher_p'])

	for trait in trait_ids:

		reference_set = reference_set_library[trait]
		reference_set = set(reference_set).intersection(set(background))

		if len(reference_set) < min_overlap:
			# result[trait] = 1.0
			result.loc[trait] = [np.nan, 1.0]
			continue

		a = len(set(query).intersection(set(reference_set)))
		b = len(set(query).difference(set(reference_set)))
		c = len(set(reference_set).difference(set(query)))
		d = len(background) - len(query) - len(reference_set) + a

		ctg = [[a,b],[c,d]]

		OR,p = fisher_exact(ctg,alternative='greater')

		result.loc[trait] = [OR, p]

	result['fisher_fdr'] = fdrcorrection(result.fisher_p)[1]
	result = result.join(terms_dict)

	return result


def get_microbe_set_library(pickle_fpath):

	with open(pickle_fpath, 'rb') as handle:
	    msl = pickle.load(handle)

	return msl


def convert_to_ncbi_taxid(lst, fmt):

	if fmt == 'name':
		# tax_ids = ncbi_taxid_from_name_lst(lst)
		return ncbi_taxid_from_name_lst(lst)
	elif fmt == 'taxonomy':
		# lst = ?
		return ncbi_taxid_from_name_lst(lst)
	elif fmt == 'tax_id':
		return lst

	else:
		raise ValueError('Did not receive a valid taxa format.')


def get_reference_set_library(gmt_fpath, gmt_fname):

	with open(gmt_fpath + gmt_fname, 'rb') as handle:
	    msl = pickle.load(handle)

	return msl


def make_output_path(output_path):

	if not output_path:
		ts_str = int(datetime.timestamp(datetime.now()))
		output_path = './results/TaxSEA_{}'.format(ts_str)
		print("No output path provided, writing to:")
		print(output_path)

	if not os.path.exists(output_path):
		os.makedirs(output_path)

	print("Output directory: {}...".format(output_path))
	return output_path


def get_query(query_path, fmt, mode):
	if not os.path.exists(query_path):
		raise ValueError('ERROR: Path to a query file must be provided.')
	if mode in ['continuous','plot']:
		query = pd.read_csv(query_path,index_col=0,header=None)
		query.index = convert_to_ncbi_taxid(query.index, fmt=fmt)
		query.columns = ['change']
		query = query.sort_values('change',ascending=False)
	elif mode == 'discrete':
		with open(query_path,'r') as f: query = f.read().splitlines()
	return query

def get_background(background_path,fmt,mode):
	if mode in ['continuous','plot']: return None
	if not os.path.exists(background_path):
		raise ValueError('ERROR: Path to a background file must be provided.')
	with open(background_path,'r') as f: background = f.read().splitlines()
	background = convert_to_ncbi_taxid(background, fmt=fmt)
	return background


def run_plot_TaxSEA(query,term_id,pnorm=1):

	level1,level2 = terms_dict.loc[term_id,['level1','level2']]
	gmt_fname = terms_dict.loc[term_id,'gmt'].replace('.gmt','.pickle')
	gmt_fpath = '{}/gmts/{}/{}/'.format(DBPATH,level1,level2)

	reference_set_library = get_reference_set_library(gmt_fpath, gmt_fname)
	reference_set = reference_set_library[term_id]
	reference_set = np.intersect1d(query.index.values, reference_set)

	ES_obj = EnrichmentScore(term_id, terms_dict.loc[term_id,'term'])

	if dry_run: exit()

	ES_obj.compute_enrichment_path(query, reference_set, p=pnorm)

	fig = ES_obj.get_figure(query)
	table = ES_obj.get_table(query)

	return fig, table



def run_discrete_TaxSEA(query, background):

	# query = get_query(query_path,'discrete')
	# background = get_background(background_path)

	enrichment_tables = []

	for gmt_fname in gmt_pickles:
		reference_set_library = get_reference_set_library(gmt_fpath, gmt_fname)

		if dry_run: continue
		result = search_reference_discrete(query, background, reference_set_library)
		enrichment_tables.append(result)

	if dry_run: exit()
	df_result = pd.concat(enrichment_tables)
	df_result = df_result[DISCRETE_COL_ORDER]

	return df_result



def run_continuous_TaxSEA(query, num_permutations=1000, pnorm=1):

	# query = get_query(query_path,'continuous')

	enrichment_results = []
	enrichment_tables = []

	for gmt_fname in gmt_pickles:

		feature, source, _ = gmt_fname.split('.')

		print("Analyzing {} ({})".format(feature.replace('_',' ').title(),source))

		reference_set_library = get_reference_set_library(gmt_fpath, gmt_fname)

		if dry_run: continue

		enrichment_scores = search_reference_continuous(
			query=query,
			reference_set_library=reference_set_library,
			num_permutations=num_permutations,
			pnorm=pnorm
		)

		ER_obj = EnrichmentResult(
			feature,
			source,
			level1,
			level2,
			reference_set_library,
			enrichment_scores,
		)

		ER_obj.correct_multiple_tests()

		enrichment_results.append(ER_obj)

		df = ER_obj.get_table()
		df['q_value'] = multipletests(df.p_value.fillna(1))[1]
		# print(df.sort_values('p_value')[['term','ES','p_value','q_value','overlap']].head().transpose())

		enrichment_tables.append(df)

		if plot_significant: # and not no_plot:
			ix_plot = df.index[df.p_value < 0.05]

			for ix in ix_plot:

				fig = ER_obj.enrichment_scores[ix].get_figure(query)
				fpath = '{}/{}.{}'.format(output_path, ix, plot_fmt)
				fig.savefig(fpath, bbox_inches='tight')

	if dry_run: exit()
	df_result = pd.concat(enrichment_tables)
	df_result = df_result[CONTINUOUS_COL_ORDER]

	return df_result


def create_parser():

	parser = argparse.ArgumentParser(
		description="""Performs TaxSEA analysis.""")

	parser.add_argument('-q','--query', nargs='?', required=True,
		help="""Path to a query set to compute TaxSEA scores. If mode is continuous,
		a csv with taxa in rows and association statistics. If mode is discrete,
		a list of taxa.
		""")

	parser.add_argument('-o','--output-path', nargs='?', required=False,
		help="""Where to output the results.
		""")

	parser.add_argument('-f','--format', nargs='?', required=False,
		default="name",
		help="""Format of taxa identifiers. Options include
		species name ("name") [DEFAULT], NCBI taxon id ("tax_id"),
		or taxonomy ("taxonomy").
		"""
		)

	parser.add_argument('-r','--reference', nargs='?', required=False,
		help="""Reference group to search against (phenotypic, genotypic,
		biotic, abiotic).""")

	parser.add_argument('-m','--mode', nargs='?', required=True,
		# default="continuous",
		help="""Mode to perform enrichment analysis (continuous/discrete/plot).
		"""
		)

	parser.add_argument('-b','--background', nargs='?', required=False,
		help="""Background to use if mode is "discrete"."""
		)

	parser.add_argument('-p','--plot-significant', action='store_true',required=False,
		default=False,
		help="""Create enrichment plots for significant results.""")

	parser.add_argument('-t','--plot-format', nargs='?', required=False,
		default='png',
		help="""Create enrichment plots for significant results.""")

	parser.add_argument('-n','--no-plot', action='store_true',required=False,
		default=False,
		help="""TCGA experimental strategy (eg. WGS)""")

	parser.add_argument('-s','--seed',  nargs='?', required=False,
		default=1,
		help="""TCGA experimental strategy (eg. WGS)""")


	parser.add_argument('-i','--term-id',  nargs='?', required=False,
		default=1,
		help="""Term ID to generate an enrichment plot for (continuous only).""")


	parser.add_argument('-d','--dry-run',  action='store_true', required=False,
		default=False,
		help="""Test parameter set without running.""")


	# parser.add_argument('-m','--min-clipped-read-length', nargs='?', required=True,
	# 	help="""Minimum clipped read length given to pathseq.sh""")
	# parser.add_argument('-s','--statistic', nargs='?',default='unambiguous',
	# 	help="""Statistic to acquire from pathseq output. Options include
	# 	"unambiguous" (default), "score", "reads".""")
	# parser.add_argument('-d','--domain', nargs='?',default='bacteria',
	# 	help="""Domain or kingdom of interest. Options include:
	# 	"bacteria" (default), "archaea", "fungi", "viruses".""")

	return parser


def get_terms_dict():

	if not DBPATH:
		raise ValueError("""Please export the $TAXSEA_DB path. For example,
			export TAXSEA_DB="/path/to/taxsea/database/\"""")

	fname = '{}/gmts/terms_dictionary.txt'.format(DBPATH)

	print("TaxSEA database path: {}".format(DBPATH))

	if not os.path.exists(fname):
		raise ValueError("""No terms dictionary found. Make sure the TaxSEA database
			is installed and that terms_dictionary.txt exists.""")

	terms_dict = pd.read_table(fname,index_col=0)
	return terms_dict




#if __name__ == "__main__":

def main():
	print("Using TaxSEA version %s." % __version__)
        
	parser = create_parser()
	args = parser.parse_args()
	d = vars(args)
	
	print(d)

	global mode
	global dry_run
	global level1, level2
	global plot_significant

	query_path = d['query']
	query_format = d['format']
	background_path = d['background']
	level2 = d['reference']
	mode = d['mode']
	output_path = d['output_path']
	pnorm = 1
	num_permutations = 1000
	random_seed = d['seed']
	plot_significant = d['plot_significant']
	plot_fmt = d['plot_format']
	term_id = d['term_id']
	dry_run = d['dry_run']

	# background_format = query_format.copy()
	# no_plot = d['no_plot']

	global terms_dict
	terms_dict = get_terms_dict()

	np.random.seed(random_seed)

	output_path = make_output_path(output_path)

	print("Query path: {}".format(query_path))
	print("Query format: {}".format(query_format))
	print("TaxSEA reference: {}".format(level2))
	print("TaxSEA mode:",mode)

	query = get_query(query_path,query_format,mode)
	background = get_background(background_path,fmt=query_format,mode=mode)

	if mode == 'plot':
		fig, table = run_plot_TaxSEA(query, term_id)
		fpath = '{}/{}.{}'.format(output_path, term_id, plot_fmt)
		fig.savefig(fpath, bbox_inches='tight')

		fpath = '{}/{}.txt'.format(output_path, term_id)
		table.to_csv(fpath, sep='\t')

	if not level2:
		print("Please provide a reference")
		raise Exception("Please provide a reference set (-r/--reference)")

	level1 = level1_dict[level2]


	global gmt_fpath, gmt_pickles
	gmt_fpath, gmt_pickles = get_gmt_pickles(DBPATH, level1, level2)


	if mode == 'continuous':
		df_result = run_continuous_TaxSEA(
			query,
			num_permutations=num_permutations,
			pnorm=pnorm)
		df_result.to_csv('{}/TaxSEA.{}.continuous.txt'.format(output_path, level2),sep='\t')

	elif mode == 'discrete':
		df_result = run_discrete_TaxSEA(query, background)
		df_result.to_csv('{}/TaxSEA.{}.discrete.txt'.format(output_path, level2),sep='\t')\




