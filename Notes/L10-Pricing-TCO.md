# L10 — Pricing Models and Modeling TCO

Source: `Lecture 10 - Pricing Models and Modeling TCO.pdf` (32 slides; s17 break, s29-32 admin). Read directly by Claude (small deck), diagram slides 11, 12, 25-28 viewed as images. Five past-paper questions map to L10; they stay unseen for the mocks, so the scenarios below are my own.

## Scenario Plan

| # | Scenario | Concepts | Slides |
|---|---|---|---|
| 1 | One app, three workloads | on-demand vs reserved vs spot vs Savings Plan, matched to the demand pattern; per-second billing with a 60 s minimum | s4-5, s9, s20 |
| 2 | Which instance is cheaper for the job | instance families and sizes; price per unit of work, not price per hour; region price differences | s7-9 |
| 3 | Who sends you the bill | SaaS integrated vs separate pricing; what drives the price at IaaS, PaaS and SaaS level | s6, s10-12 |
| 4 | Building a monthly bill | network (inbound, outbound, inter- vs intra-cloud, tiered rates), server, storage (space over time, I/O), service (users, transactions, subscription) metrics | s18-22 |
| 5 | Should we move to the cloud? | Capex vs Opex, cost of capital, sunk costs, integration costs, lock-in costs | s13-16 |
| 6 | Owning a datacenter | datacenter TCO = depreciation + Opex for building and servers; Cases A, B, C; effect of 50% utilisation | s23-28 |

Then one mixed gap set (4-5 short questions) on what he gets wrong.

## Annotations on the slides (Joshua's handwriting, checked)

- **s9 "for spiky workloads" (on-demand), "for steady workloads" (reserved), "for non-critical workloads" (spot), "you decide based on your workload!":** correct.
- **s15 "cost of borrowing"** over cost of capital: correct.
- **s19 "because that's necessary for the cloud to work"** next to "some providers may not charge" for intra-cloud traffic: a guess, not a slide reason, and not true everywhere (AWS, for example, charges for traffic between availability zones in one region; standard AWS pricing docs). Read the slide as "intra-cloud traffic is often free or cheap", nothing more.
- **s25 "on average case B lowest cost because cost of higher power doesn't offset cost of depreciation":** cannot be checked from the slides. The pie charts on s26-28 show each case's cost *shares*, not its total, so no slide shows which case is cheapest. The reasoning is sound only as a direction: cheaper servers cut depreciation by more than the extra power adds.
- **s26 "server amortization: higher depreciation due to rapid technological obsolescence":** half right. Server amortisation dominates Case A mainly because high-end servers cost a lot to buy. Obsolescence explains why servers are written off over a few years while the building lasts much longer, which makes the yearly server charge large.
- **s27 "higher power utilization", "server depreciation went down":** correct as shares of the total.
- **s28 "50% utilization -> power goes down", "data center depreciation goes up because you're only using 50% of it even though it has been built":** correct. Half as many servers run, so power and server costs fall, but the building cost is fixed, so its share (and its cost per useful server) rises.
- **Slide figure error (not handwriting):** on s26 the Case A labels say Server Interest 3.8% and Server OPEX 3.8%, but the slices say 8.4% and 3.3%. The slice numbers add up to 100%, so they are the right ones.

## Detailed Notes

### Concept 1. Pricing models matched to the demand pattern (S1)

- **Price (slides, s4):** the unit cost of using a resource, based on time, number of transactions and so on, charged per hour, minute or second.
- **On-demand (slides, s9, s20):** pay per use, no commitment, charged to the nearest second with a 60-second minimum, counted from server start to stop. Fits spiky or unpredictable demand.
- **Reserved (slides, s5, s9, s20):** a one-time upfront fee plus a discounted hourly rate, for a term from start date to expiry date. Cheaper per hour than on-demand. Fits steady demand.
- **Spot (slides, s9):** consumers bid for unused capacity at a lower price than on-demand; suited to jobs that are not time critical. (Beyond slides: AWS stopped the bidding in 2017 and now sets the spot price itself, and spot instances can be reclaimed at short notice, which is why the job must tolerate interruption. Answer exam questions with the slide wording.)
- **Savings Plan (slides, s9):** low prices for a commitment to consistent usage over a longer term; "flexible". It is an alternative to reserved instances for steady demand, not something stacked on top of them.
- **Region (slides, s9):** prices differ by region because operating costs (energy, communication, maintenance) differ.
- **Why reserving for spikes wastes money (reasoning):** a reservation is paid for every hour of its term, used or not. The lower hourly rate only beats on-demand when the server is busy for most of those hours. Spike servers sit idle most of the month, so the cheaper rate is paid on hours nobody uses.

