@REZ
D = A;

@i
M = D;

@j
M = 0;

@REZ
D = A;

@VRH
M = D;

(START_OKO)

	@j
	D = M;
	@128
	D = D - A;
	@END_OKO
	D; JGE
	
	@i
	A = M;
	M = 1;
	
	@32
	D = A;
	
	@i
	M = M + D;
	
	@j
	M = M + 1;
	
	@START_OKO
	0; JMP
(END_OKO)

@i
D = M;

@KRIZANJE
M = D;

@j
M = 0;

(START_VOD)
	@j
	D = M;
	@8
	D = D - A;
	@END_VOD
	D; JGE
	
	@i
	A = M;
	M = -1;
	
	@i
	M = M + 1;
	
	@j
	M = M + 1;
	
	@START_VOD
	0; JMP
(END_VOD)
@KRIZANJE
D = M;

@i
M = D;

@32
D = A;

@i
M = M - D;

@2
D = A;

@i
A = M;
M = D;

@i
M = M - 1;

@k
M = 0;

(END_ROW)
@i
M = M + 1;

@brojac
M = 1;

@j
M = 0;

(START_OKOMICA)
	@k
	D = M;
	@64
	D = D - A;
	@END_OKOMICA
	D; JGE
	
	@j
	D = M;
	@16
	D = D - A;
	@END_ROW
	D; JGE
	
	@br
	D = M;
	M = M + D;
	
	@i
	A = M;
	M = M + D;
	
	@j
	M = M + 1;
	
	@k
	M = M + 1;
	
	@32
	D = A;
	@i
	M = M - D;
	
	@START_OKOMICA
	0; JMP
	
(END_OKOMICA)

@k
M = 0;

@VRH
D = M;

@i
M = D;
M = M - 1;

@2
D = A;

@VRH
A = M;
M = D;

(END_ROWS)
@i
M = M + 1;

@br
M = 1;

@j
M = 0;

(START_HIP)
	@k
	D = M;
	@128
	D = D - A;
	@END_HIP
	D; JGE
	
	@j
	D = M;
	@16
	D = D - A;
	@END_ROWS
	D; JGE
	
	@br
	D = M;
	M = M + D;
	
	@i
	A = M;
	M = M + D;
	
	@j
	M = M + 1;
	
	@k
	M = M + 1;
	
	@32
	D = A;
	@i
	M = M + D;
	
	@START_HIP
	0; JMP
(END_HIP)

(END)
@END
0; JMP