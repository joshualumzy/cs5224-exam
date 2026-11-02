# Mock B gap set (not shown to Joshua before he answers)

1. **Hybrid vs private (Q9, Q29).** A national tax authority stores every citizen's filings. All of the data is confidential by law and demand is steady all year. Which deployment model fits best, and why is hybrid not the natural choice here?
   *Key:* private (or sovereign); hybrid pays off only when part of the workload is not sensitive or demand varies, so some of it can use cheaper public capacity.
2. **Hypervisor trace (Q13, Q18).** Two companies' VMs share one physical server. Step by step, describe what happens when the guest OS in VM X tries to use memory or disk, and what stops it reading VM Y's memory. Name one thing a VPC does isolate.
   *Key:* guest request is trapped by the hypervisor (in hardware for hardware-assisted); the hypervisor maps each VM to its own memory and disk share and never lets one see the other's; the guest never touches hardware directly. VPC isolates network traffic.
3. **Maintenance ranking (Q15).** Rank from most to least maintenance work for you as the consumer: FaaS, VMs, PaaS, containers you run yourself. One line on what you still look after in each.
   *Key:* VMs (OS, patches, runtime, app) and self-run containers (images, orchestration, still the underlying VM) most; PaaS (app and data only); FaaS least (function code only).
4. **REST and Lambda (Q22).** Sort REST, AWS Lambda, EC2 and SOAP into "a place that runs your code" and "a style of talking between programs". Which place needs no server management?
   *Key:* Lambda and EC2 run code; REST and SOAP are communication styles; Lambda needs no server management.
5. **Instance cost (Q26).** A job needs 90 PFLOP and 500,000 I/O operations, done one after the other. X: 3 TFLOP/s, 4 ms per I/O, $2/s. Y: 6 TFLOP/s, 2 ms, $3/s. Z: 2 TFLOP/s, 1 ms, $1/s. Which is cheapest? Show every row.
   *Key:* X 30,000 + 2,000 = 32,000 s x $2 = $64,000. Y 15,000 + 1,000 = 16,000 s x $3 = $48,000. Z 45,000 + 500 = 45,500 s x $1 = $45,500. **Z cheapest**, though it is the slowest.
