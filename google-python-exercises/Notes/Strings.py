Strings

Contents
	1. A string literal can span multiple lines, but there must be a backslash \ at the end of each line to escape the newline. 
		String literals inside triple quotes, """"xxxx"""or '''xxxx''', can span multiple lines of text.
		一个string换行的话需要加上\
		否则用一对三个双引号或者一对三个单引号
	2. string是immutable的，创建之后不能被改变
	3. '+'链接两个string，但是不能直接把数字转化成string，需要加上str()

		 pi = 3.14
	     ##text = 'The value of pi is ' + pi      ## NO, does not work
	     text = 'The value of pi is '  + str(pi)  ## yes
	4. 没有++，但是有+=,-=
	5. integer division用//
		6.5//5    #1.0
	    6.5/5	 #1.3	 
	6. raw string在''之前加上r
	   unicode string在''之前加上u

			raw = r'this\t\n and that'
			print raw     ## this\t\n and that
			    
			multi = """It was the best of times.
			It was the worst of times."""




String Methods
	1. s.lower(), s.upper() -- lowercase/uppercase
	2. s.strip() -- 移除首尾空格
	3. s.isalpha()/s.isdigit()/s.isspace()...
	4. s.startswith('other'), s.endswith('other') -- 是否以other开头、结尾
	5. s.find('other') -- 在s中找'other'，返回first index；返回-1，如果没找到
	6. s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
	7. s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 
						   'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. 
	                       As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
	8. s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. 
					   e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

（Python没有char）


String Slices
	1. s[start:end]     [start, end) 包括start，但是不包括end
	2.       H  e  l  l  o
	         0  1  2  3  4
	         -5 -4 -3 -2 -1
	    e.g. Positive
	    	 s[1:4] is 'ell'
			 s[1:] is 'ello'
			 s[:] is 'Hello'
			 s[1:100] is 'ello'

		e.g. Negative
			 s[-1] is 'o' 
			 s[-4] is 'e' 
			 s[:-3] is 'He' 
			 s[-3:] is 'llo' 
	3. s[:n] + s[n:] == s    n可以为负数，也可以超过长度


String %
类似printf，把string连接在一起
%d int, %s string, %f%g floating point
	1.
	   # % operator
	   text = "%d little pigs come out or I'll %s and %s and %s" % (3, 'huff', 'puff', 'blow down')

	2. This code-across-lines technique works with the various grouping constructs detailed below: ( ), [ ], { }.
		# add parens to make the long-line work:
  		text = ("%d little pigs come out or I'll %s and %s and %s" %
   			(3, 'huff', 'puff', 'blow down'))


i18n Strings (Unicode)
	1. Python本身string不是Unicode。在string前加'u'前缀创建Unicode
	  > ustring = u'A unicode \u018e string \xf1'
	  > ustring
	  u'A unicode \u018e string \xf1'
	2. ustring.encode('utf-8') 把unicode string -> bytes with an encoding such as 'utf-8'
	3. unicode(s, encoding)      encoded plain bytes -> unicode string


		## (ustring from above contains a unicode string)
		> s = ustring.encode('utf-8')
		> s
		'A unicode \xc6\x8e string \xc3\xb1'  ## bytes of utf-8 encoding
		> t = unicode(s, 'utf-8')             ## Convert bytes back to a unicode string
		> t == ustring                      ## It's the same as the original, yay!
		True


If Statement
	1. if condition: ... elif condition: ... else: ...
	2. '0'都是false：None，0，empty string，empty list， empty dictionary


	if speed >= 80:
		print 'License and registration please'
	    if mood == 'terrible' or speed >= 100:
	      print 'You have the right to remain silent.'
	    elif mood == 'bad' or speed >= 90:
	      print "I'm going to have to write you a ticket."
	      write_ticket()
	    else:
	      print "Let's try to keep it under 80 ok?"
































