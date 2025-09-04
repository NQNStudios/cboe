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
@once-disp-msg = 7
	sdf 0, 2
	msg 15, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@once-dlog = 8
	sdf 0, 3
	msg 16, -1, 1
	pic 102, 3
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@inc-sdf = 9
	sdf 0, 4
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 0, -1
	ex2 -1, -1, -1
	goto 10
@if-sdf = 10
	sdf 0, 4
	msg -1, -1, -1
	pic 0, 4
	ex1 3, 16, -1
	ex2 -1, -1, -1
	goto -1
@once-dlog = 11
	sdf -1, -1
	msg 22, -1, 1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-status = 12
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 6, 14, -1
	ex2 1, 0, 2
	goto 15
@if-sdf = 13
	sdf 0, 4
	msg -1, -1, -1
	pic 0, 4
	ex1 3, 12, -1
	ex2 -1, -1, -1
	goto -1
@if-sdf = 14
	sdf 0, 5
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto 11
@set-sdf = 15
	sdf 0, 5
	msg 28, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
@disp-msg = 16
	sdf -1, -1
	msg 29, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@disp-msg = 17
	sdf -1, -1
	msg 30, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
