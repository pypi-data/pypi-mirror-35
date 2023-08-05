from Balance.scenes.main_scene import MainScene
from Balance.scenes.main_menu import MainMenu
from Balance.scenes.retry_scene import RetryScene


class ScenesControllerScript:

    @classmethod
    def get_scenes(cls):
        """
        :return: the scene list with the references to the scenes classes
        """
        return [MainMenu, MainScene, RetryScene]
