# Interview: what happens to a pack after it is sent

**Who:** Henrik Sole (`P-HEN`), Finance Analyst. He reads the packs; he does not make them.
**Interviewer:** Mei Tan (`P-MEI`), Head of Engineering.
**When:** 2026-08-21, 20 minutes.
**Why:** The producer's view was recorded on 14 August. This is the consumer's.

---

**Mei:** What do you do with a service review pack?

**Henrik:** I pull three numbers out of it into my renewal model. Attainment, deflection, and
the escalation count. The rest I skim.

**Mei:** Only three?

**Henrik:** The renewal conversation turns on whether service is getting better or worse. Three
numbers answer that. The write-up is for the account manager, not for me.

**Mei:** How do you pull them out?

**Henrik:** By hand, into my own spreadsheet. Same three cells every month.

**Mei:** So if the layout changed?

**Henrik:** I would pull the wrong cells. It has not changed in a year so I have stopped
checking.

**Mei:** Do you know how those numbers are calculated?

**Henrik:** Roughly. Attainment is inside the window over total. Deflection is the automation
rate.

**Mei:** Is it? Lucia calls it deflection and you have just called it automation rate.

**Henrik:** They are the same thing.

**Mei:** Are you certain?

**Henrik:** *[pause]* I am not, no. I have been calling it automation rate in the finance model
for a year. If it turns out they are different then the model has been wrong for a year, and I
would rather find that out from you than from a board meeting.

**Mei:** There is an open request about exactly this. REQ-011.

**Henrik:** I raised that. Nobody has come back.

**Mei:** What happens if a pack is late?

**Henrik:** For me, nothing. I build the model at quarter end, so a pack that is four days late
is still three weeks early. It matters to the account manager and the contract, not to finance.

**Mei:** What happens if a number is wrong?

**Henrik:** That is worse and it is much harder to see. A late pack announces itself. A wrong
number sits in my model until somebody notices the trend does not make sense, and by then it is
in a board slide.

**Mei:** Has that happened?

**Henrik:** The deflection thing in August. The July and August figures were computed
differently and I had them side by side as a trend. I presented that trend.

**Mei:** What would have stopped it?

**Henrik:** If the number in the pack had carried its definition with it. Then I would have seen
version two next to version three and asked.

**Mei:** There is a policy that says exactly that. POL-13.

**Henrik:** Then it is not happening, because the packs carry bare numbers.

---

## Interviewer's note

The producer and the consumer disagree about what a word means, and neither knew until asked.
`REQ-011` in the analytics repository is the same question, unanswered since 18 August.

Both interviews independently name the same missing control: a figure that carries its
definition and version. `POL-13` requires it. Nothing does it.
