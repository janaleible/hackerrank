SELECT 
    f1.x, f1.y 
FROM 
    ( SELECT  ROW_NUMBER() OVER(ORDER BY x ASC) AS id, x, y FROM functions ) f1,
    ( SELECT  ROW_NUMBER() OVER(ORDER BY x ASC) AS id, x, y FROM functions ) f2
WHERE f1.x = f2.y AND f1.y = f2.x
    AND f1.id < f2.id
ORDER BY f1.x ASC;
