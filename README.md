## Vision Zero in the 27th Ward

This summer, I got to help the 27th Ward improve traffic safety for our residents! Thanks to the Abundance (TM) I did a traffic crash analysis. 

I identified 7 high-priority intersections, and proposed potential redesign recommendations. 

Thanks to the 27th Ward for an awesome internship, where I left feeling supported and empowered. 

Thanks to Students for Abundance for introducing me to this opportunity and for supporting the internship!

## Write-up doc
TBD! Check back

## Data sources

See writeup

## Maps

Running `Crash_Analysis.ipynb` writes these interactive maps to `maps/` (open the `.html` files in a browser):

| File | What it shows |
|------|---------------|
| `crashes_by_intersection_count.html` | Intersection-related (`Y`) crashes assigned to the nearest ward intersection, colored by crash count. Toggleable crash-density heat layer. |
| `intersection_injury_cost.html` | Same intersections, colored by total KABCO injury cost (severity-weighted) instead of count. |
| `population_density_by_block.html` | 2020 Census population density (people/km²) as a block-level choropleth, clipped to the ward. |
| `non_intersection_crashes_by_distance.html` | Crashes *not* flagged intersection-related, colored by distance to the nearest intersection; toggleable layer of the intersection-related crashes for comparison. |
| `crashes_near_intersection_count.html` | Broader crash set (`Y` **or** blank, excluding only `N`) by nearest intersection, colored by count. Toggleable density heat layer. |
| `injury_cost_near_intersection.html` | Broader crash set by nearest intersection, colored by injury cost. |
| `crash_excess_factor_screening.html` | Network screening — crash **multiplicative factor** (observed ÷ expected) from the Negative-Binomial SPF + Empirical Bayes. Red = more crashes than peers of the same volume/control/layout; blue = safer than peers. |
| `injury_cost_excess_factor_screening.html` | Network screening — injury-**cost** factor (observed ÷ expected) from the Gamma GLM. Red = costlier than peers; blue = cheaper. |
| `crash_factor_context_only_screening.html` | Network screening with the **context-only** SPF (AIC-selected: volume + junction size + crime, *no* road-design covariates). EB multiplicative factor — red = more crashes than the exogenous context predicts, blue = fewer. |
| `cost_factor_context_only_screening.html` | Severity twin of the above: injury-**cost** factor (observed ÷ expected) from a context-only **Gamma GLM** (AIC-selected). Red = costlier than the exogenous context predicts, blue = cheaper. |
| `violent_crime_rate_and_density.html` | Violent crime (homicide/assault/battery), the regression covariate visualized. Two toggleable layers: per-intersection rate (crimes per 1,000 residents within ~1 block) and a kernel-density heatmap of the raw crime points. |

