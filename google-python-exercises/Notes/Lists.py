Lists

Contents
	1. list 也用len()算长度，第一个element的index是0

		  colors = ['red', 'blue', 'green']
		  print colors[0]    ## red
		  print colors[2]    ## green
		  print len(colors)  ## 3


							_____ ______ _______
		  colors   ->      |'red'|'blue'|'green'|
		  					----- ------ -------
		  			list	  0      1      2

	2. = 不是copy，而是makes the two variables point to the one list in memory
		  
		  b = colors   ## Does not copy the list
							_____ ______ _______
		  colors   ->      |'red'|'blue'|'green'|
		  					----- ------ -------
		  			list	  0      1      2

	3. empty list <=> []
	4. '+'把两个list合并在一起
		e.g. [1,2] + [3,4] => [1,2,3,4]


FOR and IN
	FOR
	用for var in list来遍历list里面的element

	  squares = [1, 4, 9, 16]
	  sum = 0
	  for num in squares:
	    sum += num
	  print sum  ## 30
	

	IN
	用value in collection来测试value是否在collection里面，returning True/False

	  list = ['larry', 'curly', 'moe']
	  if 'curly' in list:
	    print 'yay'

	FOR/IN 也可以用在string里面。String好像 a list of its chars
		因此如果prints all the chars in a string，用
			for ch in s: 
				print ch 
		
	1. Range
	range(n)用来产生0,1,...,n-1
	range(a,b)用来产生a,a+1,...,b-1 不包括b

		用for和range()可以写一个for循环：
		  ## print the numbers from 0 through 99
		  for i in range(100):
		    print i

	2. While Loop
	break和continue在python中也可以使用
		Here's a while loop which accesses every 3rd element in a list:
			  ## Access every 3rd element in a list
			  i = 0
			  while i < len(a):
			    print a[i]
			    i = i + 3

	3. List Methods
		Here are some other common list methods.

		list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
		list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
		list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
		list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
		list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
		list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
		list.reverse() -- reverses the list in place (does not return it)
		list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

		***Notice that these are *methods* on a list object, while len() is a function that takes the list (or string or whatever) as an argument.***


			list = ['larry', 'curly', 'moe']
			list.append('shemp')         ## append elem at end
			list.insert(0, 'xxx')        ## insert elem at index 0
			list.extend(['yyy', 'zzz'])  ## add list of elems at end
			print list  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
			print list.index('curly')    ## 2

			list.remove('curly')         ## search and remove that element
			list.pop(1)                  ## removes and returns 'larry'
			print list  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

		***所有以上的methods，都是在原来list基础上modify，并不返回一个新的list***

		    list = [1, 2, 3]
		    print list.append(4)   ## NO, does not work, append() returns None
		    ## Correct pattern:
		    list.append(4)
		    print list  ## [1, 2, 3, 4]

	4. List Build Up

		先建一个[]，然后在里面append()或者extend()来增加elements
		  list = []          ## Start as the empty list
		  list.append('a')   ## Use append() to add elements
		  list.append('b')

	5. List Slices
		和在string里差不多，可以用来替换sub-parts of the list
		    list = ['a', 'b', 'c', 'd']
		    print list[1:-1]   ## ['b', 'c']
		    list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
		    print list         ## ['z', 'c', 'd'] 

























