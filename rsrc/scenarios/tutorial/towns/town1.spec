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
	pic 0, 4
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
	pic 24, 4
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
@set-sdf = 8
	sdf 1, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 9, -1, -1
	ex2 -1, -1, -1
	goto 1
@once-dlog = 9
	sdf -1, -1
	msg 15, -1, 1
	pic 24, 4
	ex1 34, 10, -1
	ex2 -1, -1, -1
	goto -1
@title-msg = 10
	sdf -1, -1
	msg 21, -1, 25
	pic 17, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 14
@title-msg = 11
	sdf -1, -1
	msg 24, 32, 23
	pic 85, 3
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 13
@title-msg = 12
	sdf -1, -1
	msg 22, 31, 9
	pic 22, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 11
@title-msg = 13
	sdf -1, -1
	msg 34, 35, 33
	pic 28, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 17
@title-msg = 14
	sdf -1, -1
	msg 27, 28, 26
	pic 38, 3
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 15
@title-msg = 15
	sdf -1, -1
	msg 30, -1, 29
	pic 45, 3
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 12
@nop = 16
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@title-msg = 17
	sdf -1, -1
	msg 37, 38, 36
	pic 2, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@set-sdf = 18
	sdf 1, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 19, -1, -1
	ex2 -1, -1, -1
	goto 1
@once-dlog = 19
	sdf -1, -1
	msg 39, -1, 1
	pic 24, 4
	ex1 34, 20, -1
	ex2 -1, -1, -1
	goto -1
@once-dlog = 20
	sdf -1, -1
	msg 45, -1, 1
	pic 24, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@set-sdf = 21
	sdf 1, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 22, -1, -1
	ex2 -1, -1, -1
	goto 1
@once-dlog = 22
	sdf -1, -1
	msg 51, -1, 1
	pic 24, 4
	ex1 34, 23, -1
	ex2 -1, -1, -1
	goto -1
@once-dlog = 23
	sdf -1, -1
	msg 57, -1, 1
	pic 24, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-sdf = 24
	sdf 1, 0
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 25, -1
	ex2 -1, -1, -1
	goto 26
@stair = 25
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 24, 24, -1
	ex2 0, 1, 2
	goto -1
@disp-msg = 26
	sdf -1, -1
	msg 63, 64, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
