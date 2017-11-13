simulation_message = SimulationInit()

nodeA = simulation_message.nodes.add()
nodeA.name = "A"
nodeA.block = HEAT_PUMP_1
nodeA.inputs.append("seta")
nodeA.outputs.append("ta")

nodeB = simulation_message.nodes.add()
nodeB.name = "B"
nodeB.block = HEAT_PUMP_2
nodeB.outputs.append("tb")

nodeC = simulation_message.nodes.add()
nodeC.name = "C"
nodeC.block = THERMAL_NETWORK
nodeC.inputs.append("t1")
nodeC.inputs.append("t2")
nodeC.outputs.append("setc")

link = simulation_message.links.add()
link_input = link.input
link_input.node = "A"
link_input.attribute = "ta"

link_output = link.output
link_output.node = "C"
link_output.attribute = "t1"

from obnl.core.impl import convert_protobuf_to_data

convert_protobuf_to_data(simulation_message)