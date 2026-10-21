# Feedback, endogenous data, and organizational consequences: assessed evidence

Prepared 21 October 2026. Five full-text works were acquired and relevant methods, results, discussion and limitation sections assessed. This is a targeted mechanism search, not an exhaustive or independently screened systematic review. The PDFs are working copies outside the Git checkout; no public redistribution permission was assumed.

## Central conclusion for the rebuilt paper

There is strong **mechanism evidence** that a decision system can alter the data it later observes, but this does **not** prove a universal reinforcing loop of ever-increasing organizational complexity. Feedback can change selection, distribution or dependence without increasing the number of records. Some models converge to stable behavior; some interventions correct biased feedback. The review should distinguish (a) record quantity, (b) behavioral variety and dependence, (c) technical interdependence, and (d) organizational coordination work. The reverse arrow from DSS capability to organization-wide complexity remains a conditional synthesis supported by limited organizational evidence, not a directly estimated macro-historical law.

## Assessed sources

### `perdomo2020` — Perdomo et al., Performative Prediction (ICML/PMLR, 2020)

- **Identity:** PMLR 119, pp. 7599–7609. The official page gives these proceedings pages; do not use a guessed page range. PDF has 11 pages. Exact metadata and provenance are in `sources.json`.
- **Design:** mathematical framework and convergence results; illustrative computational analysis of strategic classification, not a longitudinal organization study.
- **Locator: PDF p. 1, Abstract and §1:** predictions used for decisions may influence the outcomes being predicted. The credit-risk example shows a policy/model choice affecting future outcomes and therefore the future data distribution. The mechanism supports **decision output → intervention/behavior → subsequent observations**.
- **Locator: PDF pp. 3–4, §2:** a distribution map depends on the model parameters. This formalizes endogenous data rather than merely an external stream becoming larger.
- **Locator: PDF pp. 5–7, §§3–4:** retraining convergence and stable/optimal distinctions depend on assumptions such as sensitivity, smoothness and convexity. This is explicit counterevidence to any claim that feedback necessarily creates runaway growth or instability.
- **Locator: PDF pp. 7–9, §5 and §6:** strategic-classification/credit experiments illustrate convergence for lower sensitivity and divergence for larger sensitivity; the discussion treats retraining as a possible equilibrating process.
- **Use in synthesis:** establish a formal basis for an endogenous data-generation loop and distinguish stable from amplifying feedback.
- **Boundary:** does not measure data-volume growth, organizational differentiation, coordination burden, or DSS historical generations. Formal assumptions need not hold in nonconvex deployed systems. Do not describe the computational illustration as field evidence that a bank reorganized.

### `chaney2018` — Chaney, Stewart and Engelhardt (RecSys, 2018)

- **Identity:** *How Algorithmic Confounding in Recommendation Systems Increases Homogeneity and Decreases Utility*, RecSys ’18, pp. 224–232, DOI 10.1145/3240323.3240370. Inspected arXiv v2 with conference metadata.
- **Design:** simulation framework for user interaction with recommendation algorithms. The paper explicitly uses simulations, not a platform-wide natural or randomized field experiment.
- **Locator: PDF p. 1, Abstract/§1 and Fig. 1:** recommendations influence user interactions; retraining on those interactions creates algorithmic confounding. A dataset is therefore partly a consequence of previous recommendations.
- **Locator: PDF p. 3, §4:** user/item utility and the interaction model define the simulated environment; those assumptions bound the conclusion.
- **Locator: PDF pp. 4–5, §§5.1–5.3, Figs. 3–5:** repeated training on confounded data homogenizes behavior beyond that required for ideal utility in their simulations; changes are not shared equally across users.
- **Locator: PDF pp. 5–6, §5.4 and §6:** effects on consumption distributions depend on algorithm; similar homogeneity can coexist with different item-consumption inequality. Confounded held-out data can favor models resembling the generating recommender. Preliminary weighting experiments can reduce homogenization and improve utility.
- **Use in synthesis:** a counterexample to “more interaction records necessarily supply more independent information” and to “more data implies more behavioral diversity.” Add an evaluation/provenance requirement.
- **Boundary:** simulation assumptions, including fixed user/item utilities, limit generalization; the paper does not empirically prove all commercial recommenders reduce utility or all organizations become more complex. The statement that production choices may respond to consumption is discussed as a possible extension, not directly measured here.

