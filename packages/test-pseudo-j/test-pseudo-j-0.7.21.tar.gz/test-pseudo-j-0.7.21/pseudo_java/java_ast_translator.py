import javalang
import os
import sys
import yaml
import pseudo_java

EQUALS_BUILTIN_TYPES = {
	'array':	'list'
}

BUILTIN_TYPES = {
	'int':	  'Int',
	'float':	'Float',
	'Integer':	'Int',
	'Float':	'Float',
	'Object':   'Object',
	'String':	'String',
	'array':	'List',
	'Map':	 'Dictionary',
	'HashMap':	'Dictionary',
	'set':	  'Set',
	'tuple':	'Tuple',
	'bool':	 'Boolean',
	'SRE_Pattern': 'Regexp',
	'SRE_Match': 'RegexpMatch'
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

KEY_TYPES = {'str', 'int', 'float', 'bool'}

PSEUDO_KEY_TYPES = {'String', 'Int', 'Float', 'Bool'}

#######
#Functions#

BUILTIN_FUNCTIONS = {'System.out.println','System.out.print',  'length', 'all', 'sum','add','index'}

BUILTIN_EQUIVALENT_FUNCTIONS = {'add':'push','println':'display','print':'display'}

BUILTIN_ARG_FUNCTIONS = {'add':'same','remove':'Int','print':'String','println':'String'}

BUILTIN_TYPE_FUNCTIONS = {'length':'Int','push':'Void','display':'Void'}

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
#Some imports in Java are not useful in Ruby/Python and can be resolved immediately.
JAVA_KNOWN_IMPORTS = {
	'java.util.Map' : 'Dictionary',
	'java.util.HashMap' : 'Dictionary'
}

class JavaASTTranslator:
	
	def w_type(self,s):
		try:
			return(int(s))
		except ValueError:
			try:
				return float(s)
			except ValueError:
				return s
	
	def translate(self,name,source):
		self.constants = []
		self.custom_exceptions = []
		self.definitions = []
		self.dependencies = []
		self.main = []
		self.main_block = []
		self.ass_store = {}
		self.meth_store = {}
		self.source_loc = {}
		self.keep_class = False
		self.keyword = {}
		self.checked = {}
		self.index = 0		
		self.lines = [name] + source.split('\n') # easier 1based access with lineno
		self.file_name = name
		self.name_scope = {}
		self.actual_scope = None #describes the actual scope. It can either be "Class", "Method" or "Block". Used to distinguish variables with the same name in the assignment store.
			
	def translate_node(self,node,parent,options=None):
		if (node,self.index) in self.checked and self.checked[(node,self.index)] == False:
			if(str(node) == 'CompilationUnit'):
				self.translate_CU(node,parent)				
			elif(str(node) == 'ClassDeclaration'):
				self.translate_CD(node,parent)
			elif(str(node) == 'MethodDeclaration'):
				return self.translate_MD(node,parent)
			elif(str(node) == 'This'):
				return self.translate_T(node,parent)	
			elif(str(node) == 'FieldDeclaration'):
				return self.translate_FD(node,parent)		
			elif(str(node) == 'ConstructorDeclaration'):
				return self.translate_CstD(node,parent)
			elif(str(node) == 'LocalVariableDeclaration'):
				return self.translate_LVD(node,parent)
			elif(str(node) == 'Literal'):
				return self.translate_LIT(node,parent,options)
			elif(str(node) == 'BinaryOperation'):
				return self.translate_BIOP(node,parent)
			elif(str(node) == 'MemberReference'):
				return self.translate_MR(node,parent)
			elif(str(node) == 'StatementExpression'):
				return self.translate_SE(node,parent)
			elif(str(node) == 'Import'):
				self.translate_I(node,parent)
			elif(str(node) == 'VariableDeclarator'):
				return self.translate_VD(node,parent,options)
			elif(str(node) == 'VariableDeclaration'):
				return self.translate_VDN(node,parent)
			elif(str(node) == 'ClassCreator'):
				return self.translate_CC(node,parent)
			elif(str(node) == 'IfStatement'):
				return self.translate_IS(node,parent)
			elif(str(node) == 'WhileStatement'):
				return self.translate_WS(node,parent)
			elif(str(node) == 'ForStatement'):
				return self.translate_FS(node,parent)
			elif(str(node) == 'BlockStatement'):
				return self.translate_BS(node,parent)
			elif(str(node) == 'Assignment'):
				return self.translate_Ass(node,parent)
			elif(str(node) == 'ReturnStatement'):
				return self.translate_RS(node,parent)
			elif(str(node) == 'TypeArgument'):
				return self.translate_TA(node,parent)
			elif(str(node) == 'MethodInvocation'):
				return self.translate_MI(node,parent)
			elif(str(node) == 'ReferenceType'):
				return self.translate_RT(node,parent)
			elif(str(node) == 'ForControl'):
				return self.translate_FC(node,parent)
			elif(str(node) == 'EnhancedForControl'):
				return self.translate_EFC(node,parent)
			elif(str(node) == 'FormalParameter'):
				return self.translate_FP(node,parent)
			elif(str(node) == 'BasicType'):
				return self.translate_BT(node,parent)
			elif(str(node) == 'ArraySelector'):
				return self.translate_AS(node,parent,options)
			elif(str(node) == 'ArrayInitializer'):
				return self.translate_AI(node,parent,options)
			else:
				self.index = self.index + 1
				raise pseudo_java.errors.translation_error('Pseudo-Java cannot translate this node: %s' % str(node),node.position, self.lines[node.position[0]])
	
	#Array Selector
	def translate_AS(self,node,parent,array=None):
		self.index = self.index + 1
		index = self.translate_node(node.index,node,REVERSE_BUILTIN_TYPES[self.ass_store[(array.member,self.name_scope[array.member][-1])]['pseudo_type'][1]])
		if('pseudo_type' in index):
			return {'index':index['value'],'pseudo_type':index['value']['pseudo_type'],'sequence':self.ass_store[(array.member,self.name_scope[array.member][-1])],'type':'index'}
		elif('reference' in index):
			index = self.ass_store[(index['reference'], self.name_scope[index['reference']][-1])]
			return {'index':index,'pseudo_type':index['pseudo_type'],'sequence':self.ass_store[(array.member,self.name_scope[array.member][-1])],'type':'index'}
		else:
			raise pseudo_java.errors.type_check_error('The array selector seems wrong. Try an integer or a int variable. Actual is: %s' % str(node.index),node.position, self.lines[node.position[0]])

	#TypeArgument
	def translate_TA(self,node,parent):
		self.index = self.index + 1
		return self.translate_node(node.type,node)
	
	#Method Invocation
	def translate_MI(self,node,parent):
		self.index = self.index + 1
		if(node.member in BUILTIN_EQUIVALENT_FUNCTIONS):
			message = BUILTIN_EQUIVALENT_FUNCTIONS[node.member]
			args = []
			for arg in node.arguments:
				if str(arg) == 'Literal':
					temp = self.translate_LIT(arg,node,self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type'][1])
				else:
					val = self.translate_node(arg,node)
					temp = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
				args.append(temp)
			if (node.qualifier,self.name_scope[node.qualifier][-1]) in self.ass_store:
				if isinstance(self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type'],list):
					pt = self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type'][-1]
				else:
					pt = self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type']
				if BUILTIN_ARG_FUNCTIONS[node.member] == 'same':
					if pt != temp['pseudo_type']:
						raise pseudo_java.errors.type_check_error('The type of the arguments is not fit for this particular function and its receiver: Arg : %s, Receiver : %s' % (temp['pseudo_type'],pt),node.position,self.lines[node.position[0]])
				return {'args':args,'message':message,'pseudo_type':BUILTIN_TYPE_FUNCTIONS[message],'receiver':self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])],'type':'standard_method_call'}
			else:
				if isinstance(self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type'],list):
					pt = self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type'][-1]
				else:
					pt = self.ass_store[(node.qualifier,self.name_scope[node.qualifier][-1])]['pseudo_type']
				if pt != BUILTIN_ARG_FUNCTIONS[node.member]:
					raise pseudo_java.errors.type_check_error('The type of the arguments is not fit for this particular function and its receiver: Arg : %s, Receiver : %s' % (pt,BUILTIN_ARG_FUNCTIONS[node.member]),node.position,self.lines[node.position[0]])	
				return {'args':args,'function':message,'pseudo_type':BUILTIN_TYPE_FUNCTIONS[message],'namespace':BUILTIN_FUNCTIONS_NAMESPACE[message],'type':'standard_call'}
		elif(node.member in self.meth_store):
			if(self.meth_store[node.member]['name'] != 'Constructor'):
				message = self.meth_store[node.member]
				args = []
				t = 0
				for arg in node.arguments:
					typ = self.meth_store[str(node.member)]['params'][t]['pseudo_type']
					if (isinstance(typ,list)):
						types = []
						for ty in typ:
							types.append(REVERSE_BUILTIN_TYPES[ty])
					else:
						types = REVERSE_BUILTIN_TYPES[typ]
					val = self.translate_node(arg,node,types)
					if 'reference' in val:
						temp = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
					elif 'value' in val and val['type'] == 'assignment' :
						temp = val['value']
					else:
						temp = val
					args.append(temp)
					t = t + 1
				return {'args':args,'function':{'name':message['name'],'pseudo_type':message['pseudo_type'],'type':'local'},'pseudo_type':message['return_type'],'type':'call'}
			else:
				args = []
				t = 0
				for arg in node.arguments:
					if str(arg) == 'Literal':
						temp = self.translate_LIT(arg,node,REVERSE_BUILTIN_TYPES[self.meth_store[str(node.member)]['params'][t]['pseudo_type']])
					else:
						val = self.translate_node(arg,node)
						temp = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
					args.append(temp)
					t = t + 1
				return {'args':args,'class_name':node.member,'pseudo_type':node.member,'type':'new_instance'}
		else:
			raise pseudo_java.errors.type_check_error('Method or function not yet translatable by Pseudo-Java : %s' %str(node.member),node.position, self.lines[node.position[0]])
			print("Function or method not translated yet "+str(node.member))
			print(self.meth_store)
	
	#Return Statement
	def translate_RS(self,node,parent):
		self.index = self.index + 1
		temp = self.translate_node(node.expression,node)
		if(str(node.expression) == 'MemberReference'):
			mr = self.ass_store[(temp['reference'],self.name_scope[temp['reference']][-1])]
			pt = mr['pseudo_type']
			val = mr
		else:
			val = temp['value']
			pt = val['pseudo_type']
		return {'pseudo_type':pt,'type':'implicit_return','value':val}
	
	#Block Statement			
	def translate_BS(self,node,parent):
		self.index = self.index + 1
		scope = self.actual_scope
		self.actual_scope = 'Block'
		res = []
		for n in node.statements:
			res.append(self.translate_node(n,node))
		self.actual_scope = scope
		for ass in list(self.ass_store):
			if ass[1] == 'Block':
				self.ass_store.pop(ass)
				self.name_scope[ass[0]].pop()
		return res
	
	#Variable Declarator
	def translate_VD(self,node,parent,typ=None):
		self.index = self.index + 1
		if(node.initializer != None):
			init = self.translate_node(node.initializer,node,typ)
			if typ != None:
				if node.name in self.name_scope:
					self.name_scope[node.name].append(self.actual_scope)				
				else:
					self.name_scope[node.name] = [self.actual_scope]
				self.ass_store[(node.name,self.actual_scope)] = {'name':node.name,'pseudo_type':BUILTIN_TYPES[typ],'type':'local'}
		else:
			init = None
			if node.name in self.name_scope:
				self.name_scope[node.name].append(self.actual_scope)				
			else:
				self.name_scope[node.name] = [self.actual_scope]
			self.ass_store[(node.name,self.actual_scope)] = {'name':node.name,'pseudo_type':BUILTIN_TYPES[typ],'type':'local'}
		return {'target':node.name,'init':init}
	
	#Variable Declaration
	def translate_VDN(self,node,parent):
		self.index = self.index + 1
		for d in node.declarators:
			if (str(node.type) == 'ReferenceType'):
				if(node.type.dimensions == []):
					bt = self.translate_node(node.type,node)
					t = self.translate_node(d,node,bt['name'])
					if(node.type.name == 'String'):
						if(d.initializer == None):
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':""}						
						elif(str(d.initializer) == 'MemberReference'):
							val = self.ass_store[(t['target'],self.name_scope[t['target']][-1])]
						else:
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':str(d.initializer.value)}
					else:
						raise('Reference type not covered by Pseudo-Java: %s' %node.type.name,node.position,self.lines[node.position[0]])
						print('Type not supported '+node.type.name)
						return None
					if d.name in self.name_scope:
						self.name_scope[d.name].append(self.actual_scope)				
					else:
						self.name_scope[d.name] = [self.actual_scope]
					self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
					return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val}
				else:
					raise pseudo_java.errors.type_check_error('Reference type %s not covered by Pseudo-Java' % node.type.name, node.position,self.lines[node.position[0]])
			elif(str(node.type) == 'BasicType'):
				if(node.type.dimensions == []):
					bt = self.translate_node(node.type,node)
					t = self.translate_node(d,node,bt['name'])
					if(node.type.name == 'int'):
						if(d.initializer == None):
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':0}
						elif(str(d.initializer) == 'MemberReference'):
							val = self.ass_store[(t['init']['reference'],self.name_scope[t['init']['reference']][-1])]
						else:
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':int(d.initializer.value)}
					elif(node.type.name == 'float'):
						if(d.initializer == None):
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':0.0}
						elif(str(d.initializer) == 'MemberReference'):
							val = self.ass_store[(t['init']['reference'],self.name_scope[t['init']['reference']][-1])]
						else:
							val = {'pseudo_type':BUILTIN_TYPES[node.type.name],'type':node.type.name,'value':float(d.initializer.value)}
					else:
						print('Type not supported '+node.type.name)
						raise pseudo_java.errors.type_check_error('Basic type %s not covered by Pseudo-Java' % node.type.name, node.position,self.lines[node.position[0]])
					if d.name in self.name_scope:
						self.name_scope[d.name].append(self.actual_scope)				
					else:
						self.name_scope[d.name] = [self.actual_scope]
					self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
					return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val}
				else:
					self.index = self.index + 1
					if(str(d.initializer) == 'ArrayInitializer'):
						val = self.translate_node(d.initializer,node,node.type.name)
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':val['pseudo_type'],'type':'local'},'value':val}
			else:
				raise pseudo_java.errors.type_check_error('Reference type %s not covered by Pseudo-Java' % node.type.name, node.position,self.lines[node.position[0]])
	
	
	#For Control
	def translate_FC(self,node,parent):
		self.index = self.index + 1
		init = self.translate_node(node.init,node)
		condition = self.translate_node(node.condition,node)
		update = self.translate_node(node.update[0],node)
		return {"init":init,"condition":condition,"update":update}
	
	#Enhanced For Control
	def translate_EFC(self,node,parent):
		self.index = self.index + 1
		var = self.translate_node(node.var,node)
		iterable = self.translate_node(node.iterable,node)
		return {'var':var,'iterable':iterable}
	
	#For Statement
	def translate_FS(self,node,parent):
		self.index = self.index + 1
		block = []
		if(str(node.control) == "ForControl"):
			test = self.translate_node(node.control,node)
			block= self.translate_node(node.body,node)
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
	def translate_WS(self,node,parent):
		self.index = self.index + 1
		test = self.translate_node(node.condition,node)
		block = self.translate_node(node.body,node)
		return{'block':block,'pseudo_type':'Void','type':'while_statement','test':test['value']}
	
	#If Statement
	def translate_IS(self,node,parent):
		self.index = self.index + 1
		test = self.translate_node(node.condition,node)
		block = self.translate_node(node.then_statement,node)
		other_block = self.translate_node(node.else_statement,node)
		if other_block != None:
			otherwise = {'block':other_block,'pseudo_type':'Void','type':'else_statement'}
		else:
			otherwise = None
		return{'block':block,'otherwise':otherwise,'pseudo_type':'Void','type':'if_statement','test':test['value']}
	
		
	#Imports
	def translate_I(self,node,parent):
		self.index = self.index + 1
		if node.path not in JAVA_KNOWN_IMPORTS:
			print(node)
	
	#Assignment node
	def translate_Ass(self,node,parent):
		self.index = self.index + 1
		member = self.translate_node(node.expressionl,node)
		val = self.translate_node(node.value,node)
		if member == None or 'reference' not in val:
			return val
		elif 'selectors' in member and member['selectors'] != []:
			target = member['selectors'][0]
			if val['selectors'] != []:
				value = val['selectors'][0]
			else:
				value = self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])]
			return {'value':value,'target':target,'type':'assignment','pseudo_type':'Void'}
		else:
			return {'value':self.ass_store[(val['reference'],self.name_scope[val['reference']][-1])],'target':self.ass_store[(member[0]['reference'],self.name_scope[member[0]['reference']][-1])],'type':'assignment','pseudo_type':'Void'}
	
	#Statement Expression
	def translate_SE(self,node,parent):
		#todo with first argument 
		self.index = self.index + 1
		ret = self.translate_node(node.expression,node)
		if str(node.expression) == 'MemberReference' and ret['postfix_op'] != []:
			if ret['postfix_op'] == ['++']:
				op = '+'
			elif ret['postfix_op'] == ['--']:
				op = '-'
			else:
				raise pseudo_java.errors.type_check_error('Postfix operator not known by Pseudo-Java %s' %ret['postfix_op'],node.position,self.lines[node.position[0]])
				print("Postfix operator not known")
				return {}
			target = self.ass_store[(ret['reference'],self.name_scope[ret['reference']][-1])]
			return {'pseudo_type':'Void','target':target,'type':'assignment','value':{'left':target,'op':op,'pseudo_type':target['pseudo_type'],'right':{'pseudo_type': target['pseudo_type'], 'type': REVERSE_BUILTIN_TYPES[target['pseudo_type']], 'value': 1},'type':'binary_op'}}
		elif str(node.expression) == 'MemberReference' and ret['prefix_op'] != []:
			return {}
		return ret
	
	
	#MemberReference
	def translate_MR(self,node,parent):
		self.index = self.index + 1
		selectors = []
		if node.selectors:
			for s in node.selectors:
				selectors.append(self.translate_node(s,node.member,node))
		return {'reference':node.member,'prefix_op':node.prefix_operators,'postfix_op':node.postfix_operators,'qualifier':node.qualifier,'selectors':selectors}
	
	#Binary Operation
	def translate_BIOP(self,node,parent):
		self.index = self.index + 1
		if(str(node.operandl) == 'MemberReference'):
			opl = self.translate_node(node.operandl,node)
			if 'selectors' in opl and opl['selectors'] != []:
				target = opl['selectors'][0]
			else:
				target = self.ass_store[(node.operandl.member,self.name_scope[node.operandl.member][-1])]
		elif(str(node.operandl) == 'BinaryOperation'):
			temp = self.translate_node(node.operandl,node)
			target = temp['value']
		else:
			raise pseudo_java.errors.type_check_error('Operand left not yet treated by Pseudo-Java',node.position,self.lines[node.position[0]])
			print("Operand left not yet treated")
		if(str(node.operandr) == "Literal"):
			val = self.translate_node(node.operandr,node, REVERSE_BUILTIN_TYPES[target['pseudo_type']])
			right = val
		elif(str(node.operandr) == "MemberReference"):
			opr = self.translate_node(node.operandr,node)
			if 'selectors' in opr and opr['selectors'] != []:
				val = opr['selectors'][0]
			else:
				val = self.ass_store[(node.operandr.member,self.name_scope[node.operandr.member][-1])]
			right = val
		else:
			raise pseudo_java.errors.type_check_error('Operand right not yet treated by Pseudo-Java',node.position,self.lines[node.position[0]])
			print("Operand right not yet treated")
		if(node.operator in PSEUDO_BINARY_OPS):
			p_typ = target['pseudo_type']
			typ = 'binary_op'
		else:
			p_typ = 'Boolean'
			typ = 'comparison'
		res = {'pseudo_type':'Void','type':'assignment','target':target,'value':{'left':target,'op':node.operator,'pseudo_type':p_typ,'right':right,'type':typ}}
		return res
	
	#Literal
	def translate_LIT(self,node,parent,typ=None):
		self.index = self.index + 1
		if(typ != None):
			return {'pseudo_type':BUILTIN_TYPES[typ],'type':typ,'value':self.w_type(node.value)}
		else:
			return None
	
			
	#LocalVariableDeclaration
	def translate_LVD(self,node,parent):
		self.checked[(node,self.index)] = True
		self.index = self.index + 1
		for d in node.declarators:
			if (str(node.type) == 'ReferenceType'):
				if(node.type.dimensions == []):
					self.translate_node(node.type,node)
					self.translate_node(d,node)
					if(node.type.name == 'String'):
						val = str(d.initializer.value.strip('\"'))
						typ = node.type.name
					elif(node.type.name == 'ArrayList'):
						typ = node.type.arguments[0].type.name
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':['List', BUILTIN_TYPES[typ]],'type':'local'}
						val = {'elements':[],'type':'list','pseudo_type':['List',BUILTIN_TYPES[typ]]} #Elements are always empty since you can't initialize a non-empty ArrayList in Java
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':['List',BUILTIN_TYPES[typ]],'type':'local'},'value':val}
					else:
						raise pseudo_java.errors.type_check_error('Reference type not covered by Pseudo-Java : %s' %node.type.name,node.position,self.lines[node.position[0]])
						print('Type not supported '+node.type.name)
						return None				
					if d.name in self.name_scope:
						self.name_scope[d.name].append(self.actual_scope)				
					else:
						self.name_scope[d.name] = [self.actual_scope]
					print(val)
					self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
					return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':['List',BUILTIN_TYPES[typ]],'type':'local'},'value':val}
				else:
					if(str(d.initializer) == 'ArrayInitializer'):
						bt = self.translate_node(node.type,node)
						val = self.translate_node(d,node,node.type.name)
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':['List', BUILTIN_TYPES[node.type.name]],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':['List',BUILTIN_TYPES[node.type.name]],'type':'local'},'value':val['init']}
					else:
						raise pseudo_java.errors.type_check_error('Type %s not covered by Pseudo-Java' % str(d.initializer), node.position,self.lines[node.position[0]])
			elif(str(node.type) == 'BasicType'):
				if(node.type.dimensions == []):
					if(str(d.initializer) == 'Literal'):
						self.translate_node(node.type,node)
						v = self.translate_node(d,node,node.type.name)
						if(node.type.name == 'int' or node.type.name == 'float'):
							val = v['init']
						else:
							raise pseudo_java.errors.type_check_error('Type not covered by Pseudo-Java: %s' %node.type.name,node.position,self.lines[node.position[0]])
							print('Type not supported '+node.type.name)
							return None
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val}
					elif(str(d.initializer) == 'BinaryOperation'):
						self.translate_node(node.type,node)
						val = self.translate_node(d,node)
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
						if 'init' in val:
							val = val['init']
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val['value']}
					elif(str(d.initializer) == 'MethodInvocation'):
						bt = self.translate_node(node.type,node)
						mi = self.translate_node(d,node)
						val = mi['init']
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':BUILTIN_TYPES[node.type.name],'type':'local'},'value':val}
					elif(str(d.initializer) == 'MemberReference'):
						bt = self.translate_node(node.type,node)
						mr = self.translate_node(d,node)
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
					elif(str(d.initializer) == 'ArrayInitializer'):
						bt = self.translate_node(node.type,node)
						val = self.translate_node(d,node,bt['name'])
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':val['init']['pseudo_type'],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':val['init']['pseudo_type'],'type':'local'},'value':val['init']}
					else:
						raise pseudo_java.errors.type_check_error('Basic type %s not covered by Pseudo-Java' % node.type.name, node.position,self.lines[node.position[0]])
						
				else:
					if(str(d.initializer) == 'ArrayInitializer'):
						bt = self.translate_node(node.type,node)
						val = self.translate_node(d,node,bt['name'])
						if d.name in self.name_scope:
							self.name_scope[d.name].append(self.actual_scope)				
						else:
							self.name_scope[d.name] = [self.actual_scope]
						self.ass_store[(d.name,self.actual_scope)] = {'name':d.name,'pseudo_type':val['init']['pseudo_type'],'type':'local'}
						return {'pseudo_type':'Void','type':'assignment','target':{'name':d.name,'pseudo_type':val['init']['pseudo_type'],'type':'local'},'value':val['init']}
					else:
						raise pseudo_java.errors.type_check_error('Type %s not covered by Pseudo-Java' % str(d.initializer), node.position,self.lines[node.position[0]])
			else:
				raise pseudo_java.errors.type_check_error('Type not covered by Pseudo-Java: %s' %node.type,node.position,self.lines[node.position[0]])	

	
	#Array Initializer
	def translate_AI(self,node,parent,typ=None):
		self.index = self.index + 1
		e = []
		for n in node.initializers:
			e.append(self.translate_node(n,node,typ))
		pt = ['List',BUILTIN_TYPES[typ]]
		for _ in range(0,len(node.initializers)-1):
			if str(n) == 'ArrayInitializer':
				pt = ['List',pt]
		return {'elements':e,'pseudo_type':pt,'type':'list'}
	
	
	#Formal Parameter
	def translate_FP(self,node,ret=False):
		if (node,self.index) in self.checked:
			self.checked[(node,self.index)] = True
		self.index = self.index + 1	
		if (str(node.type) == 'ReferenceType'):
			if node.type.dimensions == []:
				pt = node.type.name
			else:
				pt = []
				pt.append('List')
				pt.append(node.type.name)
			self.translate_node(node.type,node)
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
			self.translate_node(node.type,node)
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
			raise pseudo_java.errors.type_check_error('Type not covered by Pseudo-Java: %s' %node.type,node.position,self.lines[node.position[0]])
				
			
	#Reference Type
	def translate_RT(self,node,parent):
		if (node,self.index) in self.checked:
			self.checked[(node,self.index)] = True
		self.index = self.index + 1
		if node.arguments != None:
			for arg in node.arguments:
				self.translate_node(arg,node)
	
	
	#BasicType
	def translate_BT(self,node,parent):
		if (node,self.index) in self.checked:
			self.checked[(node,self.index)] = True
		self.index = self.index + 1
		return {'name':node.name,'dimensions':node.dimensions}
	
	
	
	#Method declaration
	def translate_MD(self,node,parent):
		self.main_block = []
		scope = self.actual_scope
		self.actual_scope = 'Method'
		pt = []
		pt.append('Function')
		if (node,self.index) in self.checked:
			self.checked[(node,self.index)] = True
		self.index = self.index + 1
		p = []
		if(node.return_type != None):
			ret = self.translate_node(node.return_type,node)
			rt = BUILTIN_TYPES[ret['name']]
		else:
			rt = 'Void'
		for param in node.parameters:
			temp = self.translate_node(param,node)
			p.append(temp[1])
			if temp[1]['name'] in self.name_scope:
					self.name_scope[temp[1]['name']].append(self.actual_scope)				
			else:
				self.name_scope[temp[1]['name']] = [self.actual_scope]
			self.ass_store[(temp[1]['name'],self.actual_scope)] = temp[1]
			pt.append(temp[0])
		self.meth_store[str(node.name)] = {'name':str(node.name),'class':str(parent.name),'return_type':rt,'pseudo_type':pt,'params':p}
		body = None
		for op in node.body:
			body = self.translate_node(op,node)
			if body != None:
				self.main_block.append(body)
		pt.append(rt)
		self.actual_scope = scope		
		temp = self.ass_store
		for ass in list(self.ass_store):
			if ass[1] == 'Method':
				self.ass_store.pop(ass)
				self.name_scope[ass[0]].pop()
		if(node.name == 'main'):
			self.main = self.main_block
			return None
		else:
			if(parent.name == self.file_name and self.keep_class == False):
				return {'block':self.main_block,'name':node.name,'params':p,'pseudo_type':pt,'return_type':rt,'type':'function_definition'}
			else:
				return {'block':self.main_block,'is_public':True,'name':node.name,'params':p,'pseudo_type':pt,'return_type':rt,'this':{'name':parent.name,'type':'typename'},'type':'method_definition'}
	
	#Field Declaration
	def translate_FD(self,node,parent):
		self.index = self.index + 1
		typ = []
		typ.append(self.translate_node(node.type,node))
		decl = []
		for (d,t) in zip(node.declarators,typ):
			decl.append(self.translate_node(d,node,t['name']))
		if(node.modifiers == {'public'}):
			is_p = True
		else:
			is_p = False
		self.ass_store[(decl[0]['target'],self.actual_scope)]['type'] = 'instance_variable'
		return {'is_public':is_p,'type':'class_attr','pseudo_type':BUILTIN_TYPES[typ[0]['name']],'name':decl[0]['target']}
	
	#This
	def translate_T(self,node,parent):
		#todo:pay attention to scope
		self.index = self.index + 1
		self.keep_class = True
		a = []
		selectors = []
		if node.selectors:
			for s in node.selectors:
				selectors.append(self.translate_node(s,node))
		return selectors		
		
	#Constructor Declaration
	def translate_CstD(self,node,parent):
		self.index = self.index + 1
		self.keep_class = True
		params = []
		for p in node.parameters:
			params.append(self.translate_node(p,node)[1])
		body = []
		for b in node.body:
			body.append(self.translate_node(b,node))
		if node.throws == None:
			rt = 'Void'
		else:
			rt = self.translate_node(node.throws,node)
		self.meth_store[str(node.name)] = {'name':'Constructor','class':str(node.name),'return_type':rt,'pseudo_type':'Void','params':params}
		return {'name':'__init__','block':body,'return_type':rt,'pseudo_type':['Function','Int',node.name],'params':params,'this':{'name':node.name,'type':'typename'},'type':'constructor'}
	
	#Class Declaration
	def translate_CD(self,node,parent):
		scope = self.actual_scope
		self.actual_scope = 'Class'
		if (node,self.index) in self.checked:
			self.checked[(node,self.index)] = True
		self.index = self.index + 1
		attrs = []
		base = None
		constructor = None
		definitions = []
		for f in node.fields:
			field = self.translate_node(f,node)
			if field != None:
				attrs.append(field)
		for c in node.constructors:
			const = self.translate_node(c,node)
			if const != None:
				constructor = const
		for m in node.methods:
			meth = self.translate_MD(m,node)
			if meth != None:
					definitions.append(meth)
					if(meth['name'] == node.name):
						constructor = meth
		if(self.keep_class == False):
			self.definitions = definitions
		else:
			self.definitions = [{'attrs':attrs,'base':base,'constructor':constructor,'methods':definitions,'name':node.name,'type':'class_definition'}]
		for ass in list(self.ass_store):
			if ass[1] == 'Class':
				self.ass_store.pop(ass)
				self.name_scope[ass[0]].pop()
		self.actual_scope = scope
		self.index = self.index + 1
	
	#Class Creator
	def translate_CC(self,node,parent):
		self.index = self.index + 1
		self.translate_node(node.type,node)	
		
	#Compilation Unit. The first node of a compilable program is always this one.
	def translate_CU(self,node,parent):
		if (node,self.index) in self.checked:
			self.checked[(node,self.index)] = True
		self.index = self.index + 1
		if node.package:
			for p in node.package:
				self.translate_node(p,node)
		if node.imports:
			for i in node.imports:
				self.translate_node(i,node)
		if node.types:
			for t in node.types:
				self.translate_node(t,node)
			
	#Begin the translation by creating a tuple with each node and its index that will be used as an unique key
	#Translate each node after that.	
	def walk_tree(self,tree):
		index = 0
		for path,node in tree:
			if (node,index) not in self.checked:#create unique and distinguishable key
				self.checked[(node,index)] = False
			index = index + 1
		temp = None
		for path,node in tree:
			self.translate_node(node,temp)
			temp = node
			

	def Test(self,name,source,options):
		if options == '-o':
			self.keep_class = True
		self.translate(name,source)
		tree = javalang.parse.parse(source)
		self.walk_tree(tree)
		trad = {'constants':self.constants,'custom_exceptions':self.custom_exceptions,'definitions':self.definitions,'dependencies':self.dependencies,'main':self.main,'type':'module'}
		return trad
	

