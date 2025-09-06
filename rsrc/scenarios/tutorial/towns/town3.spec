@once-give-spec-item = 0
	sdf 3, 0
	msg 0, -1, -1
	pic 0, 4
	ex1 2, 0, -1
	ex2 -1, -1, -1
	goto 1
@inc-sdf = 1
	sdf 1, 4
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 0, -1
	ex2 -1, -1, -1
	goto -1
@once-dlog = 2
	sdf -1, -1
	msg 1, -1, 1
	pic 19, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 3
@force-give = 3
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 25, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-monsters-alive = 4
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 0, -1, -1
	ex2 1, -1, -1
	goto 16
@once-dlog = 5
	sdf -1, -1
	msg 7, -1, 1
	pic 60, 3
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 6
@set-ptr = 6
	sdf 3, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 103, -1, -1
	ex2 -1, -1, -1
	goto 19
@if-alive = 7
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 0, 8, -1
	ex2 -1, -1, -1
	goto 21
@set-sdf = 8
	sdf 3, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 13, -1, -1
	ex2 -1, -1, -1
	goto 10
@set-sdf = 9
	sdf 3, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 14, -1, -1
	ex2 -1, -1, -1
	goto 11
@disp-msg = 10
	sdf -1, -1
	msg 15, -103, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@select-pc = 11
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 0, -1, -1
	ex2 1, -1, -1
	goto 12
@death = 12
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 0, 1, -1
	ex2 -1, -1, -1
	goto 10
@call-global = 13
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 3
@call-global = 14
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 4
@call-global = 15
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 5
@if-sdf = 16
	sdf 3, 1
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 30, -1
	ex2 -1, -1, -1
	goto 5
@disp-msg = 17
	sdf -1, -1
	msg 16, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@select-pc = 18
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 2, -104, -1
	goto 7
@set-ptr = 19
	sdf 3, 5
	msg -1, -1, -1
	pic 0, 4
	ex1 104, -1, -1
	ex2 -1, -1, -1
	goto 18
@nop = 20
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@inc-sdf = 21
	sdf 3, 5
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 0, -1
	ex2 -1, -1, -1
	goto 22
@if-sdf = 22
	sdf 3, 5
	msg -1, -1, -1
	pic 0, 4
	ex1 6, 9, -1
	ex2 -1, -1, -1
	goto 18
@block-move = 23
	sdf -1, -1
	msg 17, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto 24
@destroy-monst = 24
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 29, 18, -1
	ex2 -1, -1, -1
	goto 25
@destroy-monst = 25
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 28, 18, -1
	ex2 -1, -1, -1
	goto 29
@select-pc = 26
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 2, -1, -1
	ex2 -1, -1, -1
	goto 27
@skill-pts = 27
	sdf -1, -1
	msg 18, 19, -1
	pic 0, 4
	ex1 10, 0, -1
	ex2 -1, -1, -1
	goto 31
@if-sdf = 28
	sdf 3, 6
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto 26
@set-sdf = 29
	sdf 3, 7
	msg -1, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-sdf = 30
	sdf 3, 7
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto 17
@set-sdf = 31
	sdf 3, 6
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
