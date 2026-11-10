from dataclasses import dataclass


@dataclass
class EstateAgent:
    name: str
    phone: str


@dataclass
class Office:
    city: str
    agents: list # Composition


agents = [EstateAgent("Kim", "031-390 06 00"), EstateAgent("Alex", "031-390 06 02")]
office = Office("Gothenburg", agents)

for agent in office.agents:
    print(agent.name, agent.phone)