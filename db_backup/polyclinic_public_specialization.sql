create table specialization
(
    id   serial      not null
        constraint "Specialization_pkey"
            primary key,
    name varchar(20) not null
);

alter table specialization
    owner to postgres;

INSERT INTO public.specialization (id, name) VALUES (1, 'терапевт');
INSERT INTO public.specialization (id, name) VALUES (2, 'хирург');
INSERT INTO public.specialization (id, name) VALUES (3, 'эндокринолог');
INSERT INTO public.specialization (id, name) VALUES (4, 'кардиолог');
INSERT INTO public.specialization (id, name) VALUES (5, 'иммунолог');
INSERT INTO public.specialization (id, name) VALUES (6, 'оториноларинголог');