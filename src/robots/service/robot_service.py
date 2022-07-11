from src.robots.model.robots import Robots


class RobotService:
    def get_all(self):
        return Robots.from_data([
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
        ])