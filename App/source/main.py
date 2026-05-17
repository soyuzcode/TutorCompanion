"""Here we're gonna connect every module to UI"""
from ui import TutorCompanion
from modules.process_data import is_psk_and_username_valid
from modules.get_data import get_user_data

class Main():
    def __init__(self) -> None:

        UI = TutorCompanion(
            check_login=is_psk_and_username_valid, data=get_user_data)
        UI.run()

        # Don't write anything here!!
        # This will execute when kill UI

if __name__ == "__main__":
    Main()