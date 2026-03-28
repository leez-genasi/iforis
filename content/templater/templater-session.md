---
publish: true
created: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - sessions
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

# \[<% tp.user.getPrevSession(tp) %>|Prev Session]

## Recap:

## Agenda:

## Log:

## To Do

<%\* await tp.file.rename(tp.user.getSessionNum(tp) + ”\_” + tp.date.now(“DDMMYYYY”)) %>
