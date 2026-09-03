from decimal import Decimal
import unittest

from projects.ai_developer_assistant.assistant import ContextDocument, DeveloperAssistant
from projects.distributed_ai_platform.scheduler import JobScheduler, JobState
from projects.microservices_commerce.commerce import CommerceService, Inventory, OrderStatus
from projects.monitoring_dashboard.monitoring import MetricWindow
from projects.postgres_rest_api.api import ItemService, MemoryItemRepository


class ApiTests(unittest.TestCase):
    def test_create_retrieve_and_validation(self):
        service = ItemService(MemoryItemRepository())
        status, created = service.create({"name": "Keyboard", "price_pence": 7500})
        self.assertEqual(status, 201)
        self.assertEqual(service.retrieve(created["id"]), (200, created))
        self.assertEqual(service.create({"name": ""})[0], 422)
        self.assertEqual(service.retrieve(99)[0], 404)


class MonitoringTests(unittest.TestCase):
    def test_bounded_summary_and_health(self):
        metrics = MetricWindow(capacity=3)
        for value in (1, 2, 3, 4):
            metrics.record("latency", value)
        summary = metrics.summary("latency")
        self.assertEqual((summary.count, summary.minimum, summary.maximum), (3, 2, 4))
        self.assertEqual(metrics.health("latency", 3), "degraded")
        self.assertEqual(metrics.health("missing", 3), "unknown")


class CommerceTests(unittest.TestCase):
    def test_success_and_payment_compensation(self):
        inventory = Inventory({"book": 2})
        service = CommerceService(inventory, {"book": Decimal("12.50")})
        order = service.place_order("book", 1, lambda total: total == Decimal("12.50"))
        self.assertEqual(order.status, OrderStatus.CONFIRMED)
        failed = service.place_order("book", 1, lambda total: False)
        self.assertEqual(failed.status, OrderStatus.REJECTED)
        self.assertEqual(inventory.stock["book"], 1)


class AssistantTests(unittest.TestCase):
    def test_retrieves_context_and_calls_provider(self):
        prompts = []
        assistant = DeveloperAssistant([
            ContextDocument("auth.py", "OAuth token refresh handler"),
            ContextDocument("math.py", "decimal calculator"),
        ], lambda prompt: prompts.append(prompt) or "Use auth.py")
        self.assertEqual(assistant.answer("Where is token refresh handled?"), "Use auth.py")
        self.assertIn("auth.py", prompts[0])

    def test_rejects_secrets(self):
        assistant = DeveloperAssistant([], lambda prompt: "unused")
        with self.assertRaises(ValueError):
            assistant.answer("api_key=super-secret")


class SchedulerTests(unittest.TestCase):
    def test_successful_job(self):
        now = [10.0]
        scheduler = JobScheduler(clock=lambda: now[0])
        submitted = scheduler.submit({"model": "small"})
        claimed = scheduler.claim("worker-1", 5)
        self.assertEqual(claimed.id, submitted.id)
        self.assertEqual(scheduler.finish(claimed.id, "worker-1", True).state, JobState.SUCCEEDED)

    def test_expired_lease_and_bounded_retries(self):
        now = [10.0]
        scheduler = JobScheduler(max_attempts=2, clock=lambda: now[0])
        job = scheduler.submit({})
        scheduler.claim("dead-worker", 5)
        now[0] = 16
        claimed = scheduler.claim("replacement", 5)
        self.assertEqual(claimed.id, job.id)
        self.assertEqual(scheduler.finish(job.id, "replacement", False).state, JobState.FAILED)
        self.assertIsNone(scheduler.claim("another"))


if __name__ == "__main__":
    unittest.main()
