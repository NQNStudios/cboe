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
