--
-- PostgreSQL database dump
--

-- Dumped from database version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.6 (Ubuntu 12.6-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: app_administradores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_administradores (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    correo character varying(254) NOT NULL,
    clave character varying(50) NOT NULL
);


ALTER TABLE public.app_administradores OWNER TO postgres;

--
-- Name: app_administradores_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_administradores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_administradores_id_seq OWNER TO postgres;

--
-- Name: app_administradores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_administradores_id_seq OWNED BY public.app_administradores.id;


--
-- Name: app_examenes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_examenes (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    valor character varying(50) NOT NULL,
    fecha date NOT NULL,
    observaciones character varying(250) NOT NULL,
    paciente_id integer NOT NULL
);


ALTER TABLE public.app_examenes OWNER TO postgres;

--
-- Name: app_examenes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_examenes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_examenes_id_seq OWNER TO postgres;

--
-- Name: app_examenes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_examenes_id_seq OWNED BY public.app_examenes.id;


--
-- Name: app_pacientes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_pacientes (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    correo character varying(200) NOT NULL,
    clave character varying(50) NOT NULL,
    rut character varying(10) NOT NULL,
    edad integer NOT NULL,
    fecha date NOT NULL,
    direccion character varying(150) NOT NULL,
    ocupacion character varying(150) NOT NULL,
    telefono character varying(20) NOT NULL,
    foto character varying(65535) NOT NULL,
    resumen text NOT NULL,
    educacion text NOT NULL,
    historial text NOT NULL
);


ALTER TABLE public.app_pacientes OWNER TO postgres;

--
-- Name: app_pacientes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_pacientes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_pacientes_id_seq OWNER TO postgres;

--
-- Name: app_pacientes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_pacientes_id_seq OWNED BY public.app_pacientes.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: app_administradores id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_administradores ALTER COLUMN id SET DEFAULT nextval('public.app_administradores_id_seq'::regclass);


--
-- Name: app_examenes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_examenes ALTER COLUMN id SET DEFAULT nextval('public.app_examenes_id_seq'::regclass);


--
-- Name: app_pacientes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_pacientes ALTER COLUMN id SET DEFAULT nextval('public.app_pacientes_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: app_administradores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_administradores (id, nombre, correo, clave) FROM stdin;
\.


--
-- Data for Name: app_examenes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_examenes (id, nombre, valor, fecha, observaciones, paciente_id) FROM stdin;
32	glucosa	150	1919-01-01	edewd ewde wdew dwe dwe dwe	2
33	glucosa	150	1947-01-01	dewdewdew	2
34	glucosa	150	1900-01-01	dewdwedewdw edew d wed	2
40	hemograma	450	1957-04-01	sjwo ssjhwoqjs owqjs owq	7
35	hemograma	150	1950-01-01	e wdfewd ewd ewd ew dew	7
41	orina	160	1976-01-01	sdwqs wqswqswqs wq swq swq	2
42	orina	350	2001-01-01	swqsjwq swqjs owqj spojwq sojwqp	6
29	glucosa	150	1973-01-01	sdiwoqhs oiwhqso hqwishwq  showq	3
\.


--
-- Data for Name: app_pacientes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_pacientes (id, nombre, correo, clave, rut, edad, fecha, direccion, ocupacion, telefono, foto, resumen, educacion, historial) FROM stdin;
7	Luis Jaraquemada	luis.jaraquemada@team.awakelab.cl		1000000-5	56	2020-12-05	Santiago #45450	redes y python master	9405653554	http://yofui.com/CLFotosFiles/Evento00000866/YoFui0000000400844604-6.JPG	paciente ............	allala lalala lalalla\r\nlalala laalal alala a	lalal a\r\nlallala \r\nllla \r\nlalalalala
5	Jose guerra	jose@hotmail.com	123456	15896752-2	100	2020-12-05	las carmelitas valpo	Telecommunication Specialist	9405653554	https://media-exp1.licdn.com/dms/image/C5603AQH2_0aQAqfJPA/profile-displayphoto-shrink_200_200/0/1517395160883?e=1619654400&v=beta&t=Uy_blZEEfmdETNKayjOjnP_VZ9stM4L9C-XE5Ngd1Yw	lalal allal alaala prueba prueba	la vida	orina completa \r\norina
6	Gilbert Lagos	gilbert@gmail.com	123456	15896752-2	36	2020-12-05	las carmelitas valpo	redes y python master	5698406646	https://media-exp1.licdn.com/dms/image/C5603AQFUjuNCjWy-wQ/profile-displayphoto-shrink_200_200/0/1517629716467?e=1619654400&v=beta&t=luNfnvnHsqiw-iobq2kGJhKpof6qRYcnlGgPUiJ1mJE	la lala ala alaaalal	la vida 2	dseod dejojd e dewjd wpejd pw
2	john bruna	joncito@gmail.com		20380930-2	36	2020-12-05	las cabras #3500	Telecommunication Specialist	9405653554	https://media-exp1.licdn.com/dms/image/C5603AQEjGwKBiXp4Cg/profile-displayphoto-shrink_200_200/0/1607380799059?e=1619654400&v=beta&t=o6OpLNmhSvNVQhWAmccfJFOo3CebcjHF-e6UfkA1AAU	sdewi dewihd ewiohd iwehd ohewoid ewihdew hdihew iohd eowihdo ewhdiehw odhewdh iweohd ohewoihdihwe doihewiohd iweoh doihew oidhoeiwhd owehd ohweoihdeow ihdowe	dwehdoh wehdiohew odh ewodh eowhd eiwohdewiohd ewhdoi ewhoidh eoiwhd ew dihewid hiweo d ewihd weoh dihewoi dhweoihd ew	dihwedo ewhdiweo hdoihew oidhew hdowehdihewihd ohewo idhewodhewi dowehd ohewoi doiwedh oeiwhd oihewo dhiweo hdihew oidh oiweh doe
3	Esteban Yañex	esteban@gmail.com		30460790-2	100	2020-12-05	las carmelitas valpo	Telecommunication Specialist	5698406646	https://media-exp1.licdn.com/dms/image/C4E35AQFB2Mc2spRmOg/profile-framedphoto-shrink_200_200/0/1613672835831?e=1614304800&v=beta&t=etP8OnZs2MQ_iqRXyngxbn33T95woZzULK_x2nxkuJk	dew ewdhiweo dihew dhiweh odhoew hdih ewiohd oew\r\ndjewojd ewdjpoewj dpojew\r\ndewpdj ewpdew	dewojd ewdjhwe d\r\newjd pewj d\r\newjdpjew pojdpoejwpodj epwojd ew\r\njewjd pew	dewhd oehwidoh oewihd oehwoid eiwohd iweoh dew
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	app	0001_initial	2021-02-24 20:05:35.626838-03
2	app	0002_auto_20210225_0115	2021-02-24 22:15:15.404353-03
\.


--
-- Name: app_administradores_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_administradores_id_seq', 1, false);


--
-- Name: app_examenes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_examenes_id_seq', 42, true);


--
-- Name: app_pacientes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_pacientes_id_seq', 7, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 2, true);


--
-- Name: app_administradores app_administradores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_administradores
    ADD CONSTRAINT app_administradores_pkey PRIMARY KEY (id);


--
-- Name: app_examenes app_examenes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_examenes
    ADD CONSTRAINT app_examenes_pkey PRIMARY KEY (id);


--
-- Name: app_pacientes app_pacientes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_pacientes
    ADD CONSTRAINT app_pacientes_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: app_examenes_paciente_id_4d555407; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_examenes_paciente_id_4d555407 ON public.app_examenes USING btree (paciente_id);


--
-- Name: app_examenes app_examenes_paciente_id_4d555407_fk_app_pacientes_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_examenes
    ADD CONSTRAINT app_examenes_paciente_id_4d555407_fk_app_pacientes_id FOREIGN KEY (paciente_id) REFERENCES public.app_pacientes(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

