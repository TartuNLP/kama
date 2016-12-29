#!/usr/bin/env python3
"""
Script for manual inspection of translation outputs
"""

import sys
import argparse

def shapeLabels(args):
	if args.labels == None:
		args.labels = ['Source'] if args.no_ref else ['Source', 'Reference']
	
	i = 1
	while(len(args.labels) < len(args.translation) + 1):
		args.labels.append('Hypothesis-' + str(i))
		i += 1

def prepareArgs():
	"""
	Parse the command-line arguments
	"""
	parser = argparse.ArgumentParser(description="A script for manual inspection of translation hypotheses, displays the source text and hypothesis/reference translations neatly grouped together. For maximum effect use with 'less'.")
	
	parser.add_argument('-l', '--labels', metavar='LABEL', type=str, nargs='+', default=None, help="The labels of each sentence, defaulting to ['Source', 'Reference']. If there are less labels than there are translations, the missing labels will be generated as 'Hypothesis-1', 'Hypothesis-2', etc.")
	parser.add_argument('-n', '--no-ref', action='store_const', default=False, const=True, help="If you don't have a reference translation, this flag will skip the 'Reference' label in the default label list.")
	parser.add_argument('source', type=argparse.FileType('r'), help="The source text to be displayed first.")
	parser.add_argument('translation', type=argparse.FileType('r'), nargs='+', help="One or more translations to be displayed after the source: reference/hypotheses/etc.")

	args = parser.parse_args()
	
	shapeLabels(args)
	
	return args

def display(fileHandles, labels):
	"""
	Display the lines of given files together with labels, prettily
	"""
	idx = 1
	for lines in zip(*fileHandles):
		print("Sentence {0}".format(idx))
		
		for label, line in zip(labels, lines):
			print("{0:20} {1}".format(label + ":", line.rstrip()))
		
		print("")
		
		idx += 1

if __name__ == '__main__':
	args = prepareArgs()
	
	try:
		display([args.source] + args.translation, args.labels)
	except BrokenPipeError:
		pass
