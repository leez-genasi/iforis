---
publish: false
tags:
  - world
---
_Welcome to the world of Iforis._

# Player Characters:

- [[Arkansas]] (me)
- [[Avery Laitherhem]] (Nadia)
- [[Thornwick Meadowlark]] (Yu Xuan)
- [[Variel Farinne]] (Wan Sun)
- [[Meowtal Smith]] (Jabez)
- [[Shade the Forgotten]] (Yu Jing)

# Map:
```leaflet
id: world-map
image: [[z_map/Iforis World Map.svg]]
bounds:
- [0, 0]
- [969, 1920]
defaultZoom: -1
minZoom: -1
maxZoom: 250
recenter: true
```
# [[Quests]]
# [[Timeline]]

# Sessions:
```button
name New Session
type note(My New Note, tab) template
action templater-session
folder a_sessions
```
```dataview
TABLE
chapter AS "Chapter", description AS "Summary", location AS "Location"
FROM #sessions WHERE file.folder != "templater"
SORT file.name desc
```

# Notable NPCs:
```dataview
TABLE
affiliation as "Affiliation", title as "Title"
FROM #NPCs 
```
