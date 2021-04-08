import winsound

#SOUND VISUALISER==============================
def check(list1):
	if list1[0] == 0:
		winsound.PlaySound("0.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[0] == 1:
		winsound.PlaySound("1.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[0] == 2:
		winsound.PlaySound("2.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[0] == 3:
		winsound.PlaySound("3.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[0] == 4:
		winsound.PlaySound("4.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[0] == 5:
		winsound.PlaySound("5.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[0] == 6:
		winsound.PlaySound("6.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[0] == 7:
		winsound.PlaySound("7.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[0] == 8:
		winsound.PlaySound("8.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[0] == 9:
		winsound.PlaySound("9.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)

def check_2(list1):
	if list1[1] == 0:
		check(list1)
		winsound.PlaySound("0.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[1] == 1:
		check(list1)
		winsound.PlaySound("1.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[1] == 2:
		check(list1)
		winsound.PlaySound("2.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[1] == 3:
		check(list1)
		winsound.PlaySound("3.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[1] == 4:
		check(list1)
		winsound.PlaySound("4.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[1] == 5:
		check(list1)
		winsound.PlaySound("5.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[1] == 6:
		check(list1)
		winsound.PlaySound("6.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[1] == 7:
		check(list1)
		winsound.PlaySound("7.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[1] == 8:
		check(list1)
		winsound.PlaySound("8.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[1] == 9:
		check(list1)
		winsound.PlaySound("9.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	
def check_3(list1):
	if list1[2] == 0:
		winsound.PlaySound("0.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
		check_2(list1)
	elif list1[2] == 1:
		check_2(list1)
		winsound.PlaySound("1.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[2] == 2:
		check_2(list1)
		winsound.PlaySound("2.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[2] == 3:
		check_2(list1)
		winsound.PlaySound("3.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[2] == 4:
		check_2(list1)
		winsound.PlaySound("4.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[2] == 5:
		check_2(list1)
		winsound.PlaySound("5.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[2] == 6:
		check_2(list1)
		winsound.PlaySound("6.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[2] == 7:
		check_2(list1)
		winsound.PlaySound("7.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[2] == 8:
		check_2(list1)
		winsound.PlaySound("8.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	elif list1[2] == 9:
		check_2(list1)
		winsound.PlaySound("9.wav", winsound.SND_NOSTOP |winsound.SND_FILENAME)
	
def sound(frequency):
        #frequency is an integer valuse that will be entered with function call
        #if testing this function uncomment thee last 3 lines of the code

	list1 = [int(i) for i in str(frequency)]
	if len(list1) == 1:
		check(list1)
	elif len(list1) == 2:
		check_2(list1)
	elif len(list1) == 3:
		check_3(list1)

#if test
'''sound(456)
sound(45)
sound(6)
'''
