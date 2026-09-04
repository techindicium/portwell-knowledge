# Policies

The company's rules that reach this team, as written and circulated. Ownership sits with the
named person.

Nothing in this repository enforces any of them.

| ID | Policy | Owner | Status |
| :- | :- | :- | :- |
| `POL-02` | Published knowledge articles cite a source and name a reviewer. Articles without both are not eligible for retrieval. | `P-ANA` | current |
| `POL-03` | Customer data leaving the EU region requires a documented transfer basis. | `P-TOM` | current |
| `POL-04` | A knowledge article older than 180 days is re-verified before it is used to answer a ticket. | `P-ANA` | current |
| `POL-12` | A service review pack is delivered within five business days of month end. | `P-LUC` | current, contractual |
| `POL-13` | Every figure in a customer-facing pack names the metric definition and version it was computed from. | `P-SOF` | current |
| `POL-14` | A pack is reviewed by someone other than the person who assembled it before it is sent. | `P-LUC` | current |
| `POL-15` | A figure that cannot be sourced is omitted with a note, never estimated or carried forward. | `P-HEN` | draft |

## Where each one stands

| Policy | What would have to be true to enforce it | What exists today |
| :- | :- | :- |
| `POL-02` | The index build refusing an article missing source or reviewer | It publishes them. `KB-0131` is one. |
| `POL-04` | Article age measured against the 180 day line | Nothing measures article age |
| `POL-12` | A deadline anyone is reminded of | A date in a contract nobody on this team has open |
| `POL-13` | Figures carrying their definition and version out of the warehouse | Bare numbers arrive in a CSV |
| `POL-14` | Somewhere to record that a second person read a pack | Nowhere. See the 2026-08-14 interview. |
| `POL-15` | A convention for an unsourceable figure | The August narrative for `ACC-1008` quotes one anyway |

`POL-14` has been unenforceable since it was written, because there is no field anywhere that
records a review. The person it applies to had not heard of it.

## Rules that exist only as habit

- The pack is built from the most recent export in the shared folder. Which one that is depends
  on when somebody looks.
- Last month's file is the template. So a formatting mistake persists until someone notices.
- If a figure looks wrong, ask analytics to re-run rather than investigating it here.
