from unittest.mock import MagicMock
from src.robots.model.robots import Robots
from src.robots.service.robot_service import RobotService
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
    
    robot_service = RobotService()
    robot_service.get_all = MagicMock(return_value=robots)
    
    use_case = GetAllRobotsUseCase(robot_service)
    
    result = use_case()
    
    assert result == robots
    robot_service.get_all.assert_called_once()
    