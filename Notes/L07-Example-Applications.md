# L07 — Example Applications

Source: `Lecture 07 - Example Applications.pdf` (41 slides). No past-paper question maps to L07 (see `PAST-PAPER-MAP.md`), so scenarios test L07 applied to the L03/L06 ideas it builds on.

## Scenario Plan

| # | Scenario | Concepts | Slides |
|---|---|---|---|
| 1 | K-means as a MapReduce job | what map and reduce do, keys emitted, iterating jobs | s5-10, s14 |
| 2 | Preparing and reading k-means data | log transform for outliers, key-value design, reading cluster output, choosing k | s7, s11-13, s17-18 |
| 3 | Running it on AWS | S3 for data/code/output, EMR as managed MapReduce | s14-16 |
| 4 | Video app: workload types and splitting the stages | CPU- vs I/O-intensive, why upload and encoding run on separate server groups | s20-21, s27-29 |
| 5 | Upload to encoding hand-off | ELB, auto-scaling web servers, S3 raw bucket, SQS message, encoders polling | s22-25, s30 |
| 6 | Streaming to users | CloudFront edge caching, shared encoded-files bucket | s32-34, s36 |
| 7 | Which service model is each component | EC2/S3/ELB/auto-scaling IaaS, SQS and encoder PaaS, CloudFront/player/app SaaS | s26, s31, s35 |
| 8 | Pricing the app | cost items, monthly volumes, traditional vs inter- vs intra-cloud comparison | s37-39 |

Then one mixed gap set (4-5 short questions) on what he gets wrong.

## Detailed Notes

### Concept 1. K-means as a MapReduce job (S1)

- **K-means (slides, s3, s5-7):** group m points into k clusters (k < m) so points in a cluster are close together and clusters are far apart. Steps: initialise k centroids; iterate (assign each point to its nearest centroid, then recompute each centroid as the mean of its points); output.
- **Map = assign (slides, s8-9):** for one input point, compute the distance to every current centroid, pick the nearest, emit **one pair per point**: `(clusterID, point vector)`. N points in, N pairs out, only k distinct keys.
- **Shuffle (L06):** groups all pairs with the same clusterID onto one reducer.
- **Reduce = recompute (slides, s10, s13):** receives every point of one cluster, averages them, outputs `(clusterID, new centroid, number of points)`.
- **Iteration (slides, s7, s14):** one job = one round. The next round is a new job, with the new centroids given to every map task; repeat until the centroids stop moving (stopping rule: beyond slides). Reducers cannot feed mappers within a job.

> [!WARNING]
> **Mistake:** the k-means mapper emits `(clusterID, centroid, count)`, one summary per cluster. The mapper only labels: it emits one `(clusterID, point)` pair for every input point; averaging into a centroid and counting is the reducer's job. Same wrong model as L06 S5 (word-count mapper summing its own words).

**Key one-liner:** map labels each point with its nearest cluster, one pair per point; reduce averages each cluster's points into the new centroid; each round is a new job.

### Concept 2. Preparing and reading k-means data (S2)

- **Key-value design (slides, s11, s13):** input key = user ID, value = attribute vector; output key = cluster ID, value = number of points + centroid vector.
- **Why log (slides, s12):** outliers (e.g. 20,000 followers) heavily affect the clusters, so take log values to dampen them.
- **Mechanism (beyond slides / reasoning):** k-means sees only distance, so the attribute with the widest range dominates. A few extreme points pull a centroid out to themselves, wasting one of the k clusters; everyone else is squashed into the rest and real differences are lost. Log compresses big values ($1 → 0, $50 → 5.6, $20,000 → 14.3) and makes equal ratios equal distances. K-means always forms k clusters; the problem is wrong clusters, not none.
- **Reading output (slides, s17-18):** centroids are in log2, so a difference of d means a ratio of 2^d (8 → 256x). A small cluster far from the rest is the unusual group.
- **Choosing k (slides, s7):** "What is k?" is the open challenge; a non-empty cluster does not prove k is right.

