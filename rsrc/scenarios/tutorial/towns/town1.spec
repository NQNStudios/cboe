@once-disp-msg = 0
	sdf 1, 2
	msg 0, 1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 3
@if-look = 1
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 -1, -1, 2
	ex2 -1, -1, -1
	goto -1
@set-sdf = 2
	sdf 1, 0
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -100
@set-ptr = 3
	sdf 1, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 100, -1, -1
	ex2 -1, -1, -1
	goto -1
@nop = 4
	sdf -1, -1
	msg -1, -1, -1
	pic -1, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@set-sdf = 5
	sdf 1, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 6, -1, -1
	ex2 -1, -1, -1
	goto 1
@once-dlog = 6
	sdf -1, -1
	msg 3, -1, 1
	pic 0, 4
	ex1 34, 7, -1
	ex2 -1, -1, -1
	goto -1
@story-dlog = 7
	sdf -1, -1
	msg 3, 10, 14
	pic 24, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
