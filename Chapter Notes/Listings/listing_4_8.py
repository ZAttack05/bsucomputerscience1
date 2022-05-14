def moveTower(height,fromPole, toPole, withPole):
	if height >= 1:
		moveTower(height-1,fromPole,withPole,toPole)  		
		moveDisk(fromPole,toPole)
		moveTower(height-1,withPole,toPole,fromPole) 
def moveDisk(fp, tp):
	print("moving disk from %d to %d\n" %(fp,tp))

def main():
	f = 1
	w = 2
	t = 3
	height = 5
	moveTower(height, f, t, w)

main()ph