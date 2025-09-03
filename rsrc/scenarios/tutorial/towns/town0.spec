@once-dlog = 0
	sdf -1, -1
	msg 2, -1, 1
	pic 92, 1
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 4
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
@once-disp-msg = 3
	sdf 0, 0
	msg 1, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@once-dlog = 4
	sdf -1, -1
	msg 8, -1, 1
	pic 95, 1
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@once-disp-msg = 5
	sdf 0, 1
	msg 14, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-ter = 6
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 22, 9, -1
	ex2 133, 0, -1
	goto -1
