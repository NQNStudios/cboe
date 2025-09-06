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
	msg 1, 45, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 29
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
	goto 17
@disp-msg = 16
	sdf -1, -1
	msg 29, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 18
@set-sdf = 17
	sdf 0, 4
	msg -1, -1, -1
	pic 0, 4
	ex1 0, -1, -1
	ex2 -1, -1, -1
	goto -1
@set-sdf = 18
	sdf 0, 6
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-sdf = 19
	sdf 0, 6
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 20, -1
	ex2 -1, -1, -1
	goto -1
@if-ter = 20
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 13, 20, -1
	ex2 134, 21, -1
	goto -1
@once-dlog = 21
	sdf -1, -1
	msg 31, -1, 1
	pic 96, 1
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-spec-item = 22
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 0, -1, -1
	ex2 -1, -1, -1
	goto 23
@disp-msg = 23
	sdf -1, -1
	msg 37, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@once-give-spec-item = 24
	sdf 0, 7
	msg 38, 46, -1
	pic 0, 4
	ex1 0, 0, -1
	ex2 -1, -1, -1
	goto 36
@if-ter = 25
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 25, 24, -1
	ex2 130, 26, -1
	goto -1
@once-dlog = 26
	sdf -1, -1
	msg 39, -1, 1
	pic 214, 1
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@change-ter = 27
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 25, 24, -1
	ex2 131, -1, -1
	goto -1
@lever-generic = 28
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 -1, 27, -1
	ex2 -1, -1, -1
	goto -1
@change-ter = 29
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 24, 7, -1
	ex2 130, -1, -1
	goto -1
@if-spec-item = 30
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 0, 31, -1
	ex2 -1, -1, -1
	goto 35
@once-dlog = 31
	sdf -1, -1
	msg 47, -1, 1
	pic 137, 1
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@spell-priest = 32
	sdf -1, -1
	msg 55, -1, -1
	pic 0, 4
	ex1 18, 0, -1
	ex2 -1, -1, -1
	goto -1
@spell-priest = 33
	sdf -1, -1
	msg 56, -1, -1
	pic 0, 4
	ex1 27, 0, -1
	ex2 -1, -1, -1
	goto -1
@disp-msg = 34
	sdf -1, -1
	msg 53, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@block-move = 35
	sdf -1, -1
	msg 54, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
@inc-sdf = 36
	sdf 1, 4
	msg -1, -1, -1
	pic 0, 4
	ex1 1, 0, -1
	ex2 -1, -1, -1
	goto -1
@if-context = 37
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 2, -1, 45
	ex2 -1, -1, -1
	goto 46
@if-statistic = 38
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 2, 39, -1
	ex2 9, -1, -1
	goto 40
@once-dlog = 39
	sdf 0, 9
	msg 57, -1, 1
	pic 25, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto 42
@if-statistic = 40
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 4, 41, -1
	ex2 7, -1, -1
	goto 43
@once-dlog = 41
	sdf 0, 8
	msg 63, -1, 1
	pic 57, 7
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@nop = 42
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-statistic = 43
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 3, 44, -1
	ex2 10, -1, -1
	goto -1
@once-dlog = 44
	sdf 0, 10
	msg 69, -1, 1
	pic 26, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@block-move = 45
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 0, -1, -1
	ex2 1, -1, -1
	goto 38
@if-sdf = 46
	sdf 0, 6
	msg -1, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto 47
@block-move = 47
	sdf -1, -1
	msg 75, -1, -1
	pic 0, 4
	ex1 1, -1, -1
	ex2 -1, -1, -1
	goto -1
@once-dlog = 48
	sdf 0, 11
	msg 76, -1, 1
	pic 14, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@once-disp-msg = 49
	sdf 0, 12
	msg 82, -1, -1
	pic 0, 4
	ex1 -1, -1, -1
	ex2 -1, -1, -1
	goto -1
@if-ter = 50
	sdf -1, -1
	msg -1, -1, -1
	pic 0, 4
	ex1 22, 9, -1
	ex2 133, 4, -1
	goto -1
