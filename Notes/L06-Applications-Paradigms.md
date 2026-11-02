# L06 Applications and Paradigms (Parts 1 and 2)

Cards: `Notes/cards/L06-cards.md` (P1-C01 to C16, P2-C01 to C15). Past-paper questions (L06 main): 24S2 Q18, Q19; 25S1 Q2, Q3, Q4, Q5, Q13, Q19; 25S2 Q2, Q7, Q12, Q15, Q25 (see `PAST-PAPER-MAP.md`).

## Scenario Plan

| # | Idea (hidden from Joshua until review) | Cards | Past-paper link |
|---|---|---|---|
| 1 ✅ | Which applications suit the cloud (divisible vs complex workflow, chatty instances) and the development challenges: diagnose a symptom (performance isolation at high utilisation, failures at scale, logging cost) | P1-C02, C03 | 25S2 Q15 |
| 2 ✅ | Web architecture: three tiers, REST vs SOAP, statelessness and caching for a multi-language client base | P1-C04 to C08 | - |
| 3 ✅ | Choosing a service model for one goal (the data-analytics app): which steps the consumer does under SaaS, PaaS, IaaS; PaaS split (provider maintains stack, consumer controls deployment) | P1-C09 to C16 | 25S1 Q2, Q13, Q19; 25S2 Q2 |
| 4 ✅ | MapReduce idea and execution: what the programmer writes, where map output goes, when reducers start, where final results land | P2-C01 to C04 | 25S1 Q5 |
| 5 ✅ | Word-count trace: mapper output, reducer input and output; who does shuffle, merge and sort | P2-C05 | 25S1 Q5 |
| 6 ✅ | MapReduce performance: data locality, worker reuse, too many workers or reducers | P2-C06 | 25S1 Q3 |
| 7 ✅ | Hadoop stack (YARN, MapReduce, HDFS) vs Spark: pick for real-time or ML; why disk-based is slow | P2-C08 to C10 | - |
| 8 ✅ | FaaS fit: bursty event-driven work, no idle cost, async offloading (L01 G8 concept) vs a steady always-on workload | P2-C11 | 24S2 Q19; 25S1 Q4; 25S2 Q12, Q25 |
| 9 ✅ | FaaS limits and responsibilities: state and connections kept outside, functions not calling functions, resource limits; who manages what across VMs, containers, PaaS, FaaS | P2-C12 to C14 | 24S2 Q18; 25S2 Q7 |
| Gap ✅ | One mixed set (4-5 short questions) on concepts he actually got wrong | - | - |

## Detailed Notes

### Concept 1: Which applications suit the cloud, and the development challenges (P1 s4-6)

