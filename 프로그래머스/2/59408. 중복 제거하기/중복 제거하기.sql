-- 코드를 입력하세요
SELECT count(*) as count from 
    (SELECT NAME, count(*) FROM ANIMAL_INS Group by NAME)a
where a.NAME is not null