-- 코드를 입력하세요
SELECT  category as CATEGORY,sum(sales) as TOTAL_SALES  from 
(SELECT sales, category FROM
    (SELECT BOOK_ID, SUM(SALES) as sales FROM
            (SELECT * FROM 
                (SELECT BOOK_ID, date_format(SALES_DATE,"%Y-%M") as D, SALES From 
                    BOOK_SALES) a 
                    WHERE a.D = "2022-January") b
                Group by book_id) c
                RIGHT Join BOOK on c.BOOK_ID = BOOK.BOOK_ID) ee
                    GROUP BY category order by category
                    
