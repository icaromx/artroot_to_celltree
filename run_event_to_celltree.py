#!/usr/bin/python
import os, sys, glob, shutil

import ROOT
from ROOT import *
def main(f,run):
	f = open(sys.argv[1],'r')
	run = sys.argv[2]
	i = 0
	for line in f:
		rootfile = line[:-1]
		rf = ROOT.TFile.Open(rootfile)
		numevents = rf.Events.GetEntries()
		os.system('python artroot_to_cluster.py ' + rootfile + ' ' + str(numevents))
		if(os.path.exists('celltree_files/') != True):
                	os.system('mkdir celltree_files/')	
		os.system('mv celltree.root celltree_files/celltree_' + run + '_'  + str(i) + '.root')
		if(os.path.exists('finished_data_sp_files/') != True):
                	os.system('mkdir finished_data_sp_files/')	
		os.system('mv data_sp_files/* finished_data_sp_files/')
		if(os.path.exists('finished_result_files/') != True):
                	os.system('mkdir finished_result_files/')	
		os.system('mv result_files/* finished_result_files/')	
		if(os.path.exists('finished_pr_files/') != True):
                	os.system('mkdir finished_pr_files/')	
		os.system('mv pr_files/* finished_pr_files/')	
		i+=1	
def usage():
	print "I need inputs"

if __name__ == "__main__":
	if (len(sys.argv)<=1):
		usage()
	else:
		main(sys.argv[1],sys.argv[2])
