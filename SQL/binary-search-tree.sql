SELECT 
    nodes.N,
    --COUNT(children.N)
    CASE 
        WHEN nodes.P IS NULL THEN "Root"
        WHEN COUNT(children.N) = 0 THEN "Leaf"
        ELSE "Inner" 
    END
FROM BST nodes FULL JOIN (
    SELECT 
        N,
        P
    FROM BST 
) children ON nodes.N = children.P
WHERE nodes.N IS NOT NULL
GROUP BY nodes.N, nodes.P
ORDER BY nodes.N
