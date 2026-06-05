---
publish: true
tags:
  - world
title: Iforis
---
_Welcome to the world of Iforis._

# Player Characters:
- [[Arkansas]] (me)
- [[Avery Laitherhem]] (Nadia)
- [[Thornwick Meadowlark]] (Yu Xuan)
- [[Variel Farinne]] (Wan Sun)
- [[Meowtal Smith]] (Jabez)
- [[Shade the Forgotten]] (Yu Jing)

# [[Quests]]
# [[Timeline]]

# Sessions:

```dataview
TABLE
chapter as "Chapter", description as "Summary", location as "Location"
FROM "a_sessions"
SORT file.ctime DESC
```

# Notable NPCs:

```dataview
TABLE
affiliation as "Affiliation", title as "Title"
FROM #NPCs 
WHERE file.name != "templater-npcs"
```
