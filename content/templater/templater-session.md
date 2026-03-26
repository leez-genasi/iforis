---
tags:
  - session
chapter: 2
location:
players: Arkansas, Avery, Shade, Smith, Twig, Variel
date: <% tp.date.now("DDMMYYYY") %>
session no.: <% tp.user.getSessionNum(tp) %>
---

# [<% tp.user.getPrevSession(tp) %>|Prev Session]

## Recap:

## Agenda:

## Log:

## To Do

<%* await tp.file.rename(tp.user.getSessionNum(tp) + ”_” + tp.date.now(“DDMMYYYY”)) %>