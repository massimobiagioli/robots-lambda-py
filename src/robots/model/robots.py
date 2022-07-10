from dataclasses import asdict
from src.robots.model.robot import Robot


class Robots:
    def __init__(self, data = []):
        self.robots = data
        
    @classmethod
    def from_data(cls, data):
        return cls([Robot(id=item["id"], name=item["name"]) for item in data])
        
    def serialize(self):
        return [asdict(robot) for robot in self.robots]