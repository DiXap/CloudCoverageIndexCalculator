import core.ArgsParser as args
from core.IPP import ImagePreProcesor as ip

def start():
    try:
        args.initialize()
    except Exception:
        print('Woops! something went wrong')
    

if __name__ == "__main__":
    start()