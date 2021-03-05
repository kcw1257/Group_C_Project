from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)
db = client.project


solve = {
    "wall": [],
    "holes":[],
    "start":[0,0],
    "end":[0,0],
    "path":[],
    "success":True,
    "auto": True,
    "frameData":[]
}

for i in range(10):
    frameData = {
        "frame": i,
        "speed": 0,
        "acceleration": 0,
        "speedDirection": 0,
        "accelerationDirection": 0,
        "xTilt": 0,
        "yTilt": 0
    }
    solve["frameData"].append(frameData)

solve["wall"].append([2,3])


solves = db.solves
solves.insert_one(solve)
