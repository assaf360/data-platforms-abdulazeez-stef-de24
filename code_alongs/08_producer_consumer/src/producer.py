from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application 

# Define the path to the 'data' directory
data_path = Path(__file__).parents[1] / "data"
print(data_path)

# Open the jokes.json file and load its content
with open(data_path / "jokes.json", "r") as file:
    jokes = json.load(file)

# Print the jokes loaded from the file
print(jokes)

app = Application(broker_address="localhost:9092", consumer_group="text-splitter")

jokes_topic = app.topic(name = "jokes", value_serializer="json")

print(jokes_topic)

def main():
    with app.get_producer() as producer:
        #print(producer)
        
        
        for joke in jokes:
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)
            
            print(kafka_msg.key, kafka_msg.value)

# run this code only when executing this script and not when importing this module        
if __name__ == '__main__':
    #pprint(jokes)
    main()