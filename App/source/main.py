"""Here we're gonna connect every module to UI"""
from ui import TutorCompanion
from modules.process_data import is_psk_and_username_valid
from modules.process_data import process_data_from_user_dict
from modules.get_data import get_user_data

class Main():
    def __init__(self) -> None:

        UI = TutorCompanion(
            check_login=self.check_login)
        UI.run()

        # Don't write anything here!!
        # This will execute when kill UI

    def check_login(self, user, psk) -> bool:
        if is_psk_and_username_valid(user=user, psk=psk, data=process_data_from_user_dict(get_user_data())):
            return True
        
        return False


if __name__ == "__main__":
    Main()