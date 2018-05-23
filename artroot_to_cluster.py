#!/usr/bin/python
import os, sys, glob, shutil

import ROOT
from ROOT import TFile

def main(filepath, enum):
	filepath = sys.argv[1]
        enum = sys.argv[2]
	os.system("lar -c celltree_uboone_data.fcl " + filepath + " -n " + str(enum))
	os.system("rm test.root")
	if(os.path.exists('data_sp_files/') != True):
		os.system('mkdir data_sp_files/')
	if(os.path.exists('result_files/') != True):
		os.system('mkdir result_files/')
	if(os.path.exists('pr_files/') != True):
		os.system('mkdir pr_files/')
	f = TFile("celltree.root")
	sim = f.Get("Event/Sim")
	events = sim.GetEntries()
        for i in xrange(0,int(events)):
        	os.system('wire-cell-real-data-sp ChannelWireGeometry_v2.txt celltree.root ' + str(i) + ' -t0 -s0')
	new_sp_files = glob.glob('data-sp_*.root')
	if(len(new_sp_files) > 0):
		os.system('mv data-sp_*.root data_sp_files/')
	data_sp_files = glob.glob('data_sp_files/*.root')
	for x in data_sp_files:
                os.system('wire-cell-imaging-lmem ChannelWireGeometry_v2.txt ' + x + ' -s0')
	new_result_files = glob.glob('result_*.root')
	if(len(new_result_files) > 0):
		os.system('mv result_*.root result_files/')
        result_files = glob.glob('result_files/*.root')
	for x in result_files:
		os.system('wire-cell-cluster-icaro ChannelWireGeometry_v2.txt ' + x)
	new_pr_files = glob.glob('pr_*.root')
        if(len(new_pr_files) > 0):
		os.system('mv pr_*.root pr_files/')

        pr_files = glob.glob('pr_files/*.root')
	print("DONE")
"""
	if(os.path.exists('data/') == True):
		os.system('rm -r data/')
		os.system('mkdir data/')
	else:
		os.system('mkdir data/')

	if(os.path.exists('to_upload.zip') == True):
		os.system('rm to_upload.zip')
        
        folder = 0
	for x in pr_files:
		os.system('/uboone/app/users/icaro/work/JSON_cluster_maker/DumpWCDataCluster ' + x + ' T_charge_cluster > cluster.txt')
		run_num = x[x.rfind('/')+4:x.rfind('_')-3]
		ev_num = x[x.rfind('/')+12:x.rfind('.')]
			
		os.system('mkdir data/' + str(folder))
  		os.system('python makeJSON_cluster.py cluster.txt clustering ' + str(run_num) + ' ' + str(ev_num) + ' > ' + str(folder) + '-cluster.json')
                os.system('mv ' + str(folder) + '-cluster.json data/' + str(folder))
		folder += 1

  	os.system('rm cluster.txt')
	os.system('zip -r to_upload.zip data')

	print("DONE")
"""
def usage():
	print "I need inputs"

if __name__ == "__main__":
	if (len(sys.argv)<=1):
		usage()
	else:
		main(sys.argv[1],sys.argv[2])
