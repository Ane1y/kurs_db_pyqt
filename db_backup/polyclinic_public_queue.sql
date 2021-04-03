create table queue
(
    id           serial    not null
        constraint "Queue_pkey"
            primary key,
    patient_id   integer   not null
        constraint "FK_QueuePatients"
            references patients,
    physician_id integer   not null
        constraint "FK_QueuePhysicians"
            references physicians,
    time         timestamp not null
);

alter table queue
    owner to postgres;

create index "fki_FK_QueuePatients"
    on queue (patient_id);

create index "fki_FK_QueuePhysicians"
    on queue (physician_id);

INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (61, 2, 1, '2020-12-17 08:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (62, 2, 1, '2020-12-17 08:30:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (63, 19, 3, '2020-12-17 08:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (11, 2, 6, '2020-12-23 09:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (19, 2, 1, '2020-12-06 09:30:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (6, 1, 5, '2020-12-23 10:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (18, 1, 1, '2020-12-06 09:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (8, 2, 1, '2020-12-23 17:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (3, 5, 1, '2020-12-23 09:30:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (39, 1, 1, '2020-12-13 08:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (40, 1, 6, '2020-12-13 08:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (41, 1, 6, '2020-12-13 08:30:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (42, 1, 7, '2020-12-14 08:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (43, 1, 1, '2020-12-13 08:30:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (24, 6, 3, '2020-12-26 13:30:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (22, 1, 4, '2021-12-02 09:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (2, 2, 1, '2020-12-19 13:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (4, 5, 2, '2020-12-23 10:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (7, 1, 1, '2020-12-30 13:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (25, 1, 4, '2021-01-02 10:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (23, 1, 4, '2020-12-28 09:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (9, 2, 2, '2020-12-20 10:30:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (5, 6, 4, '2020-12-20 09:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (10, 5, 2, '2020-12-23 12:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (1, 2, 3, '2020-12-23 13:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (44, 1, 2, '2020-12-17 08:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (45, 1, 6, '2020-12-15 08:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (46, 1, 6, '2020-12-15 08:30:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (47, 1, 1, '2020-12-15 08:00:00.000000');
INSERT INTO public.queue (id, patient_id, physician_id, time) VALUES (48, 1, 1, '2020-12-15 08:30:00.000000');