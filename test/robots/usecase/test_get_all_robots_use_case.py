from unittest.mock import MagicMock
from src.robots.model.robots import Robots
from src.robots.repository.robots_repository import RobotsRepository
from src.robots.usecase.get_all_robots_use_case import GetAllRobotsUseCase


def test_get_all_robots():
    data = [
        {
            "id": 1,
            "name": "Mazinga Z"
        },
        {
            "id": 2,
            "name": "Starzinger"
        },
        {
            "id": 3,
            "name": "Daitarn 3"
        }
    ]
    robots = Robots.from_data(data)
    
    robot_repository = RobotsRepository()
    robot_repository.get_all = MagicMock(return_value=robots)
    
    use_case = GetAllRobotsUseCase(robot_repository)
    
    result = use_case()
    
    assert result == robots
    robot_repository.get_all.assert_called_once()
    