- **Ideal (slides, P1 s4):** applications that can be divided into as many independent tasks as possible: web services, database services, search, machine learning with large models.
- **Not ideal (slides, P1 s4):** (1) a complex workflow with multiple dependencies (part A → B → C, as in high-performance computing), because the steps cannot run in parallel; (2) intense communication among concurrent instances, because every exchange goes over the network, so bandwidth and latency become the limit.
- **Key challenges (slides, P1 s5):** the consumer must scale with a dynamic load, recover after failure and support checkpoint/restart; the provider must manage many systems and guarantee quality of service.
- **Development challenges (slides, P1 s6):**
  - **Performance isolation:** virtualisation shares VMs and multitenancy shares application services, so performance degrades when utilisation is high (a CPU-only slowdown at the provider's busy time points here).
  - **Reliability:** with many cooperating servers, failures are expected, not exceptional.
  - **Latency/bandwidth fluctuations:** caused by shared network resources (needs network traffic to apply).
  - **Data logging:** needed for recovery, but limited because logging costs performance.

**Key one-liner:** the cloud suits work that splits into independent tasks; sequential dependencies and chatty instances fit poorly, and shared resources mean performance can sag when everyone is busy.

### Concept 2: Web architecture, REST and statelessness (P1 s7-13)

- **Web-based style (slides, P1 s7):** cloud apps use a web client-server architecture (browser client, web server); web technology is both how services are built and how they are managed.
- **Three tiers (slides, P1 s8-9):** presentation (user interface; sits on **both** client and server side), application (logic; the web server handles requests and generates content), data (persistent stores; web and application servers talk to the database).
- **SOAP (slides, P1 s10):** a protocol with a common **XML** message format for requests and responses.
- **REST (slides, P1 s11-12):** an architecture for distributed hypermedia systems with **stateless servers**, platform and language independent, supports caching. Principles: uniform interface, client-server decoupling, statelessness, cacheability, layered system, code on demand (optional).
- **Why statelessness matters (reasoning, links to L03 load balancing):** a stateless server keeps nothing about earlier requests, so each request carries what it needs. Then a load balancer can send any request to any copy. If servers keep per-user state in their own memory, the next request may land on a server that never saw the user: wrong results or errors. Fix: the client sends the state with each request (page number, token), or the state lives in a shared external store.
- **Web service APIs (slides, P1 s13):** clients in different languages need one standard interface; REST requests and responses travel over HTTP as XML or JSON.

**Key one-liner:** stateless servers let any copy answer any request, which is what makes scaling out behind a load balancer work; REST is the lightweight, cacheable, language-independent way to expose that.

### Concept 3: Choosing a service model for one goal (P1 s16-29)

The slides run one goal (a data-analytics app) through all three models; "which as-a-service?" "It depends" (P1 s23) on how much the consumer wants to build and control.

| | SaaS | PaaS | IaaS |
|---|---|---|---|
| Consumer does (slides, P1 s25, s27, s28) | open the app, give it data, read the report | build own pipeline on a ready MERN system, give data, report | create a Linux instance, install and configure MERN, build pipeline, give data, report |
| Consumer controls | only its data; no APIs, no platform | its software's deployment and configuration settings | everything installed above the OS (versions, settings) |
| Provider handles | the whole app, run transparently; multi-tenant; pricing free, pay-as-you-go or subscription | installs and maintains software, libraries, middleware; hides the infrastructure; exposes an API; built-in scalability, maintenance, versioning | physical infrastructure and the OS; offers preconfigured VMs, elastic scaling, metering |
| Typical user (P1 s16) | end users | application developers | network architects, IT administrators |
| Pick it when | no programmers, need results fast | developers want to write code but not run the stack | need a specific software version, or lift-and-shift |

- **Annotation check:** Joshua's note "LAMP stack - packaged dev env" on the IaaS slide (P1 s22) is wrong: a packaged stack is the PaaS route; on IaaS you install it yourself. The nearest IaaS item is "preconfigured VMs" (a ready machine image, not a managed platform).

**Key one-liner:** moving IaaS → PaaS → SaaS removes steps from the consumer's list (install stack, then build pipeline) and takes away the matching control.

### Concept 4: MapReduce idea and execution (P2 s3-7)

- **Idea (slides, P2 s3-4):** for arbitrarily divisible work on web-scale data (hundreds of GB to PB, too big for one disk, so a distributed file system is needed). Split the data into blocks, run the same program on each block in parallel (SPMD: same program, multiple data), then merge the partial results once all are done. Input and output are sets of <key, value> pairs.
- **Programmer's view (slides, P2 s5):** read data, MAP (extract what you need from each record), shuffle and sort, REDUCE (aggregate, summarise, filter), write results. **The programmer writes only map and reduce**; the system does the rest.
- **Phases (slides, P2 s6):** mappers process splits in isolation; their intermediate outputs are read into reducers (that reading is **shuffling**); reducers produce the final outputs.
- **Execution (slides, P2 s7):** (1) the application starts a master, M map workers and later R reduce workers; (2) the master partitions the input into M segments; (3) each map worker processes its segment; (4) map results go to the **local disk** of that worker's server; (5) only when **all** map workers have finished do the R reducers read and merge the partial results; (6) reducers write final results to a **shared storage server**; (7) the master monitors and ends the application when all tasks are complete.
- **Why local disk (reasoning, from P2 s12):** writing where the data was produced avoids pushing all intermediate data over the network to one shared server, which would also become a bottleneck.

**Key one-liner:** the programmer writes map and reduce; map output stays on local disk, reducers start only after every mapper is done, and only final results go to shared storage.

### Concept 5: Word-count trace and the shuffle (P2 s8-11)

- **Map (slides, P2 s8, s11):** tokenise each line and emit **(word, 1) for every occurrence**. "to be or not to be" gives (to,1) twice, never (to,2).
- **Partition and shuffle (slides, P2 s9-10):** each map task splits its output into partitions by key, one per reduce task; the system moves each partition to its reducer (shuffle), where arriving partitions are **merged and sorted** into one file. The programmer does none of this.
- **Reduce (slides, P2 s11):** receives each word with its list of 1s, e.g. cloud: [1,1,1], sums them and emits (cloud,3). Final pairs go to HDFS (P2 s10).

> [!WARNING]
> **Mistake:** the mapper adds up repeats within its own split and emits (cloud,2). In the slides' model the mapper emits (word,1) for every occurrence and only the reducer adds up; the reducer therefore receives a list of 1s, cloud: [1,1,1]. (Map-side pre-summing, a Hadoop "combiner", is beyond the slides.)

**Key one-liner:** map emits (word,1) per occurrence; the system partitions by key, shuffles, merges and sorts; reduce sums the list of 1s.

### Concept 6: MapReduce performance (P2 s12)

- **Data locality (slides):** the master creates data-localised tasks (a map task runs where its input block already is) to minimise network communication, and so latency.
- **Worker reuse (slides):** worker nodes switch between mapper and reducer, so the machines that mapped can then reduce (no separate reducer fleet).
- **Parallel maps and reduces (slides):** each map worker has its own data and produces local intermediate values; reduce workers also run in parallel.
- **More is not always faster (slides: "an optimal number of reducers for best performance"):** past the optimum, (1) the master is overloaded coordinating and monitoring tasks; (2) shuffle traffic grows, because each reducer fetches from every mapper, and machines spread over more racks add latency; also (3) more servers mean more expected failures (P1 s6), and (4) tiny splits let fixed per-task overhead dominate (reasoning).

**Key one-liner:** run tasks where the data is and reuse workers; adding workers helps only up to an optimum, after which master overload and network traffic slow the job.

### Concept 7: Hadoop and Spark (P2 s14-18)

- **Hadoop (slides, P2 s14-15):** the open-source MapReduce (Apache + Yahoo), after Google's closed one; adds a distributed storage layer, **HDFS**, which mimics Google File System.
- **Stack (slides, P2 s16):** **YARN** = resource allocation (scheduler: who gets CPU and memory); **Hadoop MapReduce** = computation; **HDFS** = storage.
- **Multi-node flow (slides, P2 s17):** each node reads from its local HDFS store, maps, partitions; intermediate pairs are exchanged among all nodes (shuffle), sorted, reduced and written back to local HDFS. Writing to disk between phases is the slow part.
- **Spark vs Hadoop MapReduce (slides, P2 s18):**

| | Spark | Hadoop MapReduce |
|---|---|---|
| Batch processing | yes (faster) | yes |
| Real-time processing | yes | no |
| Machine learning | built in (MLlib) | needs external tools |
| Where it works | in memory | on disk between phases |
| Pick it when | results needed in seconds, or ML on the data | large nightly batch jobs |

- Spark **can run independently or on top of Hadoop**, so an existing Hadoop cluster can add Spark and keep its data in HDFS.

**Key one-liner:** Hadoop = YARN (schedules) + MapReduce (computes) + HDFS (stores), disk-based and batch-only; Spark adds in-memory, real-time and built-in ML, and can sit on the same cluster.

### Concept 8: When FaaS fits (P2 s20-22; includes the L01 G8 async concept)

- **FaaS (slides, P2 s20):** build scalable, reactive, **event-driven** applications from small single-purpose (Lambda) functions; an event triggers a function, which exits after running. **No idle capacity.** Lambda is **stateless**.
- **Serverless (slides, P2 s21-22):** no servers to provision or manage; the consumer **pays only while code executes**; no VMs or containers in the programming model; the vendor scales with the workload. Use cases: web/mobile backends, real-time data processing, chatbots. Nesting: event-driven computing ⊃ FaaS ⊃ serverless FaaS.
- **Asynchronous offloading (beyond slides; source: 25S2 Q25 answer key, "doing these operations async is key and here FaaS ... can help"; slides only imply it via event-driven FaaS, P2 s20, and message queueing, P1 s3):** when a request does slow follow-up work (thumbnails, moderation, fare, receipt) before replying, reply at once and hand the rest to background functions triggered by an event. The user stops waiting because nothing waits for the work, not because the function is fast.
- **Fits:** bursty or spiky, event-triggered, short tasks with idle periods (pay nothing at 3 am). **Fits poorly:** steady 24/7 load (no idle time to save) or work that must hold connections or in-memory state between calls.

> [!WARNING]
> **Mistake (twice: L01 G8, L06 S8):** making a slow request feel instant by making the work faster (a "lightweight, fast" Lambda). What makes the reply immediate is **asynchronous processing**: reply now, fire an event, and let background functions do the slow work. FaaS then adds cost that follows usage (no idle capacity, pay per execution).

**Key one-liner:** FaaS fits spiky, event-triggered, short work: reply now, process in the background, pay only when code runs; a steady, stateful, always-connected service does not fit.

### Concept 9: FaaS limits, best practices and who manages what (P2 s23-29)

- **Best practices (slides, P2 s23):** one action per function (lightweight); self-contained, so functions **do not call other functions**; as few libraries as possible. To build a pipeline, chain single-purpose functions by **events** (one function's output, e.g. a saved file, triggers the next), not by direct calls.
- **Advantages vs VMs, containers, PaaS (slides, P2 s24-25):** provisioning in milliseconds (vs minutes vs hours); almost no ongoing administration; elastic scaling, since each action scales by itself; **no capacity planning**; provider handles all maintenance (like PaaS), so of the four compute models, **containers and VMs need the most maintenance** (24S2 Q18 key); high availability is inherent; excellent resource utilisation.
- **Limits (slides, P2 s24-25):** limited ability to persist connections, and **state must be kept in an external service or resource** (database, cache); the FaaS model has **resource limits**, so long, heavy jobs (e.g. converting a 2-hour 4K video) belong on a VM or container.
- **How Lambda runs (slides, P2 s26-27):** event source → event → your function (code) → other services. You supply the code and the configuration (which event sources invoke it); the system wires event sources to functions and runs the infrastructure that detects events.
- **Annotation check:** Joshua's note "cookies -> maintain state" (P2 s24): cookies are one client-side way to carry state; the slide's fix is an external service or resource.

> [!WARNING]
> **Mistake (S9, G4 for chaining; S2, S9, G1 for state):** when a FaaS rule is broken, moving the work off FaaS or merging functions (to PaaS for chained functions, to a container for state). The slide fixes stay inside FaaS: chain single-purpose functions by **events**, and keep state in an **external service** (database or cache). Leave FaaS only for its resource limits (long, heavy jobs).

**Key one-liner:** FaaS removes administration and capacity planning, but each function must be small, self-contained and stateless: chain by events, keep state outside, and move heavy long jobs to VMs or containers.

## Annotations to verify (Joshua's handwritten notes on the slides)

Check each one when its concept comes up; call out any that are wrong.
- P1 s22 (IaaS): "LAMP stack - packaged dev env". **Called out in S3: wrong.** on IaaS the consumer installs the stack (P1 s28 IaaS route installs MERN itself); a packaged, ready-made stack is the PaaS route (s26-27). A preconfigured VM image is the nearest IaaS fit.
- P2 s6: "intermediary output stored on local disk": matches s7 step 4.
- P2 s12: "reuse the machine that did mapping to do reducing" (cost reduction): consistent with "worker nodes switch between mapper and reducer".
- P2 s24: "cookies -> maintain state" (checked in S9, partly right): state must be kept outside the function (external service); cookies are one client-side way, the slide says external service or resource.

## Reference only (not tested)

- Provider common features (P1 s3), SOAP message format and transport (P1 s10), MapReduce industry uses (P2 s13), Hadoop history and GFS (P2 s14-15), Lambda setup steps and CLIs (P2 s28-29).

## Not yet tested

None: every L06 concept was tested (gap set about 65%). Reference-only items above are not tested by design.
