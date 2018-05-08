def fibonacci():
	#Program to display the Fibonacci sequence up to n-th term
	terms=False
	#loopng condition
	while not terms:
		nterms=int(input("Enter number of terms: "))
		#ask user to input number of terms
		if nterms <=0:
			print ("Please enter a positive integer")
			terms=False
		#first if condition to test number of terms is a positive integer
		#if test fail, start while-loop again
		elif nterms >100:
			print ("the term is out of range")
			terms=False
		#second if condition to test number of term is within the defined range
		#if test fail, start while-loop again
		else:
			n1=0
			n2=1
			#assign values to first two terms
			count=0
			if nterms ==1:
				print ("Fibonacci sequence is :")
				print (n1)
			#only print first term if number of terms is 1
			else:
				print ("Fibonacci sequence is :")
				while count < nterms:
					print(n1, end=', ')
					#end a print statement with comma
					#next print statement will continue after comma instead of starting from a new line
					nth=n1+n2
					#calculate value of the next term
					n1=n2
					n2=nth
					#update values for n1 and n2
					count +=1
					#update value of count by adding 1
				break
				#break while-loop to finish the program
			    
