import json

class DataLoader:
    @staticmethod
    def load_json_data():
        data = """
        {
            "VP8": {
                "name": "Some Name",
                "age": 30,
                "location": "Some Location"
            }
        }
        """
        return json.loads(data)
