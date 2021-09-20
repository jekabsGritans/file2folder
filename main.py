import os, sys
from pathlib import Path

def main():
	if len(sys.argv) ==2:
		dir = sys.argv[1]
		if os.path.exists(dir):
			os.chdir(dir)
			ffs = os.listdir()
			for ff in ffs:
				if os.path.isfile(ff):
					folder = Path(ff).stem
					os.mkdir(folder)
					os.replace(ff, folder+"/"+ff)


if __name__ == "__main__":
	main()
