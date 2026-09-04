# Interview: how the service review packs get made

**Who:** Lucia Ferreira (`P-LUC`), Service Delivery Manager. She has made every pack for the
last fourteen months.
**Interviewer:** Mei Tan (`P-MEI`), Head of Engineering.
**When:** 2026-08-14, 45 minutes.
**Why:** Before deciding whether any of this can be automated, somebody should write down what
actually happens.

Lightly tidied. Filler removed, wording kept.

---

**Mei:** Start at the beginning. It is the first of the month. What happens?

**Lucia:** Nothing, for a few days. I cannot do anything until Declan sends me the figures, and
he cannot run them until the month is properly closed. So realistically I start on the third or
the fourth.

**Mei:** How do the figures arrive?

**Lucia:** A CSV. He drops it in the shared folder and messages me. Sometimes he just pastes the
numbers into the message and I copy them out. That is worse but it is quicker for him.

**Mei:** Is there a standard format?

**Lucia:** More or less. It has the accounts down the side and the measures across. The columns
have moved before. When they move I notice because my copy-paste goes into the wrong cells and
the numbers look mad.

**Mei:** And if they did not look mad?

**Lucia:** *[pause]* Then I would not notice. Yes. I know.

**Mei:** Walk me through building one pack.

**Lucia:** I open last month's file for that account, save it as the new month, and change the
numbers. The tabs are all set up, the formulas are there, so mostly it is typing over four or
five cells and the rest recalculates.

**Mei:** Which cells?

**Lucia:** Ticket count, how many were inside the window, proposals, deflected. The percentages
work themselves out. Then the volumes tab, which is a longer list but it is just paste.

**Mei:** You said the percentages work themselves out. Have you ever seen one not?

**Lucia:** Not that I have noticed. Why, should I have?

**Mei:** I am asking, not implying.

**Lucia:** Then no.

**Mei:** What about the write-up?

**Lucia:** That takes longer than the spreadsheet. I look at what moved, I look at the open
escalations, and I write a page. I try to say why something moved and not just that it did,
because otherwise there is no point sending it.

**Mei:** Where do you get the why?

**Lucia:** From knowing. I sit next to support. If the EDI thing blew up in the middle of the
month I know that is why integrations is high, because I was there.

**Mei:** And if you had not been there?

**Lucia:** Then I would write that volumes were up. Which is true and useless.

**Mei:** Who checks the pack before it goes out?

**Lucia:** It depends. If there is something sensitive in it I ask Gabriela to read it. If it is
a normal month I just send it.

**Mei:** How often is it a normal month?

**Lucia:** Most months.

**Mei:** There is a policy that says a pack is reviewed by someone other than the person who
made it.

**Lucia:** Is there? Then I am not following it. Nobody has ever mentioned it to me and there is
nowhere to record that a review happened, so I would not know how to prove I had.

**Mei:** What is the deadline?

**Lucia:** Five working days after month end. It is in the Enterprise contracts. I have missed
it twice, once when Declan was on leave and once in March when I was.

**Mei:** What happened when you missed it?

**Lucia:** Nothing happened. Nobody chased. Which I do not think means it is fine, it means
nobody was reading them that month.

**Mei:** How do you know a number in the pack is right?

**Lucia:** I do not, really. I know it is what Declan sent me. If the customer disputes it I go
back to him and he re-runs it.

**Mei:** Has that happened?

**Lucia:** Once, in August. Sunder asked why their deflection had changed and it turned out the
definition had changed underneath us. Nobody told me. I had sent them a number in July computed
one way and a number in August computed another way and presented them as a trend.

**Mei:** Whose fault was that?

**Lucia:** Not Declan's. He changed it for a good reason. There is just no list anywhere of who
is using which number, so there was nobody for him to tell.

**Mei:** If you could fix one thing.

**Lucia:** I would want each number in the pack to say where it came from. Not for the customer,
for me. So that when someone asks in November why the July figure was what it was, I can answer
without going back to Declan and hoping he remembers.

**Mei:** Not the deadline?

**Lucia:** The deadline is only hard because the rest is slow. If assembling it took twenty
minutes the deadline would not be a problem.

**Mei:** Last one. If a machine did this, what should it not be allowed to do?

**Lucia:** Send it. It can build the whole thing, I do not care. But somebody has to look at a
number and decide it is fit to put in front of a customer, and that has to be a person, because
if it is wrong it is the account manager who gets the call and not the machine.

---

## Interviewer's note

Three things worth recording separately.

1. She does not know whether the percentages have ever failed to recalculate, and there is no
   way for her to find out. That is worth checking.
2. `POL-14` requires a second reader. She has never heard of it and there is nowhere to record
   compliance, so it has been unenforceable since it was written.
3. The August definition change is `INC-03` in the analytics repository. She has the consumer
   side of it and Declan has the producer side. Neither of them has the whole picture, and the
   thing that would have prevented it (a list of consumers per metric) belongs to neither.
