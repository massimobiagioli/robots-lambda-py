import json

from src.robots.repository.robots_repository import RobotsRepository
from src.robots.usecase.get_all_robots_use_case import GetAllRobotsUseCase

robots_repository = RobotsRepository()
use_case = GetAllRobotsUseCase(robots_repository)


def invoke(event, context):
    robots = use_case()
    
    response = {
        "statusCode": 200,
        "body": json.dumps(robots.serialize())
    }

    return response