# from smart_mirror.app import main
from smart_mirror import app
import smart_mirror.app

def main():
    app.run(port=5000)

if __name__ == "__main__":
    main()