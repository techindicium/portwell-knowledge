---
id: ARTICLE-0128
title: Resolving EDI inbound feed rejections
area: integrations
status: published
source: https://portwell.example/docs/edi-troubleshooting
reviewer: Priya Nair
reviewed_at: 2026-06-30
---

An inbound EDI feed rejecting messages with code E-114 has a schema mismatch on the ASN segment. Compare the partner profile against the current ASN template before changing retry settings. Do not disable webhook retries: the feed depends on them for at-least-once delivery.
