from math import exp


def multiplica(r1: float, o1: float, r2: float, o2: float) -> tuple:
    r: float = r1 * r2
    o: float = o1 + o2
    return r, o


def divide(r1: float, o1: float, r2: float, o2: float) -> tuple:
    r: float = r1 / r2
    o: float = abs(o1 - o2)
    return r, o


def main() -> None:
    acao: str = input()
    
    while acao.upper() != "VAZIO":
        r1: float = float(input())
        o1: float = float(input())
        r2: float = float(input())
        o2: float = float(input())
        r, o = 0.0, 0.0
        if acao.upper() == "MULTIPLICA":
            r, o = multiplica(r1, o1, r2, o2)
        elif acao.upper() == "DIVIDE":
            r, o = divide(r1, o1, r2, o2)
        
        print(f"r1={r1:.2f}, t1={o1:.2f}, r2={r2:.2f}, t2={o2:.2f}, rf={r:.2f}, tf={o:.2f}")
        acao: str = input()
        

if __name__ == "__main__":
    main()
