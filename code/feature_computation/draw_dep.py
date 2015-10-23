#!/usr/bin/python
import sys
import re
import string
import os
from Queue import *


def draw_tex (_sDepFile, _sTexFile):
	fdraw = open(_sTexFile,'w')
	fdraw.write("\documentclass[landscape,letterpaper]{article}\n" +\
				"\usepackage[left=5pt,top=5pt,right=5pt]{geometry}\n" +\
				"\usepackage{pgf}\n" +\
				"\usepackage{tikz}\n" +\
				"\usetikzlibrary{positioning,shapes,arrows,automata}\n" +\
				"\\begin{document}\n" +\
				"\\footnotesize\n\n");

	fin  = open(_sDepFile)
	print "processing " + _sDepFile + " ..."

	count   = 0
	gdeps   = []
	words   = []

	num = 1
	for line in fin:
		line = line.strip()
		line = line.replace("\\","")
		line = line.replace("$","\$")
		line = line.replace("#","*")
		line = line.replace("&","and")
		line = line.replace("%","\%")
		line = line.replace("_","-")
		line = line.replace("^","hat")
		
		if num % 4 == 1:
			words = line.split(' ')
				
		if num % 4 == 2:
			tokens = line.split(":");
			tokens[1] = tokens[1].strip()
			gdeps = tokens[1].split(" ")
			if gdeps[0] == '':
				gdeps = []

			fdraw.write ("\\begin{center}\n" +\
						 "\\begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=0.5cm,semithick,scale=1.5]\n")
			fdraw.write ("\\tikzstyle{every state} = [fill=none,draw=gray,text=black,style={rounded rectangle},inner sep=3pt,minimum size=3pt]\n")
			fdraw.write ("\\tikzstyle{every edge} = [draw=blue]\n")

			for i in range(0,len(words)):
				pair = words[i].split(":")[1]
				wt = pair.split("/")
				word = wt[0]
				tag = ""
				if len(wt) > 1:
					tag = wt[1]
					tag = tag.replace('_','-')
				word = word.replace("/","")
				if 0 == i:
					fdraw.write ("\\node[state] (" + str(i) + ") {" + word + "};\n")
				else:
					fdraw.write ("\\node[state] (" + str(i) +\
								 ") [right=of " + str(i-1) + "] {" + word + "};\n")

			for dp in gdeps:
				(iFrom,iTo,sType) = dp.split('\x01')
				fdraw.write ("\\path (" + str(iFrom) + ") edge [bend left] node {" +\
							 sType + "} (" + str(iTo) + ");\n")

			fdraw.write("\end{tikzpicture}\n\end{center}\n")

		num = num + 1

	fdraw.write("\n\end{document}")
