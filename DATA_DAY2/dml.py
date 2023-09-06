import psycopg2
import time
import csv

conn = psycopg2.connect(
    host="localhost", # oreumi.aws.
    database="retaurant", # 접속할 데이터베이스
    user="postgres", # 관리자 유저
    password="1234", # 관리자 비밀번호
    )

cursor = conn.cursor() # 커서 생성

create_table_query = """
    -- Table: public.fastfood_restaurant_us

    -- DROP TABLE IF EXISTS public.fastfood_restaurant_us;

    CREATE TABLE IF NOT EXISTS public.fastfood_restaurant_us
    (
        address character varying(100) COLLATE pg_catalog."default",
        categories character varying(100) COLLATE pg_catalog."default",
        city character varying(100) COLLATE pg_catalog."default",
        country character varying(30) COLLATE pg_catalog."default",
        keys character varying(200) COLLATE pg_catalog."default",
        latitude real,
        longitude real,
        name character varying(50) COLLATE pg_catalog."default",
        "postalCode" character varying(30) COLLATE pg_catalog."default",
        province character(2) COLLATE pg_catalog."default",
        "sourceURLs" text COLLATE pg_catalog."default",
        websites text COLLATE pg_catalog."default",
        "dateAdded" timestamp without time zone,
        "dateUpdated" timestamp without time zone,
        id character varying(30) COLLATE pg_catalog."default"
    )

    TABLESPACE pg_default;

    ALTER TABLE IF EXISTS public.fastfood_restaurant_us
        OWNER to postgres;
"""


cursor.execute(create_table_query)

conn.commit()
conn.close()