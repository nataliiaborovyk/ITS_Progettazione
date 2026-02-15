

create table categoria (
	nome stringa primary key,
	super stringa,
	check (nome <> super)
);

alter table add foreign key (super)
		references categoria(nome);

-- WITH RECURSIVE


create table utente (
	username stringa primary key,
	registrazione timestamp
);

create table privato (
	utente stringa primary key,
	foreign key (utente)
		references utente(username)
);

create table venditoreprof (
	utente stringa primary key,
	vetrina URL not null,
	unique(vetrina),
	foreign key (utente)
		references utente(username)
);

-- [V.Utente.compl] e [V.Utente.disj] non ancora implementati


create table postoggetto (
	id serial primary key,
	pubblica stringa not null,
	descrizione stringa not null,
	pubblicazione timestamp not null,
	ha_feedback boolean not null,
	voto Voto,
	commento stringa,
	istante_feedback timestamp,
	categoria stringa not null,
	-- vincoli di ennupla per modellare [V.PostOggetto.feedback]
	check(
		(ha_feedback = true)
		=
		(voto is not null and istante_feedback is not null)
		),
	-- se c'è il commento allora ha_feedback è true
	check (commento is null OR ha_feedback=true),
	foreign key (categoria)
		references categoria(nome),


	-- v.incl. (id) occorre in met_post(postoggetto)

	foreign key (pubblica)
		references utente(username)
);


create table postoggettonuovo (
	postoggetto integer primary key,
	pubblica_nuovo stringa not null,
	anni_garanzia IntGE2 not null,

	foreign key (pubblica_nuovo) 
		references venditoreprof(utente),


	# implementa [V.PostOggettoNuovo.pubblica.isa]
	foreign key (postoggetto, pubblica_nuovo)
		references postoggetto(id, pubblica),
);

create table metodopagamento (
	nome stringa primary key
);

create table met_post (
	postoggetto integer not null,
	metodo stringa not null,
	primary key (postoggetto, metodo),
	foreign key (postoggetto)
		references postoggetto(id),
	foreign key (metodo)
		references metodopagamento(nome)
);