**Key one-liner:** commit (reserved or Savings Plan) only for capacity that runs nearly all the time; use on-demand for unpredictable extra capacity and spot for work that can be interrupted and delayed.

### Concept 2. Price per unit of work, not per hour (S2)

- **Instance types (slides, s7):** EC2 VMs come in families (general purpose, compute optimised, memory optimised, accelerated computing, storage optimised, HPC optimised), each split into sizes with different CPU, memory, storage and network.
- **What to compare (reasoning):** a job needs a fixed amount of work, so the cost is price per hour × hours needed = price per hour ÷ work per hour. A dearer instance that matches the job's bottleneck (CPU for encoding) can finish so much faster that it costs less in total.
- **Short jobs and the 60 s minimum (slides, s9; arithmetic my reasoning):** each on-demand launch is billed at least 60 s. Jobs shorter than a minute, each on its own instance, pay for time they never use; running them back to back on one instance avoids that.

> [!WARNING]
> **Mistake:** a cost answer given in hours ("$16.66") because the hourly price was never applied. Write the unit next to every number (h, GB, $) and finish with price × quantity. Same kind of slip as L07 G5 (off by 100x).

**Key one-liner:** compare instances by cost per unit of work (price per hour ÷ work per hour), and batch jobs shorter than a minute onto one instance.

### Concept 3. SaaS integrated vs separate pricing (S3)

- **What drives the price at each level (slides, s6):** IaaS by resources allocated and used (number of virtual servers, network data transferred, storage allocated); PaaS also by software configuration, development tools and licence fees; SaaS by number of application modules subscribed, number of nominated users and number of transactions.
- **Integrated (slides, s10-11):** the consumer pays the SaaS provider, which in turn pays the IaaS provider for hosting. One bill.
- **Separate (slides, s10, s12):** the consumer pays the SaaS provider for the software and the IaaS provider for hosting it. Two bills.
- **Who carries the usage risk (reasoning):** under integrated pricing the consumer's bill follows the SaaS price driver (for example per user), so a usage surge with the same users changes nothing for the consumer; the SaaS provider pays the bigger hosting bill. Under separate pricing the hosting bill moves with server count, so the consumer pays for the surge, but in normal months pays actual usage without the SaaS provider's markup and safety margin, and can see the hosting cost.

**Key one-liner:** integrated = one bill, SaaS provider carries the hosting cost and its swings; separate = two bills, the consumer carries them but pays actual usage.

### Concept 4. Usage cost metrics and building a bill (S4)

- **Four metric groups (slides, s18):** network (inbound, outbound, intra-cloud), server (on-demand and reserved VMs), storage (space allocated, I/O transfers), service (subscription duration, number of users, number of transactions).
- **Network (slides, s19):** total bytes accumulated over a period, with tiered rates (example: first 1 GB free, S$0.01/GB up to 1 TB, S$0.005/GB after). Inter-cloud traffic (replication, synchronisation to another cloud) may have different in and out rates; many providers do not charge inbound. Some providers do not charge intra-cloud traffic.
- **Tiers are charged band by band (reasoning, standard tiered pricing):** each band of usage is billed at its own rate, like tax brackets. Crossing a threshold makes only the usage above it cheaper, never the usage below it.
- **Server (slides, s20):** on-demand counts from server start to stop; reserved has an upfront cost and runs from start date to expiry date.
- **Storage (slides, s21):** bytes allocated, summed over time from allocation to release; I/O data transferred may also be charged (some providers do not).
- **Service (slides, s22):** subscription duration, number of nominated users (example S$0.90 per extra user per month), number of transactions (request-response exchanges; example S$0.05 per 1,000).

> [!WARNING]
> **Mistake:** charging all 14,000 GB at the top tier's rate once usage passed 10,000 GB. Tiered rates apply band by band: 100 GB free, the next 9,900 GB at $0.09, only the 4,100 GB above 10,000 at $0.05 (total $1,096, not $700). Charging everything at the top rate would make the bill drop as usage grows.

