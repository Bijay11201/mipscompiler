package main

func main() {

	var a int = 5
	var i int
	for i = 0; i < 10; i++ { // incdec doesnt work rn
		a = a + 1
	}
	printf(a)
	for ; i < 20; i++ { // incdec doesnt work rn
		a = a + 1
	}
	printf(a)
	for i = 0; ; i++ { // incdec doesnt work rn
		a = a + 1
		break
	}
	printf(a)
	for i = 0; i < 10; { // incdec doesnt work rn
		a = a + 1
		i++
	}
	printf(a)
	for i < 20 { // incdec doesnt work rn
		a = a + 1
		i++
	}
	printf(a)
	for i = 0; ; { // incdec doesnt work rn
		a = a + 1
		i++
		break
	}
	printf(a)
	for ; ; i++ { // incdec doesnt work rn
		a = a + 1
		break
	}
	printf(a)
	i = 0
	for { // incdec doesnt work rn
		a = a + 1
		i++
		if i == 10 {
			break
		}
	}
	printf(a)
	return
}
