# NS3-Simulation-of-802.11-CSMA-CA
In this Lab, we aim to study the saturation throughput in an IEEE 802.11 network that uses CSMA/CA with binary exponential backoff to avoid collisions (also referred to as DCF).

## Understanding the Lab Objectives
Goal: Investigate how IEEE 802.11 DCF (CSMA/CA with binary exponential backoff) behaves in saturation.
Main Focus: Measure throughput under two different backoff window settings (Case A and Case B) while varying:
- Number of Nodes(N) in the network.
- Traffic Data Rate(R) in the network.

## Setting Up Your Simulation(Scenario):
- Network Topology
  - Place a node in the terrain to act as the common receiver.
  - Place N wireless transmitter nodes uniformly in the terrain such that all the nodes are within the radio range of each other and that of the common receiver.
- Wi-Fi Configuration:
  - Use the default PHY settings in NS-3.
  - Set up the MAC layer for IEEE 802.11 DCF (CSMA/CA).
- Traffic Generation:
  - Install an OnOffApplication on each transmitter node to generate continuous CBR traffic.
  - Use a packet size of 512 bytes and set an offered data rate of R Mbps.
  - Install a PacketSink on the receiver node to capture all incoming traffic.
  - Assuming that each transmitter node always has packets to send, simulate packet transmissions long enough to get good estimates of the throughput.
- Simulation Duration and Data Collection:
  - Run the simulation long enough to reach steady state.
  - Use FlowMonitor (or similar tools) to measure the metrics.
## Consider 2 cases:
- Case A: minimum backoff window size as 1 and maximum backoff window size as 1023 units of slot times.
- Case B: minimum backoff window size as 63 and maximum backoff window size as 127 units of slot times.

For each case,
- Experiment 1 (varying Number of Nodes (N) in the network): Increase the offered load by increasing the number of nodes N: Set the data rate to a reasonable value and vary the number of nodes N and calculate the throughput at the receiver for each value of N. 
- Experiment 2 (varying Traffic Data Rate (R) in the network): Increase the offered load by increasing the data rate: Keep the number of nodes fixed at 20 and vary R in sufficiently fine granularity.

## Evaluation
Performance Metrics(Averaged over several runs):

- Total throughput (aggregate) :Throughput v.s. N in Experiment 1, and Throughput v.s. R in Experiment 2
- Per-node throughput
