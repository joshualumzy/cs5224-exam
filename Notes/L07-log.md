# L07 Log

---

## S1. K-means as a MapReduce job

**Scenario:** A streaming service clusters 50 million users, each `(userID, [hours watched per week, genres watched])`, into 5 segments with k-means on MapReduce. Q1: what does a map task do with one record and what pair does it emit; what does a reducer receive and output? Q2 (MCQ): after the first job produces 5 centroids, what next? (a) done, one job is all of k-means (b) another job runs with the new centroids given to every map task, repeating until the centroids stop changing (c) reducers send centroids back to the mappers within the same job (d) the master recomputes the clusters (e) increase k and rerun.

**Your answer:** Q1: "The map receives one input record (key user ID, value the list of hours and genres), computes the distance between it and all the centroids, and assigns the point to a cluster. The key will be the cluster, and the value the centroid of that cluster and the number of points in it. But then map might take in 10,000 points and only output five centroids; I don't know if that's possible. Every reducer receives all the labelled points of a particular cluster and outputs the new centre." Q2: "B."

**Grade: about 75%.** Q1 about 60%: the map logic (distance to every centroid, pick the nearest) and the reducer are right; the emitted pair is wrong: centroid + count is the reducer's output format, not the mapper's. Same wrong model as L06 S5 (the mapper summarises instead of emitting one pair per input). Q2 100%.

**Correct:** Q1: per record, the mapper computes the distance to every current centroid, picks the nearest, and emits one pair `(clusterID, point vector)`, e.g. `(cluster3, [12, 4])` (s9). 50 million records in, 50 million pairs out; only 5 distinct keys. The shuffle groups the pairs by key, so the reducer for cluster3 receives every point assigned to cluster3, averages them into the new centroid, and outputs `(cluster3, [new centroid], number of points)` (s10, s13). Q2: (b): k-means iterates (s7) and each round is a new job with the latest centroids (s9 "previously obtained centroids", s14 "repeat as necessary"); MapReduce has no path from reducers back to mappers within a job (L06).

---

## S2. Preparing and reading k-means data

**Scenario:** A mobile game clusters players by minutes played per day and total in-game spending; most spend $0-50, a few "whales" over $20,000. Q1: on raw numbers, what goes wrong because of the whales; what to do to the data first, and how does it fix it? Q2 (MCQ): after pre-processing, k = 3 gives cluster0 40,000 players (log2 minutes 5.0, log2 dollars 1.0), cluster1 3,000 (5.1, 9.0), cluster2 25,000 (2.0, 0.5). Supported conclusion? (a) cluster1 spends ~9x cluster0 (b) cluster1 plays about as long as cluster0 but spends ~250x, small group (c) cluster2 has lowest values so fewest players (d) centroids are average dollar amounts (e) k = 3 confirmed because no cluster is empty.

**Your answer:** Q1: "The whale is an outlier, very far from everybody else, so they might form their own cluster; why is that a problem? Or if the values are very spread out it might be difficult to form a cluster; not sure. Before clustering, take the log; this dampens the effect of very large numbers." Q2: "B."

**Grade: about 75%.** Q1 about 50%: fix right; mechanism not explained (own-cluster idea raised but not followed through; "difficult to form a cluster" is wrong, k-means always forms k clusters). Q2 100%.

**Correct:** Q1: k-means uses only distance; dollars span 0-20,000 while minutes span 0-300, so dollars dominate the distance (beyond slides). A few whales pull a centroid out to themselves, wasting one of the k clusters on a handful of players; the rest are squashed into the remaining clusters and real differences among them are lost ("clusters are heavily affected", s12). Log compresses large values ($1 → 0, $50 → 5.6, $20,000 → 14.3) and turns equal ratios into equal distances (reasoning). Q2: (b): 9.0 - 1.0 = 8 in log2, 2^8 = 256 (s11-13, s17-18 read output the same way).

---

## S3. Running k-means on AWS

**Scenario:** The game company moves its monthly clustering from 20 owned servers (idle most of the month) to an EMR cluster started per run and shut down after. Q1: an engineer proposes keeping input data, code and results on the EMR nodes' own disks, "to keep the data close to the workers", instead of S3; what goes wrong, and why does S3 suit this setup better? Q2 (MCQ): what does EMR change vs building the cluster on plain EC2? (a) nothing, team installs Hadoop itself (b) provider sets up and runs the MapReduce framework; team supplies data and map/reduce code (c) finished clustering app, no code (d) no storage needed (e) iterates automatically in one job.

