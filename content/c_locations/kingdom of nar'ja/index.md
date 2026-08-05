---
publish: true
tags:
  - world
title: Kingdom of Nar'ja
aliases:
  - Nar'ja
---
# Notable People:
```dataview
TABLE
titles AS "Title"
FROM #NPCs
WHERE contains(kingdom, [[c_locations/kingdom of nar'ja/index]])
```
# Cities
```dataview
TABLE
FROM "c_locations/kingdom of nar'ja"
WHERE file.name != "index"
```
