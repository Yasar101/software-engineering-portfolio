"""Regression tests for failures found during the employer-facing release audit."""
from decimal import Decimal
import unittest

from projects.ai_developer_assistant.assistant import ContextDocument, DeveloperAssistant
from projects.cli_calculator.calculator import CalculationError, calculate
from projects.distributed_ai_platform.scheduler import JobScheduler, JobState
from projects.microservices_commerce.commerce import CommerceService, Inventory
from projects.postgres_rest_api.api import ItemService, MemoryItemRepository


class ReleaseReliabilityTests(unittest.TestCase):
    def test_payment_exception_releases_reservation(self):
        inventory = Inventory({"book": 1})
        service = CommerceService(inventory, {"book": Decimal("2")})
        def unavailable(total):
            raise TimeoutError("payment outcome unknown")
        with self.assertRaises(TimeoutError):
            service.place_order("book", 1, unavailable)
        self.assertEqual(inventory.stock["book"], 1)

    def test_expired_worker_cannot_finish(self):
        now = [0.0]
        scheduler = JobScheduler(clock=lambda: now[0])
        job = scheduler.submit({})
        scheduler.claim("worker", 1)
        now[0] = 1.0
        with self.assertRaises(ValueError):
            scheduler.finish(job.id, "worker", True)

    def test_final_expired_attempt_becomes_terminal(self):
        now = [0.0]
        scheduler = JobScheduler(max_attempts=1, clock=lambda: now[0])
        job = scheduler.submit({})
        scheduler.claim("worker", 1)
        now[0] = 2.0
        self.assertIsNone(scheduler.claim("replacement"))
        self.assertEqual(scheduler.get(job.id).state, JobState.FAILED)

    def test_invalid_retry_budget(self):
        for attempts in (0, -1, True, 1.5):
            with self.subTest(attempts=attempts), self.assertRaises(ValueError):
                JobScheduler(max_attempts=attempts)

    def test_invalid_lease(self):
        scheduler = JobScheduler()
        scheduler.submit({})
        for lease in (float("nan"), float("inf")):
            with self.subTest(lease=lease), self.assertRaises(ValueError):
                scheduler.claim("worker", lease)

    def test_payload_cannot_mutate_scheduler_state(self):
        scheduler = JobScheduler()
        payload = {"nested": {"value": 1}}
        job = scheduler.submit(payload)
        payload["nested"]["value"] = 2
        job.payload["nested"]["value"] = 3
        self.assertEqual(scheduler.get(job.id).payload["nested"]["value"], 1)

    def test_secret_in_retrieved_document_never_reaches_provider(self):
        calls = []
        assistant = DeveloperAssistant([
            ContextDocument("config.py", 'configuration: "api_key": "dummy-test-value"'),
        ], lambda prompt: calls.append(prompt) or "unexpected")
        with self.assertRaises(ValueError):
            assistant.answer("configuration")
        self.assertEqual(calls, [])

    def test_secret_in_context_path_never_reaches_provider(self):
        assistant = DeveloperAssistant([
            ContextDocument("password=dummy-test-value", "configuration"),
        ], lambda prompt: self.fail("provider must not be called"))
        with self.assertRaises(ValueError):
            assistant.answer("configuration")

    def test_question_length_is_bounded(self):
        assistant = DeveloperAssistant([], lambda prompt: self.fail("provider must not be called"))
        with self.assertRaises(ValueError):
            assistant.answer("x" * 4001)

    def test_api_rejects_non_string_name(self):
        service = ItemService(MemoryItemRepository())
        for value in (None, [], {}, 123, True):
            with self.subTest(value=value):
                self.assertEqual(service.create({"name": value, "price_pence": 1})[0], 422)
        self.assertEqual(service.list(), (200, {"items": []}))

    def test_calculator_rejects_non_finite_operands(self):
        for expression in ("NaN + 1", "Infinity * 0", "-Infinity / 2"):
            with self.subTest(expression=expression), self.assertRaises(CalculationError):
                calculate(expression)
