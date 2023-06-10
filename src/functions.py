import dicts
import sqlite3
import io
import pandas as pd


def to_dataframe(lista_ipytv):
    lista_dict = []

    for i in range(lista_ipytv.length()):
        canal = lista_ipytv.get_channel(i)
        dicionario = canal.attributes
        dicionario["duration"] = canal.duration
        dicionario["name"] = canal.name
        dicionario["url"] = canal.url
        lista_dict.append(dicionario)

    return pd.DataFrame(lista_dict)