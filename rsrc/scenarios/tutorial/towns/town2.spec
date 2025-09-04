@once-give-spec-item = 0
	sdf 2, 0
	msg 0, 34, -1
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
	goto 31
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
@block-move = 17
	sdf -1, -1
	msg 27, 28, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto 22
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
@if-sdf = 20
	sdf 2, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 3, -1, -1
	ex2 -1, -1, -1
	goto 17
@if-sdf = 21
	sdf 2, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 3, 17, -1
	ex2 -1, -1, -1
	goto -1
@set-sdf = 22
	sdf 2, 5
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-sdf = 23
	sdf 2, 6
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 24, -1
	ex2 -1, -1, -1
	goto -1
@disp-msg = 24
	sdf -1, -1
	msg 29, 30, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 25
@start-talk = 25
	sdf -1, -1
	msg -1, -1, -1
	pic 71, 4
	ex1 21, -1, -1
	ex2 -1, -1, -1
	goto -1
@set-sdf = 26
	sdf 2, 7
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-sdf = 27
	sdf 2, 7
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 28, -1
	ex2 -1, -1, -1
	goto 21
@block-move = 28
	sdf -1, -1
	msg 31, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-ter = 29
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 23, 20, -1
	ex2 127, 30, -1
	goto -1
@disp-msg = 30
	sdf -1, -1
	msg 32, 33, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@change-ter = 31
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 27, 20, -1
	ex2 131, -1, -1
	goto -1
@if-sdf = 32
	sdf 2, 8
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 33, -1
	ex2 -1, -1, -1
	goto -1
@destroy-monst = 33
	sdf -1, -1
	msg 35, 36, -1
	pic 0, 4
	ex1 36, 20, -1
	ex2 -1, -1, -1
	goto 34
@set-sdf = 34
	sdf 2, 8
	msg -1, -1, -1
	pic 0, 4
	ex1 0, -1, -1
	ex2 -1, -1, -1
	goto -1
@once-dlog = 35
	sdf 2, 9
	msg 37, -1, 1
	pic 0, 19
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@disp-msg = 36
	sdf -1, -1
	msg 43, 36, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
