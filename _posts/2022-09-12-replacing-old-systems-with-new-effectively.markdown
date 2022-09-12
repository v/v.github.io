---
layout: post
title: "Replacing old systems with new systems effectively"
date: 2022-09-12
published: true
---

You are an engineer in a 100+ person organization. Often, when you show up to work, you're asked to build a new system to replace an old system. Maybe there's some code that's buggy or slow that needs to be swapped out. Maybe you're switching a piece of cloud infrastructure - you're going to run CI on Buildkite instead of CircleCI, or log metrics using Datadog instead of Cloudwatch. Or maybe you're swapping out business process A for producing widgets with business process B.

<div class="flex-row-centered">
    <img src="https://via.placeholder.com/500" />
</div>

Depending on the approach that you take, the final result can end up looking pretty different.

**Result A: You build the new system, and you make it available to use in production**

You tested that the new code produces correct results. You integrated the Buildkite and Datadog so that they work in production. You implemented business process B in the internal tool so customers can start using it.

This is the bare minimum work that you have to do. If you stop here, your work is yet to add any business value. A person in the future has to start using your new system before the company realizes any of the benefits.

**Result B: Result A + proof that the new system is better than the old system**

This step is not always trivial, but you typically want to show that the new thing you built actually achieves the result you want to achieve. The bug or performance problem is fixed. The new cloud infrastructure is faster / cheaper / easier to use. The new business process achieves the result we set out to achieve.

If you skip this step, you risk making things worse.

**Result C: Result B + you swap out frequent occurrences of the old system with the new system**

Now, we start realizing the value of the new thing we built. The bug is fixed in the most common codepaths. The new cloud infrastructure is used by a majority of engineers. Business process B is used more frequently by customers than business process A.

It is important that you adopt the new feature in frequently used areas of the business, and not in simpler toy use cases. This is not always easy, because the frequently used areas of the business are more complex. But you get more value from integrating into the frequently used areas of the business, and you ensure that your new system is a more complete replacement for the old system.

**Result D: Result C + you eliminate the old system entirely in favor of the new system**

This is the holy grail for changes you're trying to make. People that solve the same problem in the future will use the new system and get its benefits automatically. We can stop keeping the lights on for the old system, which means we can save on cloud bills, on engineering maintenance costs, and the awkwardness of explaining why there are two ways to solve the same problem.

### How you should use this information

As an engineer, you can use this framework to figure out what your project will and won't achieve. You should aim to achieve Result D whenever possible, because it leads to a simpler architecture for the next person, or your future self. That being said, you might also encounter situations in which eliminating every last use of the old system is not desirable. For example, if you've decided to start storing data in SQL tables instead of storing them in a document store, it might not make sense to edit parts of the business that are infrequently used or infrequently edited. Data migrations are usually not simple, and the juice may not be worth the squeeze on the non-critical parts of the business.

As an engineering leader, you ought to establish a culture where engineers are rewarded for achieving maximum adoption for the new systems they build. Recognize people for driving adoption of their features rather than leaving it as an afterthought. Recognize teams that can make such product changes frequently and smoothly, and teams that build features without adding accidental complexity. These teams have strong soft skills and customer relationships. The future of your organization depends on making such changes effectively, and unless you're a ladder climbing politician, you ought to make life easier for your future self.