**Your answer:** Q1: "EMR is not made for storage; I'm not sure after you shut it down whether the data will still be there, whereas S3 is meant for storage." Q2: "Probably B."

**Grade: about 70%.** Q1 about 40%: right instinct, but hedged, and no reason why S3 suits the setup. Q2 100%.

**Correct:** Q1: the nodes' disks are deleted when the cluster shuts down, so results are lost and input must be re-uploaded every run. S3 stores data independently of compute: data and code uploaded once, reused by every round and every run, results viewable after the cluster is gone (s14-16). That separation lets the cluster be thrown away after each run, so they pay for compute only while the job runs (reasoning; pay-per-use, L01). The engineer's locality point is real (L06) but traded for persistence and no idle cost. Q2: (b): EMR is "a managed cluster platform that simplifies running big data frameworks" (s15).

---

## S4. Splitting the video app's stages

**Scenario:** A video site's version 1 runs one server group that both accepts uploads and converts them. A creator uploads 30 long 4K videos; for an hour other users' uploads time out and the upload page is slow; servers at 100% CPU. Q1 (open): what is happening, and how would you restructure so it can't recur? Q2 (MCQ): stage-to-bottleneck pairing: (a) upload CPU, encoding I/O, streaming CPU (b) upload I/O, encoding CPU, streaming I/O (c) upload I/O, encoding I/O, streaming CPU (d) all CPU-bound (e) upload CPU, encoding CPU, streaming I/O.

**Your answer:** Q1: "The same server accepts uploads and converts... long high quality videos take a lot of CPU power to convert... because they share the same servers therefore the uploads time out." Fix: "separate the web server part from the uploading part so they wouldn't affect each other because one is super lightweight job, the other is a very heavy job... one job is blocking another." Q2: "Upload is definitely IO bound, encoding is CPU bound, streaming is probably IO bound as well, so it's B."

**Grade: about 80%.** Q1 about 60%: diagnosis right (CPU-heavy encoding starves upload handling on the shared servers). Fix muddled in wording: "web server vs uploading", but upload *is* the web part; his reasoning showed he meant upload vs encoding, so graded that way. Missing the hand-off and independent scaling. Q2 100%.

**Correct:** Q1: encoding is CPU-heavy, so 30 long 4K conversions take all CPU and the same servers can no longer handle upload connections. Fix: two server groups. (1) Hand-off: the upload server saves the raw video to S3 and records a conversion job; a separate encoder group picks it up, so the upload server is free as soon as the file is saved (detail in S5, s25, s30). (2) Each group scales on its own: uploaders on the number of users uploading, encoders on the conversion backlog. A spike only makes the encoders busier; the worst case is slower conversion, not failed uploads (s27-29). Name the two groups exactly: upload (web) servers vs encoding servers. Q2: (b) (s20): upload is I/O (waiting on network and storage), encoding is CPU (decode and re-compress every frame), streaming is I/O (sending stored bytes). Different bottlenecks mean separate groups, each sized for its own bottleneck.

---

## S5. The upload-to-encoding hand-off

**Scenario:** Version 2 splits upload (web) servers and encoding servers. The upload server saves the raw video to S3, then sends a direct request to one encoding server ("convert file X") and waits for "done" before telling the user "upload complete". Complaints: (1) at busy times users wait minutes after the file finished uploading, some get errors; (2) when the encoding group shrinks at night, some videos are never converted. Q1 (open): why each, and how should the hand-off work, step by step? Q2 (MCQ): the encoding group's auto-scaling should be based on (a) number of upload servers (b) upload servers' CPU (c) number of conversion jobs waiting (d) videos in the encoded bucket (e) number of viewers streaming.

**Your answer:** Q1: "The upload server is waiting for the encoder server to come back, so they're tightly coupled. Once the video is uploaded, it tells the user the video is uploaded and adds the encoding job to a queue. Separately, the encoding server picks up the job from the message queue and encodes. This way the upload server and the encoding group can also scale separately." Q2: "C."

**Grade: about 80%.** Q1 about 60%: complaint 1 and the queue fix right. Complaint 2 not explained (why jobs vanish on scale-in, and how the queue prevents it), and the steps stop at "encodes" (no S3 download, encoded bucket, or removing the message). Q2 100%.

