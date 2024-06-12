import math


def main():
	a = input()
	b = input()
	c = input()
	a = float(a)
	b = float(b)
	c = float(c)
	if a != 0:
		delta = (b ** 2) - (4 * c * a)
		if delta >= 0:
			x1 = ((-b) + (delta ** 0.5)) / (2 * a)
			x2 = ((-b) - (delta ** 0.5)) / (2 * a)
			print(f"x1={x1:.2f}")
			print(f"x2={x2:.2f}")
			return 0
		print("NAO TEM SOLUCAO NO DOMINIO DO NUMEROS REAIS")
		return 0
	print("NAO EH EQ 2G")
	return 0


if __name__ == '__main__':
	main()