**Key one-liner:** distance-based clustering is dominated by extreme values, so log-transform first; read log2 centroids as ratios (difference d = 2^d times).

### Concept 3. Running it on AWS (S3)

- **Steps (slides, s14):** upload data, upload code, create cluster, view results, repeat for the next clusters.
- **S3 + EMR (slides, s15-16):** S3 holds data, code and output; EMR is "a managed cluster platform that simplifies running big data frameworks": the provider runs the MapReduce framework, the team brings data and map/reduce code.
- **Why storage is separate (reasoning):** cluster nodes' disks are deleted when the cluster shuts down. S3 persists independently, so data is uploaded once and reused every round and run, results outlive the cluster, and the cluster runs (and is paid for) only during the job. Cost: reading over the network instead of the local disk (L06 data locality).

**Key one-liner:** keep data in S3 and compute in a throwaway EMR cluster, so you pay for compute only while the job runs and lose nothing when it stops.

### Concept 4. Splitting the video app's stages (S4)

- **Stages (slides, s20-21):** upload, encode (convert to a streaming format, since not every format can be streamed), stream.
- **Bottlenecks (slides, s20):** encoding is **CPU-intensive** (decode and re-compress every frame); upload and streaming are **I/O-intensive** (waiting on the network and storage, sending stored bytes).
- **Why separate groups (slides, s27-29):** encoding needs its own servers and load balancing "because encoding is compute expensive"; separated, "busy uploading wouldn't affect the encoding and vice versa". On shared servers, a burst of long conversions takes all CPU and uploads time out.
- **How the split works (slides s25, s30; reasoning):** the upload (web) server saves the raw video to S3 and leaves a job message; a separate encoder group picks it up. The upload server is free once the file is saved. Each group scales on its own: upload servers on the number of uploaders, encoders on the conversion backlog. A spike makes conversion slower, never makes uploads fail.

**Key one-liner:** different bottlenecks (I/O upload, CPU encoding) go on separate server groups that scale independently, so heavy encoding can only delay conversion, not block uploads.

### Concept 5. Upload-to-encoding hand-off (S5)

- **Upload path (slides, s25):** browser → Elastic Load Balancer → auto-scaling group of web servers on EC2 (metadata in RDS) → raw video into the **S3 raw-files bucket** → message into **SQS**.
- **Encoding path (slides, s30):** encoders (EC2 auto-scaling group, ffmpeg) poll SQS for "file uploaded" messages → download the raw video from S3 → encode → upload to the **S3 encoded-files bucket**.
- **Why a queue, not a direct call (reasoning):** a direct call is synchronous: the upload server and the user wait until encoding finishes, and time out when encoders are busy. With a queue, the upload server replies once the file is saved; busy encoders only make the queue longer.
- **Why no job is lost (beyond slides, SQS docs):** the message is a pointer to the S3 file, not the video. A taken message is hidden, not deleted; the encoder deletes it only after the encoded file is stored. If the encoder is terminated mid-job (e.g. scale-in), the message reappears after a timeout and another encoder takes it. A direct request lives only in that one server and dies with it.
- **Scaling (beyond slides, AWS docs):** the encoder group scales on the queue backlog (jobs waiting), which measures encoding demand directly; upload servers scale on upload traffic.

**Key one-liner:** save the raw video to S3, leave a pointer in SQS and reply at once; encoders poll, convert, store, then delete the message, so users never wait for encoding and no job is lost if an encoder dies.

### Concept 6. Streaming to viewers (S6)