**Correct:** Q1: (1) The request is synchronous: the user's request is held open until the encoder finishes, and when all encoders are busy it waits or times out. (2) The job exists only inside the encoding server that received it; scale-in terminates that server mid-job and nothing records that the video still needs converting. Fix (s25, s30): the upload server saves the raw video to the S3 raw bucket, puts a short message in SQS ("file X is in the raw bucket", a pointer, not the video) and replies to the user at once. Each encoder polls SQS, takes a message, downloads the raw file from S3, encodes it, uploads the result to the S3 encoded bucket, and only then deletes the message (beyond slides, SQS docs). A taken message is hidden, not deleted; if the encoder dies before deleting it, it reappears after a timeout and another encoder takes it, so no job is lost. Busy encoders just make the queue longer. Q2: (c): the waiting-job count measures encoding demand directly (beyond slides: AWS recommends scaling workers on queue backlog). (a)/(b) measure upload demand, (d) is finished work, (e) is streaming load.

---

## S6. Streaming to viewers

**Scenario:** All encoded videos sit in one S3 bucket in Singapore; viewers stream directly from it. Europe and Brazil viewers complain of buffering, Singapore viewers don't; then a Singapore creator's video goes viral worldwide. Q1 (open): why do far viewers buffer; how does CloudFront in front of the bucket fix it; what happens on the first and second view in Paris? Q2 (MCQ): after CloudFront, which viewer benefits least? (a) 10,000th Paris viewer of the viral video (b) Brazil viewer of an old, rarely watched video nobody nearby watched recently (c) second London viewer a minute after the first (d) Tokyo viewer of the viral video at peak (e) Paris viewer rewatching after an hour.

**Your answer:** Q1: "Latency: the S3 bucket is too far from the clients, so the transfer over the network takes long. CloudFront caches every video, has a local copy for the viewers in Europe, so the videos they commonly view are cached closer to them. First view in Paris: they try the CloudFront cache, don't get it, so get it from S3, so buffering takes a while; it gets added to the cache. The second view is already cached, so it does not buffer." Q2: "B."

**Grade: about 90%.** Q1 about 80%: cause, miss-then-fill and the second view right. Imprecise: "caches every video" (it caches only what has been requested, and drops rarely watched videos), and the first view is not slower than before. Did not mention the viral spike: the edges, not the single bucket, serve the crowd. Q2 100%.

**Correct:** Q1: every chunk of video travels a long path from Singapore; the long round trip and many network hops mean data arrives slower than the video plays, so the player pauses (reasoning). CloudFront (s33-34) streams from edge locations near viewers. First Paris view: the Paris edge has no copy (a miss), fetches the video from the S3 bucket (the origin), streams it to the viewer while keeping a copy; the viewer gets about the same speed as without CloudFront. Second Paris view: the edge has it (a hit), so it is served from nearby and the origin isn't contacted. Edges keep only what is being requested and drop what isn't watched. For the viral video, thousands of viewers are served by their nearest edge, so the single bucket sends each video only once per edge instead of once per viewer. Q2: (b): a rarely watched video is almost never in the nearby edge's cache, so each view is a miss that goes back to Singapore. (a), (c), (d) and probably (e) are hits.

---

## S7. Which service model is each component

**Scenario:** Q1 (open): a teammate says SQS is IaaS "because, like EC2, it's just Amazon infrastructure we rent", and the media player is PaaS "because developers built it". What is wrong with each, and what decides a component's model? Q2 (MCQ): the team replaces its EC2 web servers + auto-scaling with a platform where it uploads code that is run and scaled automatically. (a) team: IaaS → PaaS; viewers: still SaaS (b) team: PaaS → IaaS; viewers SaaS (c) team: IaaS → SaaS; viewers PaaS (d) team: IaaS → PaaS; viewers PaaS too (e) nothing changes.

**Your answer:** Q1: "SQS is not infrastructure, SQS is PaaS, because it's not served as infrastructure; it is something AWS has built on top of its infrastructure to provide this message queue. Media player is SaaS because that is a finished product that people just use." Q2: "IaaS to PaaS, for viewers still SaaS: A."

**Grade: about 85%.** Q1 about 70%: both labels right, media-player reason right. SQS reason weak: "built on top of infrastructure" is true of every PaaS and SaaS, so it doesn't separate the models; the deciding rule was not stated. Q2 100%.

**Correct:** Q1: the model depends on what the consumer gets and what they still do themselves, not on who built it or whether it runs on hardware (everything does). EC2 gives a virtual machine: the team installs and runs its own software on it (IaaS, "machine level", s26). SQS gives a ready-made building block: the team writes code that sends and receives messages through its API and runs no queue servers (PaaS, "need to program some logic", s26). The media player is finished software the viewer just uses (SaaS, "for the end user", s35); that developers built it is true of every product. Q2: (a): the team moves from managing machines to uploading code (L02); viewers still just use the finished site, whatever runs underneath (s35 "Entire Application: SaaS").

