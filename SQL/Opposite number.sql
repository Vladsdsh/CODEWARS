/*Very simple, given an integer or a floating-point number, find its opposite.
Examples:
1: -1
14: -14
-34: 34
You will be given a table: opposite, with a column: number. Return a table with a column: res.*/

SELECT
  NUMBER * (-1) AS res
FROM OPPOSITE

-- refactor 

Select -number AS res FROM opposite

-- refactor

select -number res from opposite


