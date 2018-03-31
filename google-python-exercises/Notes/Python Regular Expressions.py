Python Regular Expressions


In Python a regular expression search is typically written as:
	  match = re.search(pat, str) ## pat - regular expression pattern
	  							  ## str - a string and searches for that patter within the string
re.search()之后会紧跟着if-statement，看是否match成功

example, searches for the pattern 'word:' followed by a 3 letter word :
	str = 'an example word:cat!!'
	match = re.search(r'word:\w\w\w', str)
	# If-statement after search() tests if it succeeded
    if match:                      
      print 'found', match.group() ## 'found word:cat'
    else:
      print 'did not find'


Basic Patterns
	\w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. 
	Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. 
	\W (upper case W) matches any non-word character.

	\s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]. 
	\S (upper case S) matches any non-whitespace character.

	\t, \n, \r -- tab, newline, return

	\d -- decimal digit [0-9] (some older regex utilities do not support but \d, but they all support \w and \s)

	^ = start, $ = end -- match the start or end of the string
	
	\ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash. If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, \@, to make sure it is treated just as a character.


	在第一个找到地方停止
	example:
		## Search for pattern 'iii' in string 'piiig'.
		## All of the pattern must match, but it may appear anywhere.
		## On success, match.group() is matched text.
		match = re.search(r'iii', 'piiig') =>  found, match.group() == "iii"
		match = re.search(r'igs', 'piiig') =>  not found, match == None

		## . = any char but \n
		match = re.search(r'..g', 'piiig') =>  found, match.group() == "iig"

		## \d = digit char, \w = word char
		match = re.search(r'\d\d\d', 'p123g') =>  found, match.group() == "123"
		match = re.search(r'\w\w\w', '@@abcd!!') =>  found, match.group() == "abc"


Repetition
	Things get more interesting when you use + and * to specify repetition in the pattern
		+ -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
		* -- 0 or more occurrences of the pattern to its left
		? -- match 0 or 1 occurrences of the pattern to its left	


Leftmost & Largest
	先找到第一个符合的位置，然后greedy的院子，走的越远越好，找到符合pattern的字母越多越好
	Example:
	  ## i+ = one or more i's, as many as possible.
	  match = re.search(r'pi+', 'piiig') =>  found, match.group() == "piii"

	  ## Finds the first/leftmost solution, and within it drives the +
	  ## as far as possible (aka 'leftmost and largest').
	  ## In this example, note that it does not get to the second set of i's.
	  match = re.search(r'i+', 'piigiiii') =>  found, match.group() == "ii"

	  ## \s* = zero or more whitespace chars
	  ## Here look for 3 digits, possibly separated by whitespace.
	  match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') =>  found, match.group() == "1 2   3"
	  match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') =>  found, match.group() == "12  3"
	  match = re.search(r'\d\s*\d\s*\d', 'xx123xx') =>  found, match.group() == "123"

	  ## ^ = matches the start of string, so this fails:
	  match = re.search(r'^b\w+', 'foobar') =>  not found, match == None
	  ## but without the ^ it succeeds:
	  match = re.search(r'b\w+', 'foobar') =>  found, match.group() == "bar"
	
	Emails Example: '\w+@\w+'不能显示整个email address，因为'\w'不能match'-'或者'.'
		str = 'purple alice-b@google.com monkey dishwasher'
	  	match = re.search(r'\w+@\w+', str)
	    if match:
	      print match.group()  ## 'b@google'


Square Brackets
	'[]'表示括号中的a set of chars，比如[abc]就match'a'或者'b'或者'c'。
	\w \s这种也可以放在'[]'里面
	'.'仅仅是个'.'而已
	对于email example，可以就把'[]'内加上'.'和'-'就行了。



		  match = re.search(r'[\w.-]+@[\w.-]+', str)
		  if match:
		    print match.group()  ## 'alice-b@google.com'

	也可以用'-'表示范围，[a-z]就表示所有lowercase letters
	也可以[abc-]，就是没有右半边的范围。
	'^'方括号开始处是invert的意思。e.g. [^ab]就是任何char除了'a'或者'b'的意思

Group Extraction: 可以把满足的某一部分拆出来
	e.g.  r'([\w.-]+)@([\w.-]+)' 就可以拆出来email的username和host
	the parenthesis do not change what the pattern will match, instead they establish logical "group" inside of the match text


		  str = 'purple alice-b@google.com monkey dishwasher'
		  match = re.search('([\w.-]+)@([\w.-]+)', str)
		  if match:
		    print match.group()   ## 'alice-b@google.com' (the whole match)
		    print match.group(1)  ## 'alice-b' (the username, group 1)
		    print match.group(2)  ## 'google.com' (the host, group 2)


findall: 找所有match的并且把每个match的都放在一个list of strings里面
	  ## Suppose we have a text with many email addresses
	  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

	  ## Here re.findall() returns a list of all the found email strings
	  emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
	  for email in emails:
	    # do something with each found email string
	    print email

findall With Files
	call findall() on each line in the file
	Just feed the whole file text into findall() and let it return a list of all the matches in a single step 
	(recall that f.read() returns the whole text of a file in a single string)
	
	  # Open file
	  f = open('test.txt', 'r')
	  # Feed the file text into findall(); it returns a list of all the found strings
	  strings = re.findall(r'some pattern', f.read())

findall and Groups
	If the pattern includes 2 or more parenthesis groups, then instead of returning a list of strings, findall() returns a list of *tuples*
	Each tuple represents one match of the pattern, and inside the tuple is the group(1), group(2) .. data
	So if 2 parenthesis groups are added to the email pattern, then findall() returns a list of tuples, each length 2 containing the username and host, e.g. ('alice', 'google.com').
	如果pattern只有一个parenthesis的话，findall() returns a list of strings

		  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
		  tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
		  print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
		  for tuple in tuples:
		    print tuple[0]  ## username
		    print tuple[1]  ## host

Options: 可以选定pattern match的方式
	1. 忽略大小写：IGNORECASE -- ignore upper/lowercase differences for matching, so 'a' matches both 'a' and 'A'.
	2. '.'可以match new linw：DOTALL -- allow dot (.) to match newline -- normally it matches anything but newline. This can trip you up -- you think .* matches everything, but by default it does not go past the end of a line. Note that \s (whitespace) includes newlines, so if you want to match a run of whitespace that may include a newline, you can just use \s*
	3. MULTILINE -- Within a string made of many lines, allow ^ and $ to match the start and end of each line. Normally ^/$ would just match the start and end of the whole string.



Greedy vs. Non-Greedy (optional)
	因为".*"可以match所有东西，所以在"<b>foo</b> and <i>so on</i>"里面，".*"会match整个txt。
	这是因为，".*"是greedy的，会尽可能多的match。（greedy）

	可以用"[^>]*"来跳过所有不是">"的东西，终结在">"

Substitution (optional)
	re.sub(pat, replacement, str) 可以找所有的str中满足pattern的地方，然后替换他们


	example, 找到所有的email address，把host变成"yo-yo-dyne"，user(\1)不变:
		  str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
		  ## re.sub(pat, replacement, str) -- returns new string with all replacements,
		  ## \1 is group(1), \2 group(2) in the replacement
		  print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
		  ## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher








