"""Provider-neutral retrieval and prompt construction for a coding assistant."""

from dataclasses import dataclass
import re
from typing import Callable


TOKEN = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]+")
SECRET = re.compile(r"(?i)(api[_-]?key|token|password)\s*[=:]\s*\S+")


@dataclass(frozen=True)
class ContextDocument:
    path: str
    content: str


class DeveloperAssistant:
    def __init__(self, documents: list[ContextDocument], provider: Callable[[str], str]) -> None:
        self.documents, self.provider = documents, provider

    def retrieve(self, question: str, limit: int = 3) -> list[ContextDocument]:
        terms = {word.lower() for word in TOKEN.findall(question)}
        ranked = sorted(self.documents, key=lambda doc: len(terms & {word.lower() for word in TOKEN.findall(doc.content)}), reverse=True)
        return [doc for doc in ranked if terms & {word.lower() for word in TOKEN.findall(doc.content)}][:limit]

    def answer(self, question: str) -> str:
        if SECRET.search(question):
            raise ValueError("potential secret detected; redact credentials before continuing")
        context = self.retrieve(question)
        excerpts = "\n\n".join(f"FILE: {doc.path}\n{doc.content[:2000]}" for doc in context)
        prompt = f"Answer using only the supplied repository context.\n\n{excerpts}\n\nQUESTION: {question}"
        return self.provider(prompt)
