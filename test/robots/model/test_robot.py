from src.robots.model.robot import Robot


def test_create_robot():
    robot = Robot(id=1, name="Mazinga Z")
    
    assert robot.id == 1
    assert robot.name == "Mazinga Z"