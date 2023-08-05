import pseudo_java.java_ast_translator
import yaml

def translate(name,source,options):
	j = java_ast_translator.JavaASTTranslator()
	return j.Test(name,source,options)

def translate_to_yaml(name,source):
	translation = translate(name,source,None)
	print(translation)
	noaliases = yaml.dumper.SafeDumper
	noaliases.ignore_aliases = lambda self, data: True
	return yaml.dump(translation,Dumper = noaliases)