### `ensign2018` — Ensign et al., Runaway Feedback Loops in Predictive Policing (FAT/PMLR, 2018)

- **Identity:** PMLR 81, pp. 160–171 on the official article page; PDF internally paginated 1–12.
- **Design:** formal urn models, simulations and black-box PredPol experiments using historical incident data/scenarios. This is not a trial assigning actual police patrol policies to evaluate realized crime effects.
- **Locator: PDF pp. 1–3, Abstract/§1 and §3:** deployment based on discovered incidents changes which incidents will be observed, feeding those discoveries into the next allocation. Reported and discovered incidents are different observation mechanisms.
- **Locator: PDF pp. 6–8, §§3.4–3.5:** independently reported incidents can attenuate feedback but do not generally eliminate it; corrective input weighting/rejection sampling is developed under model assumptions.
- **Locator: PDF pp. 8–11, §§4–5 and Fig. 2:** simulations and PredPol experiments illustrate feedback and a black-box input modification intended to recover underlying relative rates.
- **Locator: PDF pp. 11–12, §6:** urn models abstract from richer predictive covariates and differing crime types; reporting and discovery rates tracking true crime is an important assumption with acknowledged weaknesses.
- **Use in synthesis:** decision-support allocation can shape data collection, produce biased accumulation and create a governance/correction requirement. Separating observed activity from underlying activity is essential.
- **Boundary:** do not equate higher discovered incidents with higher true crime or a simple increase in organizational complexity. The results are conditional and demonstrate corrective as well as reinforcing mechanisms.

### `sculley2015` — Sculley et al., Hidden Technical Debt in Machine Learning Systems (NeurIPS, 2015)

- **Identity:** *Advances in Neural Information Processing Systems*, vol. 28. Nine-page official PDF; author names checked against official proceedings metadata. No DOI or unverified proceedings page range supplied.
- **Design:** practice-informed conceptual/engineering taxonomy of production ML risks. It does not present a controlled experiment or representative organizational survey quantifying cost effects.
- **Locator: PDF pp. 1–2, §1–§2:** models can erode abstraction boundaries; changes in features and model components can produce broad effects. Adding ML can create maintenance obligations beyond model code.
- **Locator: PDF p. 3, §3:** data dependencies, unstable inputs and undeclared consumers complicate maintenance and change management.
- **Locator: PDF p. 4, Fig. 1 and §4:** live systems may influence their own future training data; hidden feedback may connect otherwise separate systems indirectly through behavior. The diagram is qualitative, not a measured claim that a fixed percentage of infrastructure is ML code.
- **Locator: PDF pp. 6–8, §§6–9:** configurations, external changes, monitoring and debt measurement are system-level concerns; debt can be serviced through refactoring, dependency reduction and explicit management.
- **Use in synthesis:** architecture and data growth can create new technical interdependence and maintenance/coordination demands. Governance and modularity are potential balancing mechanisms, not optional post-processing.
- **Boundary:** supports a mechanism and practitioner-informed risks; does not estimate how much organizational complexity increased, identify a historical DSS transition, or show that every new architecture increases debt.

### `amershi2019` — Amershi et al., Software Engineering for Machine Learning: A Case Study (ICSE-SEIP, 2019)

