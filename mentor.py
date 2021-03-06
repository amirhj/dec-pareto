from functions import Functions
from random import choice
import sys, os, json
from datetime import datetime
import numpy as np
import matplotlib.cm as cm
from pareto import get_pareto_frontier_by_point

class Mentor:
	def __init__(self, agents, fg, ms, opt):
		self.agents = agents
		self.fg = fg
		self.ms = ms
		self.opt = opt

		self.convergenc_count = 0

		self.path_log = []
		self.pareto_frontier = []

	def initialize(self):
		self.ms.load(self.agents)


	def run(self):
		# initalizing starting point for agnets
		initial_value_indecies = {a:choice(range(self.fg.variables[a].domain_size)) for a in self.fg.variables}
		for a in self.agents:
			self.agents[a].set_neighbours_values(initial_value_indecies)

		value_indecies = {k:initial_value_indecies[k] for k in initial_value_indecies}

		# running learning episodes
		for e in range(self.opt['learning_episodes']):
			steps = 0
			converged = False
			while not converged:
				# getting choosen action of agents
				choosen_actions = {}
				for a in self.agents:
					choosen_actions[a] = self.agents[a].get_action()

				# advertising actions of neighbours to agnets
				for a in self.agents:
					self.agents[a].set_taken_actions(choosen_actions)

				steps += 1

				value_indecies = self.apply_actions(value_indecies, choosen_actions)
				values = self.get_values(value_indecies)
				function_values = self.get_function_values(values)

				raw_set = self.pareto_frontier + [(tuple(value_indecies.values()), tuple(function_values.values()))]
				new_frontier = get_pareto_frontier_by_point(raw_set)

				if set(self.pareto_frontier) == set(new_frontier):
					self.convergenc_count += 1
					if self.convergenc_count == self.opt['convergence']:
						converged = True
						print 'Episode %d converged in %d steps.' % (e, steps)
				else:
					self.convergenc_count = 0

				self.pareto_frontier = new_frontier

				self.path_log.append({'actions':choosen_actions, 'variables': values, 'functions': function_values, 'pareto': self.pareto_frontier})

	def apply_actions(self, value_indecies, choosen_actions):
		for v in value_indecies:
			if choosen_actions[v] == 'inc':
				if value_indecies[v] < self.fg.variables[v].domain_size-1:
					value_indecies[v] += 1
			elif choosen_actions[v] == 'dec':
				if value_indecies[v] > 0:
					value_indecies[v] -= 1
		return value_indecies

	def get_values(self, value_indecies):
		values = {}
		for v in value_indecies:
			values[v] = self.fg.variables[v].domain[value_indecies[v]]
		return values

	def get_function_values(self, variables_values):
		values = {}
		calculator = Functions(self.fg)
		for f in self.fg.functions:
			values[f] = calculator.calculate(f, variables_values)
		return values

	def converged(self, new_frontier, old_frontier):
		if set(self.pareto_frontier) == set(new_frontier):
			self.convergenc_count += 1
			if self.convergenc_count == self.opt['convergence']:
				converged = True
				print 'Episode %d converged in %d steps.' % (e, step)
		else:
			self.convergenc_count = 0

	def terminate(self):
		sys.stdout.flush()
		sys.stderr.flush()

		folder = 'results/'+datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		os.mkdir(folder)

		res = open(folder+'/results.json', 'w')
		res.write(json.dumps({'opt':self.opt, 'path_log': self.path_log}))
		res.close()
