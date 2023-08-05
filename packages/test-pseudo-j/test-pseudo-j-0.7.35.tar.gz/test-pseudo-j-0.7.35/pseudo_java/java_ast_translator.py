import javalang
import os
import sys
import yaml
import pseudo_java
from pseudo_java.api_translator import JAVA_KNOWN_IMPORTS

EQUALS_BUILTIN_TYPES = {
	'array':	'list'
}

BUILTIN_TYPES = {
	'int':	  'Int',
	'float':	'Float',
	'Integer':	'Int',
	'Float'	:	'Float',
	'Object':   'Object',
	'String':	'String',
    'string':	'String',
	'array':	'List',
	'Map'	:	 'Dictionary',
	'HashMap':	'Dictionary',
	'List'	:	'List',
	'ArrayList':	'List',
	'LinkedList':	'List',
	'set'	:	  'Set',
	'tuple'	:	'Tuple',
	'boolean':	 'Boolean',
}

PSEUDO_BUILTIN_TYPES = {v: k for k, v in BUILTIN_TYPES.items()}

BUILTIN_SIMPLE_TYPES = {
	'int':	  'Int',
	'Integer':	'Int',
	'Float':	'Float',
	'float':	'Float',
	'str':	  'String',
	'bool':	 'Boolean'
}

REVERSE_BUILTIN_TYPES = {
	'Int':		'int',
	'Float':	'float',
	'String':	'string',
	'Boolean':	'bool',
	'List' :	'array'
}

KEY_TYPES = {'String', 'int', 'float', 'Boolean'}

PSEUDO_KEY_TYPES = {'String', 'Int', 'Float', 'Bool'}


BUILTIN_FUNCTIONS_NAMESPACE = {'display':'io'}
#######

FORBIDDEN_TOP_LEVEL_FUNCTIONS = {'map', 'filter'}

ITERABLE_TYPES = {'String', 'List', 'Dictionary', 'Set', 'Array'}

TESTABLE_TYPE = 'Boolean'

INDEXABLE_TYPES = {'String', 'List', 'Dictionary', 'Array', 'Tuple'}

COMPARABLE_TYPES = {'Int', 'Float', 'String'}

TYPES_WITH_LENGTH = {'String', 'List', 'Dictionary', 'Array', 'Tuple', 'Set'}

NUMBER_TYPES = {'Int', 'Float'}

PSEUDO_OPS = {
	'+': '+',
	'-': '-',
	'/': '/',
	'*': '*',
	'**': '**',
	'==': '==',
	'<': '<',
	'>': '>',
	'<=': '<=',
	'>=': '>=',
	'!=': '!=',
	
	'%': '%',

	'and': 'and',
	'or':  'or',
	'not': 'not',
	'&': '&',
	'|': '|',
	'^': '^'
}

PSEUDO_BINARY_OPS = {
	'+': '+',
	'-': '-',
	'/': '/',
	'*': '*',
	'**': '**',
	
	'%': '%'

}

