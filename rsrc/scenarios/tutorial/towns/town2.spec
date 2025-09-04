@once-give-spec-item = 0
	sdf 2, 0
	msg 0, -1, -1
	pic 0, 4
	ex1 1, 0, -1
	ex2 -1, -1, -1
	goto 1
@inc-sdf = 1
	sdf 1, 4
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 0, -1
	ex2 -1, -1, -1
	goto -1
@if-ter = 2
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 9, 7, -1
	ex2 126, 3, -1
	goto -1
@once-dlog = 3
	sdf -1, -1
	msg 1, -1, 1
	pic 90, 1
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-ter = 4
	sdf -1, -1
	msg 7, -1, 1
	pic 18, 3
	ex1 9, 7, -1
	ex2 129, 5, -1
	goto 6
@block-move = 5
	sdf -1, -1
	msg 13, 10, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-ter = 6
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 11, 10, -1
	ex2 260, 8, -1
	goto -1
@once-dlog = 7
	sdf -1, -1
	msg 14, -1, 1
	pic 18, 3
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-item-class = 8
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 9, -1
	ex2 -1, -1, -1
	goto 7
@if-item-class-equip = 9
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto 10
@once-dlog = 10
	sdf -1, -1
	msg 20, -1, 1
	pic 18, 3
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@relocate = 11
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 2, 4, -1
	ex2 101, -101, -1
	goto 16
@set-ptr = 12
	sdf 2, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 101, -1, -1
	ex2 -1, -1, -1
	goto 13
@set-sdf = 13
	sdf 2, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
@set-sdf = 14
	sdf 2, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 3, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-sdf = 15
	sdf 2, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 3, 13, -1
	ex2 -1, -1, -1
	goto 14
@disp-sm-msg = 16
	sdf -1, -1
	msg 26, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 15
@nop = 17
	sdf -1, -1
	msg -1, -1, -1
	pic -1, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-sdf = 18
	sdf 2, 3
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 11, -1
	ex2 -1, -1, -1
	goto -1
@once-dlog = 19
	sdf 2, 4
	msg 7, -1, 1
	pic 18, 3
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@nop = 20
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
