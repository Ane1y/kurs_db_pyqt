create table medical_record_audit
(
    id            serial    not null
        constraint "Mr_audit_pkey"
            primary key,
    time          timestamp not null,
    mr_id         integer   not null
        constraint medical_record_audit_mr_id_fkey
            references medical_records,
    old_diagnosis text      not null
);

alter table medical_record_audit
    owner to postgres;

INSERT INTO public.medical_record_audit (id, time, mr_id, old_diagnosis) VALUES (1, '2020-11-18 11:11:35.057002', 18, 'Старый диагноз');
INSERT INTO public.medical_record_audit (id, time, mr_id, old_diagnosis) VALUES (2, '2020-12-16 02:28:50.654858', 50, 'Демонстрирую БД сане');
INSERT INTO public.medical_record_audit (id, time, mr_id, old_diagnosis) VALUES (3, '2020-12-16 02:30:09.327357', 50, 'Новый диагноз');
INSERT INTO public.medical_record_audit (id, time, mr_id, old_diagnosis) VALUES (4, '2020-12-16 02:30:23.098145', 50, 'Новейший диагноз');
INSERT INTO public.medical_record_audit (id, time, mr_id, old_diagnosis) VALUES (5, '2020-12-16 15:51:49.155808', 52, 'Последний тест');
INSERT INTO public.medical_record_audit (id, time, mr_id, old_diagnosis) VALUES (6, '2020-12-16 17:35:48.375671', 53, 'Диагноз дя демонстрации КП');