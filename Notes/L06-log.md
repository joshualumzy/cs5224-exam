# L06 Log

---

## S1. Which workloads suit the cloud; development challenges

**Scenario:** A research group moves two workloads to a public cloud. A: a weather simulation on 200 instances where each time step needs the previous one and every instance exchanges boundary data with its neighbours every second. B: resizing 5 million archived photos into thumbnails. Q1: which suits the cloud better, and two reasons the other is a poor fit? Q2 (MCQ): B runs on unchanged VM sizes; at month-end, when the provider's other customers are busiest, each thumbnail takes longer to compute; purely CPU-bound, no network traffic. Cause? (a) reliability (b) performance isolation (c) latency/bandwidth fluctuations (d) data logging overhead (e) under-provisioning.

**Your answer:** Q1: "B, because it's parallelizable whereas A runs in sequence; and each of B's pieces can be done independently, whereas A has to exchange boundary data with its neighbours every second so it can't run independently." Q2: "Nothing is sent over the network, so not latency or bandwidth. Performance isolation: when utilisation is high, performance degrades."

**Grade: about 90%.** Q1 ~85%: B and the sequential dependency are right; the second reason named the constant data exchange but not why it hurts (it depends on network bandwidth and latency, which are shared and fluctuate in the cloud). Q2 100%: (b), with the network distractor correctly ruled out.

**Correct:** Q1: B. A is a poor fit because (1) it is a complex workflow with dependencies (step N needs step N-1), so it cannot be split into independent tasks, and (2) it has intense communication among concurrent instances, so performance is bound by network bandwidth and latency (P1 s4). Q2: (b) performance isolation: VMs and multitenant services share hardware, so performance drops when overall utilisation is high (P1 s6).

---

## S2. Web architecture: statelessness, REST vs SOAP, three tiers

**Scenario:** A fitness company's cloud API serves a Swift iOS app, a Kotlin Android app and a partner's Python script. Each API server remembers in its own memory which page each user last saw, to serve "page 2". After scaling to 5 identical servers behind a load balancer, users randomly get page 1 again or an error. Q1: which design principle was broken, and how do you fix it? Q2 (MCQ, false statement): (a) REST + JSON over HTTP gives all three clients one interface (b) SOAP defines a common XML message format (c) REST caching answers repeated requests faster (d) in three-tier, the presentation layer runs only in the browser (e) client-server decoupling lets the apps change without changing the server.

**Your answer:** Q1: "Statelessness. Each API server kept its own state, and when scaled to five identical servers the states have a conflict." Q2: "D, because the presentation layer runs on both the client and the server side."

**Grade: about 75%.** Q1 50%: principle right; mechanism off (nothing conflicts: the next request lands on a server that has no record of the user); no fix given although asked. Q2 100%.

**Correct:** Q1: statelessness (REST principle, P1 s12; "client communication with stateless servers", P1 s11). The load balancer sends the next request to another server that never saw the earlier one. Fix: keep no session state on the servers: the client sends what is needed with every request (e.g. the page number or a page token), or the state goes into a shared external store all servers read; then any copy can serve any request. Q2: (d): the presentation layer sits on both the client and the server side (P1 s9).

---

## S3. Choosing a service model for one goal

**Scenario:** A retail chain wants three teams to analyse last month's sales and report. X: marketing analysts, no programmers, need results this week. Y: developers building their own pipeline in code who do not want to install or update databases, libraries or middleware. Z: must run one specific older database version with custom OS settings. Q1: which service model for each, one reason each? Q2: for Y's model, one thing the team still controls and one the provider takes off its hands.

**Your answer:** Q1: "X SaaS, they have no programmers so they need the finished software. Y PaaS, a platform for developers to build their pipeline. Z IaaS, it lets them run specific databases and custom OS settings; it gives access to the resources themselves so they can manage it." Q2: "The team controls the software, its deployment and configuration settings. The provider takes off the installation and maintenance of the libraries, software and middleware."

**Grade: 100%.**

