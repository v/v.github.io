---
layout: post
title: "Learnings from a year in engineering management"
date: 2019-06-08
published: false
---

In 2018, I spent 9 months as an engineering manager at [Cruise Automation](https://getcruise.com). In 2019, I returned to a Software Engineering role after deciding that it wasn't the right role for me, especially at this stage of my career.

Setting aside the outcome of my role change, I learned a great deal about how front line management works in a growing startup.

I'll note that this is a story of one person's experience on one team at one company. It is not a reflection of every manager's experience (at Cruise or otherwise).

### Starting the role 

Six months after joining Cruise as a Senior Engineer, I was offered an engineering manager role on a small team where I was the tech lead. I worked on Ground Truth, which had grown from 5 engineers to 20+ engineers in 6 months.

When I took on the role, I set the following goals for myself:

GT-Pegasus is a high performing team.

1. We consistently deliver datasets to our customers at the agreed upon timelines.
1. We build robust, scalable platforms that are self-serve and require very little engineering oversight to maintain.

The engineers on GT-Pegasus enjoy being on the team.

1. They feel like they're growing as ICs.
1. They feel like they have autonomy in their work.
1. I am not a blocker for engineering work getting scoped or done on the team.
1. They know why we make the decisions that we do, and have a say in the work that gets done.
1. They understand the long term vision, goals of the ground truth team. 
1. The work on the team feels collaborative. Multiple people know about each subsystem. There are no single points of failure.

The software we build is of high quality.

1. A new engineer can easily contribute to our code. They can set up our projects, make a change, send out a code review and deploy it within a day.
1. Engineers can efficiently gain confidence in the code they're shipping. 
1. Engineers can make cross-cutting changes without fear, and lean on automated tests, the development environment, and the architecture of the code to know that their changes are good. 
1. Once a change has passed tests and been code reviewed, it's rare that it'll break in fundamental ways in production.
1. Our production systems are monitored so that severe faults are detected automatically, rather than by a human.

In hindsight, here's the advice I'd give to 2018 Vaibhav.

**Many of your goals are a senior engineer's job and not an engineering manager's job** 

A manager cannot make a team build high quality software, write tests or review code quickly. A manager cannot make a team monitor their services so that outages are automatically detected.

A senior engineer should be setting the technical vision for your team, not a manager. Your engineers are responsible for writing and operating software, and its their job to do it well. Your best engineers are leaders, and they should be driving these decisions on your team. If you do this in their place, you're denying them a growth opportunity. You're also going to be less effective at this job as you stop writing code.

**You're not thinking about building relationships with other teams and other functions at the company**

To do anything impactful at a company, many people need to work together towards a common goal. In my role at Cruise, this involved our sister engineering teams, product managers, designers, and operations team. It's important for you to build trust and alignment with the people on these teams. You usually start this by building a good relationship with the team's leaders - make small talk with team, wish them happy birthday, and smile at them in the hallway. 

<video style="max-width: 100%" autoplay loop muted playsinline src="https://media.giphy.com/media/l1J9HZMI8IpXXVY5i/giphy.mp4"></video>

When you need something from the team in the future, having a good relationship will help you get what you want. Humans are social creatures and they co-operate with people they like. If you find yourself disagreeing with someone, you'll want to resolve the disagreement without damaging the relationship. A sub-optimal decision is usually not going to cause your team to fail. A broken relationship very well might.

Without alignment with your stakeholders, you'll have limited impact. Two teams working on an initiative with shared goals can accomplish much more than one talented team working in a silo.

**Performance management is a HARD job**

You know how to write clean code, and how to build great products. These are not your job anymore, because you have five engineers that can do this as well as you can.

Your job is to build and grow a team under you. No one else is going to do this for you. 

Managing people's careers is hard. You're expected to rate people's performance after a short period of time. You're supposed to provide them continuous feedback so no performance review is a surprise. At a growing startup, teams move around a fair bit, so you are managing new members each month. In this environment, it's important that you can distinguish between poor, acceptable and outstanding performance, especially given seniority, and deliver the message consistently. You'll spend a great deal of time crafting a message for each of your reports.

Ultimately, someone's performance is a list of their accomplishments at the company. 

There are many other behaviors and activities that cloud your judgement - someone can be late to meetings, they can bring in cake for their coworkers's birthdays, they can be more experienced than you, or they can have the best restaurant recommendations. You want to reward people for completing projects that make a difference at the company. That's it. People can't deliver results consistently unless they do good work.

You'll also have to learn to tell people that they're doing a poor job, and that they'll be better off at a different company. This is a difficult, emotional conversation so you're going to feel lousy about having it. If you delay it, you will feel even worse, because it'll nag at you each day.

### The importance of hiring

Hiring is your company's life blood and YOU own it.

As a manager, your attention is being pulled at by many things at once. You already have a calendar full of team meetings, one-on-ones and project discussions. Your communication apps are an endless fountain of messages.

INSERT GIF HERE

It's easy to see how you neglect hiring in this world. After all, hiring another person means that you have one more reason to be interrupted at any time. Hiring is also a risk, and puts you in a position of vulnerability. If you hire the wrong person, you'll spend many months managing them before you part ways.

That being said, hiring is absolutely critical at any growing startup. Your startup has a small chance of succeeding, and one of the most reliable ways to improve your chances is to double the team. 

Before you build amazing infrastructure, a killer product, or an ingenious marketing campaign, you must build a repeatable hiring process.

It is your job to maintain a healthy pipeline of candidates for your team, give each candidate a good interviewing experience, and convince the good candidates to work for you. Good recruiters and sourcers will help you in this process, but you have to own your team's hiring outcomes. It's a long term bet, but boy does it pay off!

A good hire will change the company in unimaginable ways. Entire teams and departments will be built around them. The impact of these teams will pale in comparison to the 10 extra messages you could have answered on any given day.

### Good intentions and holding people accountable

TODO


### Failed projects

TODO


### Promotion and Calibration

Going through the calibration and promotion process was one of the most eye opening experiences as a manager.

Once a year, Cruise goes through a company wide performance review followed by calibration, promotion and compensation adjustments. Companies like Cruise want to be careful to reward the right people, and ensure fairness regardless of your manager or team.

It starts with written 360 feedback - you, your manager and your peers answer questions about your performance over the last year. Managers nominate you for promotion, and decide if you are falling below the expectations of your role.

Once this happens, front line managers in your group get into a room with a Senior Manager and discuss each employee's ratings. 

As a manager, it's your job to defend the ratings that you give. The company usually has a guideline on how many employees should end up in each rating bucket. For example, at Hogwarts, the ratings and guidelines may look like this for the [O.W.L. exam](https://harrypotter.fandom.com/wiki/Ordinary_Wizarding_Level):

| Rating | Expected Distribution | Number of employees (for a team of 20) |
| ------ | :-------------------: | :----------------------------------: |
| Poor | 10% | 2 |
| Acceptable | 70% | 14 |
| Exceeds Expectations | 10% | 2 | 
| Outstanding | 10% | 2 | 

As the managers in a group of 20 employees, you'll need to agree on which 2 members receive "Poor" ratings, and which members receive "Outstanding" ratings. If you don't fall within the guidelines, your group will have to make the case that it is an especially high performing group compared with the rest of the company.

<video style="max-width: 100%" autoplay loop muted playsinline src="/static/sorting_hat.mp4"></video>

As a manager, this means that you have to sell your peers on the achievements of your reports to get them the rewards you think they deserve.

As an employee, this means that other teams and managers should be aware of the good work that you're doing. It's much easier to get a raise or promotion if managers on other teams vouch for your accomplishments. This is why self-promotion is important in the corporate environment. Quietly doing your job while limiting interactions outside your team will not help you progress. You want to take credit for your work, and you want your work to be visible to leaders at the company. The tone of your communication should be along the lines of "I am proud of my contribution to project X which was invaluable to the company in achieving Y and Z goals."

If this is the first time you're hearing about calibration, you may think it is unfair to compare employees, and only reward employees for visible, high-profile projects. After all, who is going to fix technical debt? Rewarding self-promotion means that the company values personality and likeability over work ethic.

I feel that the calibration process has flaws (like any process), but is overall a positive thing for a company. A company wants to encourage employees with a strong work ethic to pick up critical, visible projects. The company also wants to reward people that maintain good relationships with neighboring teams. Regardless of your personal brilliance, the best work happens at a company when many teams work together. Finally, the company also wants to keep managers honest. They don't want employees getting raises and promotions or have low perfoming employees stick around for a long time just because their manager is lenient.

Scratchpad

- My goals for myself
- Things change all the time
- Sentiment of 
- Performance Management is critical
- Salesmanship is an important part of your role
- Good intentions do not get you rewards, neither does doing another person's job.
- Holding people accountable
- IC ladder after 
    * Technical vision for the team or many teams.
- You have to let things fail and be patient.
