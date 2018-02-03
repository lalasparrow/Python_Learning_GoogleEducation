Python Sorting
	1. Contents
		用sorted()来sort一个list，返回一个新的list，原来的list不变
			
			a = [5, 1, 4, 3]
			print sorted(a)  ## [1, 3, 4, 5]
			print a  ## [5, 1, 4, 3]

		sorted()可以有optional arguments。e.g. sorted(list, reverse=True), 可以按由大到小sort
			
			strs = ['aa', 'BB', 'zz', 'CC']
			print sorted(strs)  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
			print sorted(strs, reverse=True)   ## ['zz', 'aa', 'CC', 'BB']
	
	2. Custom Sorting With key=
		可以用"key="来自定义一个"key"function，在比较之前transform each element
	    The key function takes in 1 value and returns 1 value, and the returned "proxy" value is used for the comparisons within the sort.
		
			e.g.    
			    strs = ['ccc', 'aaaa', 'd', 'bb']
				print sorted(strs, key=len)  ## ['d', 'bb', 'ccc', 'aaaa']

				_____________________________
			   | 'ccc' | 'aaaa' | 'd' | 'bb' |
			    -----------------------------
			
			key=len|       |      |     |
			
				_____________________________
		 proxy |   3   |    4   |  1  |  2   |
		 value	-----------------------------

	sort the original list  |
	using the proxy value	|
	       		_____________________________
	       	   | 'd' | 'bb' | 'ccc' | 'aaaa' |
				-----------------------------


			e.g. "str.lower" as the key function，to force the sorting to treat uppercase and lowercase the same:
			    ## "key" argument specifying str.lower function to use for sorting
	  			print sorted(strs, key=str.lower)  ## ['aa', 'BB', 'CC', 'zz']



	  		e.g. 也可以自己定义一个MyFn当做key function:
	  		    ## Say we have a list of strings we want to sort by the last letter of the string.
				strs = ['xc', 'zb', 'yd' ,'wa']

				## Write a little function that takes a string, and returns its last letter.
				## This will be the key function (takes in 1 value, returns 1 value).
				def MyFn(s):
				return s[-1]

				## Now pass key=MyFn to sorted() to sort by the last letter:
				print sorted(strs, key=MyFn)  ## ['wa', 'zb', 'xc', 'yd']

		也可以用"cmp=cmpFn"在sorted()里面当argument。用两个参数来比较，返回negative/0/positive来排列顺序。
			e.g. cmp(a,b)

	3. sort() method
		和sorted()是一样的，可以sort一个list，变成升序排列。改变原来的list，返回None
			
			e.g.
			    alist.sort()            ## correct
  				alist = blist.sort()    ## NO incorrect, sort() returns None

  		但是sort()只能用在list上，不能用在任何enumerable collection里面（但是sorted()可以）
  		sort()不用创建一个新的list，所以，sort()会在元素已经在list里时，sort的快一些

  	4. Tuples
  		A tuple is a fixed size grouping of elements, such as an (x, y) co-ordinate. 
  		Tuples are like lists, except they are immutable and do not change size (tuples are not strictly immutable since one of the contained elements could be mutable).
  		Tuple里面的len(), [], for, in, etc.都和list里面一样的。
  		"empty" tuple: ()

  			tuple = (1, 2, 'hi')
			print len(tuple)  ## 3
			print tuple[2]    ## hi
			tuple[2] = 'bye'  ## NO, tuples cannot be changed
			tuple = (1, 2, 'bye')  ## this works

		size-1 tuple需要加一个comma

			tuple = ('hi',)   ## size-1 tuple

		(x, y, z) = (42, 13, "hike")  ## 对应的element得到对应的值
		print z  ## hike
		(err_string, err_code) = Foo()  ## Foo() returns a length-2 tuple
										## 两个tuple的大小不同，会throw an error

	5. List Comprehensions(optional)
		A list comprehension is a compact way to write an expression that expands to a whole list. 
			e.g. 假设有list nums[1,2,3,4], 用list comprehension来计算他们平方的list[1,4,9,16]:
			
			nums = [1, 2, 3, 4]
			squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]

		syntax是 [expr for var in list] -- for var in list和for-loop相同，但是没有冒号(:)
		expr是得到新list的方法，每个element都过一遍expr

			e.g. 每个元素变成大写，并且append上"!!!"
			strs = ['hello', 'and', 'goodbye']
			shouting = [ s.upper() + '!!!' for s in strs ]
			## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

		也可以在后面加上一个if，只有满足if的element才会被选中

			e.g.
				## Select values <= 2
				nums = [2, 8, 1, 6]
				small = [ n for n in nums if n <= 2 ]  ## [2, 1]

				## Select fruits containing 'a', change to upper case
				fruits = ['apple', 'cherry', 'bannana', 'lemon']
				afruits = [ s.upper() for s in fruits if 'a' in s ]
				## ['APPLE', 'BANNANA']