**Correct:** X SaaS (supply data, get results; P1 s24-25). Y PaaS (consumer creates software with the provider's tools and controls deployment and configuration; provider installs and maintains software, libraries and middleware, hides the infrastructure, gives scalability, maintenance and versioning; P1 s26-27). Z IaaS (consumer creates a Linux instance and installs and configures the stack itself, so it chooses versions and OS settings; P1 s28). Annotation called out: Joshua's note "LAMP stack - packaged dev env" on the IaaS slide (P1 s22) is wrong; a packaged stack is the PaaS route; on IaaS you install it yourself; the nearest IaaS item is "preconfigured VMs".

---

## S4. MapReduce execution: where map output goes

**Scenario:** A shop counts clicks per product over 40 TB of logs with MapReduce (100 map workers, 10 reduce workers). An engineer proposes each map worker write its output straight to the shared storage server "so reducers can find it easily". Q1: where does MapReduce put each map worker's output, and why is that better? Q2 (MCQ, true statement): (a) a reducer starts merging when the first map worker finishes (b) the programmer writes map, shuffle and reduce (c) the master splits the input into 100 segments and ends the application when every task is complete (d) final results go to the map workers' local disks (e) each reducer reads from only one assigned map worker.

**Your answer:** Q1: "Into each map worker's own local disk. Better because it minimises network communication and therefore reduces latency." Q2: "C."

**Grade: 100%.**

**Correct:** Q1: on the local disk of the server where the map instance runs (P2 s7 step 4); only final results go to a shared storage server (step 6). Keeping data where it was produced cuts network traffic (P2 s12: data-localised tasks minimise network communication), and avoids 100 workers flooding one shared server (bottleneck). Q2: (c) (P2 s7 steps 1-2, 7). Reducers start only when all maps have finished (step 5); the programmer writes only map and reduce (P2 s5, s11); final results go to shared storage; each reducer reads its partition from every map task (P2 s9).

---

## S5. Word-count trace

**Scenario:** Word count on Split 1 "cloud is cheap" and Split 2 "cloud is fast cloud". Q1: mapper 2's output; what the reducer receives for "cloud" and what it outputs. Q2 (MCQ, 3 reduce tasks): how do all "cloud" pairs reach one reducer? (a) master sends every pair to every reducer, which discards others (b) each map task partitions its output by key, one partition per reduce task; the system sends each partition to its reducer, where partitions are merged and sorted (c) reducers re-read the input splits (d) mappers send pairs to shared storage and reducers search it (e) the programmer's reduce function fetches pairs by key.

**Your answer:** Q1: "Mapper 2 outputs cloud 2, is 1, fast 1. The reducer receives for cloud 1, 2 and outputs 3." Q2: "B."

**Grade: about 75%.** Q1 50%: final count right, but the mapper aggregated (cloud,2), so the reducer input was wrong. Q2 100%.

**Correct:** Q1: mapper 2 emits one pair per occurrence: (cloud,1), (is,1), (fast,1), (cloud,1) (P2 s8: Hamlet's mapper emits "to,1" twice). The reducer receives cloud: [1,1,1] and outputs (cloud,3) (P2 s8, s11: reduce "gets the word along with a list of 1s" and sums them). Map only extracts; reduce aggregates. (A "combiner" that pre-sums on the map side exists in Hadoop but is beyond the slides.) Q2: (b) (P2 s9).

---

## S6. MapReduce performance: more workers is not always faster

**Scenario:** A job takes 60 min on 20 workers; on 2,000 workers the team expects ~36 s but gets 25 min, with the master at 100% CPU. Q1: two reasons 100x workers did not give 100x speed. Q2 (MCQ): where does the master prefer to run a map task, and why? (a) idle server in another datacenter, spread load (b) the server already storing the task's input block, minimise network communication (c) a dedicated map-only machine (d) the shared storage server (e) the fastest CPU wherever the data is.

**Your answer:** Q1: "The master node is at 100% CPU, so it's overwhelmed with coordination work; the slides say there's an optimal number of workers for best performance. Second reason: not sure." Q2: "B."

**Grade: about 75%.** Q1 50%: master overload / optimal number right; no second reason. Q2 100%.

**Correct:** Q1: (1) the master is overloaded coordinating and monitoring thousands of tasks; there is an optimal number of workers/reducers for best performance (P2 s12). (2) Network communication grows: each reducer fetches its partition from every mapper, so shuffle traffic explodes, and machines spread across more racks add latency (P2 s7, s12). Also acceptable: more servers mean more expected failures (P1 s6); tiny per-worker splits let fixed per-task overhead dominate (reasoning). Q2: (b): data-localised tasks minimise network communication (P2 s12); (c) is wrong because worker nodes switch between mapper and reducer.

---

## S7. Hadoop stack vs Spark

**Scenario:** A bank runs nightly Hadoop MapReduce batch jobs on its own cluster with data in HDFS; it now wants to flag suspicious card payments within seconds and to train ML models on the same data. Q1: what to add or change while keeping the data where it is, and why it is faster than Hadoop MapReduce? Q2 (MCQ): which Hadoop layer decides CPU and memory per job? (a) HDFS (b) Hadoop MapReduce (c) YARN (d) GFS (e) reduce workers.

**Your answer:** Q1: "Change to Apache Spark: it's designed for real-time and advanced analytics, so they can train ML models and flag payments within seconds; it's a fast in-memory engine, whereas MapReduce stores things on disk, which is slower and would not meet the time requirement." Q2: "YARN."

**Grade: about 90%.** Q1 ~85%: Spark and both reasons right; missed that Spark runs on top of the existing Hadoop cluster and reads HDFS ("change to" implied replacing). Q2 100%.

**Correct:** Q1: add Spark on top of the existing Hadoop cluster (it "can run independently or on top of Hadoop", P2 s18), reading the same HDFS data. Spark does real-time processing (Hadoop: no) and has built-in ML (MLlib; Hadoop needs external tools); it is faster because it processes in memory, while MapReduce writes intermediate results to disk between phases (P2 s7, s17-18). Q2: (c) YARN, resource allocation/scheduler; MapReduce = computation, HDFS = storage (P2 s16).

---

## S8. When FaaS fits: async offloading vs steady stateful load

**Scenario:** A ride-hailing company runs two parts on always-on VMs sized for rush hour. (i) At trip end the server computes the fare, emails a receipt and updates loyalty points before the app shows "Trip complete" (~6 s); trips spike at rush hour, near zero 2-5 am. (ii) Driver matching keeps an open connection to every active driver's phone and holds live positions in memory; steady load 24/7. Q1: for (i), what change makes "Trip complete" appear at once and cost follow trips? Q2 (MCQ): is FaaS a good fit for (ii)? (a) yes, scales automatically (b) no: stateless, no persistent connections, and steady load gains little from no idle capacity (c) yes, Lambda keeps positions in memory (d) no, cannot be triggered by phone events (e) yes, if one function keeps calling the others.

**Your answer:** Q1: "Add a lambda function triggered by the end of a trip; it's very lightweight to email a receipt and update loyalty points, and it can work very fast." Q2: "B."

**Grade: about 75%.** Q1 50%: event-triggered Lambda right (covers cost following trips, though the no-idle-cost reason was not stated); the immediate reply was attributed to speed, not to asynchronous processing. Second time (L01 G8 had the same gap). Q2 100%.

**Correct:** Q1: reply "Trip complete" immediately and publish a trip-ended event; the fare, receipt and loyalty work run in the background (asynchronously) as event-triggered functions, ideally one single-purpose function each (P2 s23), so the rider never waits. Cost follows trips because FaaS has no idle capacity and you pay only while code executes, scaling with the workload (P2 s20-21). Q2: (b): Lambda is stateless and has limited ability to persist connections; state must live in an external service (P2 s20, s24); steady 24/7 load gains little from no idle capacity.

---

## S9. FaaS limits and responsibilities

**Scenario:** A startup moves its image-upload API to FaaS. (i) One function resizes, then calls a second to watermark, which calls a third to save metadata. (ii) A function keeps the user's login session in a variable inside the function; on the next request the session is sometimes gone. (iii) A function converting 2-hour 4K videos fails partway every time. Q1: one line each: what is wrong and what to do instead? Q2 (MCQ, false statement): (a) FaaS provider handles all maintenance, like PaaS (b) high availability is inherent (c) the consumer must still plan capacity for peak (d) a function is provisioned in ms, a VM far longer (e) resource utilisation is excellent.

**Your answer:** Q1: "(i) Functions should be self-contained; one calling another is wrong; use a different solution, maybe PaaS. (ii) Wrong because FaaS is stateless; if they want it stateful, put it in a container. (iii) Too big, not lightweight; the lambda gets killed halfway; use a VM because of the video size." Q2: "C." Also asked where the slides mention asynchronous processing.

**Grade: about 80%.** Q1 ~65%: all three diagnoses right; fixes for (i) and (ii) left FaaS instead of applying the slide fix within FaaS; (iii) right. Q2 100%.

**Correct:** Q1: (i) functions must be self-contained and not call other functions (P2 s23): keep three single-purpose functions chained by events (the resize result being saved triggers watermarking, whose output triggers the metadata function). (ii) Lambda is stateless: keep state in an external service or resource such as a database or cache (P2 s24), the same fix as S2. (iii) the FaaS model has resource limits (P2 s25): run heavy, long jobs on a VM or container. Q2: (c): FaaS needs no capacity planning; each action is inherently scaled (P2 s24). Asynchronous processing: not in the slides; the source is the 25S2 Q25 answer key ("doing these operations async is key and here FaaS ... can help"); slides only imply it (event-driven FaaS, P2 s20; message queueing, P1 s3).

---

## Gap set (G1-G5)

Joshua first pointed out that the S9 review named the in-FaaS fixes without explaining them. Explained: chaining by events (upload triggers Resize; Resize saves its output; that save event triggers Watermark; its save triggers Save metadata; functions never call each other; which events trigger which function is set in the function's configuration, P2 s26-27) and external state (each run reads the user's data from a database or cache by user ID, works, writes it back; any copy can serve the next request). AWS products (S3 events, queues, DynamoDB) are beyond the slides.

**G1 (open):** Cart service on Lambda: where does the cart live between clicks, and why can't the function keep it? **Answer:** "Not sure where; Lambda is stateless so the function can't keep it." **50%.** Correct: in an external database or cache keyed by user ID, read at the start and written at the end of each invocation (P2 s24).

**G2 (MCQ):** Mapper output for "red blue red"? **Answer:** "B" ((red,1), (blue,1), (red,1)). **100%.**

**G3 (open):** Ticket site waits 7 s generating a PDF, emailing it and updating analytics before "Order confirmed". Fix? **Answer:** "Asynchronous processing, making the confirmation appear instantly." **70%.** Concept right, mechanism missing. Correct: confirm once the order is saved, publish an "order placed" event, and run the PDF, email and analytics as background functions (25S2 Q25 key).

**G4 (MCQ):** A validates, then B charges and C emails. Best design? (a) A calls B calls C (b) merge into one function (c) A publishes an "order validated" event that triggers B and C (d) move to a VM (e) A waits in a loop. **Answer:** "Put both in one lambda so a lambda doesn't call another: B." **0%.** Correct: (c); merging breaks "one action per function" (P2 s23). Second miss on chaining by events (S9 (i)).

**G5 (open):** 50 → 5,000 workers is slower, master at only 30% CPU. Cause? **Answer:** "Reducers taking data from the mappers: overhead; too many workers so splits are too small, and passing from mappers to reducers means a lot of communication." **100%.** Correct: shuffle traffic (each reducer fetches from every mapper) plus per-task overhead of tiny splits; the master is not the bottleneck here.

**Gap set: about 65%.** Real misconceptions (twice or more): asynchronous offloading (L01 G8, S8, G3 thin); fixing statelessness by an external store (S2 no fix, S9 container, G1 unsure); chaining FaaS functions by events (S9, G4).
