---
tags:
  - sessions
session: <% tp.user.getSessionNum(tp) %>
date: <% tp.date.now("YYYY-MM-DD") %>
chapter: 3
location:
characters:
  - "[[Arkansas]]"
  - "[[Avery Laitherhem|Avery]]"
  - "[[Thornwick Meadowlark|Twig]]"
  - "[[Variel Farinne|Variel]]"
  - "[[Shade the Forgotten|Shade]]"
description:
publish: true
---
```dataviewjs  
const fm = dv.current();  
  
dv.paragraph(  
`**Session:** ${fm.session}  
**Chapter:** ${fm.chapter}  
**Date:** ${fm.date.toFormat("dd/MM/yyyy")}  
**Location:** ${fm.location}  
**Characters:** ${fm.characters}  
**Summary:** ${fm.description}`
);
```

# [[<% tp.user.getPrevSession(tp) %>|Prev Session]]

## Recap:

## Agenda:

## Log:

## To Do

<%* await tp.file.rename(tp.user.getSessionNum(tp) + "_" + tp.date.now("DDMMYYYY")) %>