**Key one-liner:** count only billable traffic (outbound, including replication to another cloud), charge each tier band at its own rate, and charge storage for the time it is allocated.

### Concept 5. Business cost metrics: should we move to the cloud? (S5)

- **Business costs = Capex + Opex (slides, s14).** Up-front costs (Capex): the initial investment to obtain, deploy and administer IT resources; high on-premise (hardware, software, deployment), low in the cloud (labour to set up the cloud environment). On-going costs (Opex): running and maintaining resources (licensing fees, electricity, maintenance); higher on-premise.
- **Cost of capital (slides, s15):** the cost of raising funds (borrowing). If high, leasing cloud resources is justified, because the cloud avoids borrowing for a big Capex.
- **Sunk costs (slides, s15):** prior investment in existing IT resources. If significant, the cloud cannot be justified. Mechanism (reasoning): the hardware is already paid for and still usable, so moving means paying cloud bills while that investment sits idle; the case for the cloud returns when the hardware reaches end of life.
- **Integration costs (slides, s16):** the effort to make IT resources inter-operate on the new environment (for example a new cloud platform). High cost makes the cloud less appealing. Custom systems tied to local hardware are the typical high case; off-the-shelf software is the low case (reasoning).
- **Locked-in costs (slides, s16):** the cost of moving from one cloud provider to another. High cost makes the cloud less appealing. Not the same as integration cost, which is the cost of the first move onto a platform.
- **Cost metrics in general (slides, s13):** a financial comparison of on-premise TCO against cloud provisioning, used by the consumer (should we adopt?) and by the provider (how to price a service).

**Key one-liner:** the cloud wins when borrowing is expensive and there is little to throw away or rewire; recent hardware (sunk cost) or hard-to-move custom systems (integration cost) argue for waiting.

### Concept 6. Datacenter TCO and utilisation (S6)

- **TCO = Capex + Opex (slides, s23).** Capex: up-front investment depreciated over a set time frame (building the datacenter, buying servers). Opex: recurring running costs (electricity, repairs and maintenance, salaries).
- **TCO of owning hardware (slides, s24):** datacenter depreciation + datacenter Opex (the building and the infrastructure that keeps hardware working) + server depreciation + server Opex (the IT equipment).
- **Case A (slides, s25-26):** high-end servers. Server amortisation dominates (65.9%), because high-end servers are expensive and are written off over a few years.
- **Case B (slides, s25, s27):** lower-cost, higher-power servers. Server amortisation falls to 29.5%; power (server power 14.3%, PUE overhead 11.5%) and datacenter costs (amortisation 18.5%, interest 10.3%, Opex 10.6%) become larger shares.
- **Case C (slides, s25, s28):** Case B at 50% datacenter utilisation. DC amortisation rises to 32.4% and DC interest to 18.1%; server amortisation falls to 17.3% and server power to 8.4%.
- **Shares are not totals (reasoning):** each pie shows shares of its own total. A larger share of a smaller total can be fewer dollars, so compare designs by total TCO for the same useful work, never by slice size.
- **Why utilisation matters (reasoning):** the building's yearly depreciation is fixed once it is built, used or not. Running half the servers halves the server and power costs but not the building charge, so the building's cost per useful server doubles and its share of TCO grows.

> [!WARNING]
> **Mistake:** reading the pie charts as if a bigger slice meant more dollars, and thinking the building's depreciation goes up when only half the datacenter is used. Each pie is shares of its own total. The building's yearly charge is fixed; at 50% utilisation it stays the same while server and power costs halve, so it becomes a bigger share and costs twice as much per running server.

**Key one-liner:** the building is a fixed yearly cost, so an underused datacenter pays the same for its building with fewer servers to spread it over; compare designs by total cost per unit of work, not by pie shares.

## Reference only (not tested)

- EC2 family names and letters (s7): look them up in the slides.
- Pricing factors for the provider (s4): design/operation overhead, savings from sharing and datacenter optimisation, competition and regulation.
- Payment options (s5): customisation, prepaid, postpaid, instalments; volume discounts.

## Not yet tested

Not tested by a scenario: provider pricing factors (s4) and payment options (s5), both reference only; service-usage arithmetic per user and per transaction (s22) and storage I/O charges (s21), which work like the network and storage arithmetic already tested.
