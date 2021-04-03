create table finance_report
(
    id           serial  not null
        constraint "Finance_report_pkey"
            primary key,
    physician_id integer not null
        constraint "FK_fr_physician"
            references physicians,
    cost         integer not null
);

alter table finance_report
    owner to postgres;

INSERT INTO public.finance_report (id, physician_id, cost) VALUES (2, 2, 1000);
INSERT INTO public.finance_report (id, physician_id, cost) VALUES (4, 6, 1000);
INSERT INTO public.finance_report (id, physician_id, cost) VALUES (3, 3, 1500);
INSERT INTO public.finance_report (id, physician_id, cost) VALUES (1, 1, 9200);