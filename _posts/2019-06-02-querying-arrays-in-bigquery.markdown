---
layout: post
title: "Using UNNEST to query arrays in BigQuery"
date: 2019-06-02
published: true
---

We've started using Google BigQuery extensively at [Cruise](https://getcruise.com) as a data warehouse. The syntax for querying arrays in BigQuery isn't obvious and this post will explain how it works.

Consider a table that stores a company and its executives with the following schema:

```
companies
- name
- founding_year
- executives
    * name
    * title
```

with some sample data

```sql
WITH companies AS ( 
   SELECT 
      "Apple" as name, 1976 as founding_year,
      [
        (SELECT AS STRUCT 'Tim Cook' name, 'CEO' title),
        (SELECT AS STRUCT 'Jony Ive' name, 'Chief Design Officer' title),
        (SELECT AS STRUCT 'Jeff Williams' name, 'COO' title)

      ] as executives UNION ALL SELECT
      
      "Amazon" as name, 1994 as founding_year,
      [
        (SELECT AS STRUCT 'Jeff Bezos' name, 'CEO' title),
        (SELECT AS STRUCT 'Brian T. Olsavsky' name, 'CFO' title)
      ] as executives UNION ALL SELECT
      
      "Twitter" as name, 2006 as founding_year,
      [
        (SELECT AS STRUCT 'Jack Dorsey' name, 'CEO' title),
        (SELECT AS STRUCT 'Ned Segal' name, 'CFO' title)
      ] as executives UNION ALL SELECT
     
      "AirBNB" as name, 2008 as founding_year,
      [
        (SELECT AS STRUCT 'Brian Chesky' name, 'CEO' title),
        (SELECT AS STRUCT 'Joe Gebbia' name, 'CPO' title)
      ] as executives UNION ALL SELECT
      
      "Square" as name, 2009 as founding_year,
      [
        (SELECT AS STRUCT 'Jack Dorsey' name, 'CEO' title)
      ] as executives
      
) SELECT * FROM companies;
```

| Row | name | founding_year | executives.name | executives.title |
| --- | ---- | ------------- | --------------- | ---------------- |
| 1 | Apple | 1976 | Tim Cook | CEO |
|   |       |      | Jony Ive | Chief Design Officer |
|   |       |      | Jeff Williams | COO |
| 2 | Amazon | 1994 | Jeff Bezos | CEO |
|   |       |       | Brian T. Olsavsky | CFO |
| 3 | Twitter | 2006 | Jack Dorsey | CEO |
|   |         |      | Ned Segal | CFO |
| 4 | AirBNB | 2008 | Brian Chesky | CEO |
|   |        |      | Joe Gebbia | CPO |
| 5	| Square | 2009 | Jack Dorsey | CEO | 

We can use familiar SQL queries to query top level fields like `name` or `founding_year`


```sql
SELECT * FROM companies WHERE founding_year > 2000;
```

| Row | name | founding_year | executives.name | executives.title |
| --- | ---- | ------------- | --------------- | ---------------- |
| 1 | Twitter | 2006 | Jack Dorsey | CEO |
|   |         |      | Ned Segal | CFO |
| 2 | AirBNB | 2008 | Brian Chesky | CEO |
|   |        |      | Joe Gebbia | CPO |
| 3	| Square | 2009 | Jack Dorsey | CEO | 

To query nested fields like `executives.name` or `executives.title`, we use a combination of `CROSS JOIN` and `UNNEST`.

For example, this query returns all companies with Jack Dorsey as an executive:

```sql
SELECT * FROM companies CROSS JOIN UNNEST(executives) as executive WHERE executive.name = 'Jack Dorsey';
```

| Row | name | founding_year | executives.name | executives.title |
| --- | ---- | ------------- | --------------- | ---------------- |
| 1 | Twitter | 2006 | Jack Dorsey | CEO |
|   |         |      | Ned Segal | CFO |
| 2	| Square  | 2009 | Jack Dorsey | CEO | 

To understand how this query works, notice that `CROSS JOIN` and `UNNEST` return the row with the flat value of each item in the array.

For example, consider this query

```sql
SELECT c.*, executive FROM companies c CROSS JOIN UNNEST(c.executives) as executive
```

This returns a row for each combination of company and executive.

| Row | name | founding_year | executives.name | executives.title | executive.name | executive.title |
| --- | ---- | ------------- | --------------- | ---------------- | -------------- | --------------- |
| 1 | Apple | 1976 | Tim Cook | CEO | Tim Cook | CEO
|   |       |      | Jony Ive | Chief Design Officer |
|   |       |      | Jeff Williams | COO |
| 2 | Apple | 1976 | Tim Cook | CEO | Jony Ive | Chief Design Officer
|   |       |      | Jony Ive | Chief Design Officer |
|   |       |      | Jeff Williams | COO |
| 3 | Apple | 1976 | Tim Cook | CEO | Jeff Williams | COO
|   |       |      | Jony Ive | Chief Design Officer |
|   |       |      | Jeff Williams | COO |
| 4 | Amazon | 1994 | Jeff Bezos | CEO | Jeff Bezos | CEO
|   |       |       | Brian T. Olsavsky | CFO |
| 5 | Amazon | 1994 | Jeff Bezos | CEO | Brian T. Olsavsky | CFO
|   |       |       | Brian T. Olsavsky | CFO |
| 6 | Twitter | 2006 | Jack Dorsey | CEO | Jack Dorsey | CEO
|   |         |      | Ned Segal | CFO |
| 7 | Twitter | 2006 | Jack Dorsey | CEO | Ned Segal | SFO
|   |         |      | Ned Segal | CFO |
| 8 | AirBNB | 2008 | Brian Chesky | CEO | Brian Chesky | CEO
|   |        |      | Joe Gebbia | CPO |
| 9 | AirBNB | 2008 | Brian Chesky | CEO | Joe Gebbia | CPO
|   |        |      | Joe Gebbia | CPO |
| 10 | Square | 2009 | Jack Dorsey | CEO | Jack Dorsey | CEO


Once, we have this table, it's easy to see how `WHERE` clauses work like we expect on the `executive.name` and `executive.title` fields.

Given the results above - what would this query return?

```sql
SELECT c.name, executive.name as ceo FROM companies c CROSS JOIN UNNEST(c.executives) as executive WHERE executive.title='CEO'
```

If you guessed right, it returns the name and CEO of each company in our table.

| Row | name | ceo |
| --- | ---- | --- |
| 1 | Apple | Tim Cook |
| 2 | Amazon | Jeff Bezos |
| 3 | Twitter | Jack Dorsey |
| 4 | AirBNB | Brian Chesky |
| 5	| Square | Jack Dorsey |



**Tip**: You can use a comma in place of `CROSS JOIN` in your queries for brevity.

```sql
SELECT c.* FROM companies c CROSS JOIN UNNEST(executives) as executive WHERE executive.name = 'Jack Dorsey';
```

is equivalent to

```sql
SELECT c.* FROM companies c, UNNEST(executives) as executive WHERE executive.name = 'Jack Dorsey';
```

I hope this helps you explore datasets in BigQuery more easily. 

BigQuery has worked well for us as a data warehouse. From engineers to data analysts and managers, I've seen users of all technical abilities have use BigQuery at [Cruise](https://getcruise.com) in their day-to-day work to build a self-driving robotaxi.
