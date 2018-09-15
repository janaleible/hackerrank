SELECT 
    wands.id, 
    wands_property.age, 
    wands.coins_needed, 
    wands.power
FROM wands 
LEFT JOIN wands_property ON wands.code = wands_property.code
LEFT JOIN (
    SELECT 
        MIN(coins_needed) AS price, 
        age, 
        power
    FROM wands
    LEFT JOIN wands_property ON wands.code = wands_property.code
    WHERE wands_property.is_evil = 0
    GROUP BY age, power
) minimum_price ON (minimum_price.age = wands_property.age AND minimum_price.power = wands.power)
WHERE 
    is_evil = 0 AND 
    minimum_price.price = wands.coins_needed
ORDER BY wands.power DESC, age DESC;
