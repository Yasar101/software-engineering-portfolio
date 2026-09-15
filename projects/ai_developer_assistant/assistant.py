"""Provider-neutral retrieval and prompt construction for a coding assistant."""

from dataclasses import dataclass
import re
from typing import Callable


TOKEN = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]+")
SECRET = re.compile(
    r"(?i)(api[_-]?key|token|password)[\"']?\s*[=:]\s*\S+"
    r"|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
)


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
        if len(question) > 4000:
            raise ValueError("question must be at most 4000 characters")
        if SECRET.search(question):
            raise ValueError("potential secret detected; redact credentials before continuing")
        context = self.retrieve(question)
        if any(SECRET.search(doc.path) or SECRET.search(doc.content) for doc in context):
            raise ValueError("potential secret detected in repository context")
        if any(len(doc.path) > 256 for doc in context):
            raise ValueError("context path must be at most 256 characters")
        excerpts = "\n\n".join(f"FILE: {doc.path}\n{doc.content[:2000]}" for doc in context)
        prompt = f"Answer using only the supplied repository context.\n\n{excerpts}\n\nQUESTION: {question}"
        return self.provider(prompt)


def main() -> None:
    """Run a credential-safe local retrieval demonstration."""
    import argparse

    parser = argparse.ArgumentParser(description="Ask a local, provider-neutral repository assistant.")
    parser.add_argument("question")
    args = parser.parse_args()
    documents = [
        ContextDocument("auth.py", "OAuth token refresh handler and expiry checks."),
        ContextDocument("money.py", "Decimal calculations avoid binary floating point rounding."),
        ContextDocument("jobs.py", "Workers claim jobs with expiring leases."),
    ]
    assistant = DeveloperAssistant(documents, lambda _: "Local demo provider: context was retrieved and bounded; connect a provider callable for generated answers.")
    try:
        context = assistant.retrieve(args.question)
        answer = assistant.answer(args.question)
    except ValueError as exc:
        parser.error(str(exc))
    print("Provider: local deterministic demo (no API key or external model call).")
    print("Retrieved:", ", ".join(document.path for document in context) or "no matching documents")
    print("Answer:", answer)


if __name__ == "__main__":
    main()