PSEUDO_COMPARISON_OPS = {

	'==': '==',
	'<': '<',
	'>': '>',
	'<=': '<=',
	'>=': '>=',
	'!=': '!='

}
class JavaASTTranslator:
	
	def w_type(self,s):
		try:
			return(int(s))
		except ValueError:
			try:
				return float(s)
			except ValueError:
				return s.strip('\"')
	
	def translate(self,name,source):
		#The 4 components of the Pseudo-AST
		self.constants = []
		self.custom_exceptions = []
		self.definitions = []
		self.dependencies = []
		self.main = []
		#Helpers
		self.main_block = []#Main and main block are different depending on the instance variable keep_class
		self.ass_store = {} #Assignment store, each key is a tuple (<Variable name>, <Scope>). Each value is the translation of the variable in Pseudo.
		self.name_scope = {}#Each key is the name of a variable, and each value is a list describing the various scope where the name was described. Used to distinguish similar names in ass_store.
		self.meth_store = {}#Method store, each key is a tuple (<Method name>, <Class>) where <Class> is the class where the method was described. Each value is the translation of the method in Pseudo.
		self.class_store = {}#Class store, each key is the name of the class, mapped with a list of its methods translated in Pseudo.
		self.object_types = {}#Object store, each key is the name of the class, mapped with its constructor translated in Pseudo.
		self.lines = [name] + source.split('\n') #Mapping list to access the source code.
		self.this = None #Current class name.
		self.keep_class = False #Used to know if the file is "oriented object" or not. Set to true if the options -o is passed, or if a class has a constructor, declares an instance variable or if the keyword "this" is used somewhere. 
		self.checked = {}#Can be used to detect if all the nodes were visited
		#Index to check if the current node is the good one.
		self.index = 0
		self.file_name = name
		self.actual_scope = None #Describes the actual scope. It can either be "Class", "Method" or "Block". Used to distinguish variables with the same name in the assignment store.
			
	def translate_node(self,node,parent,options):
		print((node,self.index))
		print((node,self.index) in self.checked)
		if ((node,self.index) in self.checked and self.checked[(node,self.index)] == False) or options[0] == 'No check':
			if(str(node) == 'CompilationUnit'):
				return self.translate_CU(node,parent,options)				
			elif(str(node) == 'ClassDeclaration'):
				return self.translate_CD(node,parent,options)
			elif(str(node) == 'MethodDeclaration'):
				return self.translate_MD(node,parent,options)
			elif(str(node) == 'This'):
				return self.translate_T(node,parent,options)	
			elif(str(node) == 'FieldDeclaration'):
				return self.translate_FD(node,parent,options)		
			elif(str(node) == 'ConstructorDeclaration'):
				return self.translate_CstD(node,parent,options)
			elif(str(node) == 'LocalVariableDeclaration'):
				return self.translate_LVD(node,parent,options)
			elif(str(node) == 'Literal'):
				return self.translate_LIT(node,parent,options)
			elif(str(node) == 'BinaryOperation'):
				return self.translate_BIOP(node,parent,options)
			elif(str(node) == 'MemberReference'):
				return self.translate_MR(node,parent,options)
			elif(str(node) == 'StatementExpression'):
				return self.translate_SE(node,parent,options)
			elif(str(node) == 'Import'):
				return self.translate_I(node,parent,options)
			elif(str(node) == 'VariableDeclarator'):
				return self.translate_VD(node,parent,options)
			elif(str(node) == 'VariableDeclaration'):
				return self.translate_VDN(node,parent,options)
			elif(str(node) == 'ClassCreator'):
				return self.translate_CC(node,parent,options)
			elif(str(node) == 'IfStatement'):
				return self.translate_IS(node,parent,options)
			elif(str(node) == 'WhileStatement'):
				return self.translate_WS(node,parent,options)
			elif(str(node) == 'ForStatement'):
				return self.translate_FS(node,parent,options)
			elif(str(node) == 'BlockStatement'):
				return self.translate_BS(node,parent,options)
			elif(str(node) == 'Assignment'):
				return self.translate_Ass(node,parent,options)
			elif(str(node) == 'ReturnStatement'):
				return self.translate_RS(node,parent,options)
			elif(str(node) == 'TypeArgument'):
				return self.translate_TA(node,parent,options)
			elif(str(node) == 'MethodInvocation'):
				return self.translate_MI(node,parent,options)
			elif(str(node) == 'ReferenceType'):
				return self.translate_RT(node,parent,options)
			elif(str(node) == 'ForControl'):
				return self.translate_FC(node,parent,options)
			elif(str(node) == 'EnhancedForControl'):
				return self.translate_EFC(node,parent,options)
			elif(str(node) == 'FormalParameter'):
				return self.translate_FP(node,parent,options)
			elif(str(node) == 'BasicType'):
				return self.translate_BT(node,parent,options)
			elif(str(node) == 'ArraySelector'):
				return self.translate_AS(node,parent,options)
			elif(str(node) == 'ArrayInitializer'):
				return self.translate_AI(node,parent,options)
			elif(str(node) == 'PackageDeclaration'):
				return self.translate_PD(node,parent,options)
			else:
				self.index = self.index + 1
				raise errors.translation_error('Pseudo-Java cannot translate this node: %s' % str(node),node.position, self.lines[node.position[0]])
	
	#Array Selector
	def translate_AS(self,node,parent,options):
		self.index = self.index + 1
		index = self.translate_node(node.index,node,[options[0],REVERSE_BUILTIN_TYPES[self.ass_store[(options[1].member,self.name_scope[options[1].member][-1])]['pseudo_type'][1]]])
		if('pseudo_type' in index):
			return {'index':index['value'],'pseudo_type':index['value']['pseudo_type'],'sequence':self.ass_store[(options[1].member,self.name_scope[options[1].member][-1])],'type':'index'}
		elif('reference' in index):
			index = self.ass_store[(index['reference'], self.name_scope[index['reference']][-1])]
			return {'index':index,'pseudo_type':index['pseudo_type'],'sequence':self.ass_store[(options[1].member,self.name_scope[options[1].member][-1])],'type':'index'}
		else:
			raise errors.type_check_error('The array selector seems wrong. Try an integer or a int variable. Actual is: %s' % str(node.index),node.position, self.lines[node.position[0]])

	#TypeArgument
	def translate_TA(self,node,parent,options):
		self.index = self.index + 1
		return self.translate_node(node.type,node,options)
		
	#A method to handle particular function that are not standard call or standard method call in Pseudo (like get() for ArrayList)
	def translate_PF(self,node,parent,options):
		message = BUILTIN_EQUIVALENT_FUNCTIONS[node.member]
		if message == 'index':
			args = []
			for arg in node.arguments:
				if str(arg) == 'Literal':
					temp = self.translate_node(arg,node,[options[0],REVERSE_BUILTIN_TYPES[self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type'][1]]])
				elif str(arg) == 'MemberReference':
					val = self.translate_node(arg,node,options)
					print(val)
					temp = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
				elif str(arg) == 'This':
					val = self.translate_node(arg,node,options)
					print(val)
					temp = self.ass_store[(val['reference'],'Class')]
				else:
					temp = self.translate_node(arg,node,options)
				args.append(temp)
			sequence = self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]
			if len(args) == 1: #access with get for ArrayList
				return {'index': args[0],'pseudo_type':sequence['pseudo_type'][1],'sequence':sequence,'type':'index'}
			else:#assignment of a new pair k,v in a HashMap
				return {'pseudo_type':'Void','type':'assignment','value':args[1],'target':{'index': args[0],'pseudo_type':sequence['pseudo_type'][1],'sequence':sequence,'type':'index'}}
		else:
			raise errors.type_check_error('Method or function not yet translatable by Pseudo-Java : %s' %str(node.member),node.position, self.lines[node.position[0]])
	
	#Method Invocation
	def translate_MI(self,node,parent,options):
		self.index = self.index + 1
		if(node.member in BUILTIN_EQUIVALENT_FUNCTIONS):
			message = BUILTIN_EQUIVALENT_FUNCTIONS[node.member]
			if isinstance(message,dict):
				message = message[self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type'][0]]
			if message in PARTICULAR_FUNCTIONS:
				return self.translate_PF(node,parent,options)
			args = []
			for arg in node.arguments:
				if str(arg) == 'Literal':
					if message == 'display':
						typ = 'String'
					else:
						typ = REVERSE_BUILTIN_TYPES[self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type'][1]]
					temp = self.translate_node(arg,node,[options[0],typ])
				elif str(arg) == 'MemberReference':
					val = self.translate_node(arg,node,options)
					temp = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
				elif str(arg) == 'This':
					val = self.translate_node(arg,node,options)
					temp = self.ass_store[(val['reference'],'Class')]
				else:
					temp = self.translate_node(arg,node,options)
				args.append(temp)
			if ((node.qualifier in self.name_scope) and (node.qualifier,self.name_scope[node.qualifier][-1] in self.ass_store)):
				if isinstance(self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type'],list):
					pt = self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type'][-1]
				else:
					pt = self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type']
				ptm = BUILTIN_TYPE_FUNCTIONS[message]
				ptt = self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type']
				if isinstance(ptm,list) and ('@k' in ptm or '@v' in ptm or '@t' in ptm):
					if '@k' in ptm:
						ptm[1] = ptt[1]
					elif '@v' in ptm:
						ptm[1] = ptt[2]
					else:
						c = 0
						for a,b in zip(ptm,ptt):
							if a == '@t':
								ptm[c] = b
							c = c + 1
				if BUILTIN_ARG_FUNCTIONS[node.member] == 'same':
					if pt != temp['pseudo_type']:
						raise errors.type_check_error('The type of the arguments is not fit for this particular function and its receiver: Arg : %s, Receiver : %s' % (temp['pseudo_type'],pt))
				return {'args':args,'message':message,'pseudo_type':ptm,'receiver':self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])],'type':'standard_method_call'}
			else:
				if temp['pseudo_type'] != BUILTIN_ARG_FUNCTIONS[node.member]:
					raise errors.type_check_error('The type of the arguments is not fit for this particular function and its receiver: Arg : %s, Receiver : %s' % (temp['pseudo_type'],BUILTIN_ARG_FUNCTIONS[node.member]),node.position, self.lines[node.position[0]])
				return {'args':args,'function':message,'pseudo_type':BUILTIN_TYPE_FUNCTIONS[message],'namespace':BUILTIN_FUNCTIONS_NAMESPACE[message],'type':'standard_call'}
		elif((node.member,self.this) in self.meth_store):
			if(self.meth_store[(node.member,self.this)]['name'] != 'Constructor'):
				message = self.meth_store[(node.member,self.this)]
				args = []
				t = 0
				for arg in node.arguments:
					typ = self.meth_store[(str(node.member),self.this)]['params'][t]['pseudo_type']
					if (isinstance(typ,list)):
						types = []
						for ty in typ:
							types.append(REVERSE_BUILTIN_TYPES[ty])
					else:
						types = REVERSE_BUILTIN_TYPES[typ]
					val = self.translate_node(arg,node,[options[0],types])
					if 'reference' in val:
						temp = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
					elif 'value' in val and val['type'] == 'assignment' :
						temp = val['value']
					else:
						temp = val
					args.append(temp)
					t = t + 1
				if message['class'] != self.this:
					if message['pseudo_type'] and len(message['pseudo_type']) > 1:
						pt = message['pseudo_type'][-1]
					else:
						pt = 'Void'
					return {'args':args,'message':message['name'],'pseudo_type':pt,'type':'method_call','receiver':self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]}
				else:
					return {'args':args,'function':{'name':message['name'],'pseudo_type':message['pseudo_type'],'type':'local'},'pseudo_type':message['return_type'],'type':'call'}
			else:
				args = []
				t = 0
				for arg in node.arguments:
					if str(arg) == 'Literal':
						temp = self.translate_node(arg,node,[options[0],REVERSE_BUILTIN_TYPES[self.meth_store[(str(node.member),self.this)]['params'][t]['pseudo_type']]])
					else:
						val = self.translate_node(arg,node,options)
						temp = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
					args.append(temp)
					t = t + 1
				return {'args':args,'class_name':node.member,'pseudo_type':node.member,'type':'new_instance'}
		elif((node.qualifier,self.actual_scope) in self.ass_store and (node.member, self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type']) in self.meth_store):
			this = self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type']
			if(self.meth_store[(node.member,this)]['name'] != 'Constructor'):
				message = self.meth_store[(node.member,this)]
				args = []
				t = 0
				for arg in node.arguments:
					typ = self.meth_store[(str(node.member),this)]['params'][t]['pseudo_type']
					if (isinstance(typ,list)):
						types = []
						for ty in typ:
							types.append(REVERSE_BUILTIN_TYPES[ty])
					else:
						types = REVERSE_BUILTIN_TYPES[typ]
					val = self.translate_node(arg,node,[options[0],types])
					if 'reference' in val:
						temp = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
					elif 'value' in val and val['type'] == 'assignment' :
						temp = val['value']
					else:
						temp = val
					args.append(temp)
					t = t + 1
				if message['class'] != this:
					if message['pseudo_type'] and len(message['pseudo_type']) > 1:
						pt = message['pseudo_type'][-1]
					else:
						pt = 'Void'
					return {'args':args,'message':message['name'],'pseudo_type':pt,'type':'method_call','receiver':self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]}
				else:
					return {'args':args,'function':{'name':message['name'],'pseudo_type':message['pseudo_type'],'type':'local'},'pseudo_type':message['return_type'],'type':'call'}
			else:
				args = []
				t = 0
				for arg in node.arguments:
					if str(arg) == 'Literal':
						temp = self.translate_node(arg,node,[options[0],REVERSE_BUILTIN_TYPES[self.meth_store[(str(node.member),this)]['params'][t]['pseudo_type']]])
					else:
						val = self.translate_node(arg,node,options)
						temp = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
					args.append(temp)
					t = t + 1
				return {'args':args,'class_name':node.member,'pseudo_type':node.member,'type':'new_instance'}
		
		else:
			print(self.meth_store)
			print(self.this)
			raise errors.type_check_error('Method or function not yet translatable by Pseudo-Java : %s' %str(node.member),node.position, self.lines[node.position[0]])
	
	#Return Statement
	def translate_RS(self,node,parent,options):
		self.index = self.index + 1
		temp = self.translate_node(node.expression,node,options)
		if(str(node.expression) == 'MemberReference'):
			mr = self.ass_store[(temp['reference'],self.name_scope[temp['reference']][-1])]
			pt = mr['pseudo_type']
			val = mr
		elif(str(node.expression) == 'This'):
			mr = self.ass_store[(temp[0]['reference'],'Class')]
			pt = mr['pseudo_type']
			val = mr
		else:
			val = temp['value']
			pt = val['pseudo_type']
		return {'pseudo_type':pt,'type':'implicit_return','value':val}
	
	#Block Statement			
	def translate_BS(self,node,parent,options):
		self.index = self.index + 1
		scope = self.actual_scope
		self.actual_scope = 'Block'
		res = []
		for n in node.statements:
			res.append(self.translate_node(n,node,options))
		self.actual_scope = scope
		for ass in list(self.ass_store):
			if ass[1] == 'Block':
				self.ass_store.pop(ass)
				self.name_scope[ass[0]].pop()
		return res
	
	#Variable Declarator
	def translate_VD(self,node,parent,options):
		self.index = self.index + 1
		if(node.initializer != None):
			init = self.translate_node(node.initializer,node,options)
			if options[1] != None:
				if node.name in self.name_scope:
					self.name_scope[node.name].append(self.actual_scope)				
				else:
					self.name_scope[node.name] = [self.actual_scope]
				self.ass_store[(node.name,self.actual_scope)] = {'name':node.name,'pseudo_type':BUILTIN_TYPES[options[1]],'type':'local'}
		else:
			init = None
			if node.name in self.name_scope:
				self.name_scope[node.name].append(self.actual_scope)				
			else:
				self.name_scope[node.name] = [self.actual_scope]
			self.ass_store[(node.name,self.actual_scope)] = {'name':node.name,'pseudo_type':BUILTIN_TYPES[options[1]],'type':'local'}
		return {'target':node.name,'init':init}
	
	#Variable Declaration
	def translate_VDN(self,node,parent,options):
		self.index = self.index + 1
		for d in node.declarators:
			if (str(node.type) == 'ReferenceType'):
				if(node.type.dimensions == []):
					bt = self.translate_node(node.type,node,options)
					t = self.translate_node(d,node,[options[0],bt['name']])
					if(node.type.name == 'String'):
						if(d.initializer == None):
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':""}						
						elif(str(d.initializer) == 'MemberReference'):
							val = self.ass_store[(t['target'],self.name_scope[t['target']][-1])]					
						elif(str(d.initializer) == 'This'):
							val = self.ass_store[(t['target'],'Class')]
						else:
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':d.initializer.value.strip('\"')}
					else:
						raise errors.type_check_error('Reference type %s not covered by Pseudo-Java' % node.type.name, node.position,self.lines[node.position[0]])
					if d.name in self.name_scope:
						self.name_scope[d.name].append(self.actual_scope)				
					else:
						self.name_scope[d.name] = [self.actual_scope]
					self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
					return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val}
				else:
					#todo...
					raise errors.type_check_error('Not implemented yet array referencetype')
			elif(str(node.type) == 'BasicType'):
				if(node.type.dimensions == []):
					bt = self.translate_node(node.type,node,options)
					t = self.translate_node(d,node,[options[0],bt['name']])
					if(node.type.name == 'int'):
						if(d.initializer == None):
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':0}
						elif(str(d.initializer) == 'MemberReference'):
							val = self.ass_store[(t['init']['reference'],self.name_scope[t['init']['reference']][-1])]				
						elif(str(d.initializer) == 'This'):
							val = self.ass_store[(t['init']['reference'],'Class')]
						else:
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':int(d.initializer.value)}
					elif(node.type.name == 'float'):
						if(d.initializer == None):
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':0.0}
						elif(str(d.initializer) == 'MemberReference'):
							val = self.ass_store[(t['init']['reference'],self.name_scope[t['init']['reference']][-1])]			
						elif(str(d.initializer) == 'This'):
							val = self.ass_store[(t['init']['reference'],'Class')]
						else:
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':float(d.initializer.value)}
					else:
						raise errors.type_check_error('Basic type %s not covered by Pseudo-Java' % node.type.name, node.position,self.lines[node.position[0]])
					if d.name in self.name_scope:
						self.name_scope[d.name].append(self.actual_scope)				
					else:
						self.name_scope[d.name] = [self.actual_scope]
					self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
					return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val}
				else:
					self.index = self.index + 1
					if(str(d.initializer) == 'ArrayInitializer'):
						val = self.translate_node(d.initializer,node,[options[0],node.type.name])
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':val['pseudo_type'],'type':'local'},'value':val}
			else:
				raise errors.type_check_error('Reference type %s not covered by Pseudo-Java' % node.type.name, node.position,self.lines[node.position[0]])
	
	
	#For Control
	def translate_FC(self,node,parent,options):
		self.index = self.index + 1
		init = self.translate_node(node.init,node,options)
		condition = self.translate_node(node.condition,node,options)
		update = self.translate_node(node.update[0],node,options)
		return {"init":init,"condition":condition,"update":update}
	
	#Enhanced For Control
	def translate_EFC(self,node,parent,options):
		self.index = self.index + 1
		var = self.translate_node(node.var,node,options)
		iterable = self.translate_node(node.iterable,node,options)
		return {'var':var,'iterable':iterable}
	
	#For Statement
	def translate_FS(self,node,parent,options):
		self.index = self.index + 1
		block = []
		if(str(node.control) == "ForControl"):
			test = self.translate_node(node.control,node,options)
			block= self.translate_node(node.body,node,options)
			if(test["update"]["postfix_op"][0] == "++" or test["update"]["postfix_op"][0] == "+="):
				op = test["update"]["postfix_op"][0]
				typ = "for_range_statement"
				start = test["init"]["value"]
				end = test["condition"]["value"]["right"]
				if op == "++" :
					step = {'pseudo_type':start["pseudo_type"], 'type': 'int', 'value': 1}
				elif op == '--':
					step = {'pseudo_type':start["pseudo_type"], 'type': 'int', 'value': -1}				
				else:
					step = {'pseudo_type':start["pseudo_type"], 'type': start["type"], 'value': "todo"}
				index = test["init"]["target"]
				return {'block':block,'pseudo_type':'Void','type':'for_statement','type':typ,'start':start,'end':end,'index':index,'step':step}
			else:
				typ = "for_statement"
		
		else:
			test = self.translate_node(node.control,node)
			block= self.translate_node(node.body,node)	
			return{'block':block,'pseudo_type':'Void','iterators':{'iterator':test['var']['target'],'type':'for_iterator'},'sequences':{'sequence':self.ass_store[(test['iterable']['reference'],self.name_scope[test['iterable']['reference']][-1])],'type':'for_sequence'},'type':'for_statement'}
			return{'block':block,'pseudo_type':'Void','type':'for_statement','test':None}
	
	#While Statement
	def translate_WS(self,node,parent,options):
		self.index = self.index + 1
		test = self.translate_node(node.condition,node,options)
		block = self.translate_node(node.body,node,options)
		return{'block':block,'pseudo_type':'Void','type':'while_statement','test':test['value']}
	
	#If Statement
	def translate_IS(self,node,parent,options):
		self.index = self.index + 1
		test = self.translate_node(node.condition,node,options)
		block = self.translate_node(node.then_statement,node,options)
		other_block = self.translate_node(node.else_statement,node,options)
		if other_block != None:
			otherwise = {'block':other_block,'pseudo_type':'Void','type':'else_statement'}
		else:
			otherwise = None
		return{'block':block,'otherwise':otherwise,'pseudo_type':'Void','type':'if_statement','test':test['value']}
	
	#Package Declaration. Not yet translatable by Pseudo !	
	def translate_PD(self,node,parent,options):
		self.index = self.index + 1
		path = os.path.dirname(os.path.abspath(__file__))
		dir_path = path + '/'+ self.file_name
		files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path,f))]
		jfiles = []
		f_name = self.file_name + '.java'
		for f in files:
			if len(f)>5 and f[-5:] == '.java' and f != f_name:
				jfiles.append(f)
		for f in jfiles:
			rel_source_path = dir_path + '/' + f
			with open(rel_source_path,'r') as fi:
				source = fi.read()
			tree = javalang.parse.parse(source)
			temp_index =  self.index
			temp_scope = self.actual_scope
			actual_scope = 'Method'
			if tree.types:
				for t in tree.types:
					self.class_store[str(t.name)] = {'attrs':None,'meths':[]}
					attrs = []
					for field in t.fields:
						field = self.translate_node(field,t,['No check',None])
						if field != None:
							attrs.append(field)
					self.class_store[str(t.name)]['attrs'] = attrs
					constructors = []		
					for c in t.constructors:
						self.index = self.index + 1		
						params = []
						pt = ['Function']
						for p in c.parameters:
							param = self.translate_node(p,c,['No check',None])[1]
							params.append(param)
							pt.append(param['pseudo_type'])
						pt.append(c.name)
						if c.throws == None:
							rt = 'Void'
						else:
							rt = self.translate_node(c.throws,c,['No check',None])
						self.meth_store[(str(c.name),t.name)] = {'name':'Constructor','class':str(c.name),'return_type':rt,'pseudo_type':'Void','params':params}
						constructors.append({'name':'__init__','return_type':rt,'pseudo_type':pt,'params':params,'this':{'name':c.name,'type':'typename'},'type':'constructor'})
					if len(constructors) == 1:
						constructors = constructors[0]
					self.object_types[t.name] = constructors
					for m in t.methods:
						while((m,self.index) not in self.checked):
							self.index = self.index + 1
						pt = []
						pt.append('Function')
						self.index = self.index + 1
						p = []
						if(m.return_type != None):
							print(m.return_type)
							ret = self.translate_node(m.return_type,m,['No check',None])
							rt = BUILTIN_TYPES[ret['name']]
						else:
							rt = 'Void'
						for param in m.parameters:
							temp = self.translate_node(param,m,['No check',None])
							p.append(temp[1])
							pt.append(temp[0])
						if(rt != 'Void'):
							pt.append(rt)
						meth = {'name':str(m.name),'class':str(t.name),'return_type':rt,'pseudo_type':pt,'params':p}
						self.meth_store[(str(m.name),t.name)] = meth
						self.class_store[str(t.name)]['meths'].append(meth)
		
		self.index = temp_index
		self.actual_scope = temp_scope
		mods = []
		for c in self.class_store:
			self.dependencies.append({'module':c})
		
	
	#Imports
	def translate_I(self,node,parent):
		self.index = self.index + 1
		if node.path not in JAVA_KNOWN_IMPORTS:
			raise errors.type_check_errors('Unknown import %s'%node.path,node.position,self.lines[node.position[0]])
	
	#Assignment node
	def translate_Ass(self,node,parent,options):
		self.index = self.index + 1
		member = self.translate_node(node.expressionl,node,options)
		if(isinstance(member,list) and len(member) == 1):
			member = member[0]
			this = True
		else:
			this = False
		if member != None and 'reference' in member:
			if this:
				valm = self.ass_store[(member['reference'],'Class')]
			else:
				valm = self.ass_store[(member['reference'],self.name_scope[member['reference']][-1])]
			if isinstance(valm['pseudo_type'],list):
				typ = []
				for t in valm['pseudo_type']:
					typ.append(REVERSE_BUILTIN_TYPES[t])
			else:
				typ = REVERSE_BUILTIN_TYPES[valm['pseudo_type']]	
		else:
			typ = None
		val = self.translate_node(node.value,node,[options[0],typ])
		print(self.ass_store)
		if val != None and 'reference' not in val:
			if member == None:
				return val
			else:
				if 'reference' in member:
					if this:
						target = self.ass_store[(member['reference'],'Class')]
					else:
						target = self.ass_store[(member['reference'],self.name_scope[member['reference']][-1])]
				else:
					target = member
				if 'value' in val and 'left' in val['value'] and val['value']['left'] == target:
					return val
				return {'value':val,'target':target,'type':'assignment','pseudo_type':'Void'}
		elif member != None and 'reference' not in member:
			if val == None:
				return member
			else:
				if 'reference' in val:
					value = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
				else:
					value = val
				return {'value':value,'target':member,'type':'assignment','pseudo_type':'Void'}
		elif 'selectors' in member and member['selectors'] != []:
			target = member['selectors'][0]
			if val['selectors'] != []:
				value = val['selectors'][0]
			else:
				value = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
			return {'value':value,'target':target,'type':'assignment','pseudo_type':'Void'}
		else:
			if this:
				target = self.ass_store[(member['reference'],'Class')]
			else:
				target = self.ass_store[(member['reference'],self.name_scope[member['reference']][-1])]
			return {'value':self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])],'target':target,'type':'assignment','pseudo_type':'Void'}
	
	#Statement Expression
	def translate_SE(self,node,parent,options):
		#todo with first argument 
		self.index = self.index + 1
		ret = self.translate_node(node.expression,node,options)
		if str(node.expression) == 'MemberReference' and ret['postfix_op'] != []:
			if ret['postfix_op'] == ['++']:
				op = '+'
			elif ret['postfix_op'] == ['--']:
				op = '-'
			else:
				raise errors.type_check_error('Postfix operator not known by Pseudo-Java %s' %ret['postfix_op'],node.position,self.lines[node.position[0]])
			target = self.ass_store[(ret['reference'],self.name_scope[ret['reference']][-1])]
			return {'pseudo_type':'Void','target':target,'type':'assignment','value':{'left':target,'op':op,'pseudo_type':target['pseudo_type'],'right':{'pseudo_type': target['pseudo_type'], 'type': REVERSE_BUILTIN_TYPES[target['pseudo_type']], 'value': 1},'type':'binary_op'}}
		elif str(node.expression) == 'MemberReference' and ret['prefix_op'] != []:
			return {}
		return ret
	
	
	#MemberReference
	def translate_MR(self,node,parent,options):
		self.index = self.index + 1
		selectors = []
		if node.selectors:
			for s in node.selectors:
				selectors.append(self.translate_node(s,node.selectors,[options[0],node]))
		return {'reference':node.member,'prefix_op':node.prefix_operators,'postfix_op':node.postfix_operators,'qualifier':node.qualifier,'selectors':selectors}
	
	#Binary Operation
	def translate_BIOP(self,node,parent,options):
		self.index = self.index + 1
		if(str(node.operandl) == 'MemberReference'):
			opl = self.translate_node(node.operandl,node,options)
			if 'selectors' in opl and opl['selectors'] != []:
				target = opl['selectors'][0]
			else:
				target = self.ass_store[(node.operandl.member,self.name_scope[node.operandl.member][-1])]
		elif(str(node.operandl) == 'BinaryOperation'):
			temp = self.translate_node(node.operandl,node,options)
			target = temp['value']
		elif(str(node.operandl) == 'This'):
			opr = self.translate_node(node.operandl,node,options)	
			if 'selectors' in opr and opr['selectors'] != []:
				val = opr['selectors'][0]
			else:
				val = self.ass_store[(opr[0]['reference'],'Class')]
			right = val
		else:
			raise errors.type_check_error('Operand left : %s not yet treated by Pseudo-Java'%str(node.operandl),node.position,self.lines[node.position[0]])
		if(str(node.operandr) == "Literal"):
			val = self.translate_node(node.operandr,node, [options[0],REVERSE_BUILTIN_TYPES[target['pseudo_type']]])
			right = val
		elif(str(node.operandr) == "MemberReference"):
			opr = self.translate_node(node.operandr,node,options)
			if 'selectors' in opr and opr['selectors'] != []:
				val = opr['selectors'][0]
			else:
				val = self.ass_store[(node.operandr.member,self.name_scope[node.operandr.member][-1])]
			right = val
		elif(str(node.operandr) == 'This'):
			opr = self.translate_node(node.operandr,node,options)
			if 'selectors' in opr and opr['selectors'] != []:
				val = opr['selectors'][0]
			else:
				val = self.ass_store[(opr[0]['reference'],'Class')]
			right = val
		else:
			raise errors.type_check_error('Operand right : %s not yet treated by Pseudo-Java'%str(node.operandr),node.position,self.lines[node.position[0]])
		if(node.operator in PSEUDO_BINARY_OPS):
			p_typ = target['pseudo_type']
			typ = 'binary_op'
		else:
			p_typ = 'Boolean'
			typ = 'comparison'
		res = {'pseudo_type':'Void','type':'assignment','target':target,'value':{'left':target,'op':node.operator,'pseudo_type':p_typ,'right':right,'type':typ}}
		return res

	#Literal
	def translate_LIT(self,node,parent,options):
		self.index = self.index + 1
		if(options[1] != None):
			return {'pseudo_type':BUILTIN_TYPES[options[1]],'type':options[1],'value':self.w_type(node.value)}
		else:
			return {'pseudo_type':None,'type':None,'value':self.w_type(node.value)}
	
			
	#LocalVariableDeclaration
	def translate_LVD(self,node,parent,options):
		self.index = self.index + 1
		for d in node.declarators:
			if (str(node.type) == 'ReferenceType'):
				if(node.type.dimensions == []):
					rt = self.translate_node(node.type,node,options)
					mt = self.translate_node(d,node,options)
					if(node.type.name == 'String'):
						temp = d.initializer.value.strip('\"')
						typ = REVERSE_BUILTIN_TYPES[node.type.name]
						val = {'pseudo_type':'String','type':'string','value':temp}
					elif(node.type.name == 'ArrayList'):
						typ = node.type.arguments[0].type.name
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':['List', BUILTIN_TYPES[typ]],'type':'local'}
						if(mt['init'] == None):
							val = {'elements':[],'type':'list','pseudo_type':['List',BUILTIN_TYPES[typ]]} 
						else:
							val = mt['init']
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':['List',BUILTIN_TYPES[typ]],'type':'local'},'value':val}
					elif(node.type.name == 'List'):
						typ = node.type.arguments[0].type.name
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':['List', BUILTIN_TYPES[typ]],'type':'local'}
						if(mt['init'] == None):
							val = {'elements':[],'type':'list','pseudo_type':['List',BUILTIN_TYPES[typ]]} 
						else:
							val = mt['init']
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':['List',BUILTIN_TYPES[typ]],'type':'local'},'value':val}
					elif(node.type.name == 'Set'):
						typ = node.type.arguments[0].type.name
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':['Set', BUILTIN_TYPES[typ]],'type':'local'}
						if(mt['init'] == None):
							val = {'elements':[],'type':'set','pseudo_type':['Set',BUILTIN_TYPES[typ]]} 
						else:
							val = mt['init']
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':['Set',BUILTIN_TYPES[typ]],'type':'local'},'value':val}
					elif(node.type.name == 'Map'):
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':['Dictionary', BUILTIN_TYPES[rt['kt']],BUILTIN_TYPES[rt['vt']]],'type':'local'}
						val = {'pairs':[],'type':'dictionary','pseudo_type':['Dictionary', BUILTIN_TYPES[rt['kt']],BUILTIN_TYPES[rt['vt']]]} #Pairs are always empty since you can't initialize a non-empty HashMap in Java
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':['Dictionary',BUILTIN_TYPES[rt['kt']],BUILTIN_TYPES[rt['vt']]],'type':'local'},'value':val}
					elif(node.type.name in self.object_types):
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':rt['name'],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':rt['name'],'type':'local'},'value':{'args':mt['init']['args'],'type':'new_instance','class_name':rt['name'],'pseudo_type':rt['name']}}
					else:
						raise errors.type_check_error('Reference type not covered by Pseudo-Java : %s' %node.type.name,node.position,self.lines[node.position[0]])
					if d.name in self.name_scope:
						self.name_scope[d.name].append(self.actual_scope)				
					else:
						self.name_scope[d.name] = [self.actual_scope]
					self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
					return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val}
				else:
					raise errors.type_check_error('Reference array type not covered by Pseudo-Java : %s' %node.type.name,node.position,self.lines[node.position[0]])
			elif(str(node.type) == 'BasicType'):
				if(node.type.dimensions == []):
					if(str(d.initializer) == 'Literal'):
						self.translate_node(node.type,node,options)
						v = self.translate_node(d,node,[options[0],node.type.name])
						if(node.type.name == 'int' or node.type.name == 'float'):
							val = v['init']
						else:
							raise errors.type_check_error('Basic type not covered by Pseudo-Java : %s' %node.type.name,node.position,self.lines[node.position[0]])
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val}
					elif(str(d.initializer) == 'BinaryOperation'):
						self.translate_node(node.type,node,options)
						val = self.translate_node(d,node,options)
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
						if 'init' in val:
							val = val['init']
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val['value']}
					elif(str(d.initializer) == 'MethodInvocation'):
						bt = self.translate_node(node.type,node,options)
						mi = self.translate_node(d,node,options)
						val = mi['init']
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val}
					elif(str(d.initializer) == 'MemberReference'):
						bt = self.translate_node(node.type,node,options)
						mr = self.translate_node(d,node,options)
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[bt['name']],'type':'local'}
						if mr['init']['selectors'] != []:
							selectors = mr['init']['selectors'][0]
						else:
							selectors = None
						return {'pseudo_type':'Void','type':'assignment','target':self.ass_store[(mr['target'],self.name_scope[mr['target']][-1])],'value':selectors}
					elif(str(d.initializer) == 'This'):
						bt = self.translate_node(node.type,node,options)
						mr = self.translate_node(d,node,options)
						if d.name in self.name_scope:
							self.name_scope[d.name].append('Class')				
						else:
							self.name_scope[d.name] = ['Class']
						self.ass_store[(d.name,'Class')] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[bt['name']],'type':'local'}
						if mr['init']['selectors'] != []:
							selectors = mr['init']['selectors'][0]
						else:
							selectors = None
						return {'pseudo_type':'Void','type':'assignment','target':self.ass_store[(mr['target'],self.name_scope[mr['target']][-1])],'value':selectors}
					elif(str(d.initializer) == 'ArrayInitializer'):
						bt = self.translate_node(node.type,node,options)
						mr = self.translate_node(d,node,options)
						val = self.translate_node(d,node,[options[0],bt['name']])
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':val['init']['pseudo_type'],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':val['init']['pseudo_type'],'type':'local'},'value':val['init']}
					else:
						raise errors.type_check_error('Basic type not covered by Pseudo-Java : %s' %node.type.name,node.position,self.lines[node.position[0]])
						
				else:
					if(str(d.initializer) == 'ArrayInitializer'):
						bt = self.translate_node(node.type,node,options)
						val = self.translate_node(d,node,[options[0],bt['name']])
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':val['init']['pseudo_type'],'type':'local'}
						pt = val['init']['pseudo_type']
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':pt,'type':'local'},'value':val['init']}
			else:
				raise errors.type_check_error('Type not covered by Pseudo-Java: %s' %node.type,node.position,self.lines[node.position[0]])	

	
	#Array Initializer
	def translate_AI(self,node,parent,options):
		self.index = self.index + 1
		e = []
		for n in node.initializers:
			e.append(self.translate_node(n,node,options))
		pt = ['List',BUILTIN_TYPES[options[1]]]
		for _ in range(0,len(node.initializers)-1):
			if str(n) == 'ArrayInitializer':
				pt = ['List',pt]
		return {'elements':e,'pseudo_type':pt,'type':'list'}
	
	
	#Formal Parameter
	def translate_FP(self,node,parent,options):
		self.index = self.index + 1
		if (str(node.type) == 'ReferenceType'):
			if node.type.dimensions == []:
				pt = node.type.name
			else:
				pt = []
				pt.append('List')
				pt.append(node.type.name)
			self.translate_node(node.type,node,options)
			if isinstance(pt,list):
				if node.name in self.name_scope:
					self.name_scope[node.name].append(self.actual_scope)				
				else:
					self.name_scope[node.name] = [self.actual_scope]
				self.ass_store[(node.name,self.actual_scope)] = {'name':node.name,'pseudo_type':pt,'type':'local'}
				return (pt,{'name':node.name,'pseudo_type':pt,'type':'local'})
			else:
				if node.name in self.name_scope:
					self.name_scope[node.name].append(self.actual_scope)				
				else:
					self.name_scope[node.name] = [self.actual_scope]
				self.ass_store[(node.name,self.actual_scope)] = {'name':node.name,'pseudo_type':BUILTIN_TYPES[pt],'type':'local'}
				return (BUILTIN_TYPES[pt],{'name':node.name,'pseudo_type':BUILTIN_TYPES[pt],'type':'local'})
		elif(str(node.type) == 'BasicType'):
			if node.type.dimensions == []:
				pt = node.type.name
			else:
				pt = []
				pt.append('List')
				pt.append(BUILTIN_TYPES[node.type.name])
			self.translate_node(node.type,node,options)
			if isinstance(pt,list):
				if node.name in self.name_scope:
					self.name_scope[node.name].append(self.actual_scope)				
				else:
					self.name_scope[node.name] = [self.actual_scope]
				self.ass_store[(node.name,self.actual_scope)] = {'name':node.name,'pseudo_type':pt,'type':'local'}
				return (pt,{'name':node.name,'pseudo_type':pt,'type':'local'})
			else:
				if node.name in self.name_scope:
					self.name_scope[node.name].append(self.actual_scope)				
				else:
					self.name_scope[node.name] = [self.actual_scope]
				self.ass_store[(node.name,self.actual_scope)] = {'name':node.name,'pseudo_type':BUILTIN_TYPES[pt],'type':'local'}
				return (BUILTIN_TYPES[pt],{'name':node.name,'pseudo_type':BUILTIN_TYPES[pt],'type':'local'})
		else:
			raise errors.type_check_error('Type not covered by Pseudo-Java: %s' %node.type,node.position,self.lines[node.position[0]])
				
			
	#Reference Type
	def translate_RT(self,node,parent,options):
		self.index = self.index + 1
		args = []
		if node.arguments != None:
			for arg in node.arguments:
				args.append(self.translate_node(arg,node,options))	
		print('RT')			
		print(args)
		if node.name == 'Map':
			return {'kt':args[0]['name'],'vt':args[1]['name']}
		return {'args':args,'name':node.name}
	
	
	#BasicType
	def translate_BT(self,node,parent,options):
		self.index = self.index + 1
		return {'name':node.name,'dimensions':node.dimensions}
	
	
	
	#Method declaration
	def translate_MD(self,node,parent,options):
		self.main_block = []
		scope = self.actual_scope
		self.actual_scope = 'Method'
		pt = []
		pt.append('Function')
		self.index = self.index + 1
		p = []
		if(node.return_type != None):
			ret = self.translate_node(node.return_type,node,options)
			rt = BUILTIN_TYPES[ret['name']]
		else:
			rt = 'Void'
		for param in node.parameters:
			temp = self.translate_node(param,node,options)
			p.append(temp[1])
			if temp[1]['name'] in self.name_scope:
					self.name_scope[temp[1]['name']].append(self.actual_scope)				
			else:
				self.name_scope[temp[1]['name']] = [self.actual_scope]
			self.ass_store[(temp[1]['name'],self.actual_scope)] = temp[1]
			pt.append(temp[0])
		self.meth_store[(str(node.name),self.this)] = {'name':str(node.name),'class':str(parent.name),'return_type':rt,'pseudo_type':pt,'params':p}
		body = None
		for op in node.body:
			body = self.translate_node(op,node,options)
			if body != None:
				self.main_block.append(body)
		pt.append(rt)
		self.actual_scope = scope		
		temp = self.ass_store
		for ass in list(self.ass_store):
			if ass[1] == 'Method':
				self.ass_store.pop(ass)
				self.name_scope[ass[0]].pop()
		if(node.name == 'main' and self.keep_class == False):
			self.main = self.main_block
			return None
		else:
			if(parent.name == self.file_name and self.keep_class == False):
				return {'block':self.main_block,'name':node.name,'params':p,'pseudo_type':pt,'return_type':rt,'type':'function_definition'}
			else:
				return {'block':self.main_block,'is_public':True,'name':node.name,'params':p,'pseudo_type':pt,'return_type':rt,'this':{'name':parent.name,'type':'typename'},'type':'method_definition'}
	
	#Field Declaration
	def translate_FD(self,node,parent,options):
		print(node)
		print(node.type)
		self.index = self.index + 1
		typ = []
		typ.append(self.translate_node(node.type,node,options))
		decl = []
		print("Declarators")
		print(typ)
		for (d,t) in zip(node.declarators,typ):
			print(d)
			print(t)
			decl.append(self.translate_node(d,node,[options[0],t['name']]))
		print("END DECL")
		print(decl)
		if(node.modifiers == {'public'}):
			is_p = True
		else:
			is_p = False
		#if __init__ not present, return it
		self.ass_store[(decl[0]['target'],self.actual_scope)]['type'] = 'instance_variable'
		print(self.ass_store)
		return {'is_public':is_p,'type':'class_attr','pseudo_type':BUILTIN_TYPES[typ[0]['name']],'name':decl[0]['target']}
	
	#This
	def translate_T(self,node,parent,options):
		self.index = self.index + 1
		self.keep_class = True
		a = []
		selectors = []
		if node.selectors:
			for s in node.selectors:
				selectors.append(self.translate_node(s,node,options))
		return selectors		
		
	#Constructor Declaration
	def translate_CstD(self,node,parent,options):
		self.index = self.index + 1
		self.keep_class = True
		params = []
		pt = ['Function']
		for p in node.parameters:
			param = self.translate_node(p,node,options)[1]
			params.append(param)
			pt.append(param['pseudo_type'])
		pt.append(node.name)			
		body = []
		for b in node.body:
			body.append(self.translate_node(b,node,options))
		if node.throws == None:
			rt = 'Void'
		else:
			rt = self.translate_node(node.throws,node,options)
		self.meth_store[(str(node.name),self.this)] = {'name':'Constructor','class':str(node.name),'return_type':rt,'pseudo_type':'Void','params':params}
		return {'name':'__init__','block':body,'return_type':rt,'pseudo_type':pt,'params':params,'this':{'name':node.name,'type':'typename'},'type':'constructor'}
	
	#Class Declaration
	def translate_CD(self,node,parent,options):
		scope = self.actual_scope
		self.actual_scope = 'Class'
		self.index = self.index + 1
		self.this = node.name
		attrs = []
		base = None
		constructors = []
		definitions = []
		for f in node.fields:
			field = self.translate_node(f,node,options)
			if field != None:
				attrs.append(field)
		self.actual_scope = 'Method'
		for c in node.constructors:
			const = self.translate_node(c,node,options)
			if const != None:
				constructors.append(const)
		self.actual_scope = 'Class'
		for m in node.methods:
			meth = self.translate_MD(m,node,options)
			if meth != None:
					definitions.append(meth)
					if(meth['name'] == node.name):
						constructor = meth
		if (len(constructors) == 1):
			constructors = constructors[0]
		if(self.keep_class == False):
			res = definitions
		else:
			res = {'attrs':attrs,'base':base,'constructor':constructors,'methods':definitions,'name':node.name,'type':'class_definition'}
		for ass in list(self.ass_store):
			if ass[1] == 'Class':
				self.ass_store.pop(ass)
				self.name_scope[ass[0]].pop()
		self.actual_scope = scope
		self.object_types[node.name] = constructors
		if(self.keep_class == False):
			self.definitions = res
		else:
			self.definitions.append(res)
	
	#Class Creator
	def translate_CC(self,node,parent,options):
		self.index = self.index + 1
		nt = self.translate_node(node.type,node,options)
		args = []
		obj = self.object_types[nt['name']]
		if obj:
			for arg,param in zip(node.arguments,obj['params']):
				args.append(self.translate_node(arg,node.arguments,[options[0],REVERSE_BUILTIN_TYPES[param['pseudo_type']]]))
		return{'type':nt['name'],'args':args}
		
	#Compilation Unit. The first node of a compilable program is always this one.
	def translate_CU(self,node,parent,options):
		self.index = self.index + 1
		if node.package:
			self.translate_node(node.package,node,options)
		if node.imports:
			for i in node.imports:
				self.translate_node(i,node,options)
		temp_index = self.index
		temp_scope = self.actual_scope
		self.actual_scope = 'Method'
		if node.types:
			for t in node.types:
				self.index = 0
				while((t,self.index) not in self.checked):
					self.index = self.index + 1
				self.class_store[str(t.name)] = {'attrs':None,'meths':[]}
				attrs = []
				for field in t.fields:
					while((field,self.index) not in self.checked):
						self.index = self.index + 1
					field = self.translate_node(field,t,options)
					if field != None:
						attrs.append(field)
				self.class_store[str(t.name)]['attrs'] = attrs
				constructors = []		
				for c in t.constructors:
					while((c,self.index) not in self.checked):
						self.index = self.index + 1	
					self.index = self.index + 1		
					params = []
					pt = ['Function']
					print(self.checked)
					for p in c.parameters:
						print(p)
						print(self.index)
						param = self.translate_node(p,c,options)[1]
						print(param)
						params.append(param)
						pt.append(param['pseudo_type'])
					pt.append(c.name)
					if(c.throws != None):
						while(c.throws,self.index) not in self.checked:
							self.index = self.index + 1
					if c.throws == None:
						rt = 'Void'
					else:
						rt = self.translate_node(c.throws,c,options)
					self.meth_store[(str(c.name),t.name)] = {'name':'Constructor','class':str(c.name),'return_type':rt,'pseudo_type':'Void','params':params}
					constructors.append({'name':'__init__','return_type':rt,'pseudo_type':pt,'params':params,'this':{'name':c.name,'type':'typename'},'type':'constructor'})
				if len(constructors) == 1:
					constructors = constructors[0]
				self.object_types[t.name] = constructors
				for m in t.methods:
					while((m,self.index) not in self.checked):
						self.index = self.index + 1
					pt = []
					pt.append('Function')
					self.index = self.index + 1
					p = []
					if(m.return_type != None):
						print(m.return_type)
						ret = self.translate_node(m.return_type,m,options)
						rt = BUILTIN_TYPES[ret['name']]
					else:
						rt = 'Void'
					for param in m.parameters:
						temp = self.translate_node(param,m,options)
						p.append(temp[1])
						pt.append(temp[0])
					if(rt != 'Void'):
						pt.append(rt)
					meth = {'name':str(m.name),'class':str(t.name),'return_type':rt,'pseudo_type':pt,'params':p}
					self.meth_store[(str(m.name),t.name)] = meth
					self.class_store[str(t.name)]['meths'].append(meth)
		
		self.index = temp_index
		self.actual_scope = temp_scope
		if node.types:
			for t in node.types:
				self.translate_node(t,node,options)
	
			
	#Begin the translation by creating a tuple with each node and its index that will be used as an unique key
	#Translate each node after that.	
	def walk_tree(self,tree):
		index = 0
		for path,node in tree:
			if (node,index) not in self.checked:#create unique and distinguishable key
				self.checked[(node,index)] = False
			index = index + 1
		temp = None
		self.translate_node(tree,None,['Check',None])
			

	def Test(self,name,source,options):
		if options == '-o':
			self.keep_class = True
		self.translate(name,source)
		tree = javalang.parse.parse(source)
		self.walk_tree(tree)
		trad = {'constants':self.constants,'custom_exceptions':self.custom_exceptions,'definitions':self.definitions,'dependencies':self.dependencies,'main':self.main,'type':'module'}
		return trad
	

