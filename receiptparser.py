import json
import re
from pathlib import Path

MONEY = r"\d[\d \u00a0]*,\d{2}"


def to_float(s: str) -> float:
    """'1 200,00' -> 1200.0"""
    return float(re.sub(r"[ \u00a0]", "", s).replace(",", "."))


def read_receipt(path: str = "raw.txt") -> str:
    text = Path(path).read_text(encoding="utf-8")
    return text.replace("\r\n", "\n")


def extract_items(text: str) -> list[dict]:
    """Each item looks like:
        <n>.
        <name>
        <qty> x <unit price>
        <line total>
        Стоимость
        <line total>
    """
    pattern = re.compile(
        rf"^(?P<no>\d+)\.\n"
        rf"(?P<name>.+)\n"
        rf"(?P<qty>\d+,\d{{3}}) x (?P<unit>{MONEY})\n"
        rf"(?P<total>{MONEY})\n"
        rf"Стоимость\n",
        re.MULTILINE,
    )
    items = []
    for m in pattern.finditer(text):
        items.append({
            "no": int(m["no"]),
            "name": re.sub(r"\s+", " ", m["name"]).strip(),
            "quantity": to_float(m["qty"]),
            "unit_price": to_float(m["unit"]),
            "total": to_float(m["total"]),
        })
    return items


def extract_all_prices(text: str) -> list[float]:
    """All monetary amounts on the receipt (unit prices, line totals, grand total...)."""
    return [to_float(p) for p in re.findall(rf"(?<![\d,]){MONEY}(?![\d,])", text)]


def extract_datetime(text: str) -> dict:
    m = re.search(r"Время:\s*(?P<d>\d{2})\.(?P<m>\d{2})\.(?P<y>\d{4})\s+(?P<t>\d{2}:\d{2}:\d{2})", text)
    if not m:
        return {}
    return {"date": f"{m['y']}-{m['m']}-{m['d']}", "time": m["t"]}


def extract_payment(text: str) -> dict:
    """Payment line: '<method>:' directly followed by the paid amount, before 'ИТОГО:'."""
    m = re.search(rf"^(?P<method>[А-Яа-яЁё ]+):\n(?P<amount>{MONEY})\nИТОГО:", text, re.MULTILINE)
    return {"method": m["method"], "amount": to_float(m["amount"])} if m else {}


def extract_total(text: str) -> float | None:
    m = re.search(rf"ИТОГО:\s*\n?({MONEY})", text)
    return to_float(m[1]) if m else None


def extract_meta(text: str) -> dict:
    def grab(pattern):
        m = re.search(pattern, text, re.MULTILINE)
        return m[1].strip() if m else None

    return {
        "company": grab(r"^Филиал (.+)$"),
        "bin": grab(r"^БИН (\d{12})"),
        "cash_register": grab(r"^Касса (\S+)"),
        "shift": grab(r"^Смена (\d+)"),
        "receipt_seq_no": grab(r"Порядковый номер чека №(\d+)"),
        "receipt_no": grab(r"^Чек №(\d+)"),
        "cashier": grab(r"^Кассир (.+)$"),
        "fiscal_sign": grab(r"Фискальный признак:\n(\d+)"),
        "vat_12": to_float(grab(rf"в т\.ч\. НДС 12%:\n({MONEY})")),
        "address": grab(r"^(г\. .+)$"),
        "ofd_inc": grab(r"ИНК ОФД: (\d+)"),
        "kkm_rnm": grab(r"\(РНМ\): (\d+)"),
        "znm": grab(r"ЗНМ: (\w+)"),
    }


def parse_receipt(path: str = "raw.txt") -> dict:
    text = read_receipt(path)
    items = extract_items(text)
    calculated = round(sum(i["total"] for i in items), 2)
    stated = extract_total(text)
    return {
        **extract_meta(text),
        "datetime": extract_datetime(text),
        "payment": extract_payment(text),
        "items": items,
        "product_names": [i["name"] for i in items],
        "all_prices": extract_all_prices(text),
        "calculated_total": calculated,
        "stated_total": stated,
        "total_matches": calculated == stated,
    }


def print_report(data: dict) -> None:
    print("=" * 60)
    print(f"{data['company']}  (БИН {data['bin']})")
    print(f"Чек №{data['receipt_no']} | Кассир: {data['cashier']}")
    print(f"Дата: {data['datetime']['date']}  Время: {data['datetime']['time']}")
    print(f"Оплата: {data['payment']['method']} — {data['payment']['amount']:,.2f}")
    print("-" * 60)
    for i in data["items"]:
        print(f"{i['no']:>2}. {i['name'][:38]:<38} {i['quantity']:g} x {i['unit_price']:>8,.2f} = {i['total']:>9,.2f}")
    print("-" * 60)
    print(f"Calculated total: {data['calculated_total']:,.2f}")
    print(f"Stated total:     {data['stated_total']:,.2f}  (match: {data['total_matches']})")
    print("=" * 60)


if __name__ == "__main__":
    result = parse_receipt(Path(__file__).with_name("raw.txt"))
    print_report(result)
    print("\nJSON output:\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    Path(__file__).with_name("receipt.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")