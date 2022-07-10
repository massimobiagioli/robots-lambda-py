from src.robots.model.robots import Robots


def test_create_robots():
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
    
    assert data == robots.serialize()