---

## S8. Pricing the video app

**Scenario:** s38 volumes: 50 uploads/day (100 MB, 1 min encoding each); 500 streams/day (100 MB each, 1.5 TB/month). One encoding EC2 instance runs 24/7. Q1 (open): (a) hours actually busy, and how to cut the compute bill; (b) which cost item the 1.5 TB/month mainly drives, and why the S3 bill grows every month with flat traffic. Q2 (MCQ): which is intra-cloud? (a) AWS vs Azure for encoders (b) own servers vs EC2 (c) on-demand vs spot/reserved EC2 for encoders (d) CloudFront vs Cloudflare (e) S3 vs Google Cloud Storage.

**Your answer:** Q1: "50 a day, one minute each, so the instance is busy for fifty minutes. I would cut the compute bill by having the EC2 instance auto-scale up and down so it's not running 24x7 and instead runs for those fifty minutes. The 1.5 TB drives CloudFront cost, because I'm streaming through CloudFront. The S3 storage bill grows every month even if traffic stays flat because storage cost is charged on a per-time basis." Q2: "C."

**Grade: about 80%.** Q1 about 65%: (a) right (50 min/day, ~3.5% busy; auto-scale), but not said what it scales on or that it can go to zero; (b) CloudFront right; S3 growth reason wrong: per-GB-month pricing alone gives a flat bill for flat storage. Q2 100%.

**Correct:** Q1 (a): 50 min of work in 24 h. Scale the encoder group on the SQS backlog with a minimum of zero: an instance starts when messages wait, stops when the queue is empty, so they pay for about an hour a day instead of 24 (S5; pay-per-use, L01). Cost: the first job after idle waits for an instance to start (beyond slides). (b): CloudFront delivery, charged per GB sent to viewers (beyond slides, AWS pricing). S3 grows because data accumulates: each month adds ~150 GB of raw uploads plus the encoded copies, and nothing is deleted, so month 12 stores about 12x month 1 while traffic stays flat. Fix: delete raw files once encoded, or move old videos to cheaper storage (beyond slides). Q2: (c): same provider, different offerings (s39); (a), (d), (e) are inter-cloud, (b) traditional.

---

## Gap set (G1-G5)

**Questions:** G1 (open): 1 billion `(country, response ms)` records, average response time per country with MapReduce: what does map emit for one record; what does a reducer receive and output? G2 (MCQ): k-means on houses by raw (bedrooms 1-6, price $200k-$5M): (a) bedrooms dominate (b) price dominates, clusters are price bands (c) fails to form clusters (d) equal weight (e) fewer than k clusters. G3 (open): image-resizing workers take SQS messages; one crashes mid-job: what happens, step by step; what if workers deleted each message on taking it? G4 (MCQ): which is PaaS? (a) VM for your own database (b) email-sending service your code calls, no mail servers to run (c) staff using Gmail (d) raw storage disk (e) company website as seen by customers. G5 (open): dashcam app keeps every video in S3, +100 GB/month, $0.023/GB-month: bill in month 1 and month 12; how to stop it growing.

**Your answers:** G1: "For one record, map emits the country and the response time. The reducer receives country and response time and outputs country and average response time." G2: "B." G3: "If a worker crashes halfway, the job will remain in SQS and eventually get picked up by another worker. If workers deleted each message as soon as they took it, a job would be lost if one failed halfway." G4: "B" (transcribed as "P"). G5: "Month one is 230, and month two double, 460. To stop the bill growing, delete older videos as time passes."

**Grade: about 85%.** G1 about 90%: one pair per record, so the S1/L06 S5 mapper misconception is fixed; the reducer receives **all** response times for one country (a list), not one. G2 100%. G3 about 85%: right; mechanism not named (a taken message is hidden, not deleted, and reappears after a timeout because the crashed worker never deleted it). G4 100%. G5 about 50%: idea of accumulation right, arithmetic wrong by 100x, month 12 not given.

**Correct:** G1: map emits `(country, ms)` per record; the shuffle groups by country; each reducer gets `(country, [all ms values])` and outputs `(country, average)`. G3: the worker takes the message, which becomes hidden; it crashes and never deletes it; after the timeout the message is visible again and another worker takes it from the start. Deleting on take removes the only record of the job, so a crash loses the image. G5: month 1 stores 100 GB x $0.023 = **$2.30**; month 12 stores 1,200 GB = **$27.60** (12x with flat uploads). Stop growth by deleting videos after a fixed period or moving old ones to cheaper storage.
