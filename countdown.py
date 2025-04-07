from time import sleep


def countdown(n):
    while n > 0:
        print(n)
        sleep(0.6)
        n-=1

def countdown_recursive(n):
    if n <= 0:
        print(f"STOP!")
    else:
        print(n)
        sleep(0.6)
        countdown_recursive(n-1)

if __name__ == "__main__":
    #countdown(5)
    countdown_recursive(5)