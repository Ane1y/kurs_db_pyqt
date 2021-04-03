create table patients
(
    id               serial      not null
        constraint "Patients_pkey"
            primary key,
    name             varchar(50) not null,
    user_id          integer     not null
        constraint "FK_users"
            references authentication_data,
    date_of_birth    date        not null,
    passport         bigint      not null,
    snils            bigint      not null,
    insurance_policy bigint      not null,
    contract_num     integer     not null
);

alter table patients
    owner to postgres;

create index "fki_FK_users"
    on patients (user_id);

create unique index patients_contract_num_uindex
    on patients (contract_num);

create unique index patients_insurance_policy_uindex
    on patients (insurance_policy);

create unique index patients_passport_uindex
    on patients (passport);

create unique index patients_snils_uindex
    on patients (snils);

INSERT INTO public.patients (id, name, user_id, date_of_birth, passport, snils, insurance_policy, contract_num) VALUES (1, 'Твардовский Алексей Николаевич', 8, '1945-08-06', 4567891236, 1239874565, 4566789912314564, 10103);
INSERT INTO public.patients (id, name, user_id, date_of_birth, passport, snils, insurance_policy, contract_num) VALUES (2, 'Беседин Николай Александрович', 9, '1975-04-12', 6549873211, 1239856423, 4586621476268669, 20152);
INSERT INTO public.patients (id, name, user_id, date_of_birth, passport, snils, insurance_policy, contract_num) VALUES (3, 'Замушко Татьяна Петровна', 10, '2000-01-16', 1256478963, 1478523546, 4565654489543125, 34568);
INSERT INTO public.patients (id, name, user_id, date_of_birth, passport, snils, insurance_policy, contract_num) VALUES (4, 'Клейменова Анна Евгеньевна', 11, '1988-04-09', 4548113215, 7894556546, 4645454545544568, 41235);
INSERT INTO public.patients (id, name, user_id, date_of_birth, passport, snils, insurance_policy, contract_num) VALUES (5, 'Краснова Анастасия Аркадьевна', 12, '1966-06-03', 4531251412, 4454454512, 6587863635245245, 42236);
INSERT INTO public.patients (id, name, user_id, date_of_birth, passport, snils, insurance_policy, contract_num) VALUES (6, 'Пушков Станислав Алексеевич', 13, '2005-12-09', 4544525244, 7896333332, 9666552542414158, 49533);
INSERT INTO public.patients (id, name, user_id, date_of_birth, passport, snils, insurance_policy, contract_num) VALUES (19, 'Барашкин Степан Андреевич
', 30, '2000-01-01', 4578962314, 4578965623, 4578965623562345, 1024);