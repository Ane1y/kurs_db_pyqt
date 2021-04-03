create table roles
(
    id   serial      not null
        constraint "Roles_pkey"
            primary key,
    name varchar(50) not null
);

alter table roles
    owner to postgres;

INSERT INTO public.roles (id, name) VALUES (1, 'user');
INSERT INTO public.roles (id, name) VALUES (2, 'admin');