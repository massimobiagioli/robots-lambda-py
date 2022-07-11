import json

from robots.service.robot_service import RobotService
from src.robots.usecase.get_all_robots_use_case import GetAllRobotsUseCase

robots_service = RobotService()
use_case = GetAllRobotsUseCase(robots_service)


def invoke(event, context):
    robots = use_case()
    
    response = {
        "statusCode": 200,
        "body": json.dumps(robots.serialize())
    }

    return response