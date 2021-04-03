create table authentication_data
(
    id       serial       not null
        constraint "Authentication_data_pkey"
            primary key,
    password varchar(256) not null,
    phone    varchar(11)  not null
        constraint "Authentication_data_phone_key"
            unique
);

alter table authentication_data
    owner to postgres;

INSERT INTO public.authentication_data (id, password, phone) VALUES (30, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '89657895688');
INSERT INTO public.authentication_data (id, password, phone) VALUES (10, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '84561236985');
INSERT INTO public.authentication_data (id, password, phone) VALUES (11, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '84587561265');
INSERT INTO public.authentication_data (id, password, phone) VALUES (4, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '8789445612');
INSERT INTO public.authentication_data (id, password, phone) VALUES (5, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '8894561234');
INSERT INTO public.authentication_data (id, password, phone) VALUES (6, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '88964561233');
INSERT INTO public.authentication_data (id, password, phone) VALUES (7, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '87458965624');
INSERT INTO public.authentication_data (id, password, phone) VALUES (1, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '89657996686');
INSERT INTO public.authentication_data (id, password, phone) VALUES (2, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '88001681039');
INSERT INTO public.authentication_data (id, password, phone) VALUES (3, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '88455631235');
INSERT INTO public.authentication_data (id, password, phone) VALUES (23, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '84567899632');
INSERT INTO public.authentication_data (id, password, phone) VALUES (12, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '85697894563');
INSERT INTO public.authentication_data (id, password, phone) VALUES (13, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '87454569865');
INSERT INTO public.authentication_data (id, password, phone) VALUES (8, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '87458965612');
INSERT INTO public.authentication_data (id, password, phone) VALUES (9, 'gAAAAABf2fm8vB7OUYkRHv-QYChiB-1Qg3EHpSGA7J6joZPMnZiv8o6q4K6Duy9e-w6pcOvEeLJs3B4mgCW3IXCkznZsKdk1mA==', '89657856527');