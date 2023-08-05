#Some imports in Java are not useful in Ruby/Python and can be resolved immediately.
JAVA_KNOWN_IMPORTS = {
	'java.util.Map' : 'Dictionary',
	'java.util.HashMap' : 'Dictionary',
	'java.util.ArrayList' : 'List',
	'java.util.List' : 'List',
	'java.util.LinkedList' : 'List',
	'java.util.Set':	'Set',
	'java.util.HashSet':	'Set'
}


#######
#Functions#

BUILTIN_FUNCTIONS = {'System.out.println','System.out.print', 'print','println','length', 'all', 'sum','add','index','remove','get','keySet','values'}

BUILTIN_EQUIVALENT_FUNCTIONS = {'add':{'List':'push','Set':'add'},
				'remove':{'List':'remove','Set':'remove'},
				'println':'display',
				'print':'display',
				'size':'length',
				'get':'index',
				'put':'index',
				'containsKey':'contains?',
				'keySet':'keys',
				'values':'values'}

BUILTIN_ARG_FUNCTIONS = {'add':'same',
			'remove':'Int',
			'print':'String',
			'println':'String',
			'size':None,
			'get':'Int',
			'put':'same',
			'containsKey':'same',
			'keySet':None,
			'values':None}

BUILTIN_TYPE_FUNCTIONS = {'length':'Int',
			'push':'Void',
			'display':'Void',
			'remove':'Void',
			'index':'Void',
			'contains?':'Boolean',
			'add':'Void',
			'keys':['Set','@k'],
			'values':['List','@v']}

PARTICULAR_FUNCTIONS = {'index'}

