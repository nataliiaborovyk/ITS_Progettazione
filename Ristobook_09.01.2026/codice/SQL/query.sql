-- num_prenot_accettate(d_iniz:DataOra, d_fine:DataOra): Intero >=0

select count(*)
from prenotazione p
where p.stato = 'Accettata'
    and p.data_ora_prenotata between (d_iniz, d_fine)
    

-- num_prenot_rifiutate(d_iniz:DataOra, d_fine:DataOra): Intero >=0

select count(*)
from prenotazione p
where p.stato = 'Rifiutata'
    and p.data_ora_prenotata between (d_iniz, d_fine)




-- use-state
-- args.get()

-- 999.1. 	I ristoratori possono iscriversi a RistoBook per registrare i propri ristoranti e gestire le loro prenotazioni 

-- 999.2. I ristoranti possono scegliere le tipologie di cucina da una lista gestita dallo staff di Ristobook

-- 999.4.	Il personale incaricato dei rispettivi ristoranti, deve poter accedere a Ristobook tramite una interfaccia dedicata

-- 999.5. I clienti possono iscriversi a Ristobook ed effettuare prenotazioni presso i ristoranti iscritti   POST cliente

-- 999.6. 	Il sistema deve permettere ai ristoratori di gestire lo stato delle prenotazioni

-- 999.7.  I ristoratori possono chiudere le prenotazioni per un periodo (date scelte o giorni della settimana) e fascia oraria 



-- num_prenotazioni_ristorante_nel_periodo(
-- ris: Ristorante,  
-- d_iniz : DataOra, 
-- d_fine : DataOra
-- ) : Intero>=0

select count(*)
from ristorante r, prenotazione p
where p.ristorante = r.id
    and r.id = ris.id
    and p.data_ora_prenotata between (d_iniz, d_fine)

select count(*)
from ristorante r
    join prenotatazione p on r.id = p.ristorante
where r.id = ris.id
    and p.data_ora_prenotata between (d_iniz, d_fine)



-- num_prenot_accettate_ristorante_nel_periodo(
-- ris: Ristorante, 
-- d_iniz : DataOra, 
-- d_fine : DataOra
-- ) : Intero>=0

select count(*)
from prenotazione p 
where p.ristorante = ris.id
    and p.stato = 'Accettata'
    and p.data_ora_prenotata between (d_iniz, d_fine)

-- num_prenot_rifiutate_ristorante_nel_periodo(
-- r: Ristorante, 
-- d_iniz : DataOra, 
-- d_fine : DataOra
-- ) : Intero>=0

select count(*)
from prenotazione p 
where p.ristorante = ris.id
    and p.stato = 'Rifiutata'
    and p.data_ora_prenotata between (d_iniz, d_fine)


-- num_prenotazioni_effetuate_dal_cliente_nel_periodo(
-- cl: Cliente, 
-- d_iniz : DataOra, 
-- d_fine : DataOra
-- ) : Intero >=0

select count(*)
from prenotazione p
where p.cliente = cl.email
    and p.data_ora_prenotata between (d_iniz, d_fine)

-- num_prenotazioni_effetuate_da_cliente_nel_periodo_nel_ristorante(
-- cl: Cliente, 
-- ris: Ristorante, 
-- d_iniz : DataOra, 
-- d_fine : DataOra
-- ) : Intero >=0

select count(*)
from prenotazione p 
where p.cliente = cl.email
    and p.ristorante = ris.id
    and p.data_ora_prenotata between (d_iniz, d_fine)
