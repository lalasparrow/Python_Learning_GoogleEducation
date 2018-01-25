Introduction

Imports, Command-line arguments, and len()
	1. len(sys.argv)
	2. "module"就是import的东西，A Python module can be run directly — as above "python hello.py Bob" — or it can be imported and used by some other module.
	3. run的时候，the special variable "__name__" is set to "__main__". 
	   Therefore, it is common to have the boilerplate if __name__ ==... shown above to call a main() function when the module is run directly, but not when the module is imported by some other module.
	

User-defined Functions
	1. result = s + s + s    <=>     result = s*3
		(*号要快些，因为一次就计算了size of result object)
	2. + 和 *	"overloaded" operaters；因为对于string和数字来说有不同的意义
	3. docstring:

	def repeat(s, exclaim):
	    """
	    Returns the string 's' repeated 3 times.
	    If exclaim is true, add exclamation marks.
	    """

Indentation

Code Checked at Runtime
	1. 如果typo不被执行，是不会被发现的，typo以外的部分会正常run

Variable Names
	1. 'str' 和 'list' 会override system variable

More on Modules and their Namespaces
	1. module1.foo    calls module1 中的 foo()
	   module2.foo    calls module2 中的 foo()
	   不会有冲突
	2. Python Standard Library
		sys — access to exit(), argv, stdin, stdout, ...
		re — regular expressions
		os — operating system interface, file system