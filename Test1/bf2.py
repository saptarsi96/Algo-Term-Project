#!/usr/bin/python
# -*- coding: utf-8 -*-
from bloomfilter import BloomFilter
from random import shuffle
from bitarray import bitarray
import csv
import time

class MultiBF:
	
	def __init__(self, layers, totalitems):
		self.bloomfilters = []
		self.totalitems = totalitems
		self.layers = layers
		for i in range(layers):
			self.bloomfilters.append(BloomFilter(totalitems,0.05))
		self.hash_count = self.bloomfilters[0].hash_count
		self.size =  self.bloomfilters[0].size
		self.bit_array = bitarray(self.size)
		self.bit_array.setall(0)
	
	def addLayers(self,newcount):
		if newcount < self.layers:
			return
		for i in range(newcount - self.layers):
			self.bloomfilters.append(BloomFilter(self.totalitems,0.05))
		self.layers = newcount
		#print("update the total number of layers to:",self.layers)
	
	def add(self,query):
		query = query.replace("https://","")
		query = query.replace("http://","")
		query = query.split("/")
		if len(query) > self.layers:
			#print("adding more layers")
			self.addLayers(len(query))	
		laddr = [0]*self.hash_count
		for i in range(len(query)):
			digests = self.bloomfilters[i].add(query[i])
			for i in range(self.hash_count):
				laddr[i] = laddr[i]^digests[i]
		for i in range(self.hash_count):
			self.bit_array[laddr[i]%self.size]  = 1
			
	def check(self,query):
		query = query.replace("https://","")
		query = query.replace("http://","")
		query = query.split("/")
		if len(query) > self.layers:
			return False
		laddr = [0]*self.hash_count
		for i in range(len(query)):
			if self.bloomfilters[i].check(query[i]) == False:
				return False
			digests = self.bloomfilters[i].getDigests(query[i])
			for i in range(self.hash_count):
				laddr[i] = laddr[i]^digests[i]
		for i in range(self.hash_count):
			if self.bit_array[laddr[i]%self.size]  == 0:
				return False
		return True
