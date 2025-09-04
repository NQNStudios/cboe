@select-pc = 0
	sdf -1, -1
	msg 0, 1, -1
	pic 0, 4
	ex1 0, -1, 7
	ex2 1, -1, -1
	goto 2
@change-ter = 1
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 -10, -11, -1
	ex2 259, -1, -1
	goto -1
@status = 2
	sdf -1, -1
	msg 0, 1, -1
	pic 0, 4
	ex1 3, 1, 7
	ex2 258, -1, -1
	goto 1