- **Identity:** pp. 291–300, DOI 10.1109/ICSE-SEIP.2019.00042; official metadata verified through Crossref and author-hosted Microsoft PDF.
- **Design/context:** Microsoft case study using 14 semi-structured interviews, followed by a survey with 551 responses drawn from internal AI/ML mailing lists. This is actual organizational-process evidence, not a simulation. Participants cover technical roles and product areas, but one corporation is not representative of all DSS organizations.
- **Locator: PDF pp. 3–4, §III and Table I:** snowball sampling for interviews, followed by open-ended survey and card sorting. Survey self-selection and the single-organization setting limit generalization.
- **Locator: PDF p. 3, workflow discussion:** ML workflows contain repeated loops between data collection, model choice, training, evaluation and monitoring; interacting ML components increase workflow complexity.
- **Locator: PDF pp. 5–7, §V:** pipeline support, collaboration, debugging and evolving/deploying models are reported challenges and practices; not all concerns remain equally important as teams mature.
- **Locator: PDF pp. 8–9, §VII.A and §VII.C:** changing diagnostic-data collection can require upstream engineering changes and affect data volume, performance and network use. Versioning data from different schema regimes becomes harder as project size grows. Coupled model behavior can force separately organized teams to collaborate, even when code modules remain separate.
- **Locator: PDF p. 9, §VIII:** authors explicitly identify self-selected/self-reported data and no objective baseline for the maturity metric. Do not describe maturity/effectiveness correlations as causally validated improvements.
- **Use in synthesis:** empirical support for a bounded reverse link: adopting data-dependent models creates data-management, interface, skill and interteam coordination work. Also provides a balancing mechanism: teams develop pipelines, practices and process maturity to manage demands.
- **Boundary:** does not estimate historical causation across DSS generations, prove rising data volume alone caused coordination burden, or demonstrate a universal positive feedback trajectory.
- **Reporting caution:** the methods list 4195 invitations and 551 responses while reporting a 13.6% response rate; those counts calculate to about 13.1%. Use the response count without reproducing the percentage, unless this discrepancy is resolved.

## Proposed synthesis claims (author synthesis, not direct quotations or established laws)

1. **Endogeneity proposition:** when DSS outputs alter allocation or user behavior, subsequent observations depend partly on the prior decision policy; evaluation on larger but policy-confounded datasets may overstate improvement. Supported mechanistically by Perdomo, Chaney and Ensign; empirical organization-wide prevalence is not measured here.
2. **Coordination-burden proposition:** when data/model components cross team boundaries, expanding analytical capability can create coordination and lifecycle-management work; this depends on component coupling and governance, not simply byte count. Practice taxonomy: Sculley. Organizational case evidence: Amershi.
3. **Conditional amplification proposition:** reinforcing effects strengthen when observations are predominantly generated by the policy itself and correction/independent measurement is weak. Stability, randomization, weighting and monitoring can weaken or reverse amplification. The sources provide mechanisms and counterconditions, not a universal monotonic law.
4. **Information-versus-volume proposition:** increased records need not increase independent information or behavioral variety. Homogenization and repeated observations can make nominal volume grow while informative diversity falls. Chaney is a simulation illustration; do not turn it into a cross-sector empirical estimate.
5. **Boundary proposition:** the full loop from organizational complexity to data to DSS to greater organizational complexity should be presented as a theory-informed integrative model with arrows labeled by evidence type and confidence. No reviewed study here directly tests that entire loop over the history of DSS.

## Selection and access record

Included the five full texts above because they directly address endogenous observations, feedback corrections, or organizational engineering/coordination consequences. Two management-theory candidates were inspected at metadata level only: Raisch and Krakowski (2021, canonical DOI 10.5465/amr.2018.0072) publisher full text returned 403; Faraj, Pachidi and Sayegh (2018) repository candidate was located but not pursued after five stronger directly assessed sources were obtained for this task. They must not be counted as read full texts. Search and retrieval artifacts are retained in `retrieval-log.jsonl`, `crossref-*.json`, `*-meta.json`, and official `*-page.html` files. No PRISMA counts, exhaustive search claims, or risk-of-bias scores are fabricated.
