from lib.app import PCMApp
import sys

def main():
    app = PCMApp()
    app.start(sys.argv)
    app.save()

if __name__ == "__main__":
    main()