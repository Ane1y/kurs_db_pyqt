create table medical_records
(
    id           serial  not null
        constraint "Medical_records_pkey"
            primary key,
    patient_id   integer not null
        constraint "FK_patients"
            references patients,
    physician_id integer not null
        constraint "FK_physician"
            references physicians,
    date         date    not null,
    diagnosis    text    not null,
    service_id   integer not null
        constraint "FK_services"
            references services
);

alter table medical_records
    owner to postgres;

create index "fki_FK_patients"
    on medical_records (patient_id);

create index "fki_FK_physician"
    on medical_records (physician_id);

create index "fki_FK_services"
    on medical_records (service_id);

INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (1, 1, 1, '2020-10-20', 'Диагноз: хронический панколит, пить ношпу 3 раза в день', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (3, 1, 2, '2020-10-20', 'Диагноз: Хронический ардуизм, пить горячий чай с календулой 5 раз в день и панкреатин 2т 2р  день', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (4, 2, 2, '2020-10-21', 'Диагноз: Симулятивный хрономитоз. Показания: пить Эссенциале-форте Н, суспензия, 5 раз в день.', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (5, 3, 3, '2020-10-20', 'Подозрение на зоб. Назначено УЗИ щитовидной железы. 20-10-2020', 3);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (6, 3, 3, '2020-10-20', 'Щитовидная железа увеличена, пить йодомарин раз в сутки перед едой.', 8);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (7, 4, 4, '2020-10-20', 'Аритмия повышена, наблюдается тахикардия. Пить Омегу-3 3 раза в день. Назначено дополнительное обследование у гинеколога.', 4);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (8, 1, 5, '2020-10-20', 'Слабый иммунитет, назначены дополнительные анализы: на общий иммуноглобулин Е, специфический иммуноглобулин E, G (антитела)', 5);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (9, 2, 6, '2020-10-20', 'Проведена паллиативная операция на сердце, в течение 3 дней оставаться в палате, принимать Милдронат, Панангин 5 мг внутривенно. Назначен прием у хирируга 26-10-2019', 6);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (10, 6, 3, '2020-10-20', 'Диагностирован вирус Эпштейна-Барра, назначен анализ на гетерофильные антитела, повторное обследование назначено на 25-10-2020', 3);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (11, 6, 4, '2020-10-21', 'Подозрение на отечность левого поджелудочка, назначен анализ на определение показателей липидного (жирового) обмена-холестерин (ХС)', 6);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (12, 3, 5, '2020-10-21', 'Диагнозирован синдром Гудпасчера, анти-БМК антитела отсутствуют, и имеются симптомы гломерулонефрита показана биопсия почки для подтверждения диагноза', 5);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (13, 2, 5, '2020-10-21', 'Диагнозировано злокачествоенное образование желудка, назначено анализ на суммарные иммуноглобулины A (IgA) в сыворотке', 5);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (46, 1, 1, '2020-12-11', 'Запись доабвлена через GUI', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (14, 2, 1, '2020-10-21', 'Наблюдается спазмация в области сердца, применять корвалол по 2 таблетки 2 раза в день и нимесил раз в неделю.', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (47, 1, 1, '2020-12-11', 'Запись доабвлена через GUI', 6);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (48, 1, 1, '2020-12-11', 'Запись доабвлена через GUI 3', 3);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (49, 3, 1, '2020-12-12', 'Добавлено через гуи', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (51, 4, 6, '2020-12-15', 'Диагноз: хронический пофрантаизм, принимать 3 капли аспирина 10 раз в день внутрикожно', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (15, 1, 1, '2020-06-12', 'еще одно обновление диагноза', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (36, 1, 1, '2020-11-16', 'специально для отчета', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (37, 1, 1, '2020-11-16', 'специально для отчета', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (38, 1, 2, '2020-11-16', 'специально для отчета 2 врача', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (41, 1, 2, '2020-11-16', 'специально для отчета 2 врача', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (42, 1, 3, '2020-11-16', 'специально для отчета 2 врача', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (50, 1, 2, '2020-12-15', 'Новейший диагноз', 1);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (18, 1, 5, '2020-06-20', 'новый диагноз 1', 3);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (52, 2, 3, '2020-12-16', 'Изменяю последний дриагноз', 2);
INSERT INTO public.medical_records (id, patient_id, physician_id, date, diagnosis, service_id) VALUES (53, 3, 1, '2020-12-16', 'Диагноз новый', 1);