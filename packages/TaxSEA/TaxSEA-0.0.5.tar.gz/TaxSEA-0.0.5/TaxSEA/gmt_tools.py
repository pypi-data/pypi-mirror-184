#!/opt/anaconda3/bin/python

import os
import re
import numpy as np
import pandas as pd
import warnings
import pickle

with warnings.catch_warnings():
	warnings.simplefilter("ignore")
	from ete3 import NCBITaxa


# def ncbi_init(): 
ncbi = NCBITaxa()
#     return ncbi



# 	fd.close()



def strip_brackets(s):
	'''Remove brackets from the string'''
	return re.sub("\\[|\\]","",s)

def add_brackets(s):
	'''Add brackets to the first word of each species name'''
	return re.sub("(?:^|(?:[.!?]\s))(\w+)","[\g<0>]",s) 

def ncbi_taxid_from_name_lst(lst):
	# ncbi = NCBITaxa()
	
	lst_stripped = [ strip_brackets(s) for s in lst ] 
	lst_bracketed = [ add_brackets(s) for s in lst ]
	_d = ncbi.get_name_translator(filter(lambda x: x==x, lst_bracketed + lst_stripped))
	name2taxid = { **{ strip_brackets(k):v for k,v in _d.items()}, **{ add_brackets(k):v for k,v in _d.items()} }
	tax_ids = [ int(name2taxid[name][0]) if name in name2taxid.keys() else None for name in lst  ]

	# tax_ids = [ int(name2taxid_td[name]) if name in name2taxid_td.keys() else None for name in lst  ]

	untranslated_names = [ lst[i] for i,e in enumerate(tax_ids) if not e ]

	if len(untranslated_names) > 0:
		print("WARNING: {} of {} taxon names could not be translated, including:".format(len(untranslated_names),len(lst)))
		print(untranslated_names)

	return tax_ids

# def ncbi_taxid_from_name_lst(lst):
# 	ncbi = ncbi_init()
# 	name2taxid = ncbi.get_name_translator(filter(lambda x: x==x, lst))
# 	tax_ids = [ name2taxid[name][0] if name in name2taxid.keys() else np.nan for name in lst  ]
# 	assert len(tax_ids) == len(lst)
# 	return tax_ids

# def ncbi_taxid_from_name_lst(lst):
	# tax_ids = [ int(name2taxid_td[name]) if name in name2taxid_td.keys() else None for name in lst  ]



def ncbi_name_from_taxid_lst(lst):
	# ncbi = ncbi_init()
	taxid2name = ncbi.get_taxid_translator(filter(lambda x: x==x, lst))
	names = [ taxid2name[ix] if ix in taxid2name.keys() else np.nan for ix in lst  ]
	return names


# def ncbi_rank_from_name_lst(lst):
# 		name2taxid = NCBITaxa().get_name_translator(filter(lambda x: x==x, lst))

def ncbi_rank_from_name_lst(lst):
	# ncbi = ncbi_init()
	taxid2rank = ncbi.get_rank(lst)
	ranks = [ taxid2rank[ix] if ix in taxid2rank.keys() else np.nan for ix in lst  ]
	return ranks

def ncbi_parent_from_tax_id(lst, rank):
	# ncbi = ncbi_init()
	lst_dropna = list(filter(lambda x: pd.notna(x), lst)) #[:100]

	taxid2lineage = {
		ix:{v:k for k,v in ncbi.get_rank(ncbi.get_lineage(ix)).items()} for ix in lst_dropna
	}

	taxid2rankid = {
		ix: taxid2lineage[ix][rank] if rank in taxid2lineage[ix].keys() else np.nan for ix in lst_dropna
	}

	parents = [ taxid2rankid[ix] if ix in taxid2rankid.keys() else np.nan for ix in lst ]
	return parents

def collapse_to_sp(val, ranks):
    lst = [x for x in val if ranks.get(x) == 'species' or ranks.get(x) == 'genus' or ranks.get(x) == 'species group']
    subspecies = [x for x in val if ranks.get(x) == 'subspecies' or ranks.get(x) == 'strain']
    lst += list(set(ncbi_parent_from_tax_id(subspecies, 'species')))
    return lst

def get_unique_taxa(d):
    s = pd.Series(d)
    lst = list(s)
    lst = list(set(int(x) for y in lst for x in y))
    return lst


def get_gmt_pickles(DBPATH, level1,level2):

	if level2 not in ['cellular','molecular','biotic','abiotic']:
		raise ValueError("""Please provide a reference group from the following:
			'cellular','molecular','biotic','abiotic'.""")

	fpath = '{}/gmts/{}/{}/'.format(DBPATH, level1, level2)

	gmt_pickles = [ f for f in os.listdir(fpath) if f[-6:]=='pickle']

	return fpath, gmt_pickles


def write_gmt(d, level1, level2, feature, source, gmt_num=1, sp_collapse = False):
	'''Writes GMT to ontological group.'''

	fpath = '../gmts/{}/{}/'.format(level1, level2)
	if not os.path.exists(fpath): os.makedirs(fpath)

	# fname = '{}.{}.gmt'.format(database, feature)
	fname = '{}.{}.gmt'.format(feature, source)

	terms = list(d.keys())
	terms.sort()

	n_associations = [ len(d[key]) for key in d.keys() ]
	if sp_collapse: 
		ncbi = ncbi_init()
		taxa = get_unique_taxa(d)
		ranks = ncbi.get_rank(taxa)
		for key, val in d.items():
			d[key] = collapse_to_sp(list(map(int, val)), ranks)
			#print("{}: {} species".format(key, len(d[key])))
	
	print("Writing GMT with {} features to {}.".format(len(d.keys()), fpath + fname))
	print("GMT number: {}".format(gmt_num))
	print(pd.Series(n_associations, name='number_of_associations').describe())

	# with open(fpath + fname, 'w') as out:
	with open(fpath + fname, 'w') as out: 
		
		for n, term in enumerate(terms, start=1):

			ontology = level1[0] + level2[0]

			ix = '{}-{}-{}'.format(ontology.upper(), source, str(gmt_num) + str(n).zfill(6))
			
			# ix = '{}-{}-{}'.format(source, short_name, str(n).zfill(6))
			tax_ids = list(set([ str(int(s)) for s in d[term] ]))
			out.write('{}\t{}\t{}\n'.format(ix, term, '\t'.join(tax_ids)))

	out.close()


def read_gmt(gmt_fpath):

	# fpath = '../gmts/{}/{}/'.format(level1, level2)
	# fname = '{}.{}.gmt'.format(feature, database)

	with open(gmt_fpath) as f:
		lines = [ line.split('\t') for line in f.read().splitlines() ]
	f.close()

	id2name = {}
	microbe_set_library = {}
	for line in lines:
		id2name[line[0]] = line[1]
		microbe_set_library[line[0]] = list(map(int, list(filter(lambda x: x != '', line[2:]))))

	if len(lines) != len(microbe_set_library):
		print("Index contains duplicate values")
		raise

	return id2name, microbe_set_library


def load_taxdump():
	with open('./name2taxid.obj','rb') as fd:
		name2taxid_td = pickle.load(fd)

def parse_taxdump(fpath):

	df = pd.read_table(fpath,index_col=2,header=None)
	df = df.loc[df[6]!='authority']
	d = df[0].to_dict()

	with open('name2taxid.obj','wb') as out:
		pickle.dump(d, out)



# if __name__ == "__main__":

# 	global name2taxid_td

# 	fd = open('./name2taxid.obj','rb')
# 	name2taxid_td = pickle.load(fd)
# 	fd.close()


# 	ncbi = NCBITaxa()
