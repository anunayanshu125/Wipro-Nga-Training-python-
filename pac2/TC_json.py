import json
data={
    "name":"john",
    "age":25,
    "skills":["python","java"]
}
with open("data.json","w") as file:
    json.dump(data,file,indent=3)