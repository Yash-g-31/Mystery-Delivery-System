import json, math

with open("test_case_7.json", "r") as f:
    data = json.load(f)

agents = [{"id": key, "location": value, "total_distance": 0.0, "packages_delivered":0} for key, value in data["agents"].items()]
warehouses = data['warehouses']
packages = data['packages']


for package in packages:
    warehouse_location = warehouses[package["warehouse"]]
    destination = package["destination"]

    nearest_agent = None
    min_distance = float("inf")

    # searching for nearest agent from warehouse location
    for agent in agents:

        # calculating agent distance from warehouse using euclidean method.
        distance = math.sqrt((agent["location"][0] - warehouse_location[0])**2 + (agent["location"][1] - warehouse_location[1])**2)

        if distance < min_distance:
            min_distance = distance
            nearest_agent = agent

        # if distance of two agent is same then agent with less total distance will get order
        elif distance == min_distance:
            if agent["total_distance"] < nearest_agent["total_distance"]:
                nearest_agent = agent

    agent, distance_to_warehouse = nearest_agent, min_distance

    agent["total_distance"] = agent["total_distance"] + distance_to_warehouse

    # calculating distance of agent from warehouse to destination
    distance_to_destination = math.sqrt((warehouse_location[0] - destination[0])**2 + (warehouse_location[1] - destination[1])**2)

    agent["total_distance"] = agent["total_distance"] + distance_to_destination

    # updating agent current location
    agent["location"] = destination

    agent["packages_delivered"] += 1



# generating report.json
report = {}
best_agent_id = None
min_efficiency = float("inf")


for agent in agents:

    if agent["packages_delivered"] > 0:
        efficiency = agent["total_distance"] / agent["packages_delivered"]

    else:
        efficiency = 0.0
    
    report[agent["id"]] = {
        "packages_delivered": agent["packages_delivered"],
        "total_distance": round(agent["total_distance"], 2),
        "efficiency": round(efficiency, 2)
    }

    if efficiency < min_efficiency and agent["packages_delivered"] > 0:
        min_efficiency = efficiency
        best_agent_id = agent["id"]

report["best_agent"] = best_agent_id


# saving report.json
with open("report.json", "w") as rf:
    json.dump(report, rf, indent=4)

print("Report generated successfully as 'report.json'")