# Multi-Storey Building HOA — Data Analytics Case Study
A reproducible analytics project exploring whether a multi-storey residential building could replace its property-management company and/or organize a homeowners association (HOA) to reduce consumable-resource costs and improve technical maintenance.

# Project Goals
	1. Quantify feasibility of initiating a legal vote to change the manager (requires >50% owner approval).
	2. Profile stakeholders (owners vs. tenants; residential vs. commercial properties).
	3. Aggregate community priorities from surveys/interviews and convert them into data-driven themes.
	4. Estimate potential savings from resource-efficiency and preventive-maintenance scenarios.
	5. Document barriers to adoption and recommendations for future iterations.

# Key Findings (from the initial study)
	• Residential share ≈ 70% of all units → legally sufficient base to attempt a change vote.
	• Working group ≈ 10% of the community (~30 residents) actively engaged.
	• Respondent mix (survey): ~66% owners, ~32% tenants; a portion declined to state.
	• Top blockers: low literacy in resource metering/accounting, skepticism about savings, co-financing concerns, perceived disruption from renovations.
	• Outcome: Momentum insufficient to cross the >50% threshold; recommended a phased, digital-first re-engagement plus clearer cost/benefit modeling.

# Repository Structure
# Data Sources & Dictionaries

# Methods
	• Language/Stack: Python 3.11+, Jupyter, pandas, numpy, matplotlib, scipy (optional), scikit-learn (optional).
	• Segmentation: Residential vs commercial; owner vs tenant; eligibility for legal vote.
	• Survey analysis: Descriptive stats, priority scoring, basic text aggregation (keyword counts).
	• Scenario modeling: Back-of-the-envelope savings from metering/efficiency and from preventive maintenance (sensitivity ranges).
	• Visualization: Share of eligible votes, response distributions, priority heatmaps.


# Core KPIs
	• Residential share (%): fraction of units marked residential.
	• Eligible voting base: residential share × ownership eligibility rules.
	• Engagement rate (%): working group participants ÷ total units.
	• Satisfaction index: mean Likert score by segment.
	• Priority scores: normalized interest in (a) efficiency, (b) maintenance.
	• Barrier indicators: share expressing high co-financing concern, knowledge gaps, etc.

# Results (replicable highlights)
	• Feasibility: ~70% residential units → potentially sufficient to reach >50% approval with strong engagement.
	• Engagement: ~10% active participants; indicates need for digital outreach and phased pilots.
	• Perception split: Owners more sensitive to maintenance planning; tenants report day-to-day service issues.
	• Barriers: Knowledge gaps on metering/costs; co-financing and disruption concerns dominate.

# Limitations
	• Convenience sampling in some survey channels; non-response bias likely.
	• Savings models are illustrative (order-of-magnitude) vs. audited engineering studies.
	• De-identified data → no direct follow-ups to clarify ambiguous responses.

# Recommendations & Next Steps
	1. Digital-first engagement: self-serve portal, regular updates, Q&A, transparent budgets.
	2. Pilot projects: low-risk metering/efficiency trials; publish before/after metrics.
	3. Financial clarity: simple calculators for dues/co-financing and payback periods.
	4. Phased governance: test community committees before full HOA transition.
	5. Better data: structured outreach to increase response rate and representativeness.






