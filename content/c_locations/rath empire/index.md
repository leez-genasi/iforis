---
publish: true
tags:
  - world
title: Rath Empire
aliases:
  - Rath
  - Rath Empire
---
- used to rule the entire eastern empire
- The rise (and fall) of Ersragrun caused it to fracture
- Is in constant war with the Lurian Empire
- very hierarchal
- as long as you follow the law, you're good
- Favored gods:
	- Auril, Goddess of Winter
	- lliira, Goddess of Joy
		- rath and the previous empire that conquered the western continent (before esragrun)
		- the closest to world peace was achieved, food was plentiful, few wars
# Notable People:
```dataview
TABLE
titles AS "Title"
FROM #NPCs
WHERE contains(kingdom, [[c_locations/rath empire/index]])
```
# Cities
```dataview
TABLE
FROM "c_locations/rath empire"
WHERE file.name != "index"
```
