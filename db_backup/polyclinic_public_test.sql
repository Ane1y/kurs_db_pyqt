create table test
(
    id   serial not null
        constraint test_pkey
            primary key,
    num  integer,
    data varchar
);

alter table test
    owner to postgres;

INSERT INTO public.test (id, num, data) VALUES (1, 100, 'abc''def');