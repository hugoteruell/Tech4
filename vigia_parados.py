#!/usr/bin/env python3
"""Rotina vigia-parados — implementacao executavel da Regra 1 de regras.md.

Cumpre a secao "Seguranca e tratamento de falhas": para com FONTE INDISPONIVEL,
nunca estima, conta lidos/considerados/ignorados e isola registro invalido.

Uso:  python3 vigia_parados.py [--fonte CAMINHO] [--ref AAAA-MM-DD]
"""
import argparse, csv, datetime, os, sys

LIMIAR_SUSPEITA = 0.20


def carregar(caminho):
    """Devolve as linhas ou encerra com FONTE INDISPONIVEL."""
    if not os.path.exists(caminho):
        sys.exit(f"FONTE INDISPONÍVEL · {caminho} · arquivo não encontrado")
    if not os.access(caminho, os.R_OK):
        sys.exit(f"FONTE INDISPONÍVEL · {caminho} · sem permissão de leitura")
    if os.path.getsize(caminho) == 0:
        sys.exit(f"FONTE INDISPONÍVEL · {caminho} · arquivo vazio")
    with open(caminho, newline="", encoding="utf-8") as fh:
        leitor = csv.DictReader(fh)
        if not leitor.fieldnames or "id" not in leitor.fieldnames:
            sys.exit(f"FONTE INDISPONÍVEL · {caminho} · cabeçalho ausente ou inválido")
        linhas = list(leitor)
    if not linhas:
        sys.exit(f"FONTE INDISPONÍVEL · {caminho} · arquivo sem registros")
    return linhas


def validar(reg, ref):
    """Devolve (dias, None) se valido, ou (None, motivo) se invalido."""
    ident = reg.get("id") or "(sem id)"
    if not (reg.get("status") or "").strip():
        return None, f"{ident} (status vazio)"
    bruto = (reg.get("dias_parado") or "").strip()
    if not bruto:
        return None, f"{ident} (dias_parado vazio)"
    try:
        dias = int(bruto)
    except ValueError:
        return None, f'{ident} (dias_parado não numérico: "{bruto}")'
    if dias < 0:
        return None, f"{ident} (dias_parado negativo: {dias})"
    origem = (reg.get("data_origem") or "").strip()
    try:
        datetime.date.fromisoformat(origem)
    except ValueError:
        return None, f'{ident} (data_origem fora do formato AAAA-MM-DD: "{origem}")'
    return dias, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonte", default="dados/amostra.csv")
    ap.add_argument("--ref", default=datetime.date.today().isoformat())
    args = ap.parse_args()

    linhas = carregar(args.fonte)
    considerados, ignorados, disparam, maior = 0, [], [], 0

    for reg in linhas:
        dias, motivo = validar(reg, args.ref)
        if motivo:
            ignorados.append(motivo)
            continue
        if reg["prioridade"] != "Alta":
            continue
        considerados += 1
        maior = max(maior, dias)
        if reg["status"] != "concluido" and dias > 7:
            disparam.append((reg, dias))

    contagem = (f"lidos: {len(linhas)} · considerados: {considerados} · "
                f"ignorados: {len(ignorados)}")

    if ignorados and len(ignorados) / len(linhas) > LIMIAR_SUSPEITA:
        print(f"FONTE SUSPEITA — {len(ignorados)} de {len(linhas)} registros ignorados")
        print("IGNORADOS: " + " · ".join(ignorados))
        sys.exit(2)

    agora = datetime.datetime.now().strftime("%H:%M")
    if disparam:
        print(f"{args.ref} {agora} · Regra 1 · DISPAROU · {contagem}")
        for reg, dias in disparam:
            print(f"  {reg['id']} · {reg['item']} · {dias} dias · {reg['evidencia']}")
    else:
        print(f"{args.ref} {agora} · Regra 1 · nada a reportar · {contagem}, "
              f"máximo de dias parados: {maior}")

    if ignorados:
        print("IGNORADOS: " + " · ".join(ignorados))


if __name__ == "__main__":
    main()
