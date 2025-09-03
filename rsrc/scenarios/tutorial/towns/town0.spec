@nop = 0
	sdf -1, -1
	msg -1, -1, -1
	pic -1, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-status = 1
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 2, 2, -1
	ex2 1, 0, 2
	goto -1
@block-move = 2
	sdf -1, -1
	msg 0, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
