from src.robots.model.robots import Robots
from src.robots.service.robot_service import RobotService


class GetAllRobotsUseCase:
    def __init__(self, robots_repository: RobotService):
        self.robots_repository = robots_repository
    
    def __call__(self) -> Robots:
        return self.robots_repository.get_all()