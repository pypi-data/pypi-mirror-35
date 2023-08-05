# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        '{{last_name}} {{company_suffix}}',
        '{{last_name}}-{{last_name}} {{company_suffix}}',
        '{{last_name}}, {{last_name}} e {{last_name}} {{company_suffix}}'
    )

    catch_phrase_words = (
        ('Abilità',
         'Access',
         'Adattatore',
         'Algoritmo',
         'Alleanza',
         'Analizzatore',
         'Applicazione',
         'Approccio',
         'Architettura',
         'Archivio',
         'Intelligenza artificiale',
         'Array',
         'Attitudine',
         'Benchmark',
         'Capacità',
         'Sfida',
         'Circuito',
         'Collaborazione',
         'Complessità',
         'Concetto',
         'Conglomerato',
         'Contingenza',
         'Core',
         'Database',
         'Data-warehouse',
         'Definizione',
         'Emulazione',
         'Codifica',
         'Criptazione',
         'Firmware',
         'Flessibilità',
         'Previsione',
         'Frame',
         'framework',
         'Funzione',
         'Funzionalità',
         'Interfaccia grafica',
         'Hardware',
         'Help-desk',
         'Gerarchia',
         'Hub',
         'Implementazione',
         'Infrastruttura',
         'Iniziativa',
         'Installazione',
         'Set di istruzioni',
         'Interfaccia',
         'Soluzione internet',
         'Intranet',
         'Conoscenza base',
         'Matrici',
         'Matrice',
         'Metodologia',
         'Middleware',
         'Migrazione',
         'Modello',
         'Moderazione',
         'Monitoraggio',
         'Moratoria',
         'Rete',
         'Architettura aperta',
         'Sistema aperto',
         'Orchestrazione',
         'Paradigma',
         'Parallelismo',
         'Policy',
         'Portale',
         'Struttura di prezzo',
         'Prodotto',
         'Produttività',
         'Progetto',
         'Proiezione',
         'Protocollo',
         'Servizio clienti',
         'Software',
         'Soluzione',
         'Standardizzazione',
         'Strategia',
         'Struttura',
         'Successo',
         'Sovrastruttura',
         'Supporto',
         'Sinergia',
         'Task-force',
         'Finestra temporale',
         'Strumenti',
         'Utilizzazione',
         'Sito web',
         'Forza lavoro'),
        ('adattiva',
         'avanzata',
         'migliorata',
         'assimilata',
         'automatizzata',
         'bilanciata',
         'centralizzata',
         'compatibile',
         'configurabile',
         'cross-platform',
         'decentralizzata',
         'digitalizzata',
         'distribuita',
         'piccola',
         'ergonomica',
         'esclusiva',
         'espansa',
         'estesa',
         'configurabile',
         'fondamentale',
         'orizzontale',
         'implementata',
         'innovativa',
         'integrata',
         'intuitiva',
         'inversa',
         'gestita',
         'obbligatoria',
         'monitorata',
         'multi-canale',
         'multi-laterale',
         'open-source',
         'operativa',
         'ottimizzata',
         'organica',
         'persistente',
         'polarizzata',
         'proattiva',
         'programmabile',
         'progressiva',
         'reattiva',
         'riallineata',
         'ricontestualizzata',
         'ridotta',
         'robusta',
         'sicura',
         'condivisibile',
         'stand-alone',
         'switchabile',
         'sincronizzata',
         'sinergica',
         'totale',
         'universale',
         'user-friendly',
         'versatile',
         'virtuale',
         'visionaria'),
        ('24 ore',
         '24/7',
         'terza generazione',
         'quarta generazione',
         'quinta generazione',
         'sesta generazione',
         'asimmetrica',
         'asincrona',
         'background',
         'bi-direzionale',
         'biforcata',
         'bottom-line',
         'coerente',
         'coesiva',
         'composita',
         'sensibile al contesto',
         'basta sul contesto',
         'basata sul contenuto',
         'dedicata',
         'didattica',
         'direzionale',
         'discreta',
         'dinamica',
         'eco-centrica',
         'esecutiva',
         'esplicita',
         'full-range',
         'globale',
         'euristica',
         'alto livello',
         'olistica',
         'omogenea',
         'ibrida',
         'impattante',
         'incrementale',
         'intangibile',
         'interattiva',
         'intermediaria',
         'locale',
         'logistica',
         'massimizzata',
         'metodica',
         'mission-critical',
         'mobile',
         'modulare',
         'motivazionale',
         'multimedia',
         'multi-tasking',
         'nazionale',
         'neutrale',
         'nextgeneration',
         'non-volatile',
         'object-oriented',
         'ottima',
         'ottimizzante',
         'radicale',
         'real-time',
         'reciproca',
         'regionale',
         'responsiva',
         'scalabile',
         'secondaria',
         'stabile',
         'statica',
         'sistematica',
         'sistemica',
         'tangibile',
         'terziaria',
         'uniforme',
         'valore aggiunto'))

    bsWords = (
        ('partnerships',
         'comunità',
         'ROI',
         'soluzioni',
         'e-services',
         'nicchie',
         'tecnologie',
         'contenuti',
         'supply-chains',
         'convergenze',
         'relazioni',
         'architetture',
         'interfacce',
         'mercati',
         'e-commerce',
         'sistemi',
         'modelli',
         'schemi',
         'reti',
         'applicazioni',
         'metriche',
         'e-business',
         'funzionalità',
         'esperienze',
         'webservices',
         'metodologie'),
        ('implementate',
         'utilizzo',
         'integrate',
         'ottimali',
         'evolutive',
         'abilitate',
         'reinventate',
         'aggregate',
         'migliorate',
         'incentivate',
         'monetizzate',
         'sinergizzate',
         'strategiche',
         'deploy',
         'marchi',
         'accrescitive',
         'target',
         'sintetizzate',
         'spedizioni',
         'massimizzate',
         'innovazione',
         'guida',
         'estensioni',
         'generate',
         'exploit',
         'transizionali',
         'matrici',
         'ricontestualizzate'),
        ('valore aggiunto',
         'verticalizzate',
         'proattive',
         'forti',
         'rivoluzionari',
         'scalabili',
         'innovativi',
         'intuitivi',
         'strategici',
         'e-business',
         'mission-critical',
         '24/7',
         'globali',
         'B2B',
         'B2C',
         'granulari',
         'virtuali',
         'virali',
         'dinamiche',
         'magnetiche',
         'web',
         'interattive',
         'sexy',
         'back-end',
         'real-time',
         'efficienti',
         'front-end',
         'distributivi',
         'estensibili',
         'mondiali',
         'open-source',
         'cross-platform',
         'sinergiche',
         'out-of-the-box',
         'enterprise',
         'integrate',
         'di impatto',
         'wireless',
         'trasparenti',
         'next-generation',
         'cutting-edge',
         'visionari',
         'plug-and-play',
         'collaborative',
         'olistiche',
         'ricche'))

    company_suffixes = ('SPA', 'e figli', 'Group', 's.r.l.')

    def catch_phrase(self):
        """
        :example 'Robust full-range hub'
        """
        result = []
        for word_list in self.catch_phrase_words:
            result.append(self.random_element(word_list))

        return " ".join(result)

    def bs(self):
        """
        :example 'integrate extensible convergence'
        """
        result = []
        for word_list in self.bsWords:
            result.append(self.random_element(word_list))

        return " ".join(result)
