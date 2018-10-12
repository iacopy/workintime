WorkinTime
==========

Ti dice quanti giorni (e ore) di lavoro avresti dovuto fare sulla carta dall'inizio del mese corrente, in modo da sapere se sei in pari oppure stai lavorando meno o più del dovuto.

Esempio output. Supponiamo sia il 12 ottobre 2018 e si lavori 6 ore al giorno:

::

    $ python main.py 6
    Hours per day: 6
    ---------------------------
    2018-10-01	1	6
    2018-10-02	2	12
    2018-10-03	3	18
    2018-10-04	4	24
    2018-10-05	5	30
    2018-10-08	6	36
    2018-10-09	7	42
    2018-10-10	8	48
    2018-10-11	9	54
    2018-10-12	10	60 <
    2018-10-15	11	66
    2018-10-16	12	72
    2018-10-17	13	78
    2018-10-18	14	84
    2018-10-19	15	90
    2018-10-22	16	96
    2018-10-23	17	102
    2018-10-24	18	108
    2018-10-25	19	114
    2018-10-26	20	120
    2018-10-29	21	126
    2018-10-30	22	132
    2018-10-31	23	138
    ---------------------------
    MONTH TOTAL:	23	138
