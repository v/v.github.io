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

You test that the new code produces correct results. You integrate Buildkite and Datadog so that they work in production. You implement business process B so customers can start using it.

This is the bare minimum work that you have to do. If you stop here, your work is yet to add any business value. Someone has to actually start using the new system you built before the company realizes any of the benefits.

**Result B: Result A + proof that the new system is better than the old system**

Typically, you want to show that the new system you built is actually better than the thing it's replacing. Sometimes this is simple - you check that the bug or performance problem is fixed. Often, it requires you to get some customers to start using the new system, and gather feedback to assess if things have gotten better.

If you skip this step, you risk making things worse. A few times in the life of a product, you might get away with shipping the new system and hoping for the best. But as your product matures, a rigorous evaluation of the old vs new system is the only way to guarantee that your work is having the intended effect.

**Result C: Result B + you swap out frequent occurrences of the old system with the new system**

Now that you know that the new system works, you start using it in the core parts of the product. You fix the bug in the most common codepaths. You ship the new cloud infrastructure to a majority of engineers. Cusotmers use business process B more often than business process A.

It is important that you adopt the new system in core areas of the product, and not in simpler toy use cases. This is not always easy, because the core areas of the business are more complex. But you get more value this way, and you ensure that your new system is a more complete replacement for the old system.

**Result D: Result C + you eliminate the old system entirely in favor of the new system**

If you're a conscientious engineer, this is the holy grail for new systems you're building. You switch to using the new system everywhere in your product. People that solve the same problem in the future will use the new system and get its benefits automatically. You can stop maintaining the old system, which means savings on cloud bills, but more importantly on engineering time, and the awkwardness of explaining why there are multiple ways to solve the same problem.

### How you should use this information

As an engineer, you can use this framework to figure out what your project will and won't achieve. You should aim to achieve Result D whenever possible, because it leads to a simpler architecture for the next person, or your future self. That being said, you might also encounter situations in which eliminating every last use of the old system is not desirable. For example, if you've decided to start storing data in SQL tables instead of storing them in a document store, it might not make sense to edit parts of the business that are infrequently used or infrequently edited. Data migrations are usually not simple, and the juice may not be worth the squeeze for the non-critical parts of the business.

As an engineering leader, you ought to establish a culture where engineers are rewarded for achieving maximum adoption for the new systems they build. Recognize teams for driving adoption of their features rather than leaving it as an afterthought. Encourage engineers to make cross cutting changes confidently by building tools for static analysis and mass refactoring tools. Encourage your teams to build playbooks for running experiments and measuring the impact of new features that they launch. The future of your organization depends on making such changes effectively, and unless you're a ladder climbing politician, you ought to make life easier for your future self.
