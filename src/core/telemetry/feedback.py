"""Feedback logging utilities for knowledge-search workflows."""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Optional
import json


@dataclass
class FeedbackRecord:
    """Lightweight data class for storing user feedback about summaries/search results."""

    timestamp: datetime
    user: str
    query: str
    rating: int
    notes: Optional[str] = None
    document_ids: Optional[Iterable[str]] = None


def to_jsonl(record: FeedbackRecord) -> str:
    """Serialize a feedback record to a JSON line."""

    payload = {
        "schema_version": "0.1.0",
        "timestamp": record.timestamp.isoformat(),
        "user": record.user,
        "query": record.query,
        "rating": record.rating,
    }
    if record.notes:
        payload["notes"] = record.notes
    if record.document_ids:
        payload["document_ids"] = list(record.document_ids)
    return json.dumps(payload, ensure_ascii=False)


def append_record(record: FeedbackRecord, path: Path) -> None:
    """Append a feedback record to the given JSONL file."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fp:
        fp.write(to_jsonl(record) + "\n")
