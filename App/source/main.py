"""Here we're gonna connect every module to UI"""
from ui import TutorCompanion

class Main():
    def __init__(self) -> None:

        UI = TutorCompanion()
        UI.run()

        # Don't write anything here!!
        # This will execute when kill UI

if __name__ == "__main__":
    Main()