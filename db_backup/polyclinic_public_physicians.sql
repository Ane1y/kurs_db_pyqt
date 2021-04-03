create table physicians
(
    id                serial      not null
        constraint "Physicians_pkey"
            primary key,
    name              varchar(50) not null,
    role_id           integer     not null
        constraint "FK_roles"
            references roles,
    user_id           integer     not null
        constraint "FK_users"
            references authentication_data
        constraint "FK_usersPhysicians"
            references authentication_data,
    passport          bigint      not null,
    date_of_birth     date        not null,
    specialization_id integer     not null
        constraint "FK_specialization"
            references specialization
);

alter table physicians
    owner to postgres;

create index "fki_FK_roles"
    on physicians (role_id);

create index "fki_FK_usersPhysicians"
    on physicians (user_id);

create index "fki_FK_specialization"
    on physicians (specialization_id);

INSERT INTO public.physicians (id, name, role_id, user_id, passport, date_of_birth, specialization_id) VALUES (1, 'Краснов Валерий Александрович', 2, 1, 4507691152, '1990-03-12', 1);
INSERT INTO public.physicians (id, name, role_id, user_id, passport, date_of_birth, specialization_id) VALUES (2, 'Чугановская Мария Петровна', 2, 2, 4578564512, '1980-01-06', 1);
INSERT INTO public.physicians (id, name, role_id, user_id, passport, date_of_birth, specialization_id) VALUES (3, 'Замакова Зарина Алексеевна', 1, 3, 7845781256, '1975-05-01', 2);
INSERT INTO public.physicians (id, name, role_id, user_id, passport, date_of_birth, specialization_id) VALUES (4, 'Колкова Наталья Андреевна', 1, 4, 1256785623, '1995-08-03', 3);
INSERT INTO public.physicians (id, name, role_id, user_id, passport, date_of_birth, specialization_id) VALUES (5, 'Мартынова Анна Александровна', 1, 5, 4578562345, '1970-04-07', 4);
INSERT INTO public.physicians (id, name, role_id, user_id, passport, date_of_birth, specialization_id) VALUES (6, 'Пузин Пётр Евгеньевич', 1, 6, 1232659878, '1960-05-09', 1);
INSERT INTO public.physicians (id, name, role_id, user_id, passport, date_of_birth, specialization_id) VALUES (7, 'Постин Константин Григорьевич', 1, 7, 4545785623, '1995-07-09', 1);