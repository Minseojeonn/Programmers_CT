-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME FROM
    (
        SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME, ANIMAL_OUTS.DATETIME as outd, ANIMAL_INS.DATETIME as ind
        from ANIMAL_OUTS 
        inner join ANIMAL_INS 
        on ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
     ) d
WHERE outd <= ind Order by ind