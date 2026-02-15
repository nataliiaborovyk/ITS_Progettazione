begin transaction;

create type provenienza as enum('tempo', 'sistema esterno');

create domain stringa as varchar;

create domain intgz as integer check (value > 0);

create domain intgez as integer check (value >= 0);

create domain realgz as numeric check (value > 0);

create domain realgez as numeric check (value >= 0);

create domain cf as char(16) 
    check (value ~ '^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$');

create domain email as varchar(100)
    check (value ~ '^[a-z0-9!#$%&''*+/=?^_`{|}~-]+(\.[a-z0-9!#$%&''*+/=?^_`{|}~-]+)*@([a-z0-9]([a-z0-9-]*[a-z0-9])?\.)+[a-z0-9]([a-z0-9-]*[a-z0-9])?$');

create domain sconto as numeric
    check (value BETWEEN 0 and 1);

create domain stringa_not_null as 
    varchar(100) check(value is not null);

create domain cap_not_null as
    char(5) check (value is not null and value ~ '^[0-9]{5}$');
 
create type indirizzo as (
    via     stringa_not_null,
    civico  stringa_not_null,
    cap      cap_not_null
);

create domain partitaiva as char(11)
    check (value ~ '^[0-9]{11}$'); 



create table nazione (
    nome stringa primary key
);

create table regione (
    id serial primary key,
    nome stringa not null,
    nazione stringa not null,  -- accorpa naz_reg
    unique(nome, nazione),    
    foreign key (nazione)
        references nazione(nome)   
);

create table citta (
    id serial primary key,
    nome stringa not null,
    regione integer not null,   -- accorpa reg_cit
    unique(nome, regione),
    foreign key (regione)
        references regione(id)    
);

create table persona (
    cf cf primary key,
    nome stringa not null,
    cognome stringa not null,
    data_nascita date not null
);

create table utente (
    persona cf primary key,
    email email not null,
    indirizzo indirizzo not null,
    citta integer not null,  -- accorpa cit_ut
    foreign key (persona)
        references persona(cf),
    foreign key (citta) 
        references citta(id)
);

create table cliente (
    id serial primary key
);

create table impresa (
    cliente integer primary key,
    partita_iva partitaiva not null,
    unique (partita_iva),
    ragione_sociale stringa not null,
    foreign key (cliente)
        references cliente(id)
);

create table personafisica (
    cliente integer primary key,
    partita_iva partitaiva,
    unique (partita_iva),
    persona cf not null,    --  accorpa anagrafica
    unique (persona),       -- non possono due personefisiche diverse riferirsi alla stessa persona
    foreign key (cliente)
        references cliente(id),
    foreign key (persona)
        references persona(cf)
);

create table unitamisura (
    nome stringa primary key
);

create table tipoabbonamento (
    nome stringa primary key,
    prezzo realgez not null,
    durata intgz not null,
    max_num_utenti intgz not null,
    inizio_iscrizione timestamp not null,
    fine_iscrizione timestamp not null,
    check (fine_iscrizione > inizio_iscrizione),
    unitamisura stringa not null,       -- accorpa tipab_um
    foreign key (unitamisura)
        references unitamisura(nome)
);

create table abbonamento (
    id serial primary key,
    inizio timestamp not null,
    tipoabbonamento stringa not null,  -- accorpa ab_tip
    cliente integer not null,          -- accorpa stipula
    foreign key (tipoabbonamento)
        references tipoabbonamento(nome),
    foreign key (cliente)
        references cliente(id)
);

create table postazione (
    codice intgz primary key
);

create table Storico (
    id serial primary key,
    inizio timestamp not null,
    fine timestamp,  
    check (fine is null or inizio < fine),
    utente cf not null,             -- accorpa ut_st
    abbonamento integer not null,   -- accorpa ab_st
    postazione intgz not null,      -- accorpa post_st
    foreign key (utente)
        references utente(persona),
    foreign key (abbonamento)
        references abbonamento(id),
    foreign key (postazione)
        references postazione(codice)
);

create table tiposervizio (
    nome stringa primary key,
    quantita_da provenienza not null,
    unitamisura stringa not null,
    foreign key (unitamisura)
        references unitamisura(nome)
);

create table servizio (
    id serial primary key,
    descrizione stringa not null,
    prezzo realgez not null,
    prenotabile boolean not null,
    tiposervizio stringa not null,   -- accorpa serv_tip
    foreign key (tiposervizio)
        references tiposervizio(nome)
);

create table tipab_serv (
    servizio integer not null,
    tipoabbonamento stringa not null,
    primary key (servizio, tipoabbonamento),
    soglia_mensile_gratis intgez not null,
    sconto sconto not null,
    foreign key (servizio)
        references servizio(id),
    foreign key (tipoabbonamento)
        references tipoabbonamento(nome)
);

create table accessospazio (
    id serial primary key,
    entrata timestamp not null,
    uscita timestamp,
    utente cf not null,           -- accorpa ut_asp
    storico integer not null, -- accorpa accesso_con
    check (uscita is null or uscita > entrata),
    foreign key (utente)
        references utente(persona),
    foreign key (storico)
        references storico(id)
);

create table usoservizio (
    id serial primary key,
    inizio timestamp not null,
    fine timestamp,
    quantita intgz,
    check ( 
        (fine is null and quantita is null)
        or 
        (fine is not null and quantita is not null and fine > inizio)
    ),
    accessospazio integer not null,  -- accorpa asp_serv
    servizio integer not null,       -- accorpa aserv_serv
    foreign key (accessospazio)
        references accessospazio(id),
    foreign key (servizio)
        references servizio(id)
);

create table prenotazione (
    id serial primary key,
    istante_prenotazione timestamp not null,
    inizio timestamp not null,
    fine timestamp not null,
    check (fine > inizio),
    cancellata boolean not null,
    istante_canc timestamp,
    check (
        (cancellata = false and istante_canc is null)
        or
        (cancellata = true and istante_canc is not null)
    ),
    utente cf not null,         -- accorpa ut_pren
    servizio integer not null,  -- accorpa pren_serv
    foreign key (utente) 
        references utente(persona),
    foreign key (servizio)
        references servizio(id)
);


commit;