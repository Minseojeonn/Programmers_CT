Select C.ID, IFNULL(CHILD_COUNT,0) as CHILD_COUNT FROM (Select * FROM 
(Select PARENT_ID as ID, COUNT(*) AS CHILD_COUNT FROM ECOLI_DATA GROUP BY PARENT_ID) as T 
WHERE T.ID is not null) as TB
Right JOIN 
(SELECT ID FROM ECOLI_DATA) AS C 
on C.ID = TB.ID 


    
