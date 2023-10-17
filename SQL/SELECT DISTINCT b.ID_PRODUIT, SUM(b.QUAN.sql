SELECT DISTINCT b.ID_PRODUIT, SUM(b.QUANTITE) *(SELECT prix FROM `learning-355618.TEST_BQ.PRODUITS`WHERE ID_PRODUIT = b.ID_PRODUIT) AS CA
FROM `learning-355618.TEST_BQ.SALES` b
GROUP BY b.ID_PRODUIT
ORDER BY CA DESC





SELECT 
(CASE 
WHEN a.ID_CLIENT IN (SELECT ID_CLIENT FROM `learning-355618.TEST_BQ.CUSTOMER`) THEN 'IDENTIFIE'
ELSE 'NON_IDENTIFIE'
END) AS TYPE_CLIENT, 
SUM(a.QUANTITE) AS QUANTITE
FROM `learning-355618.TEST_BQ.SALES` a
GROUP BY a.ID_CLIENT



SELECT DISTINCT
(CASE 
WHEN a.ID_CLIENT IN (SELECT ID_CLIENT FROM `learning-355618.TEST_BQ.CUSTOMER`) THEN 'IDENTIFIE'
ELSE 'NON_IDENTIFIE'
END) AS TYPE_CLIENT,
(CASE 
WHEN a.ID_CLIENT IN (SELECT ID_CLIENT FROM `learning-355618.TEST_BQ.CUSTOMER`) 
THEN (SELECT SUM (QUANTITE) FROM `learning-355618.TEST_BQ.SALES` WHERE ID_CLIENT IN (SELECT ID_CLIENT FROM `learning-355618.TEST_BQ.CUSTOMER`))
ELSE (SELECT SUM (QUANTITE) FROM `learning-355618.TEST_BQ.SALES` WHERE ID_CLIENT NOT IN (SELECT ID_CLIENT FROM `learning-355618.TEST_BQ.CUSTOMER`))
END) AS QUANTITE
 
FROM `learning-355618.TEST_BQ.SALES` a
GROUP BY a.ID_CLIENT