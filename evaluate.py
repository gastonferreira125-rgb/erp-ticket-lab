"""Evaluate saved model responses; no API calls or external packages required."""
import json
import sys
from pathlib import Path

CATEGORIES = {"Finanzas", "Ventas", "Inventario", "Autorizaciones", "Reportes", "Integraciones", "Compras", "Otros"}
KEYS = {"ticket_id", "categoria", "prioridad", "resumen", "referencia_documento", "datos_faltantes"}

def valid(response):
    return (
        isinstance(response, dict)
        and set(response) == KEYS
        and isinstance(response["ticket_id"], str)
        and isinstance(response["categoria"], str) and response["categoria"] in CATEGORIES
        and isinstance(response["prioridad"], str) and response["prioridad"] in {"Alta", "Media", "Baja"}
        and isinstance(response["resumen"], str) and bool(response["resumen"].strip())
        and (response["referencia_documento"] is None or isinstance(response["referencia_documento"], str))
        and isinstance(response["datos_faltantes"], list)
        and all(isinstance(item, str) for item in response["datos_faltantes"])
    )

def evaluate(tickets, predictions):
    expected_ids = {case["id"] for case in tickets}
    by_id = {}
    duplicates = []
    for row in predictions:
        if not isinstance(row, dict) or not isinstance(row.get("ticket_id"), str):
            continue
        key = row["ticket_id"]
        if key in by_id:
            duplicates.append(key)
        by_id[key] = row
    rows = []
    for case in tickets:
        response = by_id.get(case["id"])
        schema_ok = valid(response) if response is not None else False
        label_ok = schema_ok and all(response[key] == value for key, value in case["expected"].items())
        reference = response.get("referencia_documento") if schema_ok else None
        invented_reference = reference is not None and reference not in case["text"]
        rows.append({"ticket_id": case["id"], "present": response is not None,
                     "schema_valid": schema_ok, "labels_match": label_ok,
                     "invented_reference": invented_reference})
    count = len(tickets)
    return {"total_cases": count, "responses": sum(r["present"] for r in rows),
            "schema_valid": sum(r["schema_valid"] for r in rows),
            "labels_match": sum(r["labels_match"] for r in rows),
            "invented_references": sum(r["invented_reference"] for r in rows),
            "duplicate_ids": duplicates, "unknown_ids": sorted(set(by_id) - expected_ids),
            "note": "Summary accuracy and missing-data usefulness require human review.",
            "cases": rows}

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 evaluate.py responses.json")
    base = Path(__file__).resolve().parent
    tickets = json.loads((base / "tickets.json").read_text(encoding="utf-8"))
    predictions = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if not isinstance(predictions, list):
        raise SystemExit("responses.json must contain a JSON array.")
    print(json.dumps(evaluate(tickets, predictions), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

