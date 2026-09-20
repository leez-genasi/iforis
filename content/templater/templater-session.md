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

Evaluation Error: TypeError: fm.date.toFormat is not a function
at eval (eval at <anonymous> (plugin:dataview), <anonymous>:7:21)
at DataviewInlineApi.eval (plugin:dataview:19027:16)
at evalInContext (plugin:dataview:19028:7)
at asyncEvalInContext (plugin:dataview:19038:32)
at DataviewJSRenderer.render (plugin:dataview:19064:19)
at DataviewJSRenderer.onload (plugin:dataview:18606:14)
at DataviewJSRenderer.load (app://obsidian.md/app.js:1:727041)
at DataviewApi.executeJs (plugin:dataview:19607:18)
at Q1 (plugin:quartz-syncer:365:2492)
at Object.compile (plugin:quartz-syncer:365:3536)

# [[<% tp.user.getPrevSession(tp) %>|Prev Session]]

## Recap:

## Agenda:

## Log:

## To Do

<%\* await tp.file.rename(tp.user.getSessionNum(tp) + "\_" + tp.date.now("DDMMYYYY")) %>
