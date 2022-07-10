from src.robots.repository.robots_repository import RobotsRepository


class GetAllRobotsUseCase:
    def __init__(self, robots_repository: RobotsRepository):
        self.robots_repository = robots_repository
    
    def __call__(self):
        return self.robots_repository.get_all()