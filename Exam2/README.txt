@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Main Code: Test2.py
Code for checking Memory and Time: memory_and_time.py

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

INPUT:
For input two types of options are given. User can either take input from STDIN (option 1) or from textfile (option 2). User can also ask for help.

#Command for help:

$python3 Test2.py 
	or,
$python3 Test2.py -h

Example: 
*****************************************************************
		$python3 Test2.py -h
*****************************************************************

#Command for taking input from STDIN:

$python3 Test2.py 1 <input_array>


Example: 
*****************************************************************
		$python3 Test2.py 1 [10 9 8 7 6 5 4 3 2 1]
				or,
		$python3 Test2.py 1 [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
*****************************************************************

#Command for taking input from STDIN where the input array contains new lines

$python3 Test2.py 1 $'<input_array>'

Example: 
*****************************************************************
	$python3 Test2.py 1 $'[620 147 382 872 643 741 491 844 471 280 718 929 630
        232 754 464 898 405 179 194 828 895 788 769  30 438  58 143 201 938 729
        811 170 527 301 116 385 108  36 423 797 434 673 517 793 857 961  73 624'
*****************************************************************



#Command for taking input from input file:

$python3 Test2.py 2 <file_name>

Example: 
*****************************************************************
		$python3 Test2.py 2 test1000000.txt 
*****************************************************************

%%%%%%  NOTE:: Input file should be in the same folder as the code (Test2.py)


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

OUTPUT:

Gives the number of inversions as output in the folowing format:

	"Number of total inversions is: " <conversion_number>

Example: 
*****************************************************************
		Number of total inversions is:  45 
*****************************************************************

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
