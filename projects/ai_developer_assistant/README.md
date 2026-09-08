# AI Developer Assistant Core

**TESTED CORE** · [Portfolio](../../README.md) · [Architecture](../../docs/ARCHITECTURE.md)

Keyword-overlap retrieval and bounded prompt construction with a callable provider.

## Purpose and engineering skills

Explore context selection, model-provider boundaries and input screening without paid services.

## Structure

assistant.py holds ContextDocument and DeveloperAssistant; tests inject deterministic providers. [Source](assistant.py).

## Run

From the repository root with Python 3.11+, run this offline example using `python3` (no dependencies or credentials):

```python
from projects.ai_developer_assistant import ContextDocument, DeveloperAssistant
assistant = DeveloperAssistant([ContextDocument("tasks.py", "task completion repository")], lambda prompt: "Demo provider: inspect tasks.py")
print(assistant.answer("Where is task completion?"))
```

## Test

```sh
python3 -m unittest tests.test_systems.AssistantTests -v
python3 -m unittest discover -s tests -v
```

The full suite also includes release regression tests and executes these README examples.

## Complete and remaining

**Complete:** Up to three matched excerpts, 2,000 characters each; questions capped at 4,000 characters and selected paths at 256. Likely credential assignments/private-key markers in the question or selected context are rejected before provider invocation.

**Remaining / limitations:** No live LLM integration tested, embeddings, evaluation dataset, tools or autonomous execution. Regex screening can miss secrets; prompt instructions do not prevent injection or hallucination. Do not send private repositories to an untrusted provider.

## Learning takeaway

A fake provider tests the integration contract, not model answer quality or comprehensive AI safety.
