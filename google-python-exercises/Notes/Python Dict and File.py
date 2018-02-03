Python Dict and File
	1. Dict Hash Table
		Python的key/value hashtable structure 叫做 "dict".
		可以写成一系列的key:value pairs within braces {}, e.g. dict = {key1:value1, key2:value2, ...}
		"empty dict" 即 {}

		look up or setting a value用[], e.g. dict['foo']查找所有key是'foo'的value
		strings, numbers, and tuples 可以作为key，任何type可以是value（因为string和tuple是immutable的）
		查找dict中没有的key会throws a KeyError 
		-- 用"in"来check key是不是在dict
		-- 用dict.get(key) which returns the value or None if the key is not present
		-- 或者get(key, not-found)
			e.g.
				## Can build up a dict by starting with the the empty dict {}
				## and storing key/value pairs into the dict like this:
				## dict[key] = value-for-that-key
				dict = {}
				dict['a'] = 'alpha'
				dict['g'] = 'gamma'
				dict['o'] = 'omega'

				print dict  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

				print dict['a']     ## Simple lookup, returns 'alpha'
				dict['a'] = 6       ## Put new key/value into dict
				'a' in dict         ## True
				## print dict['z']                  ## Throws KeyError
				if 'z' in dict: print dict['z']     ## Avoid KeyError
				print dict.get('z')  ## None (instead of KeyError)


		用一个for loop来遍历keys。key的顺序是任意顺序。
		dict.keys() and dict.values() return lists of the keys or values explicitly
		items() returns a list of (key, value) tuples.检查dict中key value最efficient的方法
		这些lists都可以扔到sorted()里面
			e.g.
				## By default, iterating over a dict iterates over its keys.
				## Note that the keys are in a random order.
				for key in dict: print key
				## prints a g o

				## Exactly the same as above
				for key in dict.keys(): print key

				## Get the .keys() list:
				print dict.keys()  ## ['a', 'o', 'g']

				## Likewise, there's a .values() list of values
				print dict.values()  ## ['alpha', 'omega', 'gamma']

				## Common case -- loop over the keys in sorted order,
				## accessing each key/value
				for key in sorted(dict.keys()):
				print key, dict[key]

				## .items() is the dict expressed as (key, value) tuples
				print dict.items()  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

				## This loop syntax accesses the whole dict by looping
				## over the .items() tuple list, accessing one (key, value)
				## pair on each iteration.
				for k, v in dict.items(): print k, '>', v
				## a > alpha    o > omega     g > gamma
 		
		"iter" of these methods called iterkeys(), itervalues() and iteritems(), 可以避免建立整个list，在data is huge的时候performance比较好

 	2. Dict Formatting
 		用%可以在string里，替换dict里面的value
 			e.g.
				hash = {}
				hash['word'] = 'garfield'
				hash['count'] = 42
				s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
				# 'I want 42 copies of garfield'

	3. Del
	用来delete。也可以用在list elements或者slices，来删除部分list和entries from a dictionary
		e.g.
			var = 6
			del var  # var no more!

			list = ['a', 'b', 'c', 'd']
			del list[0]     ## Delete first element
			del list[-2:]   ## Delete last two elements
			print list      ## ['b']

			dict = {'a':1, 'b':2, 'c':3}
			del dict['b']   ## Delete 'b' entry
			print dict      ## {'a':1, 'c':3}


	4. Files
		open()返回并且return a file handle（用来读或者写file）。
		f = open('name','r') opens the file int the variable f，准备ready operations，用f.close() when finish
		'r'  -- reading
		'w'  -- writing
		'a'  -- append
		'rU' -- "Universal" option for text files where it's smart about converting different line-endings so they always come through as a simple '\n'. 
		普通的for-loop works for text files，遍历file的每一行（this works only for text files, not binary files）

			e.g.
				# Echo the contents of a file
				f = open('foo.txt', 'rU')
				for line in f:   ## iterates over the lines of the file
				  print line,    ## trailing , so print does not add an end-of-line char
								 ## since 'line' already includes the end-of line.
				f.close()

		f.readlines()可以读整个file into memory，并且返回一个list of its lines。
		f.read() 可以读整个file into a single string，这样使用regular expressions的时候比较方便

		对于writing来说，
			--f.write(string)是the easiest way to write data to an open output file
			--也可以用"print"，syntax: "print >> f, string"。在python 3000里，syntax变成一个function，argument是file，"print(string, file=f)"

	5. Files Unicode
		"codecs" module provides support for reading a unicode file.
			e.g.
				import codecs

				f = codecs.open('foo.txt', 'rU', 'utf-8')
				for line in f:
				  # here line is a *unicode* string

		对于writing来说，用f.write()，因为print does not fully suppo unicode











