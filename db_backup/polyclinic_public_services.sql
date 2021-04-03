create table services
(
    id                serial      not null
        constraint "Services_pkey"
            primary key,
    name              varchar(50) not null,
    cost              integer     not null,
    specialization_id integer     not null
        constraint "FK_specializations"
            references specialization
);

alter table services
    owner to postgres;

create index "fki_FK_specializations"
    on services (specialization_id);

INSERT INTO public.services (id, name, cost, specialization_id) VALUES (1, 'осмотр терапевта', 1000, 1);
INSERT INTO public.services (id, name, cost, specialization_id) VALUES (2, 'осмотр хирурга', 1500, 2);
INSERT INTO public.services (id, name, cost, specialization_id) VALUES (3, 'осмотр эндокринолога', 1200, 3);
INSERT INTO public.services (id, name, cost, specialization_id) VALUES (4, 'осмотр кардиолога', 1050, 4);
INSERT INTO public.services (id, name, cost, specialization_id) VALUES (5, 'осмотр иммунолога', 900, 5);
INSERT INTO public.services (id, name, cost, specialization_id) VALUES (6, 'операция на сердце', 5000, 2);
INSERT INTO public.services (id, name, cost, specialization_id) VALUES (8, 'Обследование щитовидной железы', 1200, 3);