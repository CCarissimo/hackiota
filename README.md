# hackiota

devnet node found at: http://wiki.iota.org/introduction/reference/networks/devnet

using iota-client python library

iota-client use resources: https://wiki.iota.org/iota.rs/explanations/address_key_space



Todo:

- message formatting:

  - what length message can we send?
  - what is the type of the data we can send?
  - how does it compare to the data produced from the sensors?

  - after finding messages in the tangle, convert them to readable
  - format them nicely in a file

- Sensor Data:

  - what data will we send to the tangle?
  - how will we convert it to Bytes for messages?

- Indexing:

  - is there a limit to the number of messages we can send for a given index

- Requesting:

  - how can we request that a sensor takes a measurement?
  - Easiest: with messages and indexes
  - harder: via an account and IOTA balances
  - Expert: with smart contracts, accounts and IOTA balances

- visualization

  - can we read messages from the tangle and visualize them on a map?

- accounts, currency:

  - can we set up a wallet on our sensors, to receive IOTA?
  - can we set up sensors to run python code when they receive IOTA?

- Rewarding, payments:

  - how much should sensors receive as rewards for their measurements
  - how should an Agent decide which sensors to use to learn most about an area?