- **Streaming path (slides, s32-34):** encoded video stored in the S3 encoded-files bucket ("shared with previous stage": the encoders write to it, the streamer reads from it) → Amazon CloudFront → viewer's browser. CloudFront "speeds up distribution... through a worldwide network of edge locations" (s33; Joshua's annotation "local cache" is correct).
- **Why distance causes buffering (reasoning):** each chunk crosses a long path with a long round trip and many hops, so data can arrive slower than the video plays.
- **Miss then hit (beyond slides, CDN behaviour):** first viewer near an edge: the edge has no copy, fetches from the origin (S3), streams it while keeping a copy (about the same speed as without a CDN). Later viewers near that edge are served locally, without contacting the origin. Edges keep only what is requested and drop unwatched content, so rarely watched videos keep missing.
- **Viral spikes (reasoning):** edges absorb the crowd; the origin sends each video about once per edge instead of once per viewer.

**Key one-liner:** CloudFront edges cache what nearby viewers request: the first view fetches from S3, later nearby views are served locally, so far viewers stop buffering and the bucket isn't flooded; rarely watched videos gain little.

### Concept 7. Which service model is each component (S7)

- **Slide tables (s26, s31, s35):** EC2, S3, auto-scaling, Elastic Load Balancer = IaaS ("machine level"); SQS = PaaS ("need to program some logic"); video encoder = PaaS ("internal component for dev"); CloudFront, media player, entire application = SaaS ("for the end user"). Joshua's annotations here are correct.
- **The deciding rule (L02; reasoning):** what the consumer gets and what they still do themselves. A machine you run your own software on = IaaS. A ready-made building block your code calls through an API, with no servers to run = PaaS. Finished software you just use = SaaS. Running on hardware or being built by developers is true of everything, so it decides nothing.
- **Point of view (reasoning):** the same app can be PaaS-built for the team and SaaS for viewers. Moving the web tier from EC2 + auto-scaling to an upload-your-code platform changes the team's model (IaaS → PaaS), not the viewers' (SaaS).
- **Unclear slide label:** the video encoder (ffmpeg on EC2) is labelled PaaS. Read it as the slide's annotation says: an internal software component the developers build the app with, not something end users touch. Not tested.

**Key one-liner:** the model is set by what the consumer manages: a machine (IaaS), a building block their code calls (PaaS, e.g. SQS), or finished software they just use (SaaS, e.g. the media player); viewers see the whole app as SaaS whatever runs underneath.

### Concept 8. Pricing the app (S8)

- **Cost items (slides, s37):** EC2 instances, S3 storage, CloudFront delivery, PaaS software (e.g. SQS) by usage.
- **Volumes (slides, s38):** 50 uploads/day x 100 MB = 5 GB/day, 150 GB/month; 1 min encoding each = 50 min/day; 500 streams/day x 100 MB = 50 GB/day, 1.5 TB/month. AWS Pricing Calculator for the numbers.
- **Comparisons (slides, s39):** traditional = cloud vs on-premise; inter-cloud = between providers; intra-cloud = between offerings of one provider (instance types, on-demand vs spot/reserved).
- **Reading the numbers (reasoning):** an encoder running 24/7 is busy 50 min/day (~3.5%); scaling encoders on the queue backlog down to zero pays for ~1 h/day (first job after idle waits for start-up). Streaming volume drives CloudFront cost (per GB delivered, beyond slides). S3 bills per GB-month, and stored data **accumulates** (+150 GB raw plus encoded copies each month), so the bill climbs with flat traffic unless raw files are deleted after encoding or old videos moved to cheaper storage (beyond slides).

**Key one-liner:** compute follows work done (scale encoders to zero when the queue is empty), delivery follows GB streamed (CloudFront), storage follows everything kept so far (it grows every month unless you delete).

## Reference only (not tested)

- Distance metric properties (s4): non-negative; 0 only when p = q; triangle inequality. The slide writes it with "<"; the standard definition is "≤" (equality holds when q lies on the straight line between p and r) (standard definition).
- p-norm distance (s4); Euclidean = 2-norm.
- Twitter dataset source (s8); AWS Pricing Calculator link (s38